# 🖼️ PixelWise - Interactive Image Processing Learning App

## 📌 Overview

**PixelWise** is an interactive web application built using **Streamlit** that helps users learn fundamental concepts of **Image Processing** in a practical and engaging way.

The app provides multiple lessons where users can upload images and apply different image processing techniques in real-time.

---

## 🎯 Objective

The main goal of this project is to:

* Simplify image processing concepts
* Provide hands-on learning experience
* Combine theory with real-time practice

---

## 🛠️ Technologies Used

* Python
* Streamlit (Web Application Framework)
* OpenCV (Computer Vision & Image Processing)
* NumPy
* Pillow (PIL)

---

## 🚀 Features

### 🏠 Home Page

* Simple and clean interface
* Easy navigation between lessons

---

### 📚 Lessons Included

#### 1️⃣ Digital Image

* Displays image properties:

  * Dimensions
  * Number of channels
  * Bit depth

---

#### 2️⃣ Color Systems

* Convert image to:

  * Grayscale
  * HSV
  * RGB channels (R, G, B)
* Download processed images

---

#### 3️⃣ Pixel Operations

* Adjust:

  * Brightness
  * Contrast
* Interactive sliders for real-time changes

---

#### 4️⃣ Filters & Convolution

* Apply filters:

  * Gaussian Blur
  * Sobel (X, Y)
  * Laplacian

---

#### 5️⃣ Noise Removal

* Remove noise using:

  * Gaussian Blur
  * Median Filter

---

#### 6️⃣ Edge Detection

* Detect edges using:

  * Canny
  * Sobel

---

#### 7️⃣ Morphological Operations

* Perform operations:

  * Erosion
  * Dilation
  * Opening
  * Closing

---

#### 8️⃣ Geometric Transformations

* Apply transformations:

  * Rotation
  * Scaling (Zoom in / Zoom out)
  * Cropping

---

## 🖥️ How It Works

1. Open the application
2. Select a lesson
3. Upload an image
4. Apply different image processing techniques
5. View results instantly
6. Download the processed image

---

## ▶️ Installation & Run

### 1. Install dependencies

```
pip install streamlit opencv-python pillow numpy
```

### 2. Run the application

```
streamlit run main.py
```

---

## 📁 Project Structure

```
 Photo-Project   
├── PixelWise/
    │
    ├── main.py
    ├── Images/
    │   ├── .png
    │   ├── .png
    │   ├── .png
    │   └── ...
    ├── requirements.txt
```

---

## 💡 Key Concepts

* Image Processing fundamentals
* Computer Vision basics
* Interactive UI development
* Real-time image manipulation

---

## 🎓 Use Cases

* Students learning Computer Vision
* Beginners in OpenCV
* Educational demonstrations
* Academic projects

---

## ⚠️ Notes

* Ensure the `Images` folder exists with required images
* Some operations require RGB or grayscale formats

---

## 🚀 Future Improvements

* Add Face Detection
* Add Object Detection
* Support video processing
* Integrate AI-based image enhancement

---

## 👩‍💻 Author

Balqees
