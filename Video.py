# เปิดวิดีโอด้วย OpenCV
import cv2
import datetime

cap = cv2.VideoCapture("image/Video.mp4")

while (cap.isOpened()):
    check, frame = cap.read() # เปิดวิดีโอแบบ frame ต่อ frame
    
    if check == True:
        # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # เปลี่ยนภาพสีให้เป็นภาพขาวเท่าดำ
        currentDate = str(datetime.datetime.now())
        cv2.putText(frame,"OpenCV",(10,30),cv2.FONT_HERSHEY_SIMPLEX,0.8,(0,0,0),cv2.LINE_4)
        cv2.putText(frame,currentDate,(270,20),0,0.5,(0,0,0))
        cv2.imshow("Output",frame) # gray or frame
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()