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