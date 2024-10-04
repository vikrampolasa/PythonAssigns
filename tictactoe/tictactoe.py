#!/usr/bin/env python
# coding: utf-8

# In[5]:


import os

def clear_output():
    os.system('cls' if os.name == 'nt' else 'clear')
    
print ([1,2,3])
print ([4,5,6])
print ([7,8,9])

x_o_input = 'X'
result = 0
no_result = -1
element_count = 0
last_index = 0
iter = 0
result_out = ''

row1 = [' ',' ',' ']
row2 = [' ',' ',' ']
row3 = [' ',' ',' ']
complete_row = row1+row2+row3

while (result != 1 or no_result == 0):   
    iter = iter + 1
    
    if ((iter%2) == 0):
        x_o_input = 'O'
    else:
        x_o_input = 'X'

    while True:
        try:
            input_val = int(input('Enter a position value for {}: '.format(x_o_input))) 
            if (input_val not in range(1, 10) or (row1+row2+row3)[input_val-1] != ' '):
                print ('Invalid input. Try again!')
                continue
        except:
            print ('Invalid input. Try again.')
            continue
        else:
            input_val = input_val - 1
            break            
    print('#####################################')
    if (input_val == 0 or  input_val == 1 or input_val == 2 ):
        row1[input_val] = x_o_input
    elif (input_val == 3 or  input_val == 4 or input_val == 5 ):
        input_val = (input_val%3)
        row2[input_val] = x_o_input
    elif (input_val == 6 or  input_val == 7 or input_val == 8 ):
        input_val = (input_val%3)
        row3[input_val] = x_o_input

    element_count = (row1+row2+row3).count(' ')
    
    if (element_count == 1):
        if (x_o_input == 'X'):
            x_o_input = 'O'
        elif (x_o_input == 'O'):
            x_o_input = 'X'
        input_val = input_val + 1

        last_index = (row1+row2+row3).index(' ')

        last_row = int(last_index/3)
        last_index_position = (last_index%3)

        if (last_row == 0 ):
            row1[last_index_position] = x_o_input
        elif (last_row == 1):
            input_val = (input_val%3)
            row2[last_index_position] = x_o_input
        elif (last_row == 2):
            input_val = (input_val%3)
            row3[last_index_position] = x_o_input

    clear_output()
    print ('[1,2,3]'+'    '+row1[0]+'|'+row1[1]+'|'+row1[2])
    print ('[4,5,6]'+'    '+row2[0]+'|'+row2[1]+'|'+row2[2])
    print ('[7,8,9]'+'    '+row3[0]+'|'+row3[1]+'|'+row3[2])
    
    if ((row1[0].replace(' ','1') == row1[1].replace(' ','2') == row1[2].replace(' ','3')) or 
        (row2[0].replace(' ','4') == row2[1].replace(' ','5') == row2[2].replace(' ','6')) or
        (row3[0].replace(' ','7') == row3[1].replace(' ','8') == row3[2].replace(' ','9')) or
        (row1[0].replace(' ','1') == row2[1].replace(' ','5') == row3[2].replace(' ','9')) or
        (row1[2].replace(' ','3') == row2[1].replace(' ','5') == row3[0].replace(' ','7')) or
        (row1[0].replace(' ','1') == row2[0].replace(' ','4') == row3[0].replace(' ','7')) or
        (row1[1].replace(' ','2') == row2[1].replace(' ','5') == row3[1].replace(' ','8')) or
        (row1[2].replace(' ','3') == row2[2].replace(' ','6') == row3[2].replace(' ','9'))
       ):
        result = 1
        #print ('{} won!'.format(x_o_input))
        #break
        result_out = x_o_input
    if (element_count == 1 and result == 0):
        result = 1
        result_out = 'no_result'
        #print ('No result!')
        #break

    if (element_count == 1):
        break

if (result_out == 'no_result'):
    print ('No Result!')
else: 
    print ('{} won!'.format(result_out))
    


# In[19]:


def my_function():
    for i in range(1,21):
        print(i)
        if i == 20:
            print("you got it")


# In[35]:


print(int(7/2))


# In[ ]:




