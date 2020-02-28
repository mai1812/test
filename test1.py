x = 5
if x > 5:
    print('x is greater than 5')
    print(x * 2)
elif x == 5:
    print('x is 5')
else: 
    print('x is NOT greater than 5')

a = 1
while a <= 5:
    print(a)
    a = a + 1
else:
    print('x is now greater than 10 ')

r = range(5)
for i in r:
    print(i)

for i in range(5):
    try:
        print(i / 0)
    except ZeroDivisionError as e:
        print(e, "--> Division by 0 is not allowed, sorry")