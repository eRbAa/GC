from ultralytics import YOLO

# Load a model
# model = YOLO('./data/fall.yaml')  # build a new model from YAML
model = YOLO('Z:\Aguochuang\yolov8-test\yolov8n.pt')  # load a pretrained model (recommended for training)
# model = YOLO('./fall.yaml').load('yolov8n.pt')  # build from YAML and transfer weights

# Train the model
model.train(data='Z:\Aguochuang\yolov8-test\data\cat.yaml', epochs=100, imgsz=640)