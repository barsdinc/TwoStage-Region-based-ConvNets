# Optimizing-Region-based-ConvNets-with-a-Two-Stage-Preprocessing-Approach-for-Object-Detection

## Introduction
This study proposes a two-stage preprocessing approach to optimize region-based convolutional neural networks (R-CNNs) for object detection. Our approach addresses the computational bottlenecks caused by the numerous region proposals and aims to replace candidate proposals with a concise set, effectively reducing high-frequency noise in non-object regions.

<!--The dataset and codes will be shared on Github once the study is published.-->


## Major contributions 

• Proposing a multi-task pre-processing approach based on region proposal-based deep object detection algorithms.

• Utilizing an object proposal detector to combine all weak candidate regions for each object in a single frame and implementing filter to non-object regions.

• Ensuring that the region proposal algorithm searches only noise-filtered candidate regions, reducing the number of proposals associated with the selective search.

## Get Started
### Training and Testing of Haar Cascade
In this study, the Haar Cascade algorithm was trained using 3096 positive and 10346 negative images collected from the Internet. Opencv is required for labeling and training positive images of Haar cascade. You can download it [here](https://sourceforge.net/projects/opencvlibrary/files/opencv-win/).

train_haarcascade.py file contains annotating and training of Haar Cascade algorithm. The algorithm produces an xml file in the "cascade_dir" directory that we will later use for test data.
Test images are the object detection data we use in deep learning. You can test the generated cascade model using the test.py file.

### Applying Gaussian Filter
As a result of generating object proposals by the cascade model, the candidate regions with IoU greater than zero were combined into a single frame, and a Gaussian filter was applied to the non-object regions for each image sample. The generated blurry images are used as input data for the deep learning algorithm.

## Steps

### 1) Before the training of haar cascade, the project folder looks like :

![1](https://github.com/user-attachments/assets/3b93de45-ee6f-45ca-be63-ffa3d7e6fd93)

### 2) When the training of the haar cascade is completed the xml file belonging to trained model is created in cascade_dir folder. Files of positive and negative samples used in training are also created in the project folder. 
![2](https://github.com/user-attachments/assets/96bea845-19cf-4141-be9a-71699d9bfe40)

### 3) The test folder contains the images you will use for object detection. You can test the trained cascade model by running the test_cascademodel.py file. The test_boxes.csv file created as a result of the testing process contains the coordinates predicted by the trained model for the object detection images.
![3 1](https://github.com/user-attachments/assets/4a62dde0-2a13-41ec-934f-b2884df0e411)


### 4) blurring_dir folder contains the blurred test images using coordinates predicted by the cascade model. You can run the blurring step using GaussianBlurring.py file.
![4](https://github.com/user-attachments/assets/e43a2f04-65f3-431b-bffd-eb2541e88ad5)



