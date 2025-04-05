import cv2
import os
list_per = []
list_chr = []
list_rel = []
with open("record.txt") as f:
    s = f.read()
    s = s.split("n")
    #print(s)
for i in range(len(s)):
    list_per.append(float(s[i].split(":")[0]))
for i in range(len(s)):
    list_chr.append(str(s[i].split(":")[1]))
for i in list_per:
    #print(list_per)
    list_rel.append((i/53.745600804424335)*100)
path = input("画像のファイル名:")
img = cv2.imread(path)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
org_width = img.shape[1]
org_higth = img.shape[0]
n = 1
w = input("横幅を入力:")
txt_path = '{}{}.txt'.format(path.split(".")[0],w)
f = open(txt_path, 'w')
f.close()
q = input("空白を多めにしますか？ (YorN):")
while q != "Y" and q != "N":
    q = input("質問に答えて？空白を多めにしますか？ (YorN):")
new_width = (int(w)*n)//2
per = org_width/new_width
new_highth = (org_higth//per)//n
img_changed = cv2.resize(img, (int(new_width), int(new_highth)))
#cv2.imwrite("img_changed.jpg",img_changed)
c = 0
for i in range(int(new_highth)):
    if c == 0:pass
    else:
        f = open(txt_path, 'a')
        #f.writelines("n")
        f.writelines("\n")
        f.close()
        #print(ps)
    c += 1
    ps = 0
    #if c == 6:break
    for k in range(new_width):
        px = img_changed[i,k]
        """ a = str(px).split(" ")[-1]
        px = int(a.replace("]","")) """ 
        #print(px,p)
        #p += 1
        #if p == 20:break
        per_black = 100-(px/255)*100
        if per_black < 5:chr = " "
        else:
            list_between = []
            for p in list_rel:
                between = max((per_black-p),(per_black-p)*-1)
                list_between.append(between)
            smallest = min(list_between)
            index = list_between.index(smallest)
            chr = list_chr[index]
        f = open(txt_path, 'a')
        #f.writelines("<"+str(int(per_black))+">")
        if q == "Y" and chr == '"':
            chr = " "
        f.writelines(chr*2)
        f.close()
        ps += 1