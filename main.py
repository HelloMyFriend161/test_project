materials = {
    "this":"bottle",
    "that":"bottle",
    "these":"cardboard",
    "those":"gallon"
}
tutorials = {
    "this":"hey this is text A, how're ye doing",
    "that":"sup this is text B, need help? call me up.",
    "these":"hi i am text C, i do text C stuff.",
    "those":"hello i am text D. that's all."
}

def show_valids(keyword):
    for i in materials:
        if materials[i] == keyword:
            print(i)
    print("")
def show_tutorial(keyword):
    for i in tutorials:
        if keyword == i:
            print(tutorials[i])
    print("")

while True:
    command = input(">").split()
    if len(command) > 1:
        init = command[0]
        keyw = command[1]
        if init == "show_valids":
            show_valids(keyw)
        elif init == "tutorial":
            show_tutorial(keyw)
