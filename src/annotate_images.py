# Imports
import cv2    # Gives access to the opencv_annotate tool
import os     # Allows iterating through directories

IMAGE_DIRECTORY = "../Data/Training_Images/"
ANNOTATION_DIRECTORY = "../Data/Annotation_Files/"

def load_images():
  file_list = []
  for filename in os.listdir(IMAGE_DIRECTORY):
    file_list.append(filename)
  return file_list

def load_annotations():
  annotation_list = []
  for filename in os.listdir(ANNOTATION_DIRECTORY):
    annotation_list.append(filename)
  return annotation_list

def compare_files(image_files, annotation_files):
  
#-----------------------------------------------main------------------------------------------------
images = load_images()
annotations = load_annotations()

if (len(images) == 0):
  print("ERROR: No images found in Training directory")
print(images)
print(annotations)