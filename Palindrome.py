times = int(input("How many times do you want to add a number? "))

def check(num):
    temp=num
    rev=0
    while(num>0):
        dig=num%10
        rev=rev*10+dig
        num=num//10
    if(temp==rev):
        print(f'{rev} is a palindrome!')
    else:
        print(f'{temp} is not a palindrome!')

numbers = []

for i in range(times):
    num = int(input("Enter a number: "))
    numbers.append(num)

for i in range(len(numbers)):
    check(numbers[i])

#Bibliography:
#geekforgeeks.org/python-program-to-check-palindrome/