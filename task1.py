def int_to_str(number, base):
    s = ""
    while number > 0:
        s = (str(number % base) if number % base < 10 else chr(number % base - 10 + ord('A'))) + s
        number //= base
    return s

def sum_numbers(base1, left, right, base2):
    p = 1
    s = 0
    while left > 0:
        s += (left % 10)*p
        left //= 10
        p *= base1
    p = 1
    while right > 0:
        s += (right % 10)*p
        right //= 10
        p *= base1
    return int_to_str(s, base2)