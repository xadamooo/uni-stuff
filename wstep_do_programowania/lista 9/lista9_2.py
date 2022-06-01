import os
import re
for roots, dirs, files in os.walk('E:\\Visual Studio'):
    for file in files:
        try:
            isFile = os.path.isfile(file)
        except None:
            pass
        else:
            splitted = os.path.splitext(file)
            if splitted[1] == '.pdf' and re.match('praca', splitted[0]):
                print(os.path.join(roots, file))
