
decimal = 16
binary = []
A = decimal
Q = 1
while Q!= 0:
    Q = A // 2
    R = A % 2
    A = Q
    binary.append(R)
binary.reverse()
print("".join([str(i) for i in binary]))

while A!=0:
    if (A // 2 < 0):
        binary.append(1)
    else:
        binary.append(0)
    A //= 2


print('In binary {} is: {}'.format(decimal, ("".join([str(i) for i in binary]))))