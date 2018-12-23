import os
import sys

if input('''Remove unmerged copies of FETCH_HEAD? [y/N]:
''').lower() == 'y':
    for file in os.listdir(os.path.join(sys.path[0], '.git')):
        if file.startswith('FETCH_HEAD-'):
            os.remove(os.path.join(sys.path[0], '.git', file))
