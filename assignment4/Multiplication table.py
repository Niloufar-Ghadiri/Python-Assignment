row = int(input('number of row: '))
column = int(input('number of col: '))
for i in range(1, row+1):
    for j in range(1, column+1):
        print(i*j, end=' ')
    print()