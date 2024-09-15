# Optimizing-Region-based-ConvNets-with-a-Two-Stage-Preprocessing-Approach-for-Object-Detection

## Introduction
This study proposes a two-stage preprocessing approach to optimize region-based convolutional neural networks (R-CNNs) for object detection. Our approach addresses the computational bottlenecks caused by the numerous region proposals and aims to replace candidate proposals with a concise set, effectively reducing high-frequency noise in non-object regions.
<!--
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
-->
