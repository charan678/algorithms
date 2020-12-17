# Stream is always has pattern of 2 and 3 times of previous values
# If it is appended by 0 it will become 10 (2 in decimal) means 2 times of the previous value.
# If it is appended by 1 it will become 11(3 in decimal), 2 times of previous value +1.

def is_divisible(number):
    reminder = 0
    for index in range(0, 3):
        input_val = int(input("enter on binary number ="))
        if input_val != 0 and input_val != 1:
            break
        if input_val == 1:
            reminder = (2 * reminder + 1) % number
        else:
            reminder = (2 * reminder) % number
        if (reminder % number) == 0:
            print(f"stream is divisible = {input_val}")
        else:
            print(f"not divisible = {input_val} ")

if __name__ == '__main__':
    is_divisible(3)