import cv2
import numpy as np
from PIL import Image, ImageDraw, ImageFont
size=(512,512)
black_img=np.zeros(size,np.uint8)
white_img=black_img+255
cv2.imwrite('white.jpg',white_img)
def comp(ascii):
    fonts = ImageFont.truetype('C:/Windows/Fonts/msgothic.ttc', 100)
    img = Image.open('white.jpg')
    draw = ImageDraw.Draw(img)
    draw.text((206, 206), chr(ascii), 'black', font=fonts)
    img.save('txt_sample.jpg')
    lower_black = np.array([0, 0, 0])
    upper_black = np.array([255, 255, 100])
    sample_img = cv2.imread("txt_sample.jpg")
    hsv = cv2.cvtColor(sample_img, cv2.COLOR_BGR2HSV)
    mask_b = cv2.inRange(hsv, lower_black, upper_black)
    label = cv2.connectedComponentsWithStats(mask_b)
    data = np.delete(label[2], 0, 0)
    max_index = np.argmax(data[:, 4])
    # 面積最大ブロブの情報格納用
    maxblob = {}
    # 面積最大ブロブの各種情報を取得
    maxblob["upper_left"] = (data[:, 0][max_index], data[:, 1][max_index]) # 左上座標
    maxblob["width"] = data[:, 2][max_index]  # 幅
    maxblob["height"] = data[:, 3][max_index]  # 高さ
    #a = sample_img[maxblob["upper_left"][1]-1:maxblob["upper_left"][1]+maxblob["height"],maxblob["upper_left"][0]-1:maxblob["upper_left"][0]+maxblob["width"]]
    a = sample_img[maxblob["upper_left"][1]-1:maxblob["upper_left"][1]+77,maxblob["upper_left"][0]-1:maxblob["upper_left"][0]+50]
    cv2.imwrite("./chr.jpg",a)
    hsv = cv2.cvtColor(a, cv2.COLOR_BGR2HSV)
    mask_b = cv2.inRange(hsv, lower_black, upper_black)
    white_area_b = cv2.countNonZero(mask_b)
    whole_area = mask_b.size
    per_b = white_area_b/whole_area*100
    letter = str(chr(ascii))
    txt = str(per_b)+":"+letter+"\n"
    f = open('record2.txt', 'a')
    f.writelines(txt)
    f.close()
asc = 33
for i in range(58):
    comp(asc+i)