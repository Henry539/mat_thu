sb = "abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
sb1 = "abcdefghijklmnopqrstuvwxyz"
aphal = [x.upper() for x in sb]
aphal1 = [x.upper() for x in sb1]
aphal2 = [x.upper() for x in sb1 if x != "a"]

inp = input("MT: ")


def dict_withA(basic_aphal, aphal1):
    aphal2 = []
    checkA = False
    count = 1
    for j in aphal:
        if j == aphal1:
            checkA = True
        if checkA == False:
            continue
        if count == 27:
            break
        aphal2.append(j)
        count += 1

    dict_aphal = {}
    for i, j in zip(basic_aphal, aphal2):
        dict_aphal[i] = j
    dict_aphal[" "] = " "
    return dict_aphal


def bach_van(dict_aphal, mat_thu):
    bv = []
    for i in mat_thu:
        bv.append(dict_aphal[i])
    return "".join(bv)


for i in aphal2:
    print(f"A-{i}", bach_van(dict_withA(aphal1, i), inp))
