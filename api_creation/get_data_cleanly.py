
from collections.abc import Iterable
import re


def with_brackets(type_str: str) -> str:
    return type_str.replace('<', '[').replace('>', ']')


def get_data(*lines):
    game = {}
    main_offset = 0
    section = ''
    dll_name = ''
    class_name = ''
    section_name = ''

    for line in lines:
        tabs = line.count('\t')
        stripped = line.replace('\t', '').replace('\n', '')
        address = None
        if ' : ' in stripped:
            address = stripped.split(' : ')[0]
        if tabs == 0:
            #  Main exe offset
            game = {'address': address, 'dlls': {}}
        elif tabs == 1:
            #  Dll
            dll_name = '.'.join(stripped.split(' : ')[-1].split('.')[:-1])
            print(dll_name)
            game['dlls'][dll_name] = {
                'address': address,
                'classes': {}
            }
        elif tabs == 2:
            #  Class
            class_name = stripped.split(' : ')[-1]
            game['dlls'][dll_name]['classes'][class_name] = {
                'address': address,
                'fields': {},
                'static_fields': {},
                'methods': {},
                'base_class': {},
            }
        elif tabs == 3:
            #  Field labels
            section_name = stripped
            game['dlls'][dll_name]['classes'][class_name][section_name] = {}
        elif tabs == 4:
            #  Field data
            if section_name == 'static fields':
                static_field_name = stripped.split(' : ')[-1].split(' (')[0]
                static_field_type = stripped.split(' (type: ')[-1].replace(')', '')
                static_field_type = with_brackets(static_field_type)
                game['dlls'][dll_name]['classes'][class_name][section_name][static_field_name] = {
                    'address': address,
                    'type': static_field_type,
                }

            elif section_name == 'fields':
                field_name = stripped.split(' : ')[-1].split(' (')[0]
                field_type = stripped.split(' (type: ')[-1].replace(')', '')
                field_type = with_brackets(field_type)
                game['dlls'][dll_name]['classes'][class_name][section_name][field_name] = {
                    'address': address,
                    'type': field_type,
                }

            elif section_name == 'methods':
                method_name = stripped.split(' : ')[-1].split(' (')[0]
                method_parameters_whole: str = stripped.split(' -> ')[0].split(' (')[-1].replace(')', '')
                if method_parameters_whole:
                    if ', ' in method_parameters_whole:
                        method_parameters = method_parameters_whole.split(', ')
                    else:
                        method_parameters = [method_parameters_whole]
                else:
                    method_parameters = []
                method_parameters_data = {}
                for method_param in method_parameters:
                    try:
                        method_param_name, method_param_type = method_param.split(': ')
                        method_param_type = with_brackets(method_param_type)
                        method_parameters_data[method_param_name] = {
                            'type': method_param_type,
                        }
                    except Exception as e:
                        pass

                method_return_type = stripped.split(' -> ')[-1]
                method_return_type = with_brackets(method_return_type)
                game['dlls'][dll_name]['classes'][class_name][section_name][method_name] = {
                    'address': address,
                    'params': method_parameters_data,
                    'return_type': method_return_type,
                }
            elif section_name == 'base_class':
                base_class_name = stripped.split(' : ')[-1]
                game['dlls'][dll_name]['classes'][class_name][section_name][base_class_name] = {
                    'address': address,
                }
            else:
                print(f'no section provided - {section}')
    return game





if __name__ == '__main__':
    with open('./cheat_engine_output.TXT', 'r') as file:
        data = get_data(*file.readlines())
        with open('./cheat_engine_direct_2.txt', 'w') as new_file:
            new_file.write(str(data))


