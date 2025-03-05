import random
a=int(input('welcome to password generator \n how many letters would you want in ur password'))
b=int(input('how many numbers u want'))
c=int(input('how many symbols u need'))
letters=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
numbers=['1','2','3','4','5','6','7','8','9','0']
symbols=['!','@','#','$','%']
pattern=[]
for i in range(1,a+1):
    char=random.choice(letters)
    pattern+=char
for i in range(1,b+1):
    char=random.choice(symbols)
    pattern+=char
for i in range(1,c+1):
    char=random.choice(numbers)
    pattern+=char
print(pattern)
random.shuffle(pattern)
print(pattern)
password=""
for char in pattern:
    password+=char
print(password)
