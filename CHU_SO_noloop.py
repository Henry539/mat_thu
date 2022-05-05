sb = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
aphal = [x.upper() for x in sb]
choose = input(" matthu-bachvan or bachvan-matthu:")
inp_str = input("nhap chu: ")
inp_int = int(input("nhap so: "))
if choose == "1":
    list_mt = [int(x) for x in input("MT: ").split(" ")]
else:
    list_mt = [x.upper() for x in input("MT: ")]
count = -1
check = False
dic={}

for i in aphal:
    if count == 28:
        break
    count+=1
    if aphal[count] == inp_str:
        check = True
    if not check:
        continue
    dic[inp_int] = aphal[count]
    inp_int+=1

print(list_mt)
print(dic)

def check_bv(li_mt,dic_bv):
    bv=[]
    for i in li_mt:
        for k,v in dic_bv.items():
            if i == k:
                bv.append(v)
    return "".join(bv)
def check_bv2(li_mt,dic_bv):
    bv=[]
    for i in li_mt:
        for k,v in dic_bv.items():
            if i == v:
                bv.append(k)
    return bv

if choose == "1":
    print(check_bv(list_mt,dic))
elif choose == "2":
    print(*check_bv2(list_mt,dic))

