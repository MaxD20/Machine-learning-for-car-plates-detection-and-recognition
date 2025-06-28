import cv2
import os

class VideoWriterRepo:
    def __init__(self, output_path, frame_width, frame_height, fps):
        os.makedirs(os.path.dirname(output_path), exist_ok=True)
        self.writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (frame_width, frame_height))

    def write_frame(self, frame):
        self.writer.write(frame)

    def close(self):
        self.writer.release()
