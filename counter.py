from ultralytics import YOLO
import cv2
import cvzone
import math
import numpy as np
from sort import *

video_link = "link to video"
cap = cv2.VideoCapture(video_link)

model_path = 'best.pt'

model = YOLO(model_path)
output_video_name = f"{model_path}.mp4"
frame_width = int(cap.get(3))
frame_height = int(cap.get(4))
out = cv2.VideoWriter(output_video_name, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), 30, (frame_width, frame_height))
# Tracker
tracker = Sort(max_age=20, min_hits=3,iou_threshold=0.3)

limits = [0, 436, 1571, 436]
totalCount = []
totalCount2 = []
totalCount3 = []
cv2.namedWindow("Image", cv2.WINDOW_NORMAL)
while True:
    success, image = cap.read()
    if not success:
      print(f""""Number of Vehicles on main road -> {len(totalCount)}  
            Number of cars on other road  -> {len(totalCount2)} 
            Number of autos -> {len(totalCount3)}
            Total Vehicles -> {len(totalCount) + len(totalCount2) + len(totalCount3)}
            """)
      break
    results = model(image, stream=True)
    detections = np.empty((0,5))
    for r in results:
        boxes = r.boxes
        for box in boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            w,h = x2-x1, y2-y1
            conf = math.ceil(box.conf[0] * 100) / 100

            if  conf > 0.5:
                currentArray = np.array([x1,y1,x2,y2,conf])
                detections = np.vstack((detections, currentArray))
    trackerResults = tracker.update(detections)
    cv2.line(image, (0, 900), (3900, 900), (0, 0, 255), 20)
    cv2.line(image, (300, 100), (850, 100), (0, 0, 255), 20)
    cv2.line(image, (2620, 0), (3800, 810),(0,0,255), 10)
    triangle = np.array([(2620,0), (3800, 810), (2620, 3800)])
    for results in trackerResults:
        x1,y1,x2,y2,id = results
        x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
        w, h = x2 - x1, y2 - y1
        cvzone.cornerRect(image, (x1, y1, w, h), l=1, colorR=(255,0,0), rt=10)
        cx = x1+w//2
        cy = y1+h//2
        cv2.circle(image, (cx,cy), radius=5, color=(0,255,0), thickness=-1)

        
        if cv2.pointPolygonTest(triangle, (cx,cy), False) == 1:
            if id not in totalCount3:
                totalCount3.append(id)
        
        if 0<cx<3900 and 700< cy <  1100:
            cv2.line(image, (0, 900), (3900, 900), (0, 255, 0), 20)
            if id not in totalCount:
                totalCount.append(id)
        
        if 300< cx < 750 and 80 < cy < 120:
          cv2.line(image, (300, 100), (850, 100), (0, 255,0), 20)
          if id not in totalCount2:
            totalCount2.append(id)
  
    cvzone.putTextRect(image, f"{len(totalCount)}", (3600,1200), thickness=10, scale=10)
    cvzone.putTextRect(image, f"{len(totalCount2)}", (600,300), thickness=40, scale=10)
    cvzone.putTextRect(image, f"{len(totalCount3)}", (3500,500), thickness=40, scale=10)
    # out.write(image)
    # cv2.imshow("Image", image)
    if cv2.waitKey(1) == 13:
        break
        
