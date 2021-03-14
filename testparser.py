import argparse

parser = argparse.ArgumentParser(description='key-value storage')
parser.add_argument('--key', type=str)
parser.add_argument('--val', type=str)
args = parser.parse_args()
print(args.key)
print(args.val)