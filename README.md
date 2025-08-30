# Square Vision — Sprint 4

**Course:** CIS 480 Pre-Capstone / CIS 490 Capstone  
**Institution:** Virginia Military Institute  
**Sprint:** 4  
**Branch:** `Sprint4`

## Summary
This sprint refactors the app and introduces a clearer Tkinter interface for running detections. The GUI lets the user select internal or external camera, set a confidence threshold, and run for a specified duration. New test images were added for quick checks.

## Repository Contents
- `main.py` — GUI app with camera selection, confidence slider, and timer input  
- `image_dect.py` — Detection on still images  
- `timer.py` — Simple timing and performance checks  
- `coco.names` — COCO class labels  
- `frozen_inference_graph.pb` — Pre-trained model weights  
- `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt` — Model configuration  
- `vmi.png` - GUI Element
- `testImage1.jpg`, `testImage2.jpg` — Test images  
- `OldCOde.py` — Archived earlier logic  
- `.github/workflows/blank.yml` — Placeholder workflow

## How to Run (Sprint 4)
Requirements:
- Python 3.8 or later
- OpenCV and Pillow
```bash
py -m pip install --upgrade pip
py -m pip install opencv-python pillow
```
Run the GUI:
```bash
python main.py
```

## Controls:
- Select camera: Internal or External
- Adjust confidence threshold with the slider
- Enter run time in seconds and click Enter
- Start with Custom Settings or use Default Settings
- Press q in the OpenCV window to stop.

## Notes and Limitations
- Model files and `coco.names` must be in the working directory
- GUI remains single threaded and can block while detection runs
- Basic cleanup on exit may be inconsistent on some systems