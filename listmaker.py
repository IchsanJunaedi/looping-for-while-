y = int(input('List Number: '))
x = 1
while True:
    print(f'{x}.')
    x += 1
    if x == y:
        print(f'{x}.')
        break
print('List Succeed')