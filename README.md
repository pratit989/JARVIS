# JARVIS
Just a rather very intelligent system

It is an effort to create a more helpful but maybe not as sophisticated as others out there or not as human Virtual Assistant for PC users.

**Requirements**
1. Python 3.7.x
2. Visual Studio C++ Build Tools
3. Visual Studio Community or Professional or Enterprise with C++ desktop development workload

**Installation Procedure**
1. Open cmd in Project Folder.  
2. Install PyAudio wheel with the following command.  
   ```pip install "PyAudio Wheel/PyAudio-0.2.11-cp37-cp37m-win_amd64.whl"```  
3. Install required modules from requirements.txt by running the following command from the project folder.  
```pip install -r requirements.txt```  
4. Run ```jarvis_v3.py```  
5. Download & install rainmeter from [Rainmeter.net](https://www.rainmeter.net/)  
6. Open .rmskin file downloaded from the latest release at [JARVIS releases](https://github.com/pratit989/J.A.R.V.I.S/releases)

**Usage**  
1. Take a look at ```vocabulary.py``` in project root directory for keywords that trigger specific actions.

# Real time face recognition with MobileFaceNet
#### A real time face recognition pipeline forked from [fyr91](https://github.com/fyr91/face_recognition)

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
