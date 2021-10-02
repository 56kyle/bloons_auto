
import os
import re

from typing import List, Dict, Generic, Union, Optional
from get_data import get_data


def is_delegate(path):
    return path.startswith('<') or path.split('.')[-1].startswith('<')


def parse_module_data(old_module_data: Dict[str, any]) -> Optional[Dict[str, any]]:
    if old_module_data:
        new_module_data = dict(old_module_data)
        for class_name, class_data in old_module_data.items():
            if is_delegate(class_name):
                del new_module_data[class_name]
            elif '<' in class_name:
                generic_contents = class_name.split('<')[-1].replace('>', '')
                if ',' in generic_contents:
                    new_module_data[class_name]['generics'] = generic_contents.split(',')
                else:
                    new_module_data[class_name]['generics'] = [generic_contents]
        return new_module_data


def parse_class_data(old_class_data: Dict[str, any]) -> Optional[Dict[str, any]]:
    if old_class_data:
        new_class_data = dict(old_class_data)
        new_class_data['generics'] = []
        for field_type, field_data in old_class_data.items():
            if is_delegate(field_type):
                del new_class_data[field_type]
            else:
                if '<' in field_type:
                    new_class_data['generics'] = field_type.replace('>', '').split('<')[-1]
        return new_class_data


def parse_static_field_data(old_static_field_data: Dict[str, any]) -> Optional[Dict[str, any]]:
    if old_static_field_data:
        new_static_field_data = dict(old_static_field_data)
        for static_field_name, static_field_data in old_static_field_data.items():
            if is_delegate(static_field_name):
                del new_static_field_data[static_field_name]
        return new_static_field_data


def parse_field_data(old_field_data: Dict[str, any]) -> Optional[Dict[str, any]]:
    if old_field_data:
        new_field_data = dict(old_field_data)
        for field_name, field_data in old_field_data.items():
            if is_delegate(field_name):
                new_dict = dict(field_data)
                del new_field_data[field_name]
                new_field_name = field_name.split('>')[-1]
                if '<>' not in field_name:
                    new_dict['overload'] = field_name[1:].split('>')[0]
                new_dict['name'] = new_field_name
                new_field_data[new_field_name] = new_dict
        return new_field_data


def parse_method_data(old_method_data: Dict[str, any]) -> Optional[Dict[str, any]]:
    if old_method_data:
        new_method_data = dict(old_method_data)
        for method_name, method_data in old_method_data.items():
            if is_delegate(method_name):
                del new_method_data[method_name]
        return new_method_data


def parse_base_class_data(base_class_data: Dict[str, any]) -> Optional[Dict[str, any]]:
    if base_class_data:
        new_base_class_data = dict(base_class_data)
        name = new_base_class_data['name']

        if '<' in name:
            new_base_class_data['name'] = name.split('<')[0]
            generic_contents = name.replace('>', '').split('<')[-1]
            new_base_class_data['generics'] = generic_contents.split(
                ',') if ',' in generic_contents else generic_contents
            #print(new_base_class_data)

        return new_base_class_data


def parse_invalid_data(data: Dict[str, any]) -> Dict[str, any]:
    info_parsers = {
        'static fields': parse_static_field_data,
        'fields': parse_field_data,
        'methods': parse_method_data,
        'base class': parse_base_class_data,
    }

    new_data = dict(data)

    for module_name, module_data in data.items():
        new_data[module_name] = parse_module_data(module_data)

        for class_name, class_data in module_data.items():
            if '__' not in class_name:
                new_data[module_name][class_name] = parse_class_data(class_data)
                for info_name, info_data in class_data.items():
                    if info_name != 'generics':
                        new_data[module_name][class_name][info_name] = info_parsers[info_name](class_data[info_name])
    return new_data


if __name__ == '__main__':
    unparsed_data = get_data()
    parsed_data = parse_invalid_data(unparsed_data)
    with open('./gen/data/parsed_data.py', 'w') as file:
        file.write(f'data = {parsed_data}')



