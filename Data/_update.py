import os
import base64

origin_path = os.path.dirname(__file__)
export_path = os.path.dirname(origin_path)

filenames = [i for i in os.listdir(origin_path) if not i.startswith('_')]

UNCHECKED = '#'
FILES_ENCODING = 'utf8'

try:
    for fn in filenames:
        origin_file_path = os.path.join(origin_path, fn)
        file = open(origin_file_path, 'r', encoding=FILES_ENCODING)
        lines = [
            ln
            for ln in file.read().splitlines()
            if not ln.startswith(UNCHECKED)
        ]
        file.close()

        try:
            i = 0
            while i != len(lines):
                base64.b64encode(bytes(lines[i], encoding=FILES_ENCODING)).decode()
                i += 1
        except:
            print(i, ': ', lines[i])

        text = '\n'.join([
            base64.b64encode(bytes(ln, encoding=FILES_ENCODING)).decode()
            for ln in lines
        ])

        export_file_path = os.path.join(export_path, fn)
        file = open(export_file_path, 'w', encoding=FILES_ENCODING)
        file.write(text)
        file.close()

        count = filenames.index(fn)+1
        percentage = count / len(filenames) * 100
        print(f'[{f"{percentage:.2f}".rjust(6)}%] ({count}/{len(filenames)}): Completed "{fn}"')

except Exception as e:
    import traceback
    print(traceback.format_exc())

input("Process finished!")
