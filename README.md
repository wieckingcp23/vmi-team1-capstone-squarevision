# Square Vision — 2D Object Recognition Capstone

**Course(s):** CIS 480 (Pre-Capstone) and CIS 490 (Capstone)  
**Institution:** Virginia Military Institute  
**Semester:** 2022–2023  
**Team Members:** Peyton Wiecking, John Barker, Connor Holland, Ian Salyers  
**Instructor:** Dr. Denis Gracanin  
**Advisor:** Dr. Imran Ghani  

---

## Overview
Square Vision is an object recognition software project developed as part of the senior capstone sequence at VMI. The project goal was to design and implement a **computer vision application** capable of identifying and highlighting objects in a 2D video stream.  

This repository contains the **2D implementation** of Square Vision, including sprint code submissions and documentation produced during the development cycle.

---

## Features
- Implemented with **Python** and the **OpenCV** library for image processing.  
- Basic **object detection** using contour analysis and region identification.  
- User interface elements created with **Tkinter** and **CustomTkinter**.  
- Iterative development across **seven sprints**, with progressively refined functionality.  

---

## Repository Structure
- **Sprint Branches:** Each branch (`Sprint1` through `Sprint7`) contains the code and artifacts submitted for that sprint.  
- **Main Branch:** Contains consolidated 2D implementation code and documentation.  

---

## Requirements
- Python 3.8+  
- Libraries:  
  ```bash
  py -m ensurepip --upgrade
  py -m pip install opencv-python
  py -m pip install customtkinter --upgrade
  ```

---

## Learning Outcomes
- Applied computer vision concepts using OpenCV
- Designed and tested a Python GUI for interactive recognition
- Practiced iterative development with sprint-based deliverables
- Gained experience in team collaboration, project planning, and code versioning with GitHub

--- 

## Notes
- This repository is preserved as an academic artifact.
- The project demonstrates the challenges and learning outcomes of a senior capstone, but is not actively maintained
# Square Vision — Sprint 7 (Final)

**Course:** CIS 480 Pre-Capstone / CIS 490 Capstone  
**Institution:** Virginia Military Institute  
**Sprint:** 7  
**Branch:** `Sprint7`

## Summary
Final sprint focused on stability and UX. The CustomTkinter GUI is finalized, `customMode` respects the selected camera, and a Help window explains usage and terms. Detector remains a class with configurable confidence and NMS thresholds. A simple CustomTkinter widget demo is included for UI testing.

## Repository Contents
- `main.py` — Primary GUI using the `Detector` class with Help window
- `Detector.py` — Detection class (model load, inference, drawing, FPS)
- `image_dect.py` — Detection on a single image (edit the filename in the script)
- `test2.py` — CustomTkinter UI demo sandbox
- `model_data/` — `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt`, `frozen_inference_graph.pb`, `coco.names`
- `testImage1.jpg`, `testImage2.jpg`, `testImage3.jpg`, `vmi.png` — Sample images
- `__pycache__/` — Auto-generated cache (ignored)
- `.github/workflows/blank.yml` — Placeholder workflow
- `README.md` — Project overview and instructions

## How to Run
Requirements:
- Python 3.8 or later
- OpenCV, NumPy, CustomTkinter

Install:
```bash
py -m pip install --upgrade pip
py -m pip install opencv-python numpy customtkinter
```
Run the app:
```bash
python main.py
```

## Controls:
- Select Internal or External camera
- Enter Confidence Threshold (1–100) and click Confirm
- Enter NMS Threshold (1–100) and click Confirm
- Custom Settings runs with your inputs. Default Settings runs with camera 0, confidence 50, NMS 20
- Press q in the OpenCV window to quit.
- Click Help for instructions and definitions.

### Image detection:
```bash
# Open image_dect.py and change the filename to one of:
# 'testImage1.jpg', 'testImage2.jpg', 'testImage3.jpg'
python image_dect.py
```
### Optional UI demo:
```bash
python test2.py
```

## Notes and Limitations
- All model files must remain in model_data
- GUI is single threaded and may block while detection runs
- Input validation shows warnings but does not block all edge cases
