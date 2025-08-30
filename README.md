# Square Vision — Sprint 2

**Course:** CIS 480 Pre-Capstone / CIS 490 Capstone  
**Institution:** Virginia Military Institute  
**Sprint:** 2  
**Branch:** `Sprint2`

## Summary
This sprint introduced real-time object detection using OpenCV’s deep learning module with a pre-trained SSD MobileNet v3 model trained on the COCO dataset. Two scripts were created: one for webcam input and one for image files. A sample image (`bogart.jpg`) and model files are included for testing.

## Repository Contents
- `main.py` — Real-time object detection from webcam  
- `image_dect.py` — Object detection on still images (JPG/PNG)  
- `testImage1.jpg` — Sample image for testing  
- `coco.names` — List of COCO object classes  
- `frozen_inference_graph.pb` — Pre-trained model weights  
- `ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt` — Model configuration file  

## How to Run (Sprint 2)
Install dependencies:
```bash
py -m pip install --upgrade pip
py -m pip install opencv-python
```

Run real-time detection:
```bash
python main.py
```

Run image detection:
```bash
python image_dect.py
```
Press q to quit the camera window.

## Notes and Limitations
- Requires the full model files to be present in the working directory
- Detection speed may vary by hardware
- Scripts have minimal error handling

## Next Sprint Plan
- Add timing functionality to measure performance such as FPS
- Introduce new test images for validation beyond the original sample
- Clean up or archive older detection scripts as development progresses
- Refine existing detection scripts for stability and cleaner outputs
- Begin thinking about additional UI or features beyond plain detection