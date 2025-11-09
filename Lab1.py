import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

img = cv.imread('Images/Car2.jpg', cv.IMREAD_GRAYSCALE)
if img is None:
    print("Error: No image is loaded")
    exit()

# Negative
neg_img = 255 - img

# Log Transform (Fixed)
img_float = img.astype(np.float32)
log_img = np.log(1 + img_float)
log_img = (log_img / np.max(log_img)) * 255   # Normalize to [0,255]
log_img = np.uint8(log_img)

# Gamma Transform
gamma = 0.5
gamma_img = np.power(img_float / 255.0, gamma)
gamma_img = np.uint8(gamma_img * 255)

# Display all images
titles = [
    ("Original Image in Grayscale", img),
    ("Negative Image", neg_img),
    ("Log Transform", log_img),
    (f"Gamma Transform (γ={gamma})", gamma_img)
]

plt.figure(figsize=(12, 8))
for i, (title, image) in enumerate(titles, 1):
    plt.subplot(2, 2, i)
    plt.imshow(image, cmap='gray')
    plt.title(title, fontsize=14, pad=10)
    plt.axis('off')

plt.subplots_adjust(wspace=0.1, hspace=0.25)
plt.show()
