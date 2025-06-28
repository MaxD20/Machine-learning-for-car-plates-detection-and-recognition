import os
import cv2
import pandas as pd

class PlateRepo:
    def __init__(self, output_dir):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    def save_plate_image(self, frame_count, x1, y1, gray_img):
        path = os.path.join(self.output_dir, f"frame_{frame_count}_x{int(x1)}_y{int(y1)}.png")
        cv2.imwrite(path, gray_img)
        return path

class PlateExcelRepo:
    def save_to_excel(self, codes, excel_path):
        df = pd.DataFrame(codes, columns=['Detected Codes'])
        df.to_excel(excel_path, index=False)
