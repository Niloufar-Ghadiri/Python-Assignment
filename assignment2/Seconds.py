time=list(map(int, input("Enter Time zoon: ##:##:##: ").split(':')))
print(time[0]*3600 + time[1]*60 + time[2])