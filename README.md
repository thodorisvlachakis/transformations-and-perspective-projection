# Transformations and Perspective Projection

This repository contains the implementation of the second assignment of the Computer Graphics course.  
The goal of this assignment is to implement affine transformations, camera modeling, and perspective projection, and to render a 3D object onto a 2D image.

Some utility functions for triangle rendering had already been implemented in the first assignment, for triangle filling and shading, and are being reused in the current project.
See also: [Triangle Rasterization](https://github.com/thodorisvlachakis/triangle-rasterization-and-shading)

---

## 📌 Overview

This assignment explores the fundamental concepts behind transforming and rendering 3D objects in computer graphics.

Starting from a set of 3D points that define an object, the implemented pipeline applies affine transformations, simulates a virtual camera, projects the object onto a 2D plane using perspective projection, and finally maps it to image pixel coordinates for rendering.

The assignment focuses on the fundamental steps of this computer graphics pipeline:

- Affine transformations (rotation, translation)
- Camera positioning and orientation
- Transformation from world coordinates to camera coordinates
- Perspective projection using a pinhole camera model
- Rasterization of projected points to image pixels
- Rendering of a 3D object using Gouraud shading

---

## ✨ Features

- Implementation of a full transformation pipeline (rotation & translation)
- Camera modeling using `lookat` functionality
- World-to-view coordinate transformation
- Perspective projection of 3D points with pinhole camera model
- Rasterization from continuous plane to discrete pixels (from camera plane to pixel grid)
- Rendering of 3D objects using triangle-based representation
- Integration with Gouraud shading

---

## 🛠️ Technologies

- Python 3
- NumPy
- Matplotlib
- OpenCV (cv2)

---

## 📂 Repository Structure

```
transformations-and-perspective-projection
│
├── src/                    # Python source code
│ ├── compute_lines_triangle.py
│ ├── demo.py
│ ├── f_shading.py
│ ├── g_shading.py
│ ├── lookat.py
│ ├── perspective_project.py
│ ├── rasterize.py
│ ├── render_img.py
│ ├── render_object.py
│ ├── sort_vertices.py
│ ├── TransformClass.py
│ ├── vector_interp.py
│ └── world2view.py
│
├── data/                   # Input data
│ └── hw2.npy
│
├── outputs/                # Generated images
│ ├── Initial_Object_Image.jpg
│ ├── aCase_Object_Image.jpg
│ ├── bCase_Object_Image.jpg
│ └── cCase_Object_Image.jpg
│
├── docs/                   # Documentation
│ ├── hw2_2024.pdf
│ └── report.pdf
│
├── README.md
└── .gitignore

```
---

## ⚙️ How to Run

### 1. Requirements

Make sure you have the following installed:

- Python 3.x  
- NumPy  
- Matplotlib  
- OpenCV  

You can install the required libraries using:

```bash
pip install numpy matplotlib opencv-python

```

### 2. Run the demos

Navigate to the src/ folder and run:
    _python demo.py_

The demo scripts load the required input data internally and generate the final rendered images.
The required input data is provided in the data/ folder.

---

## 🧠 Key Concepts

- Affine transformations in homogeneous coordinates
- Camera coordinate system and view transformation
- Perspective projection (pinhole camera model)
- Mapping from continuous space to discrete image grid (rasterization)
- Triangle-based rendering and shading

---

## 📄 Notes

- Rendering is performed using Gouraud shading, but .
- The background of the generated images is white.
- All computations are performed using NumPy arrays.
- OpenCV (cv2) is used for image post-processing (scaling, image resizing and color format conversion) before saving the final output.