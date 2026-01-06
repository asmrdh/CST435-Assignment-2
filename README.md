# CST435 Parallel Computing - Assignment 2: Image Processing Pipeline

## Group Members
* **Nur Asma Mardhiah binti Roszi** (162175)
* **Nur Nabila binti Normiza Shahman** (164047)
* **Naomi Tham Kah Mun** (164854)
* **Mursyidah binti Mat Jusoh** (162897)

## Project Overview
This project implements a parallel image processing pipeline on a Google Cloud Platform (GCP) VM. The system applies five sequential filters (Grayscale, Gaussian Blur, Sobel Edge Detection, Sharpening, and Brightness Adjustment) to subsets of the Food-101 dataset. We compare the performance and scalability of two Python parallel paradigms.

## Image Processing Pipeline
The pipeline consists of the following steps:
1. **Grayscale**: Converts BGR images to grayscale.
2. **Gaussian Blur**: Reduces noise using a 3x3 kernel.
3. **Sobel Filter**: Detects horizontal and vertical edges.
4. **Sharpening**: Enhances edge contrast using a kernel filter.
5. **Brightness**: Adjusts the final intensity levels.

## How to Run
### 1. Prerequisites
Ensure you have Python 3.11+ and `pip` installed on your GCP VM.

### 2. Environment Setup
```bash
# Create and activate virtual environment
python3 -m venv cst435_env
source cst435_env/bin/activate

# Install dependencies
pip install opencv-python-headless numpy
