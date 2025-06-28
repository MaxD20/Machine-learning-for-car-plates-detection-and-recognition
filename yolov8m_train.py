from ultralytics import YOLO
def main():
model = YOLO("yolov8m.pt")
results = model.train(data="E:\M_IT4T\ML\yolov8_custom\data_custom.yaml", epochs=15)
metrics = model.val()
print(results)
if __name__ == '__main__':
main()
