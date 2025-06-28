import pytest
import numpy as np
import types
from services.detection_service import detect_license_plate
from models.yolo_detector import YoloDetector


def test_detect_license_plate(monkeypatch):

    box = types.SimpleNamespace()
    box.xyxy = [np.array([10, 20, 110, 60, 0.9])]
    fake_result = types.SimpleNamespace(boxes=[box])

    monkeypatch.setattr(
        YoloDetector, "predict", lambda self, frame: [fake_result]
    )

    detector = YoloDetector("yolov8n.pt")  # path is irrelevant after patch
    dummy_frame = np.zeros((480, 640, 3), dtype=np.uint8)

    boxes = detect_license_plate(dummy_frame, detector)
    assert len(boxes) == 1
    x1, y1, x2, y2 = boxes[0].xyxy[0][:4]
    assert (x1, y1, x2, y2) == (10, 20, 110, 60)
