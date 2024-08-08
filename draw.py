import cv2

# อ่านภาพ
img = cv2.imread("image/cat.jpg")

# กำหนดขนาด
img_resize = cv2.resize(img,(700,700))

# วาดเส้นตรง
# line (ภาพ, จุดเริ่มต้น (x,y), จุดสุดท้าย (x,y), สี (BGR), ความหนา)
cv2.line(img_resize,(0,0),(0,100),(255,0,0),5)
cv2.line(img_resize,(0,100),(100,100),(255,0,0),5)
cv2.line(img_resize,(0,0),(100,0),(255,0,0),5)
cv2.line(img_resize,(100,0),(100,100),(255,0,0),5)
cv2.arrowedLine(img_resize,(500,500),(650,650),(0,0,255),5)

# วาดสีเหลี่ยม
# rectangle(ภาพ, มุมที่ 1 (บนซ้าย), มุมที่ 2 (ล่างขวา), สี,  ความหนา)
cv2.rectangle(img_resize,(250,250),(450,400),(0,0,0),2)
cv2.rectangle(img_resize,(700,0),(500,200),(0,0,0),-1) # ความหนา = -1 คือแทนที่ระบายสีข้างใน

# วาดวงกลม
# circle(ภาพ, ตำแหน่งจุดศูนย์กลาง (x,y), รัศมี, สี, ความหนา)
cv2.circle(img_resize,(0,700),100,(0,255,0),5)
cv2.circle(img_resize,(100,600),100,(0,255,0),5)

# ใส่ข้อความ
# putText(ภาพ, ข้อความ, พิกัดที่จะแสดงข้อความ (x,y), font, ขนาดข้อความ, สี, ความหนา)
cv2.putText(img_resize,"CAT",(250,150),cv2.FONT_HERSHEY_SIMPLEX,2.5,(255,255,255),cv2.LINE_AA)
cv2.putText(img_resize,"CAT",(250,245),3,2.5,(255,255,255),cv2.LINE_4)

cv2.imshow("Output",img_resize)
cv2.waitKey(0)
cv2.destroyAllWindows()