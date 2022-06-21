
def square_digits(num):
    num = str(num)
    num = [int(i) for i in (num)]
    x = []
    
    for a in (num):
         x.append(a**2)
    
    x = [str(int) for int in x]
    x_joined = "".join(x)
    x_joined = int(x_joined)
    print(x_joined)

square_digits(9119)



