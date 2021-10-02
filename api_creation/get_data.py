import os
import re

from get_structure import get_ranges_as_dict


# Returns offset from class base address, name, type
static_field_re = re.compile(r"\t*([\w{}_<>-]+) : ([^\s]+) \(type: ([\w.,<>\[\]{}_-]+)\)\n?")


def get_static_fields(lines):
    static_fields = {}
    for line in lines:
        try:
            static_field_offset, static_field_name, static_field_type = re.fullmatch(static_field_re, line).groups()
            static_fields[static_field_name] = {
                'offset': static_field_offset,
                'name': static_field_name,
                'type': static_field_type,
            }
        except AttributeError as e:
            print(e)
            print(line)
    return static_fields


# Returns offset from class base address, name, type
field_re = re.compile(r"\t*([\w\-<>]+) : ([^\s]+) \(type: ([\w.,<>{}-]+)\)\n?")


def get_fields(lines):
    fields = {}
    for line in lines:
        try:
            field_offset, field_name, field_type = re.fullmatch(field_re, line).groups()
            fields[field_name] = {
                'offset': field_offset,
                'name': field_name,
                'type': field_type,
            }
        except AttributeError as e:
            print(e)
            print(line)
    return fields


# Returns address, function name, function parameters, return type
method_re = re.compile(r"\t*([\w<>-]+) : ([\w<>_.?,-]+) \(([^)]*)\):([\w.,<>\[\]{}-]+)\n?")


def get_methods(lines):
    methods = {}
    for line in lines:
        try:
            method_offset, method_name, method_parameters, method_return_type = re.fullmatch(method_re, line).groups()
            methods[method_name] = {
                'offset': method_offset,
                'name': method_name,
                'params': method_parameters,
                'return_type': method_return_type,
            }
        except AttributeError as e:
            print(e)
            print(line)
    return methods


# Returns address, class path
class_re = re.compile(r"\t*([\w.\-<>]+) : ([\w.<>,=|{}-]+)\n?")


def get_base_class(lines: [str]) -> dict[str, any]:
    if not lines:
        return
    try:
        class_offset, class_name = re.fullmatch(class_re, lines[0]).groups()
        return {
            'offset': class_offset,
            'name': class_name,
        }
    except AttributeError as e:
        print(e)
        print(lines[0])
        return


def get_data() -> dict[str, any]:
    data = {}
    get_data_methods = {
        'static fields': get_static_fields,
        'fields': get_fields,
        'methods': get_methods,
        'base class': get_base_class,
    }
    for module_name, module_structure in get_ranges_as_dict().items():
        module_data = {}
        for class_name, class_structure in module_structure.items():
            class_data = {}
            for info_name, info_lines in class_structure.items():
                class_data[info_name] = get_data_methods[info_name](info_lines)
            module_data[class_name] = class_data
        data[module_name] = module_data
    return data


if __name__ == '__main__':
    data = get_data()
    with open(os.path.join('.', 'gen', 'data', 'cheat_engine_data.py'), 'w') as file:
        file.write(f'data = {data}')




