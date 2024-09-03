#continue statement


for number in range(10):
    if number%2==0:
        continue
    print(number)

    for n1 in range(10):
        if n1 % 2 == 0:
            continue
        else:
            print(n1)