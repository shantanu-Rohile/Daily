# 11. Get File Size
import os
def size(name):
    stats = os.stat(name)
    return stats.st_size

print(size("new.txt"))
