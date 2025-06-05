# Mediapipe-Pose-Detection
Pose Detection project using mediapipe

## Steps to replicate
- Download the following code folder and in Example Project.py please add the appropriate file path to the videos
- There are two problem statements that I am trying to work upon: Detection of person in night time and detection of person in fog
- For detection of person in fog, replace the file path in Example Project.py to match with the video having fog
- For detection of night vision, replace the file path in Example Project.py to match with the other video.
## Problems found:
- Detection of night vision does take place, i.e., mediapipe is able to detect person during night time, however, try changing the screen resolution from (1300, 1000) to something like (640, 480) and play with these values - you will observe the difference. At (1300,1000) I observed that the CHAIR was being detected as a human!
- Detection of person in fog: Even tho I can observe the person, mediapipe is unable to detect it unless it comes very close to the camera. Hence the model needs tweaks and improvements.
