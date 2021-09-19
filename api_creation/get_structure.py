import os
import re

from typing import Generic, Union, Callable


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


def is_module_start(line: str) -> bool:
    return line.startswith('\t') and not line.startswith('\t\t')


def is_a_module(line: str) -> bool:
    return line.startswith('\t') and not line.startswith('\t\t')


def is_class_start(line: str) -> bool:
    return line.startswith('\t\t') and not line.startswith('\t\t\t')


def get_class_path(line: str) -> str:
    return line.split(' : ')[1].replace('\n', '')


def is_viable_class_path(path: str) -> bool:
    if path.startswith('<'):
        # Check if the base path is a delegate
        return False
    if path.split('.')[-1].startswith('<'):
        # Check if the class is a delegate
        return False
    return True


def get_unstripped_lines():
    module_starts = []
    with open('./cheat_engine_output.TXT', 'r') as file:
        return file.readlines()[1:]


def get_line_ranges(lines, line_is_starter: Callable[[str], bool], get_current_key: Callable[[str], str]):
    all_lines = {}
    current_key = ''
    for line in lines:
        if line_is_starter(line):
            current_key = get_current_key(line)
            all_lines[current_key] = []
        if current_key:
            all_lines[current_key].append(line)
    return all_lines


def get_module_line_ranges(all_lines: [str]) -> dict[str, [str]]:
    return get_line_ranges(lines=all_lines, line_is_starter=is_module_start, get_current_key=get_module_name)


def get_class_line_ranges(module_lines: [str]) -> dict[str, [str]]:
    return get_line_ranges(lines=module_lines, line_is_starter=is_class_start, get_current_key=get_class_path)


def get_class_info_line_range(class_lines: [str], info_name: str) -> [str]:
    incorrect_info = ['static fields', 'fields', 'methods', 'base class']
    try:
        incorrect_info.remove(info_name)
    except AttributeError as e:
        print('info name is not a use-able value')
        raise e

    found_info = None
    for i, line in enumerate(strip_formatting(class_lines)):
        if found_info is not None:
            for incorrect_type in incorrect_info:
                if incorrect_type == line:
                    return found_info
            found_info.append(class_lines[i])
        if info_name == line:
            found_info = []
    return found_info


def get_static_field_line_range(class_lines: [str]) -> [str]:
    return get_class_info_line_range(class_lines=class_lines, info_name='static fields')


def get_field_line_range(class_lines: [str]) -> [str]:
    return get_class_info_line_range(class_lines=class_lines, info_name='fields')


def get_method_line_range(class_lines: [str]) -> [str]:
    return get_class_info_line_range(class_lines=class_lines, info_name='methods')


def get_base_class_line_range(class_lines: [str]) -> [str]:
    return get_class_info_line_range(class_lines=class_lines, info_name='base class')


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


def get_ranges_as_dict() -> dict[str, any]:
    all_lines = get_unstripped_lines()
    structure = {}

    module_ranges = get_module_line_ranges(all_lines)
    for module_name, module_lines in module_ranges.items():
        module_structure = {}

        class_ranges = get_class_line_ranges(module_lines)
        for class_name, class_lines in class_ranges.items():
            class_structure = {}

            for info_name in ['static fields', 'fields', 'methods', 'base class']:
                class_structure[info_name] = get_class_info_line_range(class_lines, info_name)
            module_structure[class_name] = class_structure
        structure[module_name] = module_structure
    return structure


if __name__ == '__main__':
    for module_name, module_data in get_ranges_as_dict().items():
        print(module_name)
        for class_name, class_data in module_data.items():
            print('\t', class_name)
            for info_name, info_data in class_data.items():
                print('\t\t', info_name)
                print('\t\t\t', info_data)


