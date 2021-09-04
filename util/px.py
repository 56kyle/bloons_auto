import mouse
import pyscreeze
import time
import win32gui


def get_pixel(i_x, i_y):
    hwnd = win32gui.GetForegroundWindow()
    dc = win32gui.GetDC(hwnd)
    long_colour = win32gui.GetPixel(dc, i_x, i_y)
    i_colour = int(long_colour)
    win32gui.DeleteDC(dc)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)


def main(x, y):
    time.sleep(.1)
    time.sleep(.1)
    print(get_pixel(x, y))


if __name__ == '__main__':
    while True:
        x, y = mouse.get_position()
        print(pyscreeze.pixel(x, y))
        print(get_pixel(x, y))

