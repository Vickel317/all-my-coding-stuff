k = int(input("num = "))

m = True 

if k <= 1:
    print("NOT PRIME")

else:
    for i in range(2,k):
        if k % i == 0:
            print("not prime")
            m= False
            break
    if m:
        print("Prime")
    