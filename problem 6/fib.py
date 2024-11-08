def fibonacci(n):
    fib_sequence = [0,1]
    if n < 0:
        temp_var = -1
        return temp_var
    else:
        if n == 0:
            temp_var = 0
            return temp_var
        elif n == 1:
            temp_var = 1
            return temp_var
        else:
            for loopnum in range(1,n):
                next_number = fib_sequence[-1] + fib_sequence[-2]
                fib_sequence.append(next_number)
            return fib_sequence[-1]


    return

if __name__ == '__main__':
    start_num = int(input())
    print(f'fibonacci({start_num}) is {fibonacci(start_num)}')