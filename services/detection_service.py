def detect_license_plate(frame, model):
    results = model(frame)
    boxes = results[0].boxes
    return boxes