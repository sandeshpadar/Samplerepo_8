# how to create a simple calculator

def add(x,y):
    return x + y

def mul(x,y):
    return x * y

def sub(x,y):
    return x - y

def div(x,y):
    if y == 0:
        print('cannot divide by zero plese enter correct number')
        return x / y

print('select operations:- ')
print('1. Addition')
print('2. Multiplicatino')
print('3. Substractino')
print('4. Division')

choice = input('Enter your choice (1/2/3/4):- ')

num1 = int(input('Enter your first number:- '))
num2 = int(input('Enter your second number:- '))

if choice == '1':
    result = add(num1, num2)
    operation = 'Addition'

elif choice == '2':
    result = mul(num1, num2)
    operation = 'Multiplicatin'

elif choice =='3':
    result = sub(num1, num2)
    operation = 'Substraction'

elif choice == '4':
    result = div(num1, num2)
    operation = 'Division'

else:
    result = 'invalid result'
    operation = 'invalid operation'

print(f'The {operation} is {result}')






