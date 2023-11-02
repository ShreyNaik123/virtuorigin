
# Vehicle Object Detection Assignment

## Overview

This assignment involved training an object detection model using the provided dataset. The goal was to detect vehicles within a video and calculate the total count of these vehicles.

## Steps Taken

1. **Dataset Acquisition**: I acquired the dataset from the Kaggle link provided. The dataset was used for training and validation purposes.

2. **Data Preparation**: I converted the dataset to the YOLO format. This format includes both the dataset images and annotation files in YOLO text format. XML annotations were also converted to YOLO text annotations for compatibility with YOLO models.

3. **Model Selection**: I selected the YOLO object detection model. Due to resource constraints, I chose the YOLOv8s model for training. Larger models like YOLOv8l or YOLOv8x may require more resources and caused Colab crashes.

4. **Model Training**: I trained the selected model using the YOLO framework. The model was trained on the prepared dataset.

5. **Object Detection**: After model training, I applied the model to the test video. This step involved detecting vehicles within the video frames using the trained model.

6. **Count Calculation**: To calculate the total count of vehicles, I used opencv methods to draw bounding boxes around detected vehicles. I also applied the SORT (Simple Online and Realtime Tracking) algorithm to track the movement of vehicles within the video.

## Results
![image](https://github.com/ShreyNaik123/virtuorigin/assets/61283238/7748721f-338a-4729-a178-bf2adbf3520c)
<br>

![image](https://github.com/ShreyNaik123/virtuorigin/assets/61283238/a487c905-8791-4c28-b404-702ed0e56db5)
<br>

![image](https://github.com/ShreyNaik123/virtuorigin/assets/61283238/124582c6-d21a-488b-8695-4f559038ec21)
<br>

The model successfully detected and tracked vehicles in the provided test video. The total count of vehicles was calculated and displayed on the video frames.


Number of Vehicles on main road -> 42  
Number of cars on other road  -> 26 <br>
Number of autos -> 14 <br>
Total Vehicles -> 82

