
import time
import win32gui
import pyscreeze
import mouse


x = None
y = None


def get_pixel_colour(i_x, i_y, win):
    dc = win32gui.GetWindowDC(win)
    long_colour = win32gui.GetPixel(dc, i_x, i_y)
    i_colour = int(long_colour)
    win32gui.DeleteDC(dc)
    return (i_colour & 0xff), ((i_colour >> 8) & 0xff), ((i_colour >> 16) & 0xff)


def winEnumHandler(hwnd, ctx):
    if win32gui.IsWindowVisible(hwnd):
        try:
            get_pixel_colour(x, y, hwnd)
            print(hex(hwnd), win32gui.GetWindowText(hwnd))
            print(get_pixel_colour(x, y, hwnd))
        except:
            pass


if __name__ == '__main__':
    time.sleep(4)

    x, y = mouse.get_position()
    x += 50
    print('pyscreeze')
    print(pyscreeze.screenshot().getpixel((x, y)))
    win32gui.EnumWindows(winEnumHandler, None)
