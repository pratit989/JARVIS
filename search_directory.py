import string
import os
from ctypes import windll
import tempfile
import stat
import ast

temp_dir = tempfile.gettempdir()

file_system_dict = {}


def get_dup_key(key, keys):
    count = 0
    for k in keys:
        if key in k:
            count += 1
    return count


def listdir_nohidden(path):
    return bool(os.stat(path).st_file_attributes & stat.FILE_ATTRIBUTE_HIDDEN)


def get_drives():
    drives = []
    bitmask = windll.kernel32.GetLogicalDrives()
    for letter in string.ascii_uppercase:
        if bitmask & 1:
            drives.append(letter)
        bitmask >>= 1

    return drives


def find():
    # # print('{} is a {}'.format(name, type))
    # file_dict = {}
    # dir_dict = {}

    # rex = re.compile(name.lower())
    winpath = os.environ['WINDIR'].split(':')[0]
    print(winpath)
    # drives = get_drives(
    drives = ['G']
    for drive in drives:
        # drive 'D'
        print(drive)

        for root, dirs, files in os.walk(drive + ':\\', ):
            # if len(root) == 3:

            for f in files:
                # print os.path.join(root, f.lower())
                # result = rex.search(f.lower())
                # if result:

                if listdir_nohidden(
                        os.path.join(root, f)) == False and temp_dir not in f and 'Recycle' not in f and '__' not in f:
                    key = os.path.join(root, f).rsplit('\\')[-1]
                    # print(key, os.path.join(root,f))
                    file_system_dict.update(
                        {key + '_{}'.format(get_dup_key(key, file_system_dict.keys())): os.path.join(root, f)})
                else:
                    pass  # print('Hidden')

            for dir in dirs:
                # print os.path.join(root, dir.lower())
                # result = rex.search(dir.lower())
                # if result:
                if listdir_nohidden(os.path.join(root,
                                                 dir)) is False and temp_dir not in dir and 'Recycle' not in dir and '__' not in dir:
                    key = os.path.join(root, dir).split('\\')[-1].lower().split('.')[0]
                    # print (key, os.path.join(root, dir))
                    file_system_dict.update(
                        {key + '_{}'.format(get_dup_key(key, file_system_dict.keys())): os.path.join(root, dir)})
                    # dir_dict.update({'ghost_{}'.format(get_dup_key(key, dir_dict.keys())): 'rider'})
                    # if you want to find only one
                else:
                    pass
                    # print('Hidden')

                    # else:
                    #       break
    return file_system_dict


file_name = 'dict.txt'

if os.path.exists(file_name):
    with open(file_name, 'r') as f:
        file_system_dict = ast.literal_eval(f.read())
        f.close()

else:
    with open(file_name, 'w') as f:
        print('File System dictionary not found. Wait, I am doing so for the search functionality.')
        f.write(str(find()))
        f.close()
