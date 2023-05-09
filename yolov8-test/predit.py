# from ultralytics import YOLO
# from PIL import Image
# import cv2


# model = YOLO('Z:\Aguochuang\yolov8-test\yolov8n.pt')
# # accepts all fonmats - image/dir/Path/URL/video/PIL/ndarray. 0 for webcamresults = model.predict(source="0")
# # results = model.predict(source="0",save=True) # 用摄像头
# # results = model.predict(source="folder",show=True)# Display preds. Accepts all YoLO predict argument

# # cap = cv2.VideoCapture("Z:\BaiduNetdiskDownload\mda-kaj68wvpjrkai1p8.mp4")
# results = model.track(source="Z:\BaiduNetdiskDownload\mda-kaj68wvpjrkai1p8.mp4", classes=2, save=True) 
# results = model.predict(source=vid, save=True)
#from PIL
# im1 = Image.open("Z:\Aguochuang\yolov8-test\img.png")
# results = model.predict(source=im1, save=True) # save plotted images

#from ndarray
# im2 = cv2.imread("test.jpg")
# results = model.predict(source=im2,save=True,save_txt=True) # save predictions as labels
# #from list of PIL/ndancay
# results = model. predict(source=[im1, im2])
from ultralytics import YOLO
from PIL import Image
import cv2

model = YOLO('Z:\Aguochuang\yolov8-test\yolov8n.pt')

results = model.predict(source="Z:\BaiduNetdiskDownload\yolotest.mp4", classes=2, save=True)

for res in results:
    for detection in res.xywhn:
        # Get the bounding box coordinates (left, top, right, bottom)
        left, top, right, bottom = detection[:4]
        # Calculate the center point of the bounding box
        center_x = (left + right) / 2
        center_y = (top + bottom) / 2
        # Add labels for the bounding box coordinates and center point to the image
        res.save_labels([f'Left Top: ({left:.1f}, {top:.1f})', f'Left Bottom: ({left:.1f}, {bottom:.1f})', f'Right Top: ({right:.1f}, {top:.1f})', f'Right Bottom: ({right:.1f}, {bottom:.1f})', f'Center: ({center_x:.1f}, {center_y:.1f})'], imgsz=None)

    res.render() #new command to render the results
    res.save(save_dir='Z:\BaiduNetdiskDownload', save_name='video_with_labels.mp4')