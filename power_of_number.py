num = int (input("enter number "))
pow = int (input("enter power "))

result = 1

for i in range(pow):
    result *=num

if(pow==0):
    print("1")
else:
    print(result)