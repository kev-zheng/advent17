def answer(digits):
    sum = 0
    
    n = len(digits) // 2

    for i in range(len(digits)):
        if digits[i] == digits[i - n]:
            sum += int(digits[i])
    return sum

if __name__ == "__main__":
    with open('input.txt', 'r') as infile:
        digits = infile.read()
        digits = digits.strip()
        print(answer(digits))

