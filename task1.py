while True:
    N = int(input("Enter number of stalls: "))
    if N < 0:
        print("Number must be positive!")
        continue
    else:
        break 
P = [int(P) for P in input("Enter P Values: ").split(" ")]
T = [int(T) for T in input("Enter T Values: ").split(" ")]
diff = [x-y for x,y in zip(P,T)]  
print("Output: ",sum(abs(x-y) for x,y in zip(diff+[0],[0]+diff))//2)
