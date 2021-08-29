import mouse


def give_loc(*args):
    print(mouse.get_position())





if __name__ == '__main__':
    mouse.on_click(give_loc)
    while True:
        pass


