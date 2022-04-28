from pycocotools.coco import COCO
import json
import shutil

data_directory = '../Data/coco'
data_type = 'val'
annotation_file = '{}/annotations/instances_{}.json'.format(data_directory, data_type)
image_directory = '{}/{}/'.format(data_directory, data_type)
training_directory = '../Data/Training/'
classes = ['stop sign', 'umbrella', 'scissors']
# Initialize the COCO api for instance annotations
coco = COCO(annotation_file)

def find_images():
  images = []
  image_map = {}
  if classes != None:
      # iterate for each individual class in the list
      for className in classes:
          # get all images containing given class
          catIds = coco.getCatIds(catNms=className)
          imgIds = coco.getImgIds(catIds=catIds)
          for i in range(len(imgIds)):
            found_image = json.dumps(coco.loadImgs(imgIds[i]))
            found_filepath = found_image[30:46]
            if found_image not in images:
                images.append(found_image)
                image_map.update({imgIds[i]: found_filepath})              
  else:
      imgIds = coco.getImgIds()
      images = coco.loadImgs(imgIds)
      
  return image_map

def copy_images(image_map):
  for i in image_map.items():
    source_directory = image_directory + i[1]
    target_directory = training_directory + i[1]
    shutil.copy2(source_directory, target_directory)



image_map = find_images()
copy_images(image_map)