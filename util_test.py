# -*- coding: utf-8 -*-

import psutil



def find_procs_by_name(name):
    "Return a list of processes matching 'name'."
    ls = []
    for p in psutil.process_iter(attrs=['name']):
        if p.info['name'] == name:
            ls.append(p)
    return ls

print(find_procs_by_name('python.exe'))
print(psutil.net_io_counters(pernic=True))
print(psutil.disk_partitions())

print(psutil.net_if_addrs())
print(psutil.test())