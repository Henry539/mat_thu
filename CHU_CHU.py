sb = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
aphal =[x.upper() for x in sb]

choose = input(" matthu-bachvan or bachvan-matthu:")


a1 = input("nhap chu 1:").upper()

a2 = input("nhap chu 2:").upper()

def aphal_aphal(chu1, chu2):
    aphal1 = []
    checkA = False
    count = 1
    for j in aphal:
        if j == chu1:
            checkA = True
        if checkA == False:
            continue
        if count == 27:
            break
        aphal1.append(j)
        count+=1

    aphal2 = []
    checkA = False
    count = 1
    for j in aphal:
        if j == chu2:
            checkA = True
        if checkA == False:
            continue
        if count == 27:
            break
        aphal2.append(j)
        count+=1

    dict_aphal = {}
    for i,j in zip(aphal1,aphal2):
        dict_aphal[i]=j
    dict_aphal[" "]=" "
    return dict_aphal

while True:
    dict = {}
    inp = [x.upper() for x in input("nhap: ")]
    result=[]
    if choose == "1":
        dict = aphal_aphal(a1,a2)
    elif choose == "2":
        dict = aphal_aphal(a2,a1)
    for i in inp:
        for k in dict:
            if i == k:
                result.append(dict[k])
    print("".join(result))
    a = input("PRESS ENTER TO ESCAPE!")