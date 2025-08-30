# Square Vision — Sprint 3

**Course:** CIS 480 Pre-Capstone / CIS 490 Capstone  
**Institution:** Virginia Military Institute  
**Sprint:** 3  
**Branch:** `Sprint3`

## Summary
This sprint adds a basic GUI with Tkinter on top of the SSD MobileNet v3 object detection pipeline. The app lets you pick the camera, adjust the confidence threshold with a slider, and run for a set duration with a simple timer. Detection runs in an OpenCV window while the GUI controls settings.

## Repository Contents
- `main.py` — GUI launcher with controls for camera selection, confidence, and timer  
- `image_dect.py` — Detection on still images  
- `timer.py` — Timing and performance checks  
- `coco.names` — COCO class labels  
- `frozen_inference_graph.pb` — Pre-trained model weights  
- `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt` — Model configuration  
- `vmi.png` - GUI Element
- `testImage1.jpg`, `testImage2.jpg` — Test images  
- `.github/workflows/blank.yml` — placeholder workflow

## How to Run (Sprint 3)
Requirements:
- Python 3.8 or later
- OpenCV, Pillow (for Tkinter image widgets)
```bash
py -m pip install --upgrade pip
py -m pip install opencv-python pillow
```
Run the GUI:
```bash
python main.py
```

## Controls:
- Internal Camera sets camera index to 0
- External Camera sets camera index to 1
- Confidence Threshold slider sets detection threshold from 0.01 to 1.00
- Set Timer enter seconds and click Enter
- Custom Settings runs with your selections
- Default Settings runs with internal camera, 0.50 confidence, no timer
- Press q in the OpenCV window to stop.

## Notes and Limitations
- Model files and coco.names must be in the working directory
- GUI is minimal and blocking; limited error handling
- Some resource cleanup may be inconsistent on exit

## Next Sprint Plan
- Add a Tkinter GUI to control camera source, confidence threshold, and a run timer.
- Refactor variable names and inputs for clarity, and add basic instructions to the window.
- Include new test images and keep older scripts as archived references.
- Improve startup and shutdown behavior for the camera and windows.