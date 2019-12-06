# Image Based Age-Detection

## Background

Age ,one of the  key facial attribute,plays a very foundational role in social interactions. It makes age estimation from an image  an important task in various intelligent applications.
For example, age based access control. As a mother I would not want my kid to access inappropriate content and if any app that ensures the content is age appropriate by detecting their age from their face, then I would be relieved as a parent.
Similarly age detection from face can also be used in variuos law enforcement cases like if somebody buying alcohol is within age limit.
Some other use cases can be marketing intelligence and human-computer interaction.

## Problem Statement

How to predict the age of a person from his or her facial attributes?

## Directory Links


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
    




