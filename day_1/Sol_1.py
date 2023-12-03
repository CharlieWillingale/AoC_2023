import re

def get_input(input_loc: str):

    input = []
    with  open(input_loc, "r") as f:

        for line in f.readlines():
            input.append(line.strip())

    return(input)

input = get_input('./day_1/input.txt')

#######################################
# Part 1
#######################################

# digit_pairs = []
# for line in input:

#     digit_list = []
#     for digit in line:
    
#         try:
#             (int(digit)) 
#             digit_list.append(digit)

#         except:
#             pass
    
#     pair = digit_list[0] + digit_list[-1]
#     digit_pairs.append(pair)

# sum = 0
# for pair in digit_pairs:
#     sum += int(pair)

# print(sum)

#######################################
# Part 2
#######################################

digit_pairs = []
txt_nums = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']

new_input = []
for line in input:

    for index in range(0, len(line)):

        try:
            if (line[index]+line[index + 1]+line[index + 2]) in txt_nums:
                line = re.sub(line[index] + line[index + 1]+line[index + 2],str(txt_nums.index((line[index]+line[index + 1]+line[index + 2])) + 1), line)

            elif (line[index] + line[index + 1] + line[index + 2] + line[index + 3]) in txt_nums:
                line = re.sub(line[index] + line[index + 1] + line[index + 2] + line[index + 3],str(txt_nums.index((line[index] + line[index + 1] + line[index + 2] + line[index + 3])) + 1), line)
            
            elif (line[index] + line[index + 1] + line[index + 2] + line[index + 3] + line[index + 4]) in txt_nums:
                line = re.sub(line[index] + line[index + 1] + line[index + 2] + line[index + 3] + line[index + 4],str(txt_nums.index((line[index] + line[index + 1] + line[index + 2] + line[index + 3] + line[index + 4])) + 1), line)

        except:
            break

    new_input.append(line)

for line in new_input:

    digit_list = []
    for digit in line:
    
        try:
            (int(digit)) 
            digit_list.append(digit)

        except:
            pass
    
    pair = digit_list[0] + digit_list[-1]
    digit_pairs.append(pair)

sum = 0
for pair in digit_pairs:
    sum += int(pair)

print(sum)
