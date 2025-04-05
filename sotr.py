list_per = []
list_rel = []
with open("record.txt") as f:
    s = f.read()
    s = s.split("n")
    #print(s)
for i in range(len(s)):
    list_per.append(float(s[i].split(":")[0]))
list_per.sort()
for i in list_per:
    #print(list_per)
    list_rel.append((i/53.745600804424335)*100)
print(list_rel)