snumber = int(input())
s_list = []
s = 0
for i in range(snumber):
    s1 = float(input("score : "))
    s_list.append(s1)
    s = s + s1
average = s / snumber
max=max(s_list)
min=min(s_list)
print(max , min , average)