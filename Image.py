import cv2
import numpy as np

# อ่านภาพ 
img = cv2.imread("image/cat.jpg",0) # 0, 1, -1 {Grayscale , RGB, RGB+alpha-channel}
# print(type(img.ndim))
# print(img)

# ปรับขนาดภาพ
img_resize = cv2.resize(img, (400,400))

# แสดงภาพ
cv2.imshow("My Cat",img_resize)
cv2.waitKey(delay=0) # 5000 = 5 วินาที , 0 = ปิดเอง 
cv2.destroyAllWindows()

# การเขียนภาพ
cv2.imwrite("output.jpg",img_resize)



