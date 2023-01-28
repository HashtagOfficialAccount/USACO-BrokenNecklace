'''
LANG: PYTHON3
PROG: beads
'''
x = open("beads.in")
num = int(x.readline())
order = x.readline().strip()
new_list = order * 3
length = int(num)
index = 0
overlap = False
max_occurence = 0
for i in new_list:
    if index >= length and index < length * 2:
        back_l= new_list[index]
        front_l = new_list[index + 1]
        total1 = 0
        c = 0
        if back_l == "w" and front_l == "w":
            total1 += 1
        for i in range(2, length+1):
            c+=1
            if front_l == "w":
                total1 += 1
                if new_list[index + i] == "w":
                    pass
                else:
                    total1 += 1
                    front_l = new_list[index + i]
            elif new_list[index + i] == front_l or new_list[index + i] == "w":
                if total1 == 0:
                    total1 += 2
                else:
                    total1 += 1
            else:
                if total1 == 0:
                    total1 += 1
                break
        total2 = 0
        r = length
        for i in range(1,length):
            r-= 1
            previous = total2
            if back_l == "w":
                if new_list[index - i] == "w":
                    pass
                else:
                    total2 += 1
                    back_l = new_list[index - i]
            elif new_list[index - i] == back_l or new_list[index - i] == "w":
                if total2 == 0:
                    total2 += 2
                else:
                    total2 += 1
            else:
                if total2 == 0:
                    total2 += 1
                break
            if length - c <= length - r:
                total2 = previous
                break
        if total1 + total2 > max_occurence:
            max_occurence = total1 + total2
    elif index > length:
        break
    else:
        pass
    index += 1

with open("beads.out","w") as x:
    x.write(str(max_occurence)+"\n")
