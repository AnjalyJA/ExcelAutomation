from pathlib import Path

path = Path()
#print(path.mkdir())
#print(path.rmdir())
#print(path.glob('*')) # *.*  *.py  *.xls

for file in path.glob('*'):
    print(file)





