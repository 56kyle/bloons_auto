import sys

import inflection
import os
import re

from typing import Union
from pymem import Pymem
from btd6_memory_info.cheat_engine_output_offsets import offsets

# Returns address, class path
class_re = re.compile(r"\t*([\w.\-<>]+) : ([\w.<>,=|{}-]+)\n")

# Returns offset from class base address, name, type
static_field_re = re.compile(r"\t*([\w\-<>]+) : ([^\s]+) \(type: ([\w.,<>{}-]+)\)\n")

# Returns offset from class base address, name, type
field_re = re.compile(r"\t*([\w\-<>]+) : ([^\s]+) \(type: ([\w.,<>{}-]+)\)\n")

# Returns address, function name, function parameters, return type
method_re = re.compile(r"\t*([\w\-<>]+) : (\w+) \(([^)]*)\):([\w.,<>{}-]+)\n")


def convert_all():
    data = {}
    current_module_name = None
    sys.setrecursionlimit(2000)

    with open('../btd6_memory_info/cheat_engine_output.TXT', 'r') as old:
        lines = old.readlines()
        for i, line in enumerate(lines):
            if line.startswith('\t'):
                if line.startswith('\t\t'):
                    if line.startswith('\t\t\t'):
                        # Loops through in get_class_data anyway
                        pass
                    else:
                        # Class
                        class_data = get_class_data(current_module_base, lines, i-1)

                        data['process']['modules'][current_module_name]['classes'][class_data['name']] = class_data
                else:
                    # Module
                    match = re.fullmatch(class_re, line)
                    if match:
                        address, name = match.groups()
                        current_module_name = name
                        current_module_base = int(address, 16)
                        data['process']['modules'][current_module_name] = {'offset': base_address - int(address, 16), 'classes': {}}
                        print(name)
                    else:
                        print("ONO")
                        print(line)
            else:
                # Base
                print(line)
                base_address = int(line.replace('\n', ''), 16)
                data['process'] = {'name': 'BloonsTD6.exe', 'base_address': base_address, 'modules': {}}
    with open('../btd6_memory_info/cheat_engine_data.py', 'w') as new_file:
        new_file.write('data = ' + str(data))


tab_re = re.compile('\t')


def get_class_data(module_base: int, lines: [str], base_class_tag_index: int) -> dict:
    static_field_tag_index = None
    field_tag_index = None
    method_tag_index = None
    current_line: int = base_class_tag_index + 1
    data = {
        'name': None,
        'offset': None,
        'static_fields': None,
        'fields': None,
        'methods': None,
        'base_class': None,
    }

    def has_base_class(i) -> bool:
        # I is the line that contains "base class" or is before a class address line
        current_line_tabs = 0
        for _ in re.finditer(tab_re, lines[i]):
            current_line_tabs += 1
        next_line_tabs = 0
        for _ in re.finditer(tab_re, lines[i + 1]):
            next_line_tabs += 1
        return next_line_tabs > current_line_tabs

    def get_class_metadata(i: int) -> Union[dict, None]:
        # same as has_base_class
        match = re.fullmatch(class_re, lines[i])
        if match:
            address, name = match.groups()
            return {'offset_from_module': int(address, 16) - module_base, 'name': name}
        return None

    def get_static_field_data(i: int) -> Union[dict, None]:
        # lines[i] should end with 'static fields'
        match = re.fullmatch(static_field_re, lines[i+1])
        if match:
            offset_from_class, name, type = match.groups()
            return {'offset_from_class': int(offset_from_class, 16), 'name': name, 'type': type}
        return None

    def get_field_data(i: int) -> Union[dict, None]:
        # lines[i] should end with 'fields'
        match = re.fullmatch(field_re, lines[i+1])
        if match:
            offset_from_class, name, field_type = match.groups()
            return {'offset_from_class': int(offset_from_class, 16), 'name': name, 'type': field_type}
        return None

    def get_method_data(i: int) -> Union[dict, None]:
        # lines[i] should end with 'methods'
        match = re.fullmatch(method_re, lines[i+1])
        if match:
            address, name, params, return_type = match.groups()
            return {'offset_from_module': int(address, 16) - module_base, 'name': name, 'params': params, 'return_type': return_type}
        return None

    while not (static_field_tag_index and field_tag_index and method_tag_index and base_class_tag_index):
        if not data['name'] or not data['offset']:
            metadata = get_class_metadata(current_line)
            data['offset'] = metadata['offset_from_module']
            data['name'] = metadata['name']
        if lines[current_line].endswith('static fields\n') or (static_field_tag_index and not field_tag_index):
            new_field = get_static_field_data(current_line)
            if new_field:
                data['static_fields'] = data['static_fields'] if data['static_fields'] else {}
                data['static_fields'][new_field['name']] = new_field
            static_field_tag_index = current_line
        if lines[current_line].endswith('fields\n') or (field_tag_index and not method_tag_index):
            new_field = get_field_data(current_line)
            if new_field:
                data['fields'] = data['fields'] if data['fields'] else {}
                data['fields'][new_field['name']] = new_field
            field_tag_index = current_line
        if lines[current_line].endswith('methods\n') or (method_tag_index and not base_class_tag_index):
            new_method = get_method_data(current_line)
            if new_method:
                data['methods'] = data['methods'] if data['methods'] else {}
                data['methods'][new_method['name']] = new_method
            method_tag_index = current_line
        if lines[current_line].endswith('base class\n'):
            if has_base_class(current_line):
                data['base_class'] = get_class_data(module_base, lines, current_line)
            base_class_tag_index = current_line
        current_line += 1
    else:
        print(data)
        return data


def handle_class(line):
    klass = line.strip('\t').strip('\n')
    klass_address, klass_path = klass.split(' : ')

    path_sections = klass_path.split('.')
    root = os.path.join('..', 'btd6_memory_info', 'generated')
    name = path_sections[-1]
    for folder in path_sections[:-1]:
        root = os.path.join(root, folder)
        try:
            if not os.path.isdir(root):
                os.mkdir(root)
            new_file = os.path.join(root, inflection.underscore(folder)) + '.py'
            if not os.path.isfile(new_file):
                print(new_file)
                with open(new_file, 'w') as new_klass:
                    new_klass.write(f'''class {folder}:\tpass''')
        except OSError:
            pass
    return



def re_test():
    test = re.compile(r"\t+(\w+)\s:\s(.+)\n")
    data = {}
    with open('../btd6_memory_info/cheat_engine_output.TXT', 'r') as old:
        lines = old.readlines()
        for line in lines:
            match = re.fullmatch(test, line)
            if match:
                pass


if __name__ == '__main__':
    convert_all()
