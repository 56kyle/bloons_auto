

import frida
from frida.core import Session, Script

modules = {}


def on_message(message, data):
    module = dict(message.get('payload'))
    with open(f'./data/gen/{module["module"]}.py', 'w') as file:
        file.write(f'symbols = {module["symbols"]}\nexports = {module["exports"]}')


def generate_map():
    session: Session = frida.attach('BloonsTD6.exe')
    script: Script = session.create_script('''
        var modules = Process.enumerateModules()
        var exports = []
        modules.forEach((module) => {
            let found_mod = Process.findModuleByName(module.name);
            if (found_mod) {
                var e = found_mod.enumerateExports();
                var s = found_mod.enumerateSymbols();
                send({module: module.name, exports: e, symbols: s});
            }
        });
    ''')
    script.on('message', on_message)
    script.load()
    while True:
        pass


if __name__ == '__main__':
    generate_map()


