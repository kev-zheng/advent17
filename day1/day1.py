def answer(digits):
    sum = 0
    
    for i in range(len(digits)):
        if digits[i] == digits[i - 1]:
            sum += int(digits[i])
    return sum

if __name__ == "__main__":
    #digits = input("digits!")
    #print(answer(digits))
    with open('input.txt', 'r') as infile:
        digits = infile.read()
        digits = digits.strip()
        print(answer(digits))

