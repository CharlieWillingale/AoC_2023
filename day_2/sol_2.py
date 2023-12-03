def get_input(input_loc: str):

    input = []
    with  open(input_loc, "r") as f:

        for line in f.readlines():
            input.append(line.strip())

    return(input)


input = get_input('./day_2/input.txt')


#####################################
#  Part 1
#####################################
# bag_content = {'red':12, 'green':13, 'blue': 14}

# game_record = {}

# for entry in input:

#     game = entry.split(':')
#     game_id = game[0].split(' ')[-1]
#     sub_games = game[1].split(';')

#     possible = True

#     for sub_game in sub_games:

#         cubes = sub_game.split(',')

#         for cube in cubes:


#             if int(cube.split(' ')[1]) > bag_content[cube.split(' ')[2]]:

#                 possible = False

#     game_record[game_id] = possible

# sum = 0
# for i in range(1, len(game_record) + 1):

#     if game_record[str(i)] == True:
#         sum += i

# print(sum)

#####################################
#  Part 2
#####################################

game_record = {}

for entry in input:

    game = entry.split(':')
    game_id = game[0].split(' ')[-1]
    sub_games = game[1].split(';')
    bag_content = {'red' : 0, 'green' : 0, 'blue': 0}

    for sub_game in sub_games:

        cubes = sub_game.split(',')

        for cube in cubes:

            cube_description = cube.split(' ')
            if int(cube_description[1]) > bag_content[cube_description[2]]:

                bag_content[cube_description[2]] = int(cube_description[1])

    game_record[game_id] = bag_content

sum = 0
for min_cubes in game_record.values():

    power = 1
    for value in min_cubes.values():

        power *= value

    sum += power

print(sum)