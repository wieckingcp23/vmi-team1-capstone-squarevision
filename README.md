# Square Vision — Sprint 5

**Course:** CIS 480 Pre-Capstone / CIS 490 Capstone  
**Institution:** Virginia Military Institute  
**Sprint:** 5  
**Branch:** `Sprint5`

## Summary
This sprint refactors the project to be more modular and introduces a redesigned GUI. Detection logic is now encapsulated in a `Detector` class, and the interface is built with CustomTkinter for a cleaner user experience. The GUI supports selecting a camera, setting confidence and NMS thresholds, and running the program with either default or custom settings.

## Repository Contents
- `main.py` — Application entry point with CustomTkinter GUI  
- `Detector.py` — Detection class handling model load, inference, and display  
- `image_dect.py` — Object detection on still images (`group.jpg`)  
- `test.py` — Simple test script  
- `model_data/` — Contains `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt`, `frozen_inference_graph.pb`, and `coco.names`  
- `names/` — Label files for object classes 
- `vmi.png`- GUI Element 
- `testImage1.jpg`, `testImage2.jpg`, `testImage3.jpg` — Sample images for testing  
- `oldCode.py` — Archived script  
- `__pycache__/` — Auto-generated cache (not needed for version control)  
- `.github/workflows/blank.yml` — Placeholder workflow  

## How to Run (Sprint 5)
Requirements:
- Python 3.8 or later  
- OpenCV, NumPy, and CustomTkinter

Install dependencies:
```bash
py -m pip install --upgrade pip
py -m pip install opencv-python numpy customtkinter
Run the GUI:

bash
Copy code
python main.py
Controls:

Select Camera: Internal (0) or External (1)

Confidence Threshold: Enter value between 1 and 100

NMS Threshold: Enter value between 1 and 100

Custom Settings: Runs with chosen options

Default Settings: Internal camera, confidence = 50%, NMS = 20%

Press q in the OpenCV window to quit.

Notes and Limitations
model_data and names folders must be present with the expected files

GUI validation warns about extreme threshold values but does not block execution

Some archived scripts remain for reference