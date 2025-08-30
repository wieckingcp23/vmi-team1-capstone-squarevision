# Square Vision — Sprint 1

**Course:** CIS 480 Pre-Capstone / CIS 490 Capstone  
**Institution:** Virginia Military Institute  
**Sprint:** 1  
**Branch:** `Sprint1`

## Summary
Initial spike to confirm OpenCV works with a webcam and to try basic face detection using a Haar cascade. The script opens the default camera, detects faces per frame, and draws bounding boxes.

## Repository Contents
- `.github/workflows/blank.yml` — placeholder workflow  
- `try.py` — OpenCV webcam capture and Haar face detection demo

## How to Run
Requirements:
- Python 3.8 or later
- OpenCV

Install and run:
```bash
py -m pip install --upgrade pip
py -m pip install opencv-python
python try.py
Exit the window by pressing q.
```
---

## Notes and Limitations
- Uses the default Haar cascade `haarcascade_frontalface_default.xml` from `cv2.data.haarcascades`
- Assumes a working default camera at index 0

Minimal error handling

Known cleanup issue: the release call in the code uses an undefined variable name, so the camera window may not close cleanly
