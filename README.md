# Machine-learning-for-car-plates-detection-and-recognition

The goal of the project was to develop a video processing algorithm in Python which uses 
YOLOv8 machine learning object detection, OpenCV, EasyOCR libraries for license plates 
detection, frames processing and alphanumeric characters extraction.

The algorithm process 384 frames of a 12 seconds smartphone recorded video with moving cars 
besides the road in a periurban area with traffic conditions. 
The troubleshooting faced were occlusions, varying lighting conditions and windscreen reflection. 

The training was done using 514 images from storage.googleapi dataset and 20 images
with Romanian license plates self-provided and manually annotated in CVAT. 
As output results, the model successfully localize and identify 54% of car plates 
with an overall confidence score of 0.6. 
The performance outputs significant parameters used are: confusion matrix, epoch size, train classes statistics, precision and recall. 

The split done was 80% training and 20% validation.<br>
Data training<br>
<img src="https://github.com/MaxD20/Machine-learning-for-car-plates-detection-and-recognition/blob/main/data_of_vehicle_registration_plates.jpg?raw=true" alt="Data training" height="40%" width="30%"/></br>

Execution of main programme<br>
<img src="https://github.com/MaxD20/Machine-learning-for-car-plates-detection-and-recognition/blob/main/execution_main_programme.png?raw=true" alt="Image showing processed video output" height="40%" width="30%"/></br>

Processed frame classified as vehicle_registration_plate in windscreen reflection<br>
<img src="https://github.com/MaxD20/Machine-learning-for-car-plates-detection-and-recognition/blob/main/m1.jpg?raw=true" alt="Vehicle registration plate class" height="40%"  width="30%"/></br>

Corner case of multiple license plates detection<br>
<img src="https://github.com/MaxD20/Machine-learning-for-car-plates-detection-and-recognition/blob/main/m2.jpg?raw=true" alt="Multiple license plates detection" height="40%"  width="30%"/></br>

Vehicle license plate recognition with OCR, measured in 2.5ms, 167.4ms for inference and 1.6ms for postprocessing, which indicates real time feasibility metrics for the 297th frame of the video.<br>
<img src="https://github.com/MaxD20/Machine-learning-for-car-plates-detection-and-recognition/blob/main/m3.jpg?raw=true" alt="Vehicle license plate recognition with OCR" height="40%" width="30%"/></br>

Vehicle license plate recognition with OCR 2<br>
<img src="https://github.com/MaxD20/Machine-learning-for-car-plates-detection-and-recognition/blob/main/Vehicle%20license%20plate%20recognition%20and%20OCR%202.png?raw=true" alt="text_score_2" width="30%" height="40%"/></br>

Vehicle license plate recognition - case of misdetected letter<br>
This care represent the vehicle license plate recognition and OCR of a SUV with a Bulgarian registration number plate, where is illustrated a case of misdetected letter, “I” instead of “H” from the 246th video frame. It is crucial to mention that, at detection, in the top left corner, the quality image of the registration number plate presented an amount of blur because of the lighting conditions captured in the frame. Moreover, the windscreen reflection between the phone camera and the vehicle is present in this case.
<img src="https://github.com/MaxD20/Machine-learning-for-car-plates-detection-and-recognition/blob/main/Vehicle%20license%20plate%20recognition%20and%20OCR%202nd%20case%20of%20misdetected%20letter.png?raw=true" alt="text_score_3" width="30%" height="40%"/></br>

Confidence curve of dataset training<br>
<img src="https://github.com/MaxD20/Machine-learning-for-car-plates-detection-and-recognition/blob/main/confidence_curve.png?raw=true" alt="Confidence curve" height="40%" width="30%"/></br>

Precision confidence curve<br>
<img src="https://github.com/MaxD20/Machine-learning-for-car-plates-detection-and-recognition/blob/main/precision_confidence_curve.png?raw=true" alt="Precision confidence curve" height="40%" width="30%"/></br>


