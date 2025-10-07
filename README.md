# Square Vision (2D)

**Type:** Undergraduate Capstone  
**Institution:** Virginia Military Institute  
**Course:** CIS 480/490 Capstone  
**Date:** 3 May 2023  
**Grade:** 100/100  

---

## Description
Object recognition app using OpenCV’s DNN module with a pre-trained SSD MobileNet v3 model. Final deliverable for VMI CIS 490 Capstone Team 1.  
The `main` branch contains the final runnable code and links to sprint branches for the full history.

## Features
- Real-time detection from internal or external camera
- Configurable confidence and non-max suppression thresholds
- FPS overlay and labeled bounding boxes
- CustomTkinter GUI with a Help window

## Quick Start

Requirements
- Python 3.8 or later
- OpenCV, NumPy, CustomTkinter

Install
```bash
py -m pip install --upgrade pip
py -m pip install opencv-python numpy customtkinter
```
Run the app
```bash
python main.py
```

## Controls
- Select Internal or External camera
- Enter confidence threshold (1 to 100) then Confirm
- Enter NMS threshold (1 to 100) then Confirm
- Custom Settings runs with your inputs
- Default Settings uses camera 0, confidence 50, NMS 20
- Press q in the OpenCV window to quit
- Click Help for instructions and term definitions

### Image detection utility
```bash
# Edit the filename in image_dect.py to one of:
# testImage1.jpg, testImage2.jpg, testImage3.jpg
python image_dect.py
```
## Repository Structure

- `main.py` — GUI entry point that drives the `Detector` class  
- `Detector.py` — Detection class for model load, inference, drawing, FPS  
- `image_dect.py` — Single image detection helper  
- `model_data/`
  - `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt`
  - `frozen_inference_graph.pb`
  - `coco.names`
- `testImage1.jpg`, `testImage2.jpg`, `testImage3.jpg`, `vmi.png` — Sample images  
- `test2.py` — CustomTkinter widget demo (optional)  
- `.github/workflows/blank.yml` — Placeholder workflow  
- `__pycache__/` — Ignored cache  

## Development Timeline

Each sprint branch captures the state at that time.

- [Sprint 1](https://github.com/wieckingcp23/vmi-team1-capstone-squarevision/tree/Sprint-1) — Webcam spike and Haar face detection  
- [Sprint 2](tree/Sprint2) — SSD MobileNet v3 on COCO for webcam and images  
- [Sprint 3](tree/Sprint3) — Basic Tkinter GUI, timing, new test images  
- [Sprint 4](tree/Sprint4) — GUI refinements, confidence slider, timer input  
- [Sprint 5](tree/Sprint5) — Detector class refactor and CustomTkinter GUI  
- [Sprint 6](tree/Sprint6) — Cleanup, path consolidation, minor fixes  
- [Sprint 7](tree/Sprint7) — Final bug fixes, Help window, final polish  

## Notes and Limitations

- All model files must remain in `model_data`  
- The GUI runs on a single thread while detection is active  
- Input validation shows warnings but does not catch every edge case  
- Camera index may vary by system. If an external camera is not detected, try switching the radio button or adjust the index in code  

## Team

- Peyton Wiecking:[@wieckingcp23](https://github.com/wieckingcp23) 
- John Barker: [@JohnBC11121](https://github.com/JohnBC11121)
- Connor Holland: @hollandcw23 - _Inactive Account_
- Ian Salyers: [@SalyersIJ](https://github.com/SalyersIJ)

Instructor: [Dr. Denis Gracanin](https://people.cs.vt.edu/~gracanin/home/Home.html)  
Advisor: [Dr. Imran Ghani](https://www.researchgate.net/profile/Imran-Ghani-2)

### Academic Use Disclaimer
This repository is an archived academic project completed as part of coursework at the [Virginia Military Institute](https://www.vmi.edu/cadet-life/cadet-leadership-and-development/honor-system/). It is provided **for portfolio and reference purposes only**.  

If you are a current student, do not copy or submit this work as your own. Course assignments may have changed since this project was completed, and instructors use plagiarism detection tools.

Use this repository only as a learning reference.
