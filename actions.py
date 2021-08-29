import time
import mouse
import collections
import towers
from PIL import Image
from tower import Tower

Point = collections.namedtuple('Point', 'x y')


def get_placement_map(tower, x_bounds=(0, 1920), y_bounds=(0, 1080)):
    img = Image.new('RGB', (1920, 1080))

    xi = 0 + round(tower.width / 2) - 1
    xf = 1920 - round(tower.width / 2) + 1
    yi = 0 + round(tower.height / 2) - 1
    yf = 1080 - round(tower.height / 2) + 1
    for x in range(xi if xi > x_bounds[0] else x_bounds[0], xf if xf < x_bounds[1] else x_bounds[1]):
        for y in range(yi if yi > y_bounds[0] else y_bounds[0], yf if yf < y_bounds[1] else y_bounds[1]):
            if tower.can_place(Point(x, y)):
                img.putpixel((x, y), (255, 255, 255))


if __name__ == '__main__':
    time.sleep(5)
    get_placement_map(towers.SMALL[0], x_bounds=(571, 1612))
    #get_placement_map(towers.MEDIUM[0])
    #get_placement_map(towers.SpikeFactory)
    #get_placement_map(towers.XL[0])
    #for tower in towers.RECTANGLE:
        #get_placement_map(tower)





