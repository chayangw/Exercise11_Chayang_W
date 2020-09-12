number = int(input(">> "))
pyramid ="*"
for x in range(number):
    number -=1
    print((" "*number)+(((2*x)+1)*pyramid))
