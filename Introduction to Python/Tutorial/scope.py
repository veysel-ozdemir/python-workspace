name = "Karl"  # global variable
count = 1  # global variable


def funct():
    color = "green"

    # count = 2  # valid
    # count += 1 # error
    global count  # valid
    count += 1
    print(count)

    def greeting(name):
        nonlocal color  # referencing the parent class' color variable
        color = "yellow"
        print(color)
        print(name)  # local

    greeting("Friederich")


funct()
