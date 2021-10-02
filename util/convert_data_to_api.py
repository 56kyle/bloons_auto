
import inflection
import os
from btd6_memory_info.cheat_engine_data import data


def api_up():
    for module_name, module_data in data['process']['modules'].items():
        import_lines = []
        import_names = []
        classes = []
        class_names = []

        def get_class_lines(path, data):
            name = path.split('.')[-1]
            base_class = data.get('base_class')
            parent = ''
            class_imports = []
            if base_class:
                base_path = base_class['name'].replace('.dll', '')
                base_name = base_path.split('.')[-1].replace('.dll', '')
                if base_name != name:
                    import_names.append(base_path)
                    class_imports.append(base_path)
                parent = f'({base_path})' if base_path else ''
                print(parent)
            methods = []
            if data.get('methods'):
                for method_name, method_data in data['methods'].items():
                    #print('method_name - ', method_name)
                    #print('method_data - ', method_data)
                    pass

            try:
                params = ', '.join([f'{field["name"]}: {field["type"]}' for field_name, field in data["fields"].items()])
            except AttributeError:
                params = ''

            offsets = {}
            try:
                class_variables = '\n'.join([f'\t{static_name}: {static["type"]}' for static_name, static in data['static_fields'].items()])
            except AttributeError:
                class_variables = ''

            try:
                instance_variables = '\n'.join([f'\t\tself.{field["name"]} = {field["name"]}' for field_name, field in data["fields"].items()])
            except AttributeError:
                instance_variables = ''

            if data['static_fields']:
                for cls_var in data['static_fields'].values():
                    offsets[cls_var['name']] = cls_var['offset_from_class']
                    if cls_var['type'] not in class_names and cls_var['type'] not in import_names:
                        import_names.append(cls_var['type'])
                        class_imports.append(cls_var['type'])
            if data['fields']:
                for inst_var in data['fields'].values():
                    offsets[inst_var['name']] = inst_var['offset_from_class']
                    if inst_var['type'] not in class_names and inst_var['type'] not in import_names:
                        import_names.append(inst_var['type'])
                        class_imports.append(inst_var['type'])

            class_lines = [
                f'',
                f'class {name}{parent}:',
                f'{class_variables}',
                f'    offsets = {offsets}'
                f'    ',
                f'    def __init__(self, {params + ", " if params else ""}**kwargs):',
                f'        super().__init__(self, **kwargs)',
                f'{instance_variables}'
                f'',

            ]
            classes.append('\n'.join(class_lines))
            module_data['classes'][class_data['name']]['lines'] = class_lines
            module_data['classes'][class_data['name']]['imports'] = class_imports

        for class_path, class_data in module_data['classes'].items():
            get_class_lines(class_path.replace('.dll', ''), class_data)

        with open(os.path.join('.', 'gen', module_name + '.py'), 'w') as file:
            file.write('\n'.join(import_lines) + '\n\n' + '\n\n'.join(classes))

        make_folder_api(module_name.replace('.dll', ''), module_data['classes'])


def make_folder_api(module_name, classes_data):
    gen_test = os.path.join('.', 'gen_test')
    try_to_make(gen_test)
    module_path_base: list = module_name.split('.')[:-2]
    module_path_last: str = '.'.join(module_name.split('.')[-2:])
    module_path = os.path.join(gen_test, *module_path_base, module_path_last)
    module_init = os.path.join(module_path, '__init__.py')
    try_to_make(module_path)
    with open(module_init, 'w') as file:
        pass

    for class_name, class_data in classes_data.items():
        class_path = os.path.join(module_path, *class_name.split('.'))
        class_path = class_path.replace('<', '').replace('>', '').replace(',', '_').replace('|', '').replace('=', '_')
        try_to_make(class_path)
        class_init = os.path.join(class_path, '__init__.py')
        try:
            with open(class_init, 'w') as file:
                import_lines = []
                for imp in class_data['imports']:
                    import_lines.append(f'import {imp}')
                imports = '\n'.join(import_lines)
                file.write(imports + '\n'.join(class_data['lines']))
        except Exception as e:
            print(e)


def try_to_make(path):
    try:
        os.makedirs(path.replace('<', '').replace('>', '').replace(',', '_').replace('|', ''))
        path = path.replace('<', '').replace('>', '').replace(',', '_').replace('|', '')
        print(path)
        for section in path.split('/'):
            pass
    except:
        pass


def api_down():
    os.removedirs('./gen')


if __name__ == '__main__':
    api_up()
