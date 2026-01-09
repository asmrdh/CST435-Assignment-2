import cv2
import numpy as np
import os

def apply_pipeline(image_path):
    """
    Applies 5 sequential filters to a single image.
    1. Grayscale, 2. Blur, 3. Sobel (Edges), 4. Sharpen, 5. Brightness.
    """
    img = cv2.imread(image_path)
    if img is None:
        return None

    # Step 1: Grayscale - Reduces image to a single intensity channel
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    # Step 2: Gaussian Blur - Smoothens image to reduce noise for edge detection
    blurred = cv2.GaussianBlur(gray, (3, 3), 0)
    
    # Step 3: Sobel Edge Detection - Calculates gradients in X and Y directions
    sobelx = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
    sobely = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
    # Combine the X and Y gradients to get the final edge map
    edges = np.uint8(np.absolute(sobelx) + np.absolute(sobely))
    
    # Step 4: Image Sharpening - Uses a Laplacian-style kernel to enhance edges
    kernel = np.array([[-1,-1,-1], [-1,9,-1], [-1,-1,-1]])
    sharpened = cv2.filter2D(edges, -1, kernel)
    
    # Step 5: Brightness Adjustment - Scaling pixel values (alpha) and adding offset (beta)
    final_img = cv2.convertScaleAbs(sharpened, alpha=1.2, beta=30)
    
    return final_img

def process_and_save(image_path, output_dir):
    """
    Wrapper function to process an image and save the result to disk.
    This is what the parallel workers will execute.
    """
    result = apply_pipeline(image_path)
    if result is not None:
        filename = os.path.basename(image_path)
        # Save the result with a prefix to distinguish from original
        cv2.imwrite(os.path.join(output_dir, f"proc_{filename}"), result)
