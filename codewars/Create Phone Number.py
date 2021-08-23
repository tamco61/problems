def create_phone_number(n):
    print(n)
    first = ''.join(str(i) for i in n[:3])
    second = ''.join(str(i) for i in n[3:6])
    third = ''.join(str(i) for i in n[6:])

    return f'({first}) {second}-{third}'

print(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]))