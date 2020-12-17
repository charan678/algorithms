def fibonacci(number):
    l = []
    for index in range(0, number):
        if index == 0 or index == 1:
            l.append(1)
        else:
            l.append(l[index-1] + l[index-2])
    return l


def fibonacci_recurr(number):
    if number == 0 or number == 1:
        return 1
    return fibonacci_recurr(number-1) + fibonacci_recurr(number-2)

def fibonacci_dp(number, memo={}):
    if number == 0 or number == 1:
        return 1
    if (f"%s:%s",number-1, number-2) in memo.keys():
        return memo[f"%s:%s",number-1, number-2]
    memo[f"%s:%s",number-1, number-2] = fibonacci_recurr(number-1) + fibonacci_recurr(number-2)
    return memo[f"%s:%s", number-1, number-2]

if __name__ == "__main__":
    print(fibonacci(9)[8])
    print("-"*4)
    print(fibonacci_recurr(8))
    print("#"*50)
    print(fibonacci_dp(8))
