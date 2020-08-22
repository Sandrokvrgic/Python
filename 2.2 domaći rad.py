print("Dobrodošli u fizzbuzz!")

kraj = int(input("Upišite broj između 1-100 : "))

for broj in range(1, kraj+1):

    if broj % 3 == 0 and broj % 5 == 0:

        print("fizzbuzz")

    elif broj % 5 == 0:

        print("buzz")

    elif broj % 3 == 0:

        print("fizz")

    else:

        print(broj)