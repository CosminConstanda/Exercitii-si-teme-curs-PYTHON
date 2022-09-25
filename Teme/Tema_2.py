
def palindrome(num):
    global number
    number = str(num)

    if str(num) == str(num[::-1]):
        return 'is_palindrome', True
    else:
        return 'is_palindrome' False


def prim(num):

    num = int(num)
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True


def div(num):

        n = int(num)
        div_list = []
    for i in range(1, n+1):
        if num % i == 0:
            div_list.append(i)

    return divisors_list


def max_div(num):

    return max(div(num))


def digits(num):
    return len(num)