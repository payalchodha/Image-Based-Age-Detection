# Image Based Age-Detection

## Background

Age ,one of the  key facial attribute,plays a very foundational role in social interactions. It makes age estimation from an image  an important task in various intelligent applications.
For example, age based access control. As a mother I would not want my kid to access inappropriate content and if any app that ensures the content is age appropriate by detecting their age from their face, then I would be relieved as a parent.
Similarly age detection from face can also be used in variuos law enforcement cases like if somebody buying alcohol is within age limit.
Some other use cases can be marketing intelligence and human-computer interaction.

## Problem Statement

How to predict the age of a person from his or her facial attributes?

## Directory Links
* [Initial EDA](https://github.com/payalchodha/Image-Based-Age-Detection/blob/master/Initial%20EDA.ipynb)
* [Flask](https://github.com/payalchodha/Image-Based-Age-Detection/tree/master/Flask)
* [Trained_Models](https://github.com/payalchodha/Image-Based-Age-Detection/tree/master/Trained-Models)
## Image Processing Overview

  * Displaying 

  * Manipulating 

  * Image segmentation

  * Image reshaping

  * Image recognition
 
 Common tasks in image processing include displaying images, basic manipulations like cropping, flipping, rotating etc, Image Segmentation, Classification and feature extractions, Image restoration and Image recognition. 


## Data Sources
 
 https://datahack.analyticsvidhya.com/contest/practice-problem-age-detection/
 
 ### Dataset overview
  27000+ images of various Indian Actors,with target class having three labels:
   1. YOUNG (13-30yrs)
   2. MIDDLE (31-50yrs)
   3. OLD(51 and above)
   
   The dataset was divided into two categories train and test with about 19000+ images in training set and about 6000+ images in testing dataset. I performed traintestsplit() to split the training data in train and validation set. 
   
## EDA
 I started to randomly view the dataset and check what challenges I could face when building the model. The things that I found out were:
 1. Variations in shape: One image had a shape (66, 46) whereas other had (102, 87)
 2. Multiple angles of different images: We have faces with whichever angle possible! 
 3. Brightness and Contrast differences.
 4. Some images were grayscale and some were in RGB.
 5. Most of the images were not of a very good quality.
 
 I used Image generator to pass the images with some fixed attributes, and used the image resize and resized all my images to (64,64) and also changed the images to grayscale and saved them in a numpy array.
 
 ## Model Training
I trained four models :
1. Sequential model with no regularization.(overfit)
2. Convolutional Neural Network model(CNN) with class weights to deal with the unbalanced classes.(highly overfit)
3. Convolutional Neural Network model(CNN) with class weights and regularization to deal with overfitting.(slightly overfit)
4. Implemented Transfer learning through Pretrained model VGG19 as base and then defined the final layers.

Once I had my best model(Pretrained one) I made a confusion matrix(the confusion gives the clearest visualization of how the model treats each class in the data). And then I saw the missclassified images. 

## User Interface Demonstration APP
## Framework
Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries. It has no database abstraction layer, form validation, or any other components where pre-existing third-party libraries provide common functions.

## Demonstration of the tool
 
  ![grab-landing-page](https://github.com/payalchodha/Image-Based-Age-Detection/blob/master/age_detection_app.gif)
  
## Challenges
* The classes were pretty unbalanced.
* Image Quality was very bad for most of the images.
* There were multiple viewpoints.

## Next Steps 
 
* Gathering more data to fix the unbalanced classes problem.

* Try more pretrained models may be Inception.

* From here on I can also incorporate gender, emotion detection and object detection in the same model and create a fully functional application.

## Further Improvements for the Web App
 * Deploy as a stand-alone app
 * Collaborate with UX/Web-dev teams to enhance user experience
 
## [Slide Deck Link]
(https://docs.google.com/presentation/d/1g8FuPDHm3kfxBARY4-SHFL0coee48p5N9X_HG8qpklE/edit?usp=sharing
)



    




