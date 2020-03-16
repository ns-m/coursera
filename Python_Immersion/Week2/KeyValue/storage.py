import os
from argparse import ArgumentParser
import tempfile
from json import loads, dumps


storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


def get_file():
    if not os.path.exists(storage_path):
        return {}

    with open(storage_path, 'r') as f:
        raw_data = f.read()
        if raw_data:
            return loads(raw_data)

        return {}


def paste(key, value):
    data = get_file()
    if key in data:
        data[key].append(value)
    else:
        data[key] = [value]

    with open(storage_path, 'w') as f:
        f.write(dumps(data))


def get(key):
    data = get_file()
    return data.get(key)


def clean_out():
    os.remove(storage_path)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('--key', help='key')
    parser.add_argument('--val', help='value')
    parser.add_argument('--clear', action='store_true', help='clear')

    args = parser.parse_args()

    if args.clear:
        clean_out()
    elif args.key and args.val:
        paste(args.key, args.val)
    elif args.key:
        a = get(args.key).split()
        print(" ".join(a))
    else:
        print('Bad command')
