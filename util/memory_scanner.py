import ctypes
from ctypes.wintypes import WORD, DWORD, LPVOID

PVOID = LPVOID
SIZE_T = ctypes.c_size_t

# https://msdn.microsoft.com/en-us/library/aa383751#DWORD_PTR
if ctypes.sizeof(ctypes.c_void_p) == ctypes.sizeof(ctypes.c_ulonglong):
    DWORD_PTR = ctypes.c_ulonglong
elif ctypes.sizeof(ctypes.c_void_p) == ctypes.sizeof(ctypes.c_ulong):
    DWORD_PTR = ctypes.c_ulong


class SYSTEM_INFO(ctypes.Structure):
    """https://msdn.microsoft.com/en-us/library/ms724958"""

    class _U(ctypes.Union):
        class _S(ctypes.Structure):
            _fields_ = (('wProcessorArchitecture', WORD),
                        ('wReserved', WORD))

        _fields_ = (('dwOemId', DWORD),  # obsolete
                    ('_s', _S))
        _anonymous_ = ('_s',)

    _fields_ = (('_u', _U),
                ('dwPageSize', DWORD),
                ('lpMinimumApplicationAddress', LPVOID),
                ('lpMaximumApplicationAddress', LPVOID),
                ('dwActiveProcessorMask', DWORD_PTR),
                ('dwNumberOfProcessors', DWORD),
                ('dwProcessorType', DWORD),
                ('dwAllocationGranularity', DWORD),
                ('wProcessorLevel', WORD),
                ('wProcessorRevision', WORD))
    _anonymous_ = ('_u',)


LPSYSTEM_INFO = ctypes.POINTER(SYSTEM_INFO)

Kernel32 = ctypes.WinDLL('kernel32', use_last_error=True)
Kernel32.GetSystemInfo.restype = None
Kernel32.GetSystemInfo.argtypes = (LPSYSTEM_INFO,)

sysinfo = SYSTEM_INFO()
Kernel32.GetSystemInfo(ctypes.byref(sysinfo))

print(sysinfo.lpMinimumApplicationAddress)
print(sysinfo.lpMaximumApplicationAddress)

# maybe it will change, maybe it won't. Assuming it won't.

# 2nd, get Open process.
import psutil
import sys

PID = 7208

PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_VM_READ = 0x0010

Process = Kernel32.OpenProcess(PROCESS_QUERY_INFORMATION | PROCESS_VM_READ, False, PID)
print('process:', Process)


# 3rd

class MEMORY_BASIC_INFORMATION(ctypes.Structure):
    """https://msdn.microsoft.com/en-us/library/aa366775"""
    _fields_ = (('BaseAddress', PVOID),
                ('AllocationBase', PVOID),
                ('AllocationProtect', DWORD),
                ('RegionSize', SIZE_T),
                ('State', DWORD),
                ('Protect', DWORD),
                ('Type', DWORD))


##PMEMORY_BASIC_INFORMATION = ctypes.POINTER(MEMORY_BASIC_INFORMATION)

mbi = MEMORY_BASIC_INFORMATION()
##sysinfo.lpMinimumApplicationAddress

print('VirtualQueryEx ran properly?', Kernel32.VirtualQueryEx(Process, \
                                                              sysinfo.lpMinimumApplicationAddress, ctypes.byref(mbi),
                                                              ctypes.sizeof(mbi)))

ReadProcessMemory = Kernel32.ReadProcessMemory

##
MEM_COMMIT = 0x00001000
PAGE_READWRITE = 0x04

##buffer = ctypes.c_uint()
buffer = ctypes.c_double()

nread = SIZE_T()

start = ctypes.c_void_p(mbi.BaseAddress)

current_address = sysinfo.lpMinimumApplicationAddress
end_address = sysinfo.lpMaximumApplicationAddress

while current_address < end_address:
    Kernel32.VirtualQueryEx(Process, \
                            current_address, ctypes.byref(mbi), ctypes.sizeof(mbi))

    if mbi.Protect == PAGE_READWRITE and mbi.State == MEM_COMMIT:
        print('This region can be scanned!')
        index = current_address
        end = current_address + mbi.RegionSize

        while index < end:
            res = ReadProcessMemory(Process, index, ctypes.byref(buffer), \
                                 ctypes.sizeof(buffer), ctypes.byref(nread))
            if res:
                ## value comparison to be implemented.
                print(f'res - {res}')
            else:
                print('else happend.')
            ##                pass
            ##                raise ctypes.WinError(ctypes.get_last_error())

            index += 1

    current_address += mbi.RegionSize

