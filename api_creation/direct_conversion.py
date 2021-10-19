import os
import re
import inflection
from typing import Callable, List, Union, Optional, Dict, Any


def convert_some_syntax():
    text = file_text()

    with open('./gen/data/cheat_engine_direct.py', 'w') as file:
        file.write(text.replace('; ', ', ').replace('):', ') -> '))


def without_delegates(lines):
    new_lines = []
    deleting = False
    started_deleting_tabs = 0
    for i, line in enumerate(lines):
        tabs = line.count('\t')
        if deleting and tabs == started_deleting_tabs:
            deleting = False
        if started_deleting_tabs == 4 and tabs < 4:
            deleting = False
        if (('__' in line and line.count('\t') == 2) or '<>' in line or line.split(' : ')[-1].startswith('<')) and not deleting:
            if line.split(' : ')[-1].startswith('<'):
                print(line)
            deleting = True
            started_deleting_tabs = tabs

        if not deleting:
            if line.count('\t') < 5:
                new_lines.append(line)
    return new_lines


def file_text():
    with open('./cheat_engine_output.TXT', 'r') as file:
        text = file.read()
    return text


def file_lines():
    with open('./cheat_engine_output.TXT', 'r') as file:
        lines = file.readlines()
    return lines


def make_pruned():
    with open('./gen/data/cheat_engine_direct_no_delegates.txt', 'w') as file:
        file.writelines(without_delegates(file_lines()))


def make_delegate_pruned():
    with open('./gen/data/cheat_engine_direct_no_delegates.txt', 'r') as file:
        text = file.read()
        with open('./gen/data/cheat_engine_direct_no_delegates_pruned.py', 'w') as file:
            file.write(text.replace('; ', ', ').replace('):', ') -> ').replace('base class', 'base_class'))


def oh_shit():
    checking_for_addresses = re.compile(r"\t*(\w+) : ([.\w]+).*")

    new_lines = []
    with open('./gen/data/cheat_engine_direct_no_delegates_pruned.py', 'r') as file:
        lines = file.readlines()
        dll = None
        klass = None
        field_type = None
        for line in lines:
            match = re.match(checking_for_addresses, line)
            if match:
                groups = match.groups()
                address = groups[0]
                name = groups[1]
                tabs = line.count('\t')

                if tabs == 2:  # dll
                    if not dll:
                        dll = {}
                    else:
                        lines.append(f'\t\tclass {name}')
                        lines.append(f'\t\t\toffset = {address}')
                        lines.append(f'\t\t\t')
                elif tabs == 3:  # class
                    pass
                elif tabs == 4:  # field_type
                    pass
                elif tabs == 5:  # field_entry
                    pass

                print(f'{name} - {address}')
            else:
                new_lines.append(line)
    with open('./gen/data/cheat_engine_all_plus_moved_addresses.py'):
        pass


def get_all():
    checking_for_addresses = re.compile(r"\t*(\w+) : ([.\w]+).*")
    new_lines = []
    with open('./gen/data/cheat_engine_direct_no_delegates_pruned.py', 'r') as file:
        lines = file.readlines()
        section = None
        for line in lines:
            tabs = line.count('\t')
            if ' : ' in line:
                stripped = line.replace('\t', '').replace('\n', '')
                address, rest = stripped.split(' : ')
                if tabs == 1:
                    dll = {}
                    current_class = None
                    section = None
                if tabs == 2:
                    section = None
                    current_class = {}
                    class_name = rest
                    new_lines.append(f'\tclass {class_name}:\n')
                    new_lines.append(f'\t\toffset = {address}\n')
                elif tabs == 3:
                    section = line.replace('\t', '').replace('\n', '')
                elif tabs == 4:
                    if section == 'fields':
                        field_type = rest.split('(')[-1].replace(')', '').replace('type: ', ': ')
                        if '<' in field_type:
                            field_type = field_type.replace('<', '[')
                        if '>' in field_type:
                            field_type = field_type.replace('>', ']')
                    new_lines.append(f'\t\t\tdef {rest}:\n')
                    new_lines.append(f'\t\t\t\treturn 0x{address}\n')
            else:
                new_lines.append(line)
    with open('./gen/data/cheat_engine_with_return_address.txt', 'w') as file:
        file.writelines(new_lines)


def parse_with(parse: Callable):
    with open('./gen/data/cheat_engine_direct_no_delegates_pruned.py', 'r') as file:
        lines = file.readlines()
        data = get_data(lines)
        get_api_v1(data)


def parser_v2(lines: List[str]):
    lines = without_delegates(lines)
    lines = [line for line in parse_past_5(lines)]

    return lines


def parse_past_5(lines):
    for line in lines:
        tabs = line.count('\t')
        if not past_5_tabs(tabs):
            yield line


def past_5_tabs(tabs):
    return tabs > 4


is_gen = re.compile(r"<(.*)>")
def with_brackets(line):
    return re.subn(is_gen, lambda match: f'[{match.groups()[0]}]', line)[0]


imps = re.compile(r"([\w.]+)")
def get_imports(type_ref: str) -> list[str]:
    return re.findall(imps, type_ref)


def get_data(lines):
    game = {}
    main_offset = 0
    section = ''
    dll_name = ''
    class_name = ''
    section_name = ''
    field_name = ''
    static_field_name = ''
    method_name = ''
    base_class_name = ''

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
            game['dlls'][dll_name] = {
                'address': address,
                'classes': {}
            }
        elif tabs == 2:
            #  Class
            class_name = stripped.split(' : ')[-1]
            game['dlls'][dll_name]['classes'][class_name] = {
                'address': address,
                'imports': set(),
                'fields': {},
                'static_fields': {},
                'methods': {},
                'base_class': {},
            }
            if 'MidpointRounding' in class_name:
                pass
        elif tabs == 3:
            #  Field labels
            section_name = stripped
            game['dlls'][dll_name]['classes'][class_name][section_name] = {}
        elif tabs == 4:
            if 'MidpointRounding' in class_name:
                pass
            #  Field data
            if section_name == 'static fields':
                static_field_name = stripped.split(' : ')[-1].split(' (')[0]
                if '?' in stripped:
                    static_field_type = 'Callable'
                else:
                    static_field_type = stripped.split(' (type: ')[-1].replace(')', '')
                    for imp in get_imports(static_field_type):
                        game['dlls'][dll_name]['classes'][class_name]['imports'].add(imp)

                game['dlls'][dll_name]['classes'][class_name][section_name][static_field_name] = {
                    'address': address,
                    'type': static_field_type,
                }

            elif section_name == 'fields':
                field_name = stripped.split(' : ')[-1].split(' (')[0]
                if '?' in line:
                    field_type = line.split('? - (')[-1].split(')')[0]
                else:
                    field_type = stripped.split(' (type: ')[-1].replace(')', '')
                for imp in get_imports(field_type):
                    game['dlls'][dll_name]['classes'][class_name]['imports'].add(imp)

                game['dlls'][dll_name]['classes'][class_name][section_name][field_name] = {
                    'address': address,
                    'type': field_type,
                }

            elif section_name == 'methods':
                method_name = stripped.split(' : ')[-1].split(' (')[0]
                method_parameters_whole: str = stripped.split(' -> ')[0].split(' (')[-1].replace(')', '')
                if '?' in line:
                    continue
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
                        for imp in get_imports(method_param_type):
                            game['dlls'][dll_name]['classes'][class_name]['imports'].add(imp)

                        method_parameters_data[method_param_name] = {
                            'type': method_param_type,
                        }
                    except Exception as e:
                        pass

                method_return_type = stripped.split(' -> ')[-1]
                for imp in get_imports(method_return_type):
                    game['dlls'][dll_name]['classes'][class_name]['imports'].add(imp)

                game['dlls'][dll_name]['classes'][class_name][section_name][method_name] = {
                    'address': address,
                    'params': method_parameters_data,
                    'return_type': method_return_type,
                }
            elif section_name == 'base_class':
                base_class_name = stripped.split(' : ')[-1]
                for imp in get_imports(base_class_name):
                    game['dlls'][dll_name]['classes'][class_name]['imports'].add(imp)

                game['dlls'][dll_name]['classes'][class_name][section_name][base_class_name] = {
                    'address': address,
                }
            else:
                print(f'no section provided - {section}')
    return game


def try_make_dir(path):
    try:
        if not os.path.isdir(path):
            os.makedirs(path)
    except Exception as e:
        print(e)


def try_make_init(path: str, dll_data: Dict[str, Any]) -> None:
    for k, v in dll_data['classes'].items():
        if '.' in k:
            full_path = k.split('.')
            class_name = full_path.pop()
        else:
            full_path = [k]
            class_name = full_path.pop()
        full_str_path = os.path.join(path, *full_path)
        try_make_dir(full_str_path)

        is_important = 'Facebook' in k
        if is_important:
            print(f'path - {path}')
            print(f'full_path - {full_path}')
            print(f'class_name - {class_name}')
            print(f'full_str_path - {full_str_path}')
        current_dir = path
        for name in full_path:
            if not os.path.exists(os.path.join(current_dir, '__init__.py')):
                with open(os.path.join(current_dir, '__init__.py'), 'w'):
                    pass
            current_dir = os.path.join(current_dir, name)
        if '<' in class_name:
            fixed_class_name = class_name.split('<')[0]
        else:
            fixed_class_name = class_name
        make_class_file(full_str_path, class_name, v, fixed_class_name)


def no_self_ref(value_type: str, path: str) -> str:
    if path in value_type:
        return value_type.replace(path, '')
    return value_type

starts_with_num = re.compile(r"\d+.*")

def make_class_file(path, class_name, class_data, fixed_class_name):
    important = 'Facebook' in path
    lines = []
    all_imports = set()
    all_classes = []
    pathway = os.path.join(path, '__init__.py')
    if important:
        print(pathway)
    importing = True
    if os.path.exists(pathway):
        with open(pathway, 'r') as initial_file:
            initial_lines = initial_file.readlines()
            for line in initial_lines:
                if importing:
                    if 'import' in line:
                        all_imports.add(line)
                    else:
                        importing = False
                        all_classes.append(line)
                else:
                    all_classes.append(line)

    all_imports.add('from hook import FridaHook\n')
    for imp in class_data['imports']:
        fin_imp = imp
        if '.' in imp:
            fin_imp = '.'.join(imp.split('.')[:-1])
        if re.fullmatch(starts_with_num, imp):
            continue
        if imp == class_name:
            continue
        all_imports.add(f'import {fin_imp}\n')

    with open(pathway, 'w') as file:
        parent = '(FridaHook)'
        for imp in all_imports:
            lines.append(imp)

        lines.append('\n')
        for line in all_classes:
            lines.append(line)

        if class_data['base_class']:
            parent_name = [*class_data['base_class'].keys()][0]
        lines.append(f'class {class_name}{parent}:\n')
        for static_field_name, static_field_data in class_data['static fields'].items():
            lines.append(f'\t{static_field_name}: {no_self_ref(static_field_data["type"], path)} = None\n')
        if class_data['static fields']:
            lines.append('\n')
        fields = []
        field_self_lines = []
        for field_name, field_data in class_data['fields'].items():
            fields.append(f'{field_name}: {no_self_ref(field_data["type"], path)} = None')
            field_self_lines.append(f'\t\tself.{field_name}: {no_self_ref(field_data["type"], path)} = {field_name}\n')
        lines.append(f'\tdef __init__(self, {", ".join([*fields, "**kwargs"])}):\n')
        if class_data['base_class']:
            lines.append(f'\t\tsuper().__init__(**kwargs)\n')
        if field_self_lines:
            for self_line in field_self_lines:
                lines.append(self_line)
        else:
            lines.append('\t\tpass\n')
        lines.append('\n')
        for method_name, method_data in class_data['methods'].items():
            if '?' not in method_name:
                lines.append(f'\tdef {method_name.replace(".", "")}(self, callback) -> dict:\n')
                lines.append(f'\t\treturn self._call({method_data})\n')
                lines.append('\n')
        lines.append('\n')
        with_brackets_lines = [with_brackets(lin) for lin in lines]


def get_api_v1(game):
    #gen = os.path.join('.', 'gen')
    gen = os.path.join('..', '..', 'btd6_api')
    #version = os.path.join(gen, 'src')
    version = gen
    try_make_dir(version)

    for dll_name, dll_data in game['dlls'].items():
        try_make_init(version, dll_data)

def get_straight_out():
    new_lines = []
    with open('./gen/data/cheat_engine_direct_no_delegates_pruned.py', 'r') as file:
        lines = file.readlines()
    for line in lines:
        new_line = line
        new_lines.append(new_line)

if __name__ == '__main__':
    make_pruned()
    make_delegate_pruned()
    parse_with(parser_v2)

