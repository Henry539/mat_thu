inp_str =input()
list_ip = [x for x in inp_str]


print(*list_ip)
print("".join(list_ip[::-1]))