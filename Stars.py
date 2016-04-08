def draw_stars():
    x = [4,6,1,3,5,7,25]
    for number in x:
        print "*" * number

draw_stars()


def draw_morestars():
    x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
    for item in x:
        if type(item) == int:
            print "*" * item
        else:
            print item[0].lower() * len(item)


draw_morestars()