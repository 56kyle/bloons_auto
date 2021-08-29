
import os

from tower_data import data
from config import keybinds


if __name__ == '__main__':
    for snake_name, info in data.items():
        camel_name = ''.join([word.capitalize() for word in snake_name.split('_')])
        tower_file = os.path.join('..', 'towers', f'{snake_name}.py')
        if os.path.isfile(tower_file):
            os.remove(tower_file)
        with open(tower_file, 'w') as file:
            tower_file_content = '\n'.join([
                'from tower import Tower',
                'from config import keybinds',
                '',
                '',
                f'class {camel_name}(Tower):',
                f'    name = \'{snake_name}\'',
                f'    range = {info["range"]}',
                f'    width = {info["width"]}',
                f'    height = {info["height"]}',
                f'    size = \'{info["size"]}\'',
                f'    keybind = keybinds[name]',
                f'    aquatic = {info["aquatic"]}',
                '',
                '    def __init__(self, **kwargs):',
                '        super().__init__(**kwargs)',
                ''
            ])
            file.write(tower_file_content)




