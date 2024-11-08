
binary_string = ''

def int_to_reverse_binary(num1):
    unreversed_bin_string = ''
#write your while loop here
    if num1 == 0:
        unreversed_bin_string = "0"
    else:
        while num1 > 0:
            unreversed_bin_string += str(num1 % 2)
            num1 = num1 // 2
    
    return unreversed_bin_string

def string_reverse(unreversed_bin_string): 
    reverse_input = ''
    for i in range(len(unreversed_bin_string)-1, -1, -1):
        reverse_input += unreversed_bin_string[i]
   #write your for loop here
    
    return reverse_input

if __name__ == '__main__':
    num1 = int(input())
    binary_string = ''
    binary_string = str(int_to_reverse_binary(num1))
    binary_string = str(string_reverse(binary_string))

    
    if binary_string == '' or binary_string == 0:
        binary_string = '0'
    print(binary_string)