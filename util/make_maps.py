import os
from PIL import Image


maps = {
    "Beginner": [
        "Monkey Meadow",
        "Tree Stump",
        "Town Center",
        "Resort",
        "Skates",
        "Lotus Island",
        "Candy Falls",
        "Winter Park",
        "Carved",
        "Park Path",
        "Alpine Run",
        "Frozen Over",
        "In The Loop",
        "Cubism",
        "Four Circles",
        "Hedge",
        "End Of The Road",
        "Logs",
    ],
    "Intermediate": [
        "Balance",
        "Encrypted",
        "Bazaar",
        "Adora's Temple",
        "Spring Spring",
        "KartsNDarts",
        "Moon Landing",
        "Haunted",
        "Downstream",
        "Firing Range",
        "Cracked",
        "Streambed",
        "Chutes",
        "Rake",
        "Spice Islands",
        "Bloonarius Prime",
    ],
    "Advanced": [
        "X Factor",
        "Mesa",
        "Geared",
        "Spillway",
        "Cargo",
        "Pat's Pond",
        "Peninsula",
        "High Finance",
        "Another Brick",
        "Off The Coast",
        "Cornfield",
        "Underground",
    ],
    "Expert": [
        "Sanctuary",
        "Ravine",
        "Flooded Valley",
        "Infernal",
        "Bloody Puddles",
        "Workshop",
        "Quad",
        "Dark Castle",
        "Muddy Puddles",
        "Ouch",
    ]
}


def make_map(name, diff):
    camel_name = name.replace(' ', '').replace("'", '')
    snake_name = name.lower().replace(' ', '_').replace("'", '')

    maps_dir = '../maps'
    map_dir = os.path.join(maps_dir, snake_name)
    os.mkdir(map_dir)
    placement_dir = os.path.join(map_dir, 'placement')
    os.mkdir(placement_dir)

    with open(os.path.join(map_dir, '__init__.py'), 'w') as file:
        file.write(f'from .{snake_name} import {camel_name}\n')

    with open(os.path.join(map_dir, f'{snake_name}.py'), 'w') as file:
        file_lines = [line + '\n' for line in [
            'from map import Map',
            '',
            '',
            f'class {camel_name}(Map):',
            '    def __init__(self, *args, **kwargs):',
            '        super().__init__(*args, **kwargs)',
            f"        self.name = '{snake_name}'",
            f"        self.difficulty = '{diff.lower()}'",
            ''
        ]]
        file.writelines(file_lines)

    img = Image.new('RGB', (1920, 1080), 0)

    land_dir = os.path.join(placement_dir, 'land')
    os.mkdir(land_dir)
    img.save(os.path.join(land_dir, 'small.png'))
    img.save(os.path.join(land_dir, 'medium.png'))
    img.save(os.path.join(land_dir, 'large.png'))
    img.save(os.path.join(land_dir, 'xl.png'))
    img.save(os.path.join(land_dir, 'heli_pilot.png'))
    img.save(os.path.join(land_dir, 'monkey_ace.png'))
    img.save(os.path.join(land_dir, 'banana_farm.png'))

    sea_dir = os.path.join(placement_dir, 'sea')
    os.mkdir(sea_dir)
    img.save(os.path.join(sea_dir, 'small.png'))
    img.save(os.path.join(sea_dir, 'medium.png'))
    img.save(os.path.join(sea_dir, 'large.png'))
    img.save(os.path.join(sea_dir, 'xl.png'))


if __name__ == '__main__':
    import_lines = []
    for difficulty, diff_maps in maps.items():
        for a_map in diff_maps:
            s_name = a_map.lower().replace("'", '').replace(' ', '_')
            c_name = a_map.replace(' ', '').replace("'", '')
            import_lines.append(f'from .{s_name} import {c_name}\n')
            make_map(a_map, difficulty)

    import_lines.append('\n')

    with open('../maps/__init__.py', 'w') as file:
        file.writelines(import_lines)
