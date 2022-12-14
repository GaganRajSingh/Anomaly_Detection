# SmartSurveillanceSystem


## Abstract
Object movement identification is one of the most researched problems in the field of computer vision. In this task, we try to classify a pixel as foreground or background. Even though numerous traditional machine learning and deep learning methods already exist for this problem, the two major issues with most of them are the need for large amounts of ground truth data and their inferior performance on unseen videos. Since every pixel of every frame has to be labeled, acquiring large amounts of data for these techniques gets rather expensive. Recently,  Zhao et al. proposed one of a kind Arithmetic Distribution Neural Network (ADNN) for universal background subtraction which utilizes probability information from the histogram of temporal pixels and achieves promising results. Building onto this work, we propose an intelligent video surveillance system that will use ADNN architecture for motion detection with some additional features like anomaly detection built within it.

## Feature extractor model setup

C3D weights can be found here: https://drive.google.com/drive/folders/1VIuJwUUGR_msOnbSXm8das2eVCN3uW0N?usp=sharing

Create a folder "pretrained" and paste the c3d.pickle file inside that folder.

## Pre-Trained Anomaly Detector
Check out <a href="exps/c3d/">exps/</a> for trained models on the pre-computed features

## How to run the code:

We have provided a fully fledged code and we need to run below steps in order to get results:

Step1. First we need to run `extract_frames_ft.py` and after this we get input frames and their corresponding ground truth franes which will save to Input_data/video1. 

Step2. Then we run `adnn_detect_work.py` to generate the binary foreground mask for each frame in the video. These masks are stored in the folder adnn_output. The output of this step is already computed.

Step3. Then we run `bayesian_refine_work.py` and will save our final refined frames in the bayesian_output folder. The output of this step is already computed.

Step4. To extract trimmed video we run `generate_trimmed_video.py`. This will save trimmed video in new folder named 'trimmed_video'. We have set different threhold values, depending on the input video. It will provide us the trimmed input video containing input frames having some motion in it and exclude frames which are still and not having any motion. By extracting trimmed video we are saving lot of time in anomaly detection.

Step5. In this step we are extracting the C3D features of our trimmed video. For that we need to run `feature_extractor.py` and this will save the features in feature_output folder. You can have a look into this folder and find the .txt file containing the features of the trimmed video. We use this feature to find the anomaly score which is our final step. The output of this step is already computed.

Step6. Finally, we have extracted features from trimmed video and we use these features to find the anomaly score. We run `generate_anomaly_score.py` and it will save the graph of anomaly scores in anomaly_score folder. 

        
By just following above steps we will get results. To summerize, we first have an input video and find the binary mask of each input video frame with help of ADNN and then we use bayesian refinement to refine the binary masks obtained in previous step. Then we use refined frames from bayesian refine in order to get trimmed video with the help of thresholding technique. Then we find features of trimmed input video and finally we calculate anomaly scores with the help of these features.

## Reference

The below code repositories were referred for implementation of this project:

1. https://github.com/zhaochenqiu/UBgS_ADNNet
2. https://github.com/ekosman/AnomalyDetectionCVPR2018-Pytorch