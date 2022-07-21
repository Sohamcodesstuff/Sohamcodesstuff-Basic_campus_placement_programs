num = str(1001)


result = list(num)

for i in range(len(num)):
    if num[i]=='0':
        result[i] = '1'

    else:
        result[i] = '0'

final = ""
for i in result:
    final+=i

print("The complement is " + final)