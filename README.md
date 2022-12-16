# SmartSurveillanceSystem


## Abstract
Object movement identification is one of the most researched problems in the field of computer vision. In this task, we try to classify a pixel as foreground or background. Even though numerous traditional machine learning and deep learning methods already exist for this problem, the two major issues with most of them are the need for large amounts of ground truth data and their inferior performance on unseen videos. Since every pixel of every frame has to be labeled, acquiring large amounts of data for these techniques gets rather expensive. Recently,  Zhao et al. proposed one of a kind Arithmetic Distribution Neural Network (ADNN) for universal background subtraction which utilizes probability information from the histogram of temporal pixels and achieves promising results. Building onto this work, we propose an intelligent video surveillance system that will use ADNN architecture for motion detection with some additional features like anomaly detection built within it.

## AnomalyDetectionCVPR2018-Pytorch
* C3D feature extraction

## 
C3D Weights
C3D weights can be found here: https://drive.google.com/drive/folders/1VIuJwUUGR_msOnbSXm8das2eVCN3uW0N?usp=sharing
Create a folder "pretrained" and paste the cr3.pickle file inside that folder

## Pre-Trained Anomaly Detector
Check out <a href="exps/c3d/">exps/</a> for trained models on the pre-computed features

## How to run the code:

We have provided a fully fledged code and we need to run below steps in order to get results:

Step1. First we need to run `extract_frames_ft.py` and after this we get input frames and their corresponding ground truth franes which will save to Input_data/video1. 

Step2. Then we run `adnn_detect_work.py` ADNNet (Arithmetic Distribution Neural Network) for background subtraction provided a pre-trained model which is trained with less than 1\% of ground truth frames from the CDNet2014 dataset and save the output frames in adnn_output folder. 

Step3. Then we run `bayesian_refine_work.py` and will save our final refined frames in the bayesian_output folder.  

Step4. To extract trimmed video we run `generate_trimmed_video.py`. This will save trimmed video in new folder named 'trimmed_video'. We have set different threhold values, depending on the input video. It will provide us the trimmed input video containing input frames having some motion in it and exclude frames which are still and not having any motion. By extracting trimmed video we are saving lot of time in anamoly detection. 

Step5. In this step we are extracting the features of our trimmed video. For that we need to run `feature_extractor.py` and this will save the features in feature_output folder. You can have a look into this folder and find the .txt file containing the features of the trimmed video. We use this feature to find the anamoly score which is our final step. 

Step6. Finally, we have extracted features from trimmed video and we use these features to find the anamoly score. We run `generate_anomaly_score.py` and it will save the graph of anamoly scores in anamoly_score folder. 

        
By just following above steps we will get results. To summerize, we first have an input video and find the binary mask of each input video frane with help of ADNN and then we use bayesian refinement to refine the binary masks obtained in previous step. Then we use refined frames from bayesian refine in order to get trimmed video with the help of thresholding technique. Then we will find features of trimmed input video and finally we calculate anamoly scores with the help of these features. 