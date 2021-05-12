# J.A.R.V.I.S
Virtual Assistant [ A Butler For PC Users ]

It is an effort to create a more helpful but maybe not as sophistacated as others out there or not as human Virtual Assistant for PC users.

**Requirments**
1. Python 3.7.x
2. Visual Studio C++ Build Tools
3. Visual Studio Community or Professional or Enterprise

**Installation Procedure**
1. Install PyAudio wheel.  
2. Install required modules from requirements.txt by running the following command from the project folder.  
```pip install -r requirements.txt```  
3. Run ```JARVIS_MARK_III.py```

# Real time face recognition with MobileFaceNet
##### A real time face recognition pipeline
####### Forked from [fyr91](https://github.com/fyr91/face_recognition)  
Face detection: an ultra-light face detector + five points facial feature detector

Face recognition: MobileFaceNet

### Dependency
Install all dependencies with 
```python pip install -r requirements.txt```

### Result:
![webcam](output/recog_trim.gif)

### References:
- MobileFaceNet: [link1](https://arxiv.org/abs/1804.07573), [link2](https://github.com/yangxue0827/MobileFaceNet_Tensorflow)
- UltraLight: [link](https://github.com/Linzaer/Ultra-Light-Fast-Generic-Face-Detector-1MB)
- FacialFeatures: [link](https://github.com/ageitgey/face_recognition)