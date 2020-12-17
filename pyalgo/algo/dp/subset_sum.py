def subset_sum(subset, sumval):
    if sumval == 0:
        return True
    elif sumval < 0 or len(subset) == 0:
        return False

    for index in range(0, len(subset)):
        return subset_sum(subset[index+1:], sumval - subset[index]) or subset_sum(subset[index+1:], sumval)


def subset_sum_memo(subset, sumval, memo=[]):
    if sumval == 0:
        return True
    elif sumval < 0 or len(subset) == 0:
        return False

    for index in range(0, len(subset)):
        return subset_sum(subset[index+1:], sumval - subset[index]) or subset_sum(subset[index+1:], sumval)



if __name__ == "__main__":
    subset = [10, 34, 100, 1, 4, 23, 6, 3]
    print("Sum - 132 ", subset_sum(subset, 132))
    print("Sum - 20 ", subset_sum(subset, 20))
    print("Sum - 2 ", subset_sum(subset, 2))
    print("Sum - 151 ", subset_sum(subset, 151))
    print("Sum - 110 ", subset_sum(subset, 110))

    print("---"*40)
    print("Sum - 132 ", subset_sum_memo(subset, 132))
    print("Sum - 20 ", subset_sum_memo(subset, 20))
    print("Sum - 2 ", subset_sum_memo(subset, 2))
    print("Sum - 151 ", subset_sum_memo(subset, 151))
    print("Sum - 110 ", subset_sum_memo(subset, 110))
