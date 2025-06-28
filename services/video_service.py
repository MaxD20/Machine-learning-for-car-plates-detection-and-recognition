import cv2
import os
import easyocr
import pandas as pd
from ultralytics import YOLO
from models.yolo_detector import YoloDetector
from models.ocr_reader import OcrReader
from services.detection_service import detect_license_plate
from repositories.video_repo import VideoWriterRepo
from repositories.plate_repo import PlateRepo
from utils.image_utils import draw_label
from domain.plate import is_valid_license_plate
from repositories.plate_repo import PlateExcelRepo

def process_video(video_path, model_path, output_excel, output_video_path, window_width=980, frame_skip=2, delay_ms=50):

    reader = easyocr.Reader(['en'])
    model = YOLO(model_path)
    cap = cv2.VideoCapture(video_path)
    if not cap.isOpened():
        print(f"Error: Could not open video at {video_path}.")
        return

    frame_width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    output_dir = os.path.dirname(output_video_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    grayscale_output_dir = os.path.join(output_dir, "grayscale_plates")
    if not os.path.exists(grayscale_output_dir):
        os.makedirs(grayscale_output_dir)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    out = cv2.VideoWriter(output_video_path, fourcc, fps, (frame_width, frame_height))
    detected_codes = []
    frame_count = 0

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print(f"End of video reached after processing {frame_count} frames.")
                break

            if frame_count % (frame_skip + 1) != 0:
                frame_count += 1
                continue

            boxes = detect_license_plate(frame, model)
            for box in boxes:
                x1, y1, x2, y2 = box.xyxy[0][:4].tolist()
                cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                roi = frame[int(y1):int(y2), int(x1):int(x2)]
                if roi.size == 0:
                    print(f"Empty ROI extracted, skipping OCR for this box.")
                    continue

                gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
                gray_filename = os.path.join(grayscale_output_dir, f"frame_{frame_count}_x{int(x1)}_y{int(y1)}.png")
                cv2.imwrite(gray_filename, gray_roi)
                print(f"Saved grayscale license plate: {gray_filename}")
                cv2.imshow("Grayscale License Plate", gray_roi)
                cv2.waitKey(1)

                ocr_results = reader.readtext(gray_roi)
                if not ocr_results:
                    print(f"No text detected in the ROI: {x1}, {y1}, {x2}, {y2}")
                    continue

                for (bbox, text, prob) in ocr_results:
                    print(f"Detected text: '{text}', Confidence: {prob}")
                    if prob >= 0.2:

                        padding = 10
                        text_box_height = 50
                        (text_width, text_height), baseline = cv2.getTextSize(text, cv2.FONT_HERSHEY_SIMPLEX, 1.2, 3)
                        text_box_width = text_width + 2 * padding
                        text_box_x1 = int(x1)
                        text_box_x2 = int(x1 + text_box_width)
                        text_box_y1 = int(y1) - text_box_height
                        text_box_y2 = int(y1)
                        cv2.rectangle(frame, (text_box_x1, text_box_y1), (text_box_x2, text_box_y2), (0, 255, 0), -1)

                        text_x = text_box_x1 + padding
                        text_y = text_box_y1 + (text_box_height + text_height) // 2 + baseline // 2
                        shadow_offset = 2
                        cv2.putText(frame, text, (text_x + shadow_offset, text_y + shadow_offset), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 5)
                        cv2.putText(frame, text, (text_x, text_y), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 3)

                        if is_valid_license_plate(text):
                            if text not in detected_codes:
                                detected_codes.append(text)
                                print(f"Valid license plate detected and saved: {text}")
            height = int(frame.shape[0] * (window_width / frame.shape[1]))
            resized_frame = cv2.resize(frame, (window_width, height))
            out.write(frame)
            cv2.imshow('Processed Video', resized_frame)
            if cv2.waitKey(delay_ms) & 0xFF == ord('q'):
                print("Video processing interrupted by user.")
                break
            frame_count += 1
    except KeyboardInterrupt:
        print("Processing interrupted by user.")
    finally:
        cap.release()
        out.release()
        cv2.destroyAllWindows()
        if detected_codes:
            detected_codes = [code for code in detected_codes if ' ' not in code or is_valid_license_plate(code)]
            df = pd.DataFrame(detected_codes, columns=['Detected Codes'])
            df.to_excel(output_excel, index=False)
            print(f"Detected valid license plates saved to: {output_excel}")
        else:
            print("No valid license plates detected.")