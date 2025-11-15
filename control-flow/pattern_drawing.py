patternsize = int(input('Enter the size of the pattern: '))

row = 0

while row < patternsize:
    for col in range(patternsize):
        print('*', end="")
    print()
    row += 1