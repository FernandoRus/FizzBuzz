print("¡Bienvenido al juego BizzBuzz!")

x = int(input("Para iniciar introduzca un número entre el 1 y el 100: "))
for number in range(1, x+1):
    if number % 3 == 0:
        print("fizz")

    if number % 5 == 0:
        print("buzz")

    if number % 3 == 0 and number % 5 == 0:
        print("fizzbuzz")

    else:
        print(number)
