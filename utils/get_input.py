def get_input(input_loc: str):

    input = []
    with  open(input_loc, "r") as f:

        for line in f.readlines():
            input.append(line.strip())

    return(input)