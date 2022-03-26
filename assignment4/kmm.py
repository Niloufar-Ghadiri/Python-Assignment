num1 = int(input("numbber1 :"))
num2 = int(input("numbber2 :"))
if num1 > num2:
    max  = num1
    min = num2
else:
    max = num2
    min = num1
if max % min == 0:
    print(max)
    exit()
else:
    for i in range(max , (num1*num2)+1):
        if i % num1 == 0 and i % num2 == 0:
            KMM = i
print("K.M.M :" , KMM)