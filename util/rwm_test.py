import psutil
from ReadWriteMemory import ReadWriteMemory
import win32api
import win32con


def test():
    rwm = ReadWriteMemory()
    for pid in rwm.enumerate_processes():
        process = psutil.Process(pid)
        if 'oon' in process.name():
            print(pid)
            print(f'{process.name()} - ')
            print('\tfiles - ')
            for file in process.open_files():
                print(f'\t\t{file}')
            print('\tchildren - ')
            for child in process.children():
                print(f'\t\t{child.name()} - ')
                for file in child.open_files():
                    print(f'\t\t\t{file}')


if __name__ == '__main__':
    test()

