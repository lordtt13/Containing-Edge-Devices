import cv2
import numpy as np
from skimage import io
from skimage.morphology import skeletonize
from skimage.util import invert
from skimage import img_as_ubyte

img = cv2.imread('MH2.jpeg', 0)
dst=cv2.fastNlMeansDenoising(img,None,10,10,21)

# histogram equalization
equ = cv2.equalizeHist(dst)
cv2.imwrite('eq.png', equ)

# image gradients
laplacian = cv2.Laplacian(dst, cv2.CV_64F)
sobelx = cv2.Sobel(dst, cv2.CV_64F, 1, 0, ksize=5)
sobely = cv2.Sobel(dst, cv2.CV_64F, 0, 1, ksize=5)
cv2.imwrite('laplacian.png',laplacian)
cv2.imwrite('sobelx.png',sobelx)
cv2.imwrite('sobely.png',sobely)

#erosion
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(dst,kernel,iterations = 1)
cv2.imwrite('erosion.png',erosion)

#dilation
dilation = cv2.dilate(dst,kernel,iterations = 1)
cv2.imwrite('dilation.png',dilation)

#skeletonize
threshold = 127
binarized = 1.0 * (img > threshold)
skeleton = skeletonize(binarized)
cv_image = img_as_ubyte(skeleton)
cv2.imwrite('skel.png',cv_image)




