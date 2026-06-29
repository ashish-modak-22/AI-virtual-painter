# 🎨 AI Virtual Painter — Advanced Computer Vision Hand-Tracking Drawing Application

<div align="center">
  
![Python](https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white)
![OpenCV](https://img.shields.io/badge/OpenCV-4.x-5C3EE8?style=for-the-badge&logo=opencv&logoColor=white)
![MediaPipe](https://img.shields.io/badge/MediaPipe-0.10%2B-FF6F00?style=for-the-badge&logo=google&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-1.24%2B-013243?style=for-the-badge&logo=numpy&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Active-brightgreen?style=for-the-badge)
![Canva](https://img.shields.io/badge/Canva-00C4CC?style=for-the-badge&logo=canva&logoColor=white)

<br/>

**A real-time, AI-powered virtual painting application that uses your bare hand as a brush — no physical tools required.**

Built with Google's MediaPipe framework and OpenCV, this application uses 21-point hand landmark detection to translate natural finger gestures into digital art on a live webcam feed.
 
</div>

---

## 📖 Table of Contents
 
- [Project Overview](#-project-overview)
- [Features](#-features)
- [Demo](#-demo)
- [Tech Stack](#-tech-stack)
- [System Architecture](#-system-architecture)
- [Hand Landmark System](#-hand-landmark-system)
- [Computer Vision Pipeline](#-computer-vision-pipeline)
- - [Project Structure](#-project-structure)
- [Prerequisites](#-prerequisites)
- [Installation & Setup](#-installation--setup)
  - [Virtual Environment Setup (Recommended)](#virtual-environment-setup-recommended)
  - [Dependency Installation](#dependency-installation)
- [Configuration](#-configuration)
- [Usage Guide](#-usage-guide)
  - [Gesture Controls](#gesture-controls)
  - [Color Selection](#color-selection)
  - [Drawing Mode](#drawing-mode)
  - [Eraser Mode](#eraser-mode)
- [Module Breakdown](#-module-breakdown)
  - [HandTrackingModule.py](#handtrackingmodulepy)
  - [VirtualPainter.py](#virtualpainterpy)
- [Key Algorithms Explained](#-key-algorithms-explained)
  - [Bitwise Image Compositing](#bitwise-image-compositing)
  - [Finger State Detection](#finger-state-detection)
  - [Stroke Continuity Logic](#stroke-continuity-logic)
- [Performance & Optimization](#-performance--optimization)
- [License](#-license)
- [Acknowledgements](#-acknowledgements)

---
 
# 🧠 Project Overview
 
**AI Virtual Painter** is a touchless, real-time digital drawing system powered by computer vision and artificial intelligence. The application processes live webcam frames to detect and track 21 distinct hand landmarks using Google's **MediaPipe Hands** model, then interprets the spatial coordinates and relative finger positions as intuitive drawing gestures.
 
### This project demonstrates the intersection of several advanced domains in modern software engineering and AI:
 
- **Real-time Computer Vision** — processing 30+ frames per second from a live camera stream
- **AI-based Pose Estimation** — using a pre-trained neural network to detect hand skeleton topology
- **Image Processing** — multi-layer alpha compositing, binary masking, and bitwise operations
- **Human-Computer Interaction (HCI)** — designing gesture-based interfaces as an alternative to traditional input devices
- **Modular Software Design** — separating hand-tracking logic from application logic for reusability and testability
The result is a seamless painting experience where the user can switch colors, draw strokes, and erase content — entirely through hand gestures, with zero physical contact with any device.
 
---

# ✨ Features
 
- 🖐️ **Real-time Hand Tracking** — Detects and tracks 21 hand landmarks at up to 30 FPS using MediaPipe's deep learning model
- 🎨 **Multi-Color Drawing** — Supports Green, Purple, Cyan, and Eraser modes selectable via hand gesture
- ✍️ **Gesture-Based Mode Switching** — Seamlessly switch between Selection Mode and Drawing Mode using finger gestures
- 🖌️ **Smooth Stroke Rendering** — Continuous line drawing between frames using previous-position tracking to eliminate gaps
- 🧽 **Smart Eraser** — Black-color-based eraser with a wider brush thickness for comfortable erasing
- 🖼️ **Header UI Overlay** — Visual color palette overlaid directly on the camera feed for an intuitive interface
- 🔀 **Real-time Canvas Compositing** — Drawing canvas merged with the camera feed using bitwise image operations to keep the background visible
- 📷 **Mirror Mode** — Horizontal flip of the webcam feed for a natural mirror-like interaction
- 📐 **High-Resolution Support** — Operates at 1280×720 resolution for clear, high-fidelity drawing
- 🧩 **Modular Architecture** — Clean separation of the hand-tracking module from the main painter logic
---

## 🎥 Demo
 
> Draw freely in the air using just your index finger. Switch colors by raising both your index and middle fingers and pointing at the color palette at the top of the screen.

```
[Index Finger Up Only]     →  ✍️  Drawing Mode  (draws on canvas)
[Index + Middle Finger Up] →  🖱️  Selection Mode (hover over palette to change color)
[Black Color Selected]     →  🧽  Eraser Mode    (erases with wider brush)
```
 
---

# 🛠️ Tech Stack
 
| Technology | Version | Purpose |
|---|---|---|
| **Python** | 3.8+ | Core programming language |
| **OpenCV (`cv2`)** | 4.7+ | Frame capture, image processing, drawing primitives |
| **MediaPipe** | 0.10+ | Real-time AI hand landmark detection |
| **NumPy** | 1.24+ | Canvas array creation, pixel-level image operations |
| **OS (stdlib)** | Built-in | Directory traversal for header image loading |
| **Virtual Environment (`venv`)** | Built-in | Isolated Python runtime environment |
| **Canva** |  -------------- | For user interface to select colors |

 
### Why These Technologies?
 
**OpenCV** is the industry standard for real-time computer vision tasks. Its highly optimized C++ backend, exposed via Python bindings, allows frame-by-frame processing at camera speed without significant latency.
 
**MediaPipe** provides a production-grade, pre-trained hand landmark detection pipeline developed and maintained by Google. It delivers 21 3D landmarks per hand at high accuracy without requiring a GPU, making it accessible on standard consumer hardware.
 
**NumPy** is used to create and manipulate the drawing canvas as a raw pixel array (`np.zeros`), enabling efficient, low-level pixel operations that are faster than pure Python loops.
 
**Python Virtual Environment** ensures complete dependency isolation, preventing version conflicts with other Python projects on the same system and guaranteeing reproducible builds.

**Canva** is used to make UI from where user can select colors and eraser.

---

 
# 🏗️ System Architecture
 
The application follows a **layered pipeline architecture**, where each stage processes data and passes it to the next:
 
```
┌─────────────────────────────────────────────────────────────────┐
│                        WEBCAM INPUT LAYER                       │
│              cv2.VideoCapture → Frame Acquisition               │
│                  Resolution: 1280 x 720 @ 30FPS                 │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                    PRE-PROCESSING LAYER                         │
│            Horizontal Flip (Mirror Mode via cv2.flip)           │
│              BGR → RGB Conversion for MediaPipe                 │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│              AI HAND DETECTION & LANDMARK LAYER                 │
│         MediaPipe Hands Model (min_detection_conf: 0.8)         │
│           Outputs: 21 Landmarks (x, y, z) per Hand             │
│           Draws: Hand skeleton + connections on frame           │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                  GESTURE RECOGNITION LAYER                      │
│       fingersUp() → Encodes 5-bit finger state vector           │
│   [Thumb, Index, Middle, Ring, Pinky] → e.g. [0,1,0,0,0]       │
│   Selection Mode: [_,1,1,_,_] | Drawing Mode: [_,1,0,_,_]      │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                 APPLICATION LOGIC LAYER                         │
│  ┌──────────────────────┐    ┌──────────────────────────────┐   │
│  │   SELECTION MODE     │    │       DRAWING MODE           │   │
│  │  - Color picking     │    │  - Stroke rendering          │   │
│  │  - Palette highlight │    │  - Previous pos tracking     │   │
│  │  - Header update     │    │  - Eraser detection          │   │
│  └──────────────────────┘    └──────────────────────────────┘   │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                IMAGE COMPOSITING LAYER                          │
│   drawing_canvas (NumPy array) → Gray → Binary Mask → Invert   │
│   bitwise_and(camera_frame, inverted_mask)                      │
│   bitwise_or(masked_frame, drawing_canvas)                      │
│   Overlay Header UI on top [0:125, 0:1280]                      │
└───────────────────────────┬─────────────────────────────────────┘
                            │
                            ▼
┌─────────────────────────────────────────────────────────────────┐
│                      OUTPUT LAYER                               │
│              cv2.imshow("Virtual Painter", img)                 │
│                   Real-time display window                      │
└─────────────────────────────────────────────────────────────────┘
```
 
---

# 🖐️ Hand Landmark System
 
MediaPipe detects **21 landmarks** on each hand, each identified by a unique integer ID. This project uses the following key landmarks:
 
```
                8   12  16  20
                |   |   |   |
                7   11  15  19
            4   |   |   |   |
            |   6   10  14  18
            3   |   |   |   |
            |   5---9--13--17
            2       |
             \      |
              1     |
               \    |
                0 (WRIST)
```
| Landmark ID | Name | Role in This Project |
|---|---|---|
| 0 | WRIST | Base reference point |
| 4 | THUMB_TIP | Thumb state detection |
| 3 | THUMB_IP | Thumb state comparison |
| 8 | INDEX_FINGER_TIP | Primary drawing point / pointer |
| 6 | INDEX_FINGER_PIP | Finger raise comparison |
| 12 | MIDDLE_FINGER_TIP | Selection mode detection |
| 10 | MIDDLE_FINGER_PIP | Finger raise comparison |
| 16 | RING_FINGER_TIP | State detection |
| 20 | PINKY_TIP | State detection |
 
The `tipId` list `[4, 8, 12, 16, 20]` corresponds to the tip of each finger (Thumb → Pinky), and each is compared to the joint two steps below it (the PIP joint) to determine if the finger is extended.
 
---

# 🔬 Computer Vision Pipeline
 
### Frame Acquisition
 
Each iteration of the main loop reads a raw BGR frame from the webcam at 1280×720 resolution. The frame is immediately flipped horizontally (`cv2.flip(img, 1)`) to create a natural mirror experience, ensuring the user's right hand appears on the right side of the screen.
 
### Hand Detection
 
The frame is converted from BGR (OpenCV default) to RGB (MediaPipe requirement) and passed to the `hands.process()` method. The underlying model is a lightweight MobileNet-based CNN that predicts 21 3D keypoints per hand.

### Coordinate Normalization
 
MediaPipe returns normalized coordinates in the range `[0.0, 1.0]`. These are multiplied by the frame's actual pixel dimensions (`width`, `height`) to get pixel-space coordinates:
 
```python
cx = int(landmark.x * w)
cy = int(landmark.y * h)
```
 
### Canvas Compositing
 
The drawing canvas is a black NumPy array (`np.zeros((720, 1280, 3), np.uint8)`). To merge it with the live camera feed without losing the background:
 
1. Convert canvas to grayscale
2. Apply binary inverse threshold — drawn pixels become black (0), empty canvas becomes white (255)
3. Convert inverted mask back to BGR
4. `bitwise_and` the camera frame with the inverted mask → **punches holes** where drawing exists
5. `bitwise_or` the punched frame with the drawing canvas → **fills the holes** with drawing colors
This is equivalent to alpha-blending, implemented entirely via logical bitwise operations on pixel arrays.
 
---
 
# 📁 Project Structure
 
```
ai-virtual-painter/
│
├── 📄 VirtualPainter.py          # Main application entry point
├── 📄 HandTrackingModule.py      # Reusable hand detection class
│
├── 📁 Header_Images/             # UI color palette overlay images
│   ├── 1.png                     # Green color header
│   ├── 2.png                     # Purple color header
│   ├── 3.png                     # Cyan color header
│   └── 4.png                     # Eraser (black) header
│
├── 📄 requirements.txt           # Python package dependencies
├── 📄 README.md                  # Project documentation (you are here)
└── 📄 .gitignore                 # Git ignore rules
```
 
> **Note:** The `Header_Images/` folder must contain exactly 4 images corresponding to the four color/tool options. The images are loaded in alphabetical/directory order, so naming them `1.png` through `4.png` ensures correct ordering.
 
---

# ⚙️ Prerequisites
 
Before running this project, ensure your system meets the following requirements:
 
- **Python 3.8 or higher** — [Download Python](https://www.python.org/downloads/)
- **A working webcam** — Built-in or USB webcam (minimum 720p recommended)
- **pip** — Python's package manager (bundled with Python 3.4+)
- **Git** — For cloning the repository
- **Adequate lighting** — MediaPipe hand detection accuracy improves significantly in well-lit environments

 ### Hardware Recommendations
 
| Component | Minimum | Recommended |
|---|---|---|
| CPU | Intel i5 / AMD Ryzen 5 | Intel i7 / AMD Ryzen 7 |
| RAM | 4 GB | 8 GB+ |
| Webcam | 720p @ 30FPS | 1080p @ 30FPS |
| GPU | Not required | NVIDIA GPU (for future GPU acceleration) |
 
---

# 🚀 Installation & Setup
 
## 1. Clone the Repository
 
```bash
git clone https://github.com/ashish-modak-22/AI-virtual-painter.git
cd AI-virtual-painter
```
 
## Virtual Environment Setup (Recommended)
 
Using a Python virtual environment is **strongly recommended** and was used during the development of this project. A virtual environment creates an isolated Python runtime, meaning the packages installed for this project will not interfere with your global Python installation or any other projects.
 
### On Windows
 
```bash
# Create virtual environment
python -m venv venv
 
# Activate the virtual environment
venv\Scripts\activate
 
# Your terminal prompt should now show (venv) at the beginning
# Example: (venv) C:\Users\YourName\ai-virtual-painter>
```
 
### On macOS / Linux
 
```bash
# Create virtual environment
python3 -m venv venv
 
# Activate the virtual environment
source venv/bin/activate
 
# Your terminal prompt should now show (venv) at the beginning
# Example: (venv) user@machine:~/ai-virtual-painter$
```
 
### Verifying the Virtual Environment is Active
 
```bash
# Should point to your project's venv, not the global Python
which python        # macOS/Linux
where python        # Windows
```
### Deactivating the Virtual Environment
 
When you're done working on the project, deactivate the virtual environment:
 
```bash
deactivate
```
 
> ⚠️ **Important:** Always activate your virtual environment before running the project or installing new dependencies. All subsequent commands assume the virtual environment is active.
 
---
 
## Dependency Installation
 
With the virtual environment active, install all required packages:
 
```bash
pip install -r requirements.txt
```
 
If a `requirements.txt` is not present, install the dependencies manually:
 
```bash
pip install opencv-python mediapipe numpy
```
 
### Verify Installations
 
```bash
python -c "import cv2; print('OpenCV:', cv2.__version__)"
python -c "import mediapipe as mp; print('MediaPipe:', mp.__version__)"
python -c "import numpy as np; print('NumPy:', np.__version__)"
```
 
---
 
## 3. Prepare Header Images
 
The application requires 4 header UI images inside the `Header_Images/` directory. Each image must be **1280 × 125 pixels** (to match the camera resolution and header height).
 
Create or download 4 toolbar images representing your color palette:
 
| File | Color | Hex Value |
|---|---|---|
| `1.png` | Green | `(0, 255, 0)` in BGR |
| `2.png` | Purple/Magenta | `(255, 0, 255)` in BGR |
| `3.png` | Cyan | `(0, 255, 255)` in BGR |
| `4.png` | Eraser (Black) | `(0, 0, 0)` in BGR |
 
> **Tip:** You can design these header images using any image editor (Photoshop, GIMP, Canva, etc.). Make sure each image clearly shows the color zones and the clickable region boundaries described in the source code.
 
---
 
## 4. Generate `requirements.txt` (For Contributors)
 
If you want to regenerate the `requirements.txt` after installing new packages:
 
```bash
pip freeze > requirements.txt
```
 
---

 
# ▶️ Usage Guide
 
Run the main application with:
 
```bash
python VirtualPainter.py
```
 
A window titled **"Virtual Painter"** will open showing your webcam feed with the color palette header overlaid at the top.
 
Press **`s`** to exit the application cleanly.
 
---
 
## Gesture Controls
 
The entire application is controlled through two primary hand gestures detected by the AI model:
 
| Gesture | Fingers Up | Mode | Description |
|---|---|---|---|
| ☝️ Index only | `[_, 1, 0, _, _]` | **Drawing Mode** | Draws on canvas at index finger tip position |
| ✌️ Index + Middle | `[_, 1, 1, _, _]` | **Selection Mode** | Move hand to palette to change color/tool |
 
> **Note:** The `_` in the finger vector means the state of that finger (Thumb, Ring, Pinky) does not affect the mode detection — only the Index and Middle finger states are used.

 ---
 
### Color Selection
 
1. Raise both your **index and middle fingers** (enter Selection Mode)
2. Move your hand so the index finger tip enters the **top 125 pixels** of the screen (the header region)
3. Hover over the desired color zone:
| Screen X Range | Color Selected | BGR Value |
|---|---|---|
| `250 – 450` | 🟢 Green | `(0, 255, 0)` |
| `550 – 750` | 🟣 Purple | `(255, 0, 255)` |
| `800 – 950` | 🟡 Yellow | `(0, 255, 255)` |
| `1050 – 1200` | ⬛ Eraser | `(0, 0, 0)` |
 
A colored rectangle is drawn between your index and middle finger tips as visual feedback for the currently selected color.
 
---

### Drawing Mode
 
1. Raise only your **index finger** (curl middle, ring, and pinky)
2. A circle indicator appears at your fingertip to show the active brush color
3. Move your hand freely — the application draws continuous lines connecting each frame's fingertip position to the previous one
4. The first frame you enter drawing mode sets the "pen down" starting position — no accidental strokes when switching from selection mode
---
 
### Eraser Mode
 
1. Select the **black (eraser)** color from the palette using Selection Mode
2. Switch to Drawing Mode (index finger only)
3. The eraser uses a **wider brush thickness** (`eraserThickness = 50`) compared to the regular brush (`brushThickness = 15`) for comfortable erasing
> The eraser works by drawing black pixels (`(0, 0, 0)`) on the drawing canvas. Since the compositing pipeline uses black as "transparent," black strokes effectively erase previously drawn content.
 
---
 
# 📦 Module Breakdown
 
### `HandTrackingModule.py`
 
This module encapsulates all hand-detection functionality into a clean, reusable `HandDetector` class. It is designed to be imported independently of the painter logic, making it suitable for other computer vision projects.
 
#### Class: `HandDetector`
 
```python
class HandDetector:
    def __init__(self, maxHands=2, detectionCon=0.5)
```
**Constructor Parameters:**
 
| Parameter | Type | Default | Description |
|---|---|---|---|
| `maxHands` | `int` | `2` | Maximum number of hands to detect simultaneously |
| `detectionCon` | `float` | `0.5` | Minimum confidence threshold for detection (0.0–1.0) |
 
In `VirtualPainter.py`, `detectionCon` is increased to `0.8` for higher precision, reducing false positives at the cost of slightly reduced recall in difficult lighting.
 
---
 
#### Method: `findHands(img)`
 
```python
def findHands(self, img) -> np.ndarray
```
 
Processes a BGR frame, runs it through MediaPipe's hand detection pipeline, and draws skeleton landmarks and connections onto the frame.
 
- Converts BGR → RGB internally for MediaPipe compatibility
- Stores results in `self.results` for downstream use
- Draws landmarks using `mp_draw.draw_landmarks()` with `HAND_CONNECTIONS`
- Returns the annotated frame
---
 
#### Method: `findPosition(img, handNo=0, draw=True)`
 
```python
def findPosition(self, img, handNo=0, draw=True) -> list
```
 
Extracts the pixel-space coordinates of all 21 landmarks for a specified hand.
 
**Returns:** A list of `[id, cx, cy]` tuples for each of the 21 landmarks.
 
| Return Index | Content |
|---|---|
| `lmList[0]` | `[0, wrist_x, wrist_y]` |
| `lmList[8]` | `[8, index_tip_x, index_tip_y]` |
| `lmList[12]` | `[12, middle_tip_x, middle_tip_y]` |
 
---
 
#### Method: `fingersUp()`
 
```python
def fingersUp(self) -> list[int]
```
 
Returns a **5-element binary list** representing the state of each finger:
 
```
[Thumb, Index, Middle, Ring, Pinky]
  0/1    0/1    0/1    0/1    0/1
```
 
**Logic:**
 
- **Thumb:** Compares tip X-coordinate to the joint below it. Since the thumb moves horizontally (for a hand facing the camera), an X-based comparison is used instead of Y.
- **Other 4 fingers:** Each tip's Y-coordinate is compared to the PIP joint (2 joints below). In OpenCV's coordinate system, Y increases downward — so a **smaller Y** at the tip means the finger is pointing **up**.
---
 
#### Method: `findDistance(p1, p2, img)`
 
```python
def findDistance(self, p1, p2, img) -> float
```
 
Computes the Euclidean distance in pixels between two landmarks identified by their IDs.
 
```
distance = sqrt((x2-x1)² + (y2-y1)²)
```
 
This method is available for extension — it can be used to detect pinch gestures (e.g., distance between landmark 4 and 8 for thumb-index pinch), which can trigger additional controls in future iterations.
 
---

### `VirtualPainter.py`
 
This is the main application script. It orchestrates the webcam feed, integrates the `HandDetector`, manages the drawing canvas, and handles all UI logic.

---

# 🔑 Key Algorithms Explained
 
### Bitwise Image Compositing
 
The core challenge of this project is merging a transparent-feeling drawing layer on top of a live camera feed, given that OpenCV has no native transparency support for real-time frames.
 
The solution uses a 4-step bitwise mask approach:
 
```python
# Step 1: Convert canvas to grayscale
gray_image = cv2.cvtColor(drawing_canvas, cv2.COLOR_BGR2GRAY)
 
# Step 2: Binary inverse threshold
# Empty canvas (black=0) → White (255)  [background]
# Drawn pixels (color≠0) → Black (0)    [foreground holes]
_, inverse_image = cv2.threshold(gray_image, 50, 255, cv2.THRESH_BINARY_INV)
 
# Step 3: Convert mask back to 3-channel BGR for bitwise ops
inverse_image = cv2.cvtColor(inverse_image, cv2.COLOR_GRAY2BGR)
 
# Step 4a: AND — Keep only background (zero out where drawing exists)
img = cv2.bitwise_and(img, inverse_image)
 
# Step 4b: OR — Fill the zeroed regions with the colored drawing
img = cv2.bitwise_or(img, drawing_canvas)
```
 
**Why this works:**
 
- `bitwise_and` with an inverted mask sets drawn pixels in the camera frame to `0` (black)
- `bitwise_or` then merges the colorful drawing canvas into those now-black regions
- Result: drawing appears to float on top of the real camera feed
---
 
### Finger State Detection
 
The `fingersUp()` function encodes hand pose into a compact 5-bit vector using anatomical landmark comparisons:
 
```python
def fingersUp(self):
    fingers = []
 
    # Thumb: horizontal comparison (X axis)
    if self.lmList[self.tipId[0]][1] < self.lmList[self.tipId[0]-1][1]:
        fingers.append(1)
    else:
        fingers.append(0)
 
    # Fingers 1-4: vertical comparison (Y axis)
    for id in range(1, 5):
        if self.lmList[self.tipId[id]][2] < self.lmList[self.tipId[id]-2][2]:
            fingers.append(1)
        else:
            fingers.append(0)
 
    return fingers
```
 
---
 
### Stroke Continuity Logic
 
A naive implementation would only draw a circle at the current fingertip position each frame. This produces a dotted/dashed trail at moderate drawing speeds. The solution tracks the **previous frame's position** and draws a line between consecutive positions:
 
```python
if not drawing_started:
    # First frame entering draw mode — set anchor point
    x_previous, y_previous = x_index, y_index
    drawing_started = True
else:
    # Subsequent frames — draw connecting line
    cv2.line(drawing_canvas,
             (x_previous, y_previous),
             (x_index, y_index),
             selected_color, brushThickness)
    x_previous, y_previous = x_index, y_index
```
 
---

# ⚡ Performance & Optimization
 
### Current Performance Profile
 
| Metric | Value |
|---|---|
| Target FPS | 30 FPS |
| Resolution | 1280 × 720 |
| Detection Confidence | 0.8 |
| Max Hands Tracked | 2 (configurable) |
| CPU Usage (typical) | 30–60% (single core) |
 
### Optimization Tips
 
- **Lower resolution** for slower systems: Change `cap.set(3, 640)` and `cap.set(4, 480)` and update canvas size accordingly
- **Reduce `detectionCon`** to `0.6` or `0.5` for faster but less precise detection in well-lit environments
- **Set `maxHands=1`** if only single-hand use is needed — halves the detection workload
- **Avoid running other GPU-intensive tasks** in parallel, as MediaPipe shares CPU resources
---

# 📄 License
 
This project is licensed under the **MIT License** — you are free to use, modify, and distribute this software for personal or commercial purposes with attribution.
 
```
MIT License
 
Copyright (c) 2024 [Your Name]
 
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
 
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
```
 
---
# 🙏 Acknowledgements
 
- **[Google MediaPipe](https://mediapipe.dev/)** — For the open-source, production-quality hand landmark detection model that powers the core AI functionality of this project
- **[OpenCV](https://opencv.org/)** — For the comprehensive, battle-tested computer vision library used for all image processing operations
- **[NumPy](https://numpy.org/)** — For efficient multi-dimensional array operations enabling the drawing canvas implementation
---

<div align="center">
  
**Built with ❤️ using Python, OpenCV, and MediaPipe**
 
</div>
