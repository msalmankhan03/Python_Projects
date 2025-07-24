import cv2
# 1. Import OpenCV
import cv2

# 2. Load original image
image = cv2.imread("pencel_sketch_dip/salman.png.jpg")  # Replace with your image filename
image = cv2.resize(image, (500, 500))  # Optional: resize to smaller size

# 3. Convert to grayscale
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
# 4. Invert grayscale image
inverted_image = 255 - gray_image
  
# 5. Apply Gaussian Blur
blurred = cv2.GaussianBlur(inverted_image, (21, 21), sigmaX=0, sigmaY=0)

# 6. Invert the blurred image
inverted_blur = 255 - blurred

# 7. Create the pencil sketch using color dodge
sketch = cv2.divide(gray_image, inverted_blur, scale=256.0)

# 8. Display the results
cv2.imshow("Original Image", image)
cv2.imshow("Pencil Sketch", sketch)

cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("pencil_sketch.png", sketch)
from matplotlib import pyplot as plt

plt.figure(figsize=(10,5))
plt.subplot(1, 2, 1)
plt.title("Original")
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.axis('off')

plt.subplot(1, 2, 2)
plt.title("Pencil Sketch")
plt.imshow(sketch, cmap='gray')
plt.axis('off')

plt.show()
