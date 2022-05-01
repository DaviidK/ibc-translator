
import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/TesseractOCR/tesseract.exe'

img = cv2.imread('../Data/Test_Images/text_recognition_NFL_draft.png')
# img = cv2.resize(img, (600, 360))
print(pytesseract.image_to_string(img))
cv2.imshow('Result', img)
cv2.waitKey(0)

print(pytesseract.image_to_boxes(img))
cv2.imshow('Result', img)
cv2.waitKey(0)

hImg, wImg, _ = img.shape

boxes = pytesseract.image_to_boxes(img)
for b in boxes.splitlines():
  b = b.split(' ')
  print(b)
  x, y, w, h = int(b[1]), int(b[2]), int(b[3]), int(b[4])
  cv2.rectangle(img, (x, hImg - y), (w, hImg - h), (50, 50, 255), 1)
  cv2.putText(img, b[0], (x, hImg - y + 13), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (50, 205, 50), 1)

cv2.imshow('Detected text', img)
cv2.waitKey(0)