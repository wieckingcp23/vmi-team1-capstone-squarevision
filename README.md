# Square Vision — Sprint 6

**Course:** CIS 480 Pre-Capstone / CIS 490 Capstone  
**Institution:** Virginia Military Institute  
**Sprint:** 6  
**Branch:** `Sprint6`

## Summary
This sprint focuses on refactoring and cleanup. The detection class and GUI remain, but code and names are standardized, model paths are consolidated in `model_data`, and older files are archived. The CustomTkinter GUI is the primary entry point.

## Repository Contents
- `main.py` — Primary GUI (CustomTkinter) using the `Detector` class
- `test.py` — Alternate GUI with standard Tkinter
- `Detector.py` — Detection class (model load, inference, drawing, FPS)
- `image_dect.py` — Detection on still images
- `model_data/` — `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt`, `frozen_inference_graph.pb`, `coco.names`
- `vmi.png` - GUI Element
- `testImage1.jpg`, `testImage2.jpg`, `testImage3.jpg` — Sample images
- `oldCode.py` — Archived script
- `__pycache__/` — Auto-generated cache (ignored)
- `.github/workflows/blank.yml` — Placeholder workflow

## How to Run (Sprint 6)
Requirements:
- Python 3.8 or later
- OpenCV, NumPy, CustomTkinter

Install:
```bash
py -m pip install --upgrade pip
py -m pip install opencv-python numpy customtkinter
```
Run the GUI:
```bash
python main.py
```
Optional fallback GUI:
```bash
python test.py
```
Press q in the OpenCV window to quit.

## Notes and Limitations
- All model files must remain in `model_data/`
- GUI remains single threaded while detection runs
- Basic input validation is present but not exhaustive

## Next Sprint Plan
- Fix bugs and standardize handler names and messages in the GUI
- Make customMode use the selected camera index reliabl
- Add a Help window with basic instructions and definitions
- Keep a small `CustomTkinter` demo (`test2.py`) for UI testing