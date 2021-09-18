import os
import re

from typing import *


# Returns address, class path
class_re = re.compile(r"\t*([\w.\-<>]+) : ([\w.<>,=|{}-]+)\n?")

# Returns offset from class base address, name, type
static_field_re = re.compile(r"\t*([\w\-<>]+) : ([^\s]+) \(type: ([\w.,<>{}-]+)\)\n?")

# Returns offset from class base address, name, type
field_re = re.compile(r"\t*([\w\-<>]+) : ([^\s]+) \(type: ([\w.,<>{}-]+)\)\n?")

# Returns address, function name, function parameters, return type
method_re = re.compile(r"\t*([\w<>-]+) : ([\w.,]+) \(([^)]*)\):([\w.,<>{}-]+)\n?")


def strip_formatting(lines: [str]) -> [str]:
    return [line.replace('\t', '').replace('\n', '') for line in lines]


def get_module_name(line: str) -> str:
    return line.split(' : ')[1].replace('\n', '')


def is_a_module(line: str) -> bool:
    return line.startswith('\t') and not line.startswith('\t\t')


def get_module_structures() -> dict:
    modules_structure = {}
    un_stripped_lines: [str]
    lines: [str]
    with open('./cheat_engine_output.TXT', 'r') as file:
        un_stripped_lines = file.readlines()[1:]
        lines = strip_formatting(un_stripped_lines)

    module_line_i: int = 0
    module_line_f: int = 0
    module_name: str = ''
    for i, line in enumerate(un_stripped_lines):
        if is_a_module(line):
            module_line_f = i
            if module_line_f != module_line_i:
                modules_structure[module_name]['un_stripped_lines']: [str] = un_stripped_lines[module_line_i: module_line_f]
            module_line_i = i
            module_name = get_module_name(line)
            modules_structure[module_name] = {
                'name': module_name,
                'un_stripped_lines': [],
                'markers': {},
            }
    else:
        module_line_f = len(un_stripped_lines) - 1
        if module_line_f != module_line_i:
            modules_structure[module_name]['un_stripped_lines']: [str] = un_stripped_lines[module_line_i: module_line_f]

    for module_name, module_struct_data in modules_structure.items():
        module_line_markers = {
            'fields': None,
            'static fields': None,
            'base class': None,
        }
        for i, line in enumerate(strip_formatting(module_struct_data['un_stripped_lines'])):
            if line in module_line_markers.keys():
                module_line_markers[line] = i

        modules_structure[module_name]['markers'] = module_line_markers

    return modules_structure


def get_static_fields(lines):
    static_fields = {}
    for line in lines:
        static_field_offset, static_field_name, static_field_type = re.fullmatch(static_field_re, line).groups()
        static_fields[static_field_name] = {
            'offset': static_field_offset,
            'name': static_field_name,
            'type': static_field_type,
        }
    return static_fields


def get_fields(lines):
    fields = {}
    for line in lines:
        field_offset, field_name, field_type = re.fullmatch(field_re, line).groups()
        fields[field_name] = {
            'offset': field_offset,
            'name': field_name,
            'type': field_type,
        }
    return fields


def get_methods(lines):
    methods = {}
    for line in lines:
        method_offset, method_name, method_parameters, method_return_type = re.fullmatch(method_re, line).groups()
        methods[method_name] = {
            'offset': method_offset,
            'name': method_name,
            'params': method_parameters,
            'return_type': method_return_type,
        }

def get_class_ref(line):
    class_offset, class_name = re.fullmatch(class_re, line).groups()
    return {
        'offset': class_offset,
        'name': class_name,
    }


def get_all_class_metadata_from_module(module_struct_data):
    # Class Definition
    all_metadata = {}
    for i, line in enumerate(module_struct_data['un_stripped_lines']):
        if line.startswith('\t\t') and not line.startswith('\t\t\t'):
            class_offset, class_path_name = re.fullmatch(class_re, line).groups()
            class_ending = class_path_name.split('.')[-1]
            class_generics = []
            class_parents = {}
            if not class_ending.startswith('<') and not class_path_name.startswith('<'):
                class_folder_path = os.path.join('.', *class_path_name.split('.'))
                class_init_path = os.path.join(class_folder_path, '__init__.py')
                if '<' in class_path_name or '>' in class_path_name:
                    if class_ending.endswith('>'):
                        class_ending_prepped = class_ending.replace('>', '')
                        class_name, class_generics = class_ending_prepped.split('<')
                        class_generics = class_generics.split(',')
                        # print(f'{class_name}(Generic[{", ".join(class_generics)}])')
                        class_parents = {
                            'Generic': {
                                'name': 'Generic',
                                'import': {
                                    'from': True,
                                    'base': 'typing',
                                    'value': 'Generic'
                                },
                                'as_parent': f'Generic[{", ".join(class_generics)}]'
                            }
                        }
                    else:
                        class_name = class_ending
                        class_parents = {}
                else:
                    class_name = class_ending
                    class_parents = {}
            else:
                class_name = class_ending
                class_parents = {}

            all_metadata[class_name]['parents'] = class_parents
            all_metadata[class_name]['name'] = class_name
            all_metadata[class_name]['generics'] = class_generics
            all_metadata[class_name]['parents'] = class_parents
                

def get_module_data(module_structure: dict) -> dict:
    all_module_class_metadata = get_all_class_metadata_from_module(module_structure)



if __name__ == '__main__':
    module_structures = get_module_structures()
    for module_name, module_structure in module_structures.items():
        module_data = get_module_data(module_structure)


