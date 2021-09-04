import mouse


class RegionTracker:
    def __init__(self):
        self.p1 = None
        self.p2 = None
        self.regions = []

    def give_loc(self, *args):
        if self.p2:
            self.regions.append([*self.p1, *self.p2])
            self.p1 = mouse.get_position()
        elif self.p1:
            self.p2 = mouse.get_position()
        else:
            self.p1 = mouse.get_position()

    def give_pos(self, *args):
        print(mouse.get_position())


if __name__ == '__main__':
    p1 = []
    p2 = []
    tracker = RegionTracker()
    mouse.on_click(tracker.give_pos)
    while not mouse.get_position() == (0, 0):
        pass
    print(tracker.regions)



