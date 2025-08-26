"""def add(a,b):
    return a + b
result = add(10,5)
print("sum:", result)"""

"""def prime(n):
    if n <=1:          
        print(n, "is not a prime number")
        return

    for i in range(2,n):
        if n % i == 0:
            print(n, "is not a prime number")
            return
    print(n,"is a prime number")

num = int(input("enter a number:"))
print(num)"""

# prime numbers
"""def prime(n):
    if n<=1:
        print(n,"is not a prime number")
        return
    
    for i in range(2,n):
        if n % i == 0:
            print(n, "is not a prime number")
            return
        
# take input

    print(n, "is a prim number")
num=int(input("enter a number: "))
prime(num)"""

# finding the process of prime numbers
"""for n in range (2,50):                  
    for i in range(2, n):
        if n % i == 0:
            break
    else:
        print(n)"""

"""nums = [10, 20, 30, 40, 50]
print(nums[0])
print(nums[2])
print(nums[0-2])
print(nums[-2])"""

# slicing

num=[10,20,30,40,50]

print(num[1:4])    # [20,30,40] (from index 1 to 3)
print(num[ :3])    # [10,20,30] (start default 0)
print(num[2:])     # [30,40,50] (till end)
print(num[::2])    # [10,30,50] (step of 2)
print(num[::-1])   # [50,40,30,20,10] (reverse)

"""a = "Gowthami"
b = 2345678038
result = int(str(b))[::-1]
print(a[::-1])
print(result)"""


    

   
        
