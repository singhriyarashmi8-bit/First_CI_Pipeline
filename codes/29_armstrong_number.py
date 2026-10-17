
def is_armstrong(number):
    if number < 0:
        return False

    digits = str(number)
    power = len(digits)
    total = 0

    for digit in digits:
        total += int(digit) ** power

    return total == number


if __name__ == "__main__":
    print(is_armstrong(153))
    print(is_armstrong(123))
