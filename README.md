# Smart Image Segmentation and Analysis Using K-Means Clustering

## Overview

**Smart Image Segmentation and Analysis Using K-Means Clustering** is a Computer Vision project that segments digital images into visually similar regions using the **K-Means clustering algorithm**.

The project treats image pixels as numerical data points and groups them according to their color similarity. The generated clusters are then used to create a simplified segmented image and extract individual regions.

The project also includes **image preprocessing, K-value comparison, Elbow Method analysis, region extraction, input validation, error handling, and testing**.

---

## Objectives

* Segment images using K-Means clustering.
* Convert image pixels into numerical feature vectors.
* Preprocess images before segmentation.
* Analyze different values of K.
* Use the Elbow Method to study cluster selection.
* Extract individual image regions.
* Save segmentation and analysis results.
* Provide a command-line based execution workflow.
* Test important project components.

---

## Features

* Image input and validation
* Image preprocessing
* RGB pixel-based clustering
* K-Means image segmentation
* Custom K-value selection
* Elbow Method analysis
* Region extraction
* Segmented image generation
* Result saving
* Error handling
* Command-line execution
* Automated testing

---

## Technologies Used

| Technology   | Purpose                        |
| ------------ | ------------------------------ |
| Python       | Main programming language      |
| OpenCV       | Image processing               |
| NumPy        | Numerical and pixel operations |
| Scikit-learn | K-Means clustering             |
| Matplotlib   | Graphs and visualization       |
| Pytest       | Testing                        |

---

## Project Structure

```text
smart-image-segmentation/
│
├── data/
│   └── sample_images/
│       ├── flower.jpg
│       ├── fruit.jpg
│       └── landscape.jpg
│
├── results/
│   ├── segmented/
│   ├── extracted/
│   └── analysis/
│
├── screenshots/
│
├── modules/
│   ├── __init__.py
│   ├── preprocessing.py
│   ├── segmentation.py
│   ├── analysis.py
│   ├── extraction.py
│   └── visualization.py
│
├── tests/
│   ├── test_preprocessing.py
│   ├── test_segmentation.py
│   └── test_validation.py
│
├── validation.py
├── main.py
├── requirements.txt
└── README.md
```

---

## How It Works

The project follows the following workflow:

```text
Input Image
     ↓
Input Validation
     ↓
Image Preprocessing
     ↓
Pixel Data Preparation
     ↓
K-Means Clustering
     ↓
Cluster Assignment
     ↓
Segmented Image
     ↓
┌───────────────┬───────────────┐
↓               ↓               ↓
Elbow        Region          Result
Analysis     Extraction       Saving
```

---

## K-Means Segmentation

Each RGB pixel is represented as:

```text
[R, G, B]
```

These pixel values are provided to the K-Means algorithm.

For a selected value of `K`, the algorithm:

1. Initializes cluster centers.
2. Calculates the distance between pixels and cluster centers.
3. Assigns pixels to their nearest cluster.
4. Updates cluster centers.
5. Repeats the process until convergence.
6. Reconstructs the image using the cluster centers.

For example:

```text
Original Image
      ↓
K = 3
      ↓
Cluster 0 ──► Region 1
Cluster 1 ──► Region 2
Cluster 2 ──► Region 3
```

---

## Elbow Method

The Elbow Method is used to study different values of `K`.

The system calculates clustering **inertia** for multiple K values and generates an analysis graph.

Example:

```text
K = 2
K = 3
K = 4
K = 5
K = 6
K = 7
K = 8
```

The point where the decrease in inertia begins to slow down can help identify a suitable K value.

The Elbow Method is used as a supporting technique because the most useful K value also depends on the visual characteristics of the image.

---

## Installation

### 1. Clone the project

```bash
git clone <YOUR_REPOSITORY_URL>
```

### 2. Open the project directory

```bash
cd smart-image-segmentation
```

### 3. Create a virtual environment

Windows:

```bash
python -m venv venv
```

Activate it:

```bash
venv\Scripts\activate
```

Linux/macOS:

```bash
python3 -m venv venv
```

```bash
source venv/bin/activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Project

The main application can be executed directly from the command line.

### Basic Segmentation

```bash
python main.py --input data/sample_images/flower.jpg --k 3
```

Here:

* `--input` specifies the input image.
* `--k` specifies the number of clusters.

### Example

```bash
python main.py --input data/sample_images/fruit.jpg --k 4
```

The segmented image will be generated and saved in the results directory.

---

## Elbow Analysis

To compare multiple K values:

```bash
python main.py --input data/sample_images/flower.jpg --elbow
```

The system evaluates different cluster counts and generates the corresponding analysis.

---

## Region Extraction

After segmentation, selected clusters can be extracted using the region extraction module.

The extracted regions are stored in:

```text
results/extracted/
```

---

## Output

The project generates outputs such as:

```text
results/
│
├── segmented/
│   └── segmented_image.jpg
│
├── extracted/
│   ├── cluster_0.jpg
│   ├── cluster_1.jpg
│   └── cluster_2.jpg
│
└── analysis/
    └── elbow_plot.png
```

The exact filenames may vary depending on the implementation.

---

## Testing

The project contains tests for important components such as image validation, preprocessing, and segmentation.

Run the tests using:

```bash
pytest
```

A successful test execution should display the number of passed tests.

Example:

```text
========================
X passed in X.XX seconds
========================
```

---

## Sample Results

### Original Image

Add the original input image here.

```text
[Insert Original Image Screenshot]
```

### Segmented Image

Add the generated segmented image here.

```text
[Insert Segmented Image Screenshot]
```

### Elbow Method

Add the Elbow Method graph here.

```text
[Insert Elbow Graph Screenshot]
```

### Extracted Region

Add an extracted cluster/region here.

```text
[Insert Region Extraction Screenshot]
```

---

## Advantages

* Simple and easy-to-understand segmentation approach.
* Does not require labeled training data.
* Works directly with image pixel information.
* Supports different K values.
* Provides Elbow Method analysis.
* Allows individual cluster regions to be extracted.
* Can be executed directly from the command line.
* Modular structure makes the system easier to maintain.

---

## Limitations

* Results depend on the selected K value.
* Similar-colored objects may be placed in the same cluster.
* K-Means does not inherently understand object meaning.
* Very large images can require more processing time.
* Basic RGB clustering does not fully consider spatial relationships between pixels.
* Lighting and shadows can affect segmentation results.

---

## Future Enhancements

Possible future improvements include:

* Automatic K-value selection.
* HSV or LAB color-space segmentation.
* Spatial feature integration.
* Region Growing segmentation.
* Edge-Based segmentation.
* Mean-Shift segmentation.
* Graph-Cut segmentation.
* Gaussian Mixture Models.
* Deep-learning-based semantic segmentation.
* Real-time video segmentation.

---

## Conclusion

This project demonstrates how **K-Means clustering can be applied to image segmentation** by treating image pixels as numerical data points.

The system combines Computer Vision and unsupervised machine learning concepts to preprocess images, cluster pixels, generate segmented outputs, analyze K values, and extract image regions.

It provides a practical implementation of image segmentation while maintaining a simple and understandable workflow.

---

## Author

**Aanya Pahwa**

B.Tech — Computer Science and Engineering (AIML)
VIT Bhopal University
