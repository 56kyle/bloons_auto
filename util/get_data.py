from towers import *


if __name__ == '__main__':
    data = {}
    sizes = {
        'small': (65, 57),
        'medium': (75, 65),
        'large': (87, 75),
        'xl': (119, 103),
    }
    for tower in ALL:
        data[tower.name] = {
            'range': tower.range,
            'width': tower.width,
            'height': tower.height,
            'size': None,
            'aquatic': tower.aquatic,
        }
        size = None
        for s, [w, h] in sizes.items():
            if w == tower.width and h == tower.height:
                size = s
        if not size:
            size = 'rectangle'
        data[tower.name]['size'] = size

    print(data)





