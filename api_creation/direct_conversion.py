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
        if ('__' in line or '<>' in line or line.split(' : ')[-1].startswith('<')) and not deleting:
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
        file.writelines(without_delegates())


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
    print(lines)

    return lines


def parse_past_5(lines):
    for line in lines:
        tabs = line.count('\t')
        if not past_5_tabs(tabs):
            yield line


def past_5_tabs(tabs):
    return tabs > 4


is_gen = re.compile(r"<(.*)>")
def with_brackets():
    return re.subn(is_gen, lambda match: f'[{match.groups()[0]}]')


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
                'imports': set(),
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
    with open(os.path.join(path, '__init__.py'), 'w'):
        pass
    for k, v in dll_data['classes'].items():
        if '.' in k:
            full_path = k.split('.')
            class_name = full_path.pop()
        else:
            full_path = [k]
            class_name = full_path.pop()
            print(full_path)

        is_important = 'System.Int' in k
        if is_important:
            print(f'path - {path}')
        current_dir = path
        for name in full_path:
            if is_important:
                print(name)
                print(current_dir)
            current_dir = os.path.join(current_dir, name)
            try_make_dir(current_dir)
            if not os.path.exists(os.path.join(current_dir, '__init__.py')):
                with open(os.path.join(current_dir, '__init__.py'), 'w'):
                    pass
        if '<' in class_name:
            fixed_class_name = class_name.split('<')[0]
        else:
            fixed_class_name = class_name
        current_dir = os.path.join(current_dir, fixed_class_name)
        try_make_dir(current_dir)
        make_class_file(current_dir, class_name, v, fixed_class_name)


def make_class_file(path, class_name, class_data, fixed_class_name):
    lines = []

    with open(os.path.join(path, '__init__.py'), 'w') as file:
        parent = '(FridaHook)'
        lines.append(f'from hook import FridaHook\n')
        from_imps = set()
        for imp in class_data['imports']:
            to_imp = imp.split('.')[-1]
            if '.' in imp:
                from_imp = '.'.join(imp.split('.')[:-1])
                from_imps.add(f'from {imp} import {to_imp}\n')
            else:
                from_imps.add(f'from {imp} import {to_imp}\n')
        for imp in from_imps:
            lines.append(imp)

        lines.append('\n')

        if class_data['base_class']:
            parent_name = [*class_data['base_class'].keys()][0]
            parent = f'({parent_name}, FridaHook)'
        lines.append(f'class {class_name}{parent}:\n')
        for static_field_name, static_field_data in class_data['static fields'].items():
            lines.append(f'\t{static_field_name}: {static_field_data["type"]} = None\n')
        if class_data['static fields']:
            lines.append('\n')
        fields = []
        field_self_lines = []
        for field_name, field_data in class_data['fields'].items():
            fields.append(f'{field_name}: {field_data["type"]} = None')
            field_self_lines.append(f'\t\tself.{field_name}: {field_data["type"]} = {field_name}\n')
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
        file.writelines(lines)


def get_api_v1(game):
    #gen = os.path.join('.', 'gen')
    gen = os.path.join('..', '..', 'btd6_api')
    #version = os.path.join(gen, 'src')
    version = gen
    try_make_dir(version)

    for dll_name, dll_data in game['dlls'].items():
        dll_path = os.path.join(version, *dll_name.split('.')[:-1])
        try_make_dir(dll_path)
        try_make_init(dll_path, dll_data)


if __name__ == '__main__':
    parse_with(parser_v2)
