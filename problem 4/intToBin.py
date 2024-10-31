def int_to_reverse_binary(num1):
    binary_val = ''
#write your while loop here
    while num1 > 0:
        binary_val += str(num1 % 2)
        num1 = num1 // 2
    
    return binary_val

def string_reverse(binary_val): 
    reverse_input = ''
    
    for digit in range(len(binary_val) -1, -1, -1):
        reverse_input += binary_val[digit]
   #write your for loop here
    
    return reverse_input

if __name__ == '__main__':
    num1 = int(input())
    binary_string = str(int_to_reverse_binary(num1))
    binary_string = str(string_reverse(binary_string))
    
    if binary_string == '':
        print("0")
    else:
        print(binary_string)