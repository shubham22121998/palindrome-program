def plendrom(num):
    temp=num
    rev=0
    while num!=0:
        rem = num%10
        rev = rev*10+rem
        num = num//10
    if rev==temp:
        print(temp,"is plemdrom")
    else:
        print(temp,"is not plendrom")        
num=1234
plendrom(num)        