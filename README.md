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
- [Troubleshooting](#-troubleshooting)
- [Roadmap](#-roadmap)
- [Contributing](#-contributing)
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

 **Canva** is used to design the UI from where user can select three different colors and eraser.
---
