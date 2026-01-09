# CST435 Parallel Computing - Assignment 2: Image Processing Pipeline

## Group Members
* **Nur Asma Mardhiah binti Roszi** (162175) - GCP Deployment & Benchmarking
* **Nur Nabila binti Normiza Shahman** (164047) - Parallel Paradigm 1 (`multiprocessing`)
* **Naomi Tham Kah Mun** (164854) - Parallel Paradigm 2 (`concurrent.futures`)
* **Mursyidah binti Mat Jusoh** (162897) - Technical Reporting & Data Analysis

## Project Overview
This project implements a parallel image processing pipeline on a Google Cloud Platform (GCP) VM. The system applies five sequential filters to subsets of the Food-101 dataset, comparing the performance and scalability of two Python parallel paradigms.

## Repository Structure
* `filters.py`: The core image processing logic containing the 5-filter pipeline.
* `multiproc_task.py`: Implementation using the `multiprocessing.Pool` paradigm.
* `concurrent_task.py`: Implementation using the `concurrent.futures.ProcessPoolExecutor` paradigm.
* `data/`: (Local only) Source images organized into subsets of 100, 200, 300, and 500.

## Image Processing Pipeline
Each image undergoes five sequential transformations:
1. **Grayscale**: Reduces image to a single intensity channel.
2. **Gaussian Blur**: Reduces noise using a 3x3 kernel.
3. **Sobel Filter**: Calculates gradients to detect horizontal and vertical edges.
4. **Sharpening**: Enhances edge contrast using a kernel filter.
5. **Brightness**: Adjusts the final intensity levels for clarity.

## Hardware Environment
- **Platform**: Google Cloud Platform (GCP)
- **Machine Type**: e2-standard-8 (8 vCPUs, 32 GB memory)
- **OS**: Debian GNU/Linux 12 (bookworm)

## How to Run
### 1. Prerequisites
Ensure Python 3.11+ is installed. This project requires `opencv-python-headless` and `numpy`.

### 2. Environment Setup
```bash
# Create and activate virtual environment
python3 -m venv cst435_env
source cst435_env/bin/activate

# Install dependencies
pip install opencv-python-headless numpy
