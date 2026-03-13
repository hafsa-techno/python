def infinite_sequence():
    num = 0
    while True:
        yield num
        num += 1

def is_palindrome(num):
    if num // 10 == 0:
        return (False)
    temp = num
    rev_num = 0
    while (temp != 0):
        rev_num = rev_num * 10 + temp % 10
        temp = temp // 10
    if (rev_num == num):
        return True
    else:
        return False
gen = infinite_sequence()
while True:
    num = next(gen)
    if (num >= 100):
        break
    palindrome = is_palindrome(num)
    if (palindrome):
        print (num)
    # gen = next(gen)