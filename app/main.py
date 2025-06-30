import sys
import os
import zlib
import argparse

def initialize() -> None:
    os.mkdir(".git")
    os.mkdir(".git/objects")
    os.mkdir(".git/refs")
    with open(".git/HEAD", "w") as f:
            f.write("ref: refs/heads/main\n")
    print("Initialized git directory")

def readGitObject(filename):
    with open(f".git/objects/{filename[:2]}/{filename[2:]}", "rb") as f:
        obj = zlib.decompress(f.read()).split(b"\x00")
        return obj

def readObjectContents(header) -> None:
    contents = header[1]
    print(contents.decode("utf-8"),end="")

def readObjectType(header) -> None:
    typ = header[0].split()[0]
    print(typ.decode("utf-8"),end="")

def readObjectSize(header) -> None:
    ObjSize = header[0].split()[1]
    print(ObjSize.decode("utf-8"),end="")
           

def main():

    parser = argparse.ArgumentParser()
    subparser = parser.add_subparsers(dest='main_command',required=True)

    #init parser
    init_parser = subparser.add_parser('init')

    #cat file parser
    cat_file_parser = subparser.add_parser('cat-file')

    operation_group = cat_file_parser.add_mutually_exclusive_group(required= True)
    operation_group.add_argument('-t','--type',action='store_true')
    operation_group.add_argument('-p','--print',action='store_true')
    operation_group.add_argument('-s','--size',action='store_true')
    cat_file_parser.add_argument('filename')

    args = parser.parse_args()

    if args.main_command == "init":
        initialize()
    elif args.main_command == "cat-file":
        obj = readGitObject(args.filename)
        if args.type:
            readObjectType(obj)
        elif args.print:
            readObjectContents(obj)
        elif args.size:
            readObjectSize(obj)    
    else:
        raise RuntimeError(f"Unknown command #{command}")


if __name__ == "__main__":
   main()