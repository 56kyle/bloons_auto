
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
            base_class = data['base_class']
            parent = ''
            if base_class:
                base_path = base_class['name']
                base_name = base_path.split('.')[-1]
                if base_name != name:
                    import_names.append(base_path)
                else:
                    if name not in class_names:
                        get_class_lines(base_path, base_class)
                parent = f'({base_name})' if base_name else ''

            try:
                params = ', '.join([f'{field["name"]}: {field["type"]}' for field_name, field in data["fields"].items()])
            except AttributeError:
                params = ''
            '''
            def get_method(method_data: dict) -> str:
                method_params = ', '.join([f'{}' for param in ])
                new_method_lines = [
                    f'def {}'
                ]
            method_lines = '\n'.join([
                f'\tdef {method_name}({method_params})' for method_name, data in data['methods'].items()
            ])
            '''
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
            if data['fields']:
                for inst_var in data['fields'].values():
                    offsets[inst_var['name']] = inst_var['offset_from_class']
                    if inst_var['type'] not in class_names and inst_var['type'] not in import_names:
                        import_names.append(inst_var['type'])

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

        for class_path, class_data in module_data['classes'].items():
            get_class_lines(class_path, class_data)

        with open(os.path.join('.', 'gen', module_name + '.py'), 'w') as file:
            file.write('\n'.join(import_lines) + '\n\n' + '\n\n'.join(classes))


def api_down():
    os.removedirs('./gen')


if __name__ == '__main__':
    api_up()
