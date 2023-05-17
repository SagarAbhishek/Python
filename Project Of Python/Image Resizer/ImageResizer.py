import cv2

source='Project Of Python\Image Resizer\DSC_0824.JPG'
DestinationPath= 'Project Of Python\\Image Resizer\\resize-image.jpg'
scale_percent = 50


src = cv2.imread(source, cv2.IMREAD_UNCHANGED)
new_width = int(src.shape[1] * scale_percent / 100)
new_height = int(src.shape[0] * scale_percent / 100)
dsize = (new_width, new_height)
output = cv2.resize(src, dsize)
cv2.imwrite(DestinationPath,output) 
