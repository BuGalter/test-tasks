def even_fib_numbers(number):
    even_element = []
    if number == 0:
        even_element.append(0)
        return even_element
    if number == 1:
        even_element.append(0)
        return even_element

    fib1 = 0
    fib2 = 1
    even_element.append(fib1)
    for i in range(2, number):
        fib1, fib2 = fib2, fib1 + fib2
        if (fib2 % 2) == 0:
            even_element.append(fib2)
    return even_element
