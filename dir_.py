import argparse
import os.path
import time
from os.path import join, getsize, getmtime

parser = argparse.ArgumentParser(description='Process arguments on command line to set output of %(prog)s')
parser.add_argument('dir_path', type=str, nargs='?', default='.',
                    help='path of directory')
parser.add_argument('-H', '--hidden', action='store_true', default=False,
                    help='show hidden files')
parser.add_argument('-m', '--modified', action='store_true', default=False,
                    help='show time of modification of the file')
parser.add_argument('-o', '--order', default='name',
                    choices=['n', 'name', 'm', 'modified', 's', 'size'],
                    help='sort directories and files')
parser.add_argument('-r', '--recursive', action='store_true', default=False,
                    help='show files recursive')
parser.add_argument('-s', '--sizes', action='store_true', default=False,
                    help='show file sizes')
args=parser.parse_args()

for root, dirs, files in os.walk(args.dir_path):
    if args.hidden:
        for dir in dirs:
            if dir.startswith("."):
                dirs.remove(dir)
    if args.order == 'name' or args.order == 'n':
        dirs.sort()
    if args.order == 'modified' or args.order == 'm':
        dirs.sort(key=lambda d: os.path.getmtime(os.path.join(root, d)), reverse=True)
    if args.order == 'size' or args.order == 's':
        dirs.sort(key=lambda s: os.path.getsize(os.path.join(root, s)), reverse=True)
    for dir in dirs:
        if args.modified:
            modified_time = getmtime(join(root,dir))
            convert_time = time.localtime(modified_time)
            format_time = time.strftime('%Y-%m-%d %H:%M:%S', convert_time)
            print(format_time, end=" ")
        if args.sizes:
            print(f'{getsize(join(root, dir)):>10}', end=" ")
        print(dir)
    if args.hidden:
        for file in files:
            if file.startswith("."):
                files.remove(file)
    if args.order == 'name' or args.order == 'n':
        files.sort()
    if args.order=='modified' or 'm':
        files.sort(key=lambda d: os.path.getmtime(os.path.join(root, d)), reverse=True)
    if args.order == 'size' or args.order == 's':
        files.sort(key=lambda s: os.path.getsize(os.path.join(root, s)), reverse=True)
    for file in files:
        if args.modified:
            modified_time = getmtime(join(root,file))
            convert_time = time.localtime(modified_time)
            format_time = time.strftime('%Y-%m-%d %H:%M:%S', convert_time)
            print(format_time, end=" ")
        if args.sizes:
            print(f'{getsize(join(root, file)):>10}', end=" ")
        print(file)
    if args.recursive:
        continue
    else:
        break
