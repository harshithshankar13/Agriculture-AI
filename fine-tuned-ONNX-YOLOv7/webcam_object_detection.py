import cv2
import time

from yolov7 import YOLOv7

rtsp_username = "admin"
rtsp_password = "Ridhi@2021"
rtsp_IP = "192.168.1.7"

rtsp = "rtsp://" + rtsp_username + ":" + rtsp_password + "@" + rtsp_IP + ":554/Streaming/channels/202"

# Initialize the webcam
cap = cv2.VideoCapture(rtsp)
fps = cap.get(cv2.CAP_PROP_FPS) 
print(fps)

# Initialize YOLOv7 object detector
model_path = "models/yolov7_384x640.onnx"
yolov7_detector = YOLOv7(model_path, conf_thres=0.5, iou_thres=0.5)

cv2.namedWindow("Detected Objects", cv2.WINDOW_NORMAL)

n = 0
while cap.isOpened():
    n += 1
    if n == 4: # read every 4th frame
        # Read frame from the video
        ret, frame = cap.read()

        if not ret:
            break
    
        n = 0
    
    time.sleep(1/30) # wait time

    

    

