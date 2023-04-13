import os
import re

path = os.path.dirname(__file__)
filenames = [i for i in os.listdir(path) if not i.startswith('_')]

total_lines = 0
progress_lines = 0

FILES_ENCODING = 'utf8'
UNCHECKED = '# '
CHECKED = '#$ '
INVALID_ELEMENTS = ('cha', 'tag', 'stop', 'flag', 'dbg', 'dcg', 'por', 'fade', 'hid', 'mus', 'roo', 'sou', 'ptt', 'ptf', 'fad', 'voi', 'hsh', 'map', 'var', 'bat', 'jum', 'cre', '//','ccc','cc\\d','-1000')

try:
    for fn in filenames:
        file_path = os.path.join(path, fn)
        file = open(file_path, 'r', encoding=FILES_ENCODING)
        text = file.read()
        file.close()

        lines = text.splitlines()
        file_total_lines = len(lines) // 2
        file_progress_lines = 0

        index = 0
        while index+1 < len(lines):
            line = lines[index+1]
            if line == '' or re.match(f'^({"|".join(INVALID_ELEMENTS)})', line) is not None:
                file_total_lines -= 1
                if not lines[index].startswith(CHECKED):
                    lines[index] = lines[index].replace(UNCHECKED, CHECKED)
            elif lines[index].startswith(CHECKED):
                file_progress_lines += 1
            elif lines[index].replace(UNCHECKED,'') != line:
                file_progress_lines += 1
                lines[index] = lines[index].replace(UNCHECKED, CHECKED)
            index += 2

        text = '\n'.join(lines)
        file = open(file_path, 'w', encoding=FILES_ENCODING)
        file.write(text)
        file.close()

        total_lines += file_total_lines
        progress_lines += file_progress_lines

        fpl = str(file_progress_lines).rjust(6)
        ftl = str(file_total_lines).rjust(6)
        fp = file_progress_lines / file_total_lines * 100
        print(f'[{fpl}/{ftl} | {fp:>6.2f}%]: "{fn}"')
except:
    import traceback
    print(traceback.format_exc())
    input('')
    quit()

ftl = str(total_lines).rjust(6)
fpl = str(progress_lines).rjust(6)
fp = progress_lines / total_lines * 100
print('')
print(f'[{fpl}/{ftl} | {fp:>6.2f}%]: Total Progress')
input('')

