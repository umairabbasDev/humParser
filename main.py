import argparse

parser = argparse.ArgumentParser(
    description='Parse a file with .hum extension.')
parser.add_argument('file', type=argparse.FileType(
    'r'), help='path to file with .hum extension')
args = parser.parse_args()

if not args.file.name.endswith('.hum'):
    print('Error: file format not recognized;.hum not provided ')
    print("ERROR:  syntax error")

else:
    # Do something with the file here
    print(f'Parsing {args.file.name}...')
