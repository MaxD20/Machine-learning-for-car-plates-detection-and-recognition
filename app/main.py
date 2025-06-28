from config.settings import VIDEO_PATH, MODEL_PATH, OUTPUT_EXCEL_PATH, OUTPUT_VIDEO_PATH
from models.yolo_detector import YoloDetector
from models.ocr_reader import OcrReader
from services.video_service import process_video

if __name__ == "__main__":
    process_video(
        VIDEO_PATH,
        MODEL_PATH,
        OUTPUT_EXCEL_PATH,
        OUTPUT_VIDEO_PATH
    )
