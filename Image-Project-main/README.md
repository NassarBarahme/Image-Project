<div align="center">
  <h1>🖼️ Image Processing Tool</h1>
  <p>An interactive Python application for advanced image processing operations</p>
  
  [![Python](https://img.shields.io/badge/Python-3.7+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
  [![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)](https://opencv.org/)
  [![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)](https://numpy.org/)
  [![Matplotlib](https://img.shields.io/badge/Matplotlib-11557c?style=for-the-badge&logo=python&logoColor=white)](https://matplotlib.org/)
  
  [![MIT License](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://choosealicense.com/licenses/mit/)
  
</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Installation](#-installation)
- [Usage](#-usage)
- [Operations Guide](#-operations-guide)
- [Examples](#-examples)
- [Functions Reference](#-functions-reference)
- [Customization](#-customization)
- [Troubleshooting](#-troubleshooting)
- [Contributing](#-contributing)
- [License](#-license)

---

## 🌟 Overview

This tool provides a **comprehensive menu-driven interface** for performing various image processing tasks. Built with Python, OpenCV, and Matplotlib, it offers both basic and advanced operations including filtering, edge detection, histogram analysis, and interactive region segmentation.

Perfect for:

- 📚 Learning image processing concepts
- 🔬 Experimenting with computer vision algorithms
- 🎨 Quick image manipulation tasks
- 🧪 Testing different image processing techniques

---

## ✨ Features

### Core Operations

- 🖼️ **Image Display** - View original and processed images in resizable windows
- ⚫ **Grayscale Conversion** - Convert color images to grayscale
- 📊 **Histogram Analysis** - Display and analyze pixel intensity distribution
- ⚡ **Histogram Equalization** - Enhance image contrast automatically
- 💡 **Brightness Adjustment** - Modify brightness with saturation detection
- 🎯 **Custom Filtering** - Apply custom 3×3 kernel filters
- 🎭 **Masking Operations** - Create and apply random 500×500 pixel masks
- 🔍 **Edge Detection** - Canny edge detection algorithm
- 🌱 **Region Growing** - Interactive segmentation based on pixel similarity

### Key Highlights

✅ Interactive menu-driven interface  
✅ Real-time image processing  
✅ Visual feedback for all operations  
✅ Customizable parameters  
✅ Educational comments in code  
✅ Error handling and validation

---

## 🛠️ Tech Stack

| Technology     | Purpose                     | Version |
| -------------- | --------------------------- | ------- |
| **Python**     | Core programming language   | 3.7+    |
| **OpenCV**     | Image processing operations | 4.0+    |
| **NumPy**      | Numerical computations      | Latest  |
| **Matplotlib** | Data visualization          | Latest  |

---

## 📦 Installation

### Prerequisites

Ensure you have **Python 3.7 or higher** installed on your system:

```bash
python --version
```

### Step 1: Clone the Repository

```bash
git clone https://github.com/NassarBarahme/Image-Project.git
cd Image-Project
```

### Step 2: Install Dependencies

**Option 1: Using pip directly**

```bash
pip install opencv-python matplotlib numpy
```

**Option 2: Using requirements.txt** (recommended)

```bash
pip install -r requirements.txt
```

### Step 3: Prepare Your Image

1. Place your test image in an accessible location
2. Update the image path in `first.py`:

```python
path = r"C:\path\to\your\image.jpg"  # Update this line
```

---

## 🚀 Usage

### Running the Application

1. **Start the program:**

```bash
python first.py
```

2. **Select an operation** from the interactive menu by entering a number (1-9)

3. **Follow the prompts** for specific operations (e.g., threshold input for region growing)

4. **View results** in popup windows

5. **Exit** by selecting option 0

### Menu Overview

```
╔════════════════════════════════════════════════════════════╗
║           Image Processing Tool - Main Menu                ║
╠════════════════════════════════════════════════════════════╣
║  1. Read and show the input image                          ║
║  2. Convert the image to grayscale                         ║
║  3. Show the histogram of the grayscale image              ║
║  4. Perform histogram equalization                         ║
║  5. Modify the brightness of the image                     ║
║  6. Apply a 3×3 kernel filter                              ║
║  7. Perform a masking operation                            ║
║  8. Apply edge detection (Canny)                           ║
║  9. Region growing segmentation                            ║
║  0. Exit                                                   ║
╚════════════════════════════════════════════════════════════╝
```

---

## 🔍 Operations Guide

### 1. Show Input Image

Displays the original color image in a resizable window.

**Use case:** Verify your image loaded correctly

### 2. Grayscale Conversion

Converts the input image from BGR to grayscale using OpenCV's color space conversion.

**Output:** Grayscale version of the input image  
**Use case:** Prerequisite for most other operations

### 3. Histogram Display

Calculates and displays the histogram showing the distribution of pixel intensities (0-255).

**Output:** Line plot visualization  
**Use case:** Analyze image brightness distribution

### 4. Histogram Equalization

Applies histogram equalization to enhance contrast by redistributing pixel intensities.

**Benefits:**

- Improves contrast in low-contrast images
- Redistributes pixel intensities across full range
- Makes details more visible

**Output:**

- Equalized grayscale image
- Bar chart of new histogram

### 5. Brightness Modification

Randomly adjusts image brightness by scaling pixel values. **Saturated pixels (>255) are highlighted in red.**

**Process:**

1. Generates random scaling factor (0-2)
2. Multiplies all pixel values
3. Clips values to valid range [0, 255]
4. Highlights saturated regions

**Output:** Brightened/darkened image with saturation visualization

### 6. Custom Kernel Filtering

Applies a predefined 3×3 kernel to the image for filtering operations.

**Default Kernel:**

```python
[1, 2, 2]
[1, 8, 2]
[0, 6, 6]
```

**Use case:** Edge enhancement, blurring, sharpening

### 7. Masking Operation

Creates a random 500×500 pixel mask and applies it to show only a specific region.

**Process:**

1. Randomly selects position in image
2. Creates binary mask (500×500 pixels)
3. Applies mask using bitwise AND operation

**Output:** Image with only masked region visible

### 8. Edge Detection

Applies **Canny edge detection algorithm** to identify edges in the image.

**Parameters:**

- Lower threshold: 100
- Upper threshold: 100

**Output:** Binary edge map showing detected edges  
**Use case:** Object detection, feature extraction

### 9. Region Growing (Interactive)

Interactive segmentation tool that grows a region from a user-selected seed point.

**How to use:**

1. Click on the image to select a seed point
2. Enter a threshold value (0-255) when prompted
3. Algorithm grows region by including similar pixels

**Algorithm:**

- Uses stack-based flood fill approach
- Includes pixels within ±threshold of seed value
- Processes 4-connected neighbors

**Output:** Binary mask showing segmented region

---

## 💡 Examples

### Example 1: Basic Workflow

```bash
# Run the script
python first.py

# View original image
Enter your choice: 1

# Convert to grayscale
Enter your choice: 2

# View histogram
Enter your choice: 3

# Exit
Enter your choice: 0
```

### Example 2: Contrast Enhancement

```bash
# View original histogram
Enter your choice: 3

# Apply histogram equalization
Enter your choice: 4

# Compare before/after results
```

### Example 3: Interactive Region Growing

```bash
# Select region growing
Enter your choice: 9

# Click on desired region in the image
# Enter threshold (e.g., 20 for similar pixels)
Enter the threshold value (0-255): 20

# View the segmented region
```

---

## 📚 Functions Reference

### Core Functions

#### `show(name, img)`

Displays an image in a resizable window.

**Parameters:**

- `name` (str): Window name
- `img` (ndarray): Image array

**Returns:** None

---

#### `convert(img)`

Converts BGR image to grayscale.

**Parameters:**

- `img` (ndarray): BGR color image

**Returns:** Grayscale image (ndarray)

---

#### `histo(img)`

Displays histogram of grayscale image.

**Parameters:**

- `img` (ndarray): Grayscale image

**Returns:** None (shows matplotlib plot)

---

#### `equalize(img)`

Performs histogram equalization.

**Parameters:**

- `img` (ndarray): Grayscale image

**Returns:** None (displays equalized image and histogram)

---

#### `bright(img)`

Modifies brightness with random scaling and saturation detection.

**Parameters:**

- `img` (ndarray): Grayscale image

**Returns:** None (displays result)

---

#### `kernel(img)`

Applies 3×3 filter kernel.

**Parameters:**

- `img` (ndarray): Grayscale image

**Returns:** None (displays filtered image)

---

#### `mask500(img)`

Applies random 500×500 mask.

**Parameters:**

- `img` (ndarray): Grayscale image

**Returns:** None (displays masked image)

---

#### `edge_detection(img)`

Performs Canny edge detection.

**Parameters:**

- `img` (ndarray): Grayscale image

**Returns:** None (displays edge map)

---

#### `grow_R(img)`

Interactive region growing segmentation.

**Parameters:**

- `img` (ndarray): Grayscale image

**Returns:** None (displays segmented region)

---

## 🎨 Customization

### Changing the Kernel

Modify the kernel array in the `kernel()` function:

```python
f = np.array([[1, 0, -1],
              [2, 0, -2],
              [1, 0, -1]])  # Sobel X
```

### Adjusting Edge Detection Sensitivity

Modify thresholds in `edge_detection()`:

```python
s = cv2.Canny(img, 50, 150)  # Lower and upper thresholds
```

### Changing Mask Size

Modify the size variable in `mask500()`:

```python
size = 300  # Change to desired size
```

### Brightness Range

Modify the random range in `bright()`:

```python
c = np.random.uniform(0.5, 1.5)  # Customize min and max
```

---

## 🐛 Troubleshooting

### Image Not Found

**Error:** `Fail to find image`

**Solution:**

- Check that the file path is correct
- Ensure the file exists
- Use raw string `r"path"` for Windows paths

### Import Errors

**Error:** `ModuleNotFoundError: No module named 'cv2'`

**Solution:**

```bash
pip install opencv-python
```

### Window Display Issues

If windows don't appear or close immediately:

- Ensure you're not in a headless environment
- Check GUI display support
- Run from local Python installation

### Invalid Threshold Input

**Error:** `Invalid input. Please enter an integer.`

**Solution:** In region growing, enter **only integer values** for threshold.

### Memory Issues with Large Images

If processing large images causes crashes:

- Resize the image before processing
- Reduce mask size in `mask500()`
- Use a machine with more RAM

---

## 🎯 Future Enhancements

Potential improvements for this tool:

- [ ] Add morphological operations (erosion, dilation)
- [ ] Implement color image filtering
- [ ] Add image sharpening and blurring options
- [ ] Save processed images to disk
- [ ] Batch processing capability
- [ ] More segmentation algorithms (watershed, K-means)
- [ ] Image rotation and transformation
- [ ] GUI interface using Tkinter or PyQt
- [ ] Real-time webcam processing
- [ ] Export results to multiple formats

---

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Commit** your changes (`git commit -m 'Add amazing feature'`)
4. **Push** to the branch (`git push origin feature/amazing-feature`)
5. **Open** a Pull Request

### Contribution Ideas

- Add new image processing operations
- Improve error handling
- Enhance documentation
- Add unit tests
- Create example images

---

## 📝 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Nassar Barahme**  
_Computer Engineering Undergraduate | Full Stack Web & Mobile Developer_

- 💼 LinkedIn: [Nassar Barahme](https://www.linkedin.com/in/nassar-barahme)
- 🐙 GitHub: [@NassarBarahme](https://github.com/NassarBarahme)

---

## 🙏 Acknowledgments

- **OpenCV** - Open Source Computer Vision Library
- **Python Community** - For excellent documentation and support
- **NumPy & Matplotlib** - Essential scientific computing tools

---

## 📧 Support

For questions or issues:

- 📝 Open an [Issue](https://github.com/NassarBarahme/Image-Project/issues)
- 💬 Contact via GitHub

---

<div align="center">
  <p>⭐ If you find this project helpful, please give it a star!</p>
  <p>Made with ❤️ by Nassar Barahme</p>
</div>
