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
 
## 🧠 Project Overview
 
**AI Virtual Painter** is a touchless, real-time digital drawing system powered by computer vision and artificial intelligence. The application processes live webcam frames to detect and track 21 distinct hand landmarks using Google's **MediaPipe Hands** model, then interprets the spatial coordinates and relative finger positions as intuitive drawing gestures.
 
