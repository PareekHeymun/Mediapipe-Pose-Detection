import cv2
import time
import PoseModule as pm

cap = cv2.VideoCapture("C:\\Users\\Heymun\\Desktop\\Hepyn\\Computer Vision\\Pose Estimation\\FOG_VISION.mp4")  # <-- Use your video path here
pTime = 0
detector = pm.poseDetector()

while True:
    success, img = cap.read()
    if not success or img is None:
        break
    img = cv2.resize(img, (640, 480))
    img = detector.findPose(img)
    lmList = detector.findPosition(img, draw=False)
    if len(lmList) != 0:
        print(lmList[14])
       # cv2.circle(img, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)
    cTime = time.time()
    fps = 1 / (cTime - pTime) if (cTime - pTime) > 0 else 0
    pTime = cTime
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)
    cv2.imshow("Image", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    

cv2.destroyAllWindows()