# เปิดกล้องด้วย OpenCV
import cv2

cap = cv2.VideoCapture(0)

# บรรทัดที่ 7, 8, 13 และ 17 เป็นการบันทึกวิดีโอ
fourcc = cv2.VideoWriter_fourcc(*'XVID')
result = cv2.VideoWriter("output.avi",fourcc,20.0,(640,480))

while True:
    cheak, frame = cap.read() # รับภาพจากกล้อง frame ต่อ frame
    cv2.imshow("Output",frame)
    result.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("e"):
        break

result.release()
cap.release()
cv2.destroyAllWindows()