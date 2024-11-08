def swap_values(user_val1, user_val2, user_val3, user_val4):   
   temp_store = user_val1
   user_val1 = user_val2
   user_val2 = temp_store

   temp_store = user_val3
   user_val3 = user_val4
   user_val4 = temp_store
   
   return user_val1, user_val2, user_val3, user_val4

if __name__ == '__main__':   
   user_input1 = int(input())
   user_input2 = int(input())
   user_input3 = int(input())
   user_input4 = int(input())
   #store output for every input here
   newline1 = swap_values(user_input1, user_input2, user_input3, user_input4)
   print(f"{newline1[0]} {newline1[1]} {newline1[2]} {newline1[3]}")
 