# เปิดวิดีโอด้วย OpenCV
import cv2

cap = cv2.VideoCapture("image/Video.mp4")

while (cap.isOpened()):
    check, frame = cap.read() # เปิดวิดีโอแบบ frame ต่อ frame
    
    if check == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # เปลี่ยนภาพสีให้เป็นภาพขาวเท่าดำ
        cv2.imshow("Output",gray) # gray or frame
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break
cap.release()
cv2.destroyAllWindows()