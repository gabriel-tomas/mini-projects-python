import os

dir = 'C:/Users'
c = 0 
for dirs, subdirs, archs in os.walk(dir):
    if c == 1:
        break
    print(os.path.join(dir, subdirs[1]))
    c += 1