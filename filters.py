import cv2
import numpy as np
import os

def apply_pipeline(image_path):
    # Load image
    img = cv2.imread(image_path)
    if img is None: return None

    # 1. Grayscale Conversion (Luminance formula) [cite: 24]
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # 2. Gaussian Blur (3x3 kernel) [cite: 25]
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    
    # 3. Edge Detection (Sobel filter) [cite: 26]
    sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
    edges = np.uint8(np.absolute(sobelx) + np.absolute(sobely))
    
    # 4. Image Sharpening [cite: 27]
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpened = cv2.filter2D(edges, -1, kernel)
    
    # 5. Brightness Adjustment [cite: 28]
    final_img = cv2.convertScaleAbs(sharpened, alpha=1.2, beta=30)
    
    return final_img

def process_and_save(image_path, output_dir):
    result = apply_pipeline(image_path)
    if result is not None:
        filename = os.path.basename(image_path)
        cv2.imwrite(os.path.join(output_dir, f"proc_{filename}"), result)
