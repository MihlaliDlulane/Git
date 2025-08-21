import argparse,sys
from lib import repoLib,objectLib

argparser = argparse.ArgumentParser()
argsSubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsSubparsers.required = True

argsp = argsSubparsers.add_parser("init", help= "Initialize a new, empty repository. ")
argsp.add_argument("path",
                   metavar="directory",
                   nargs="?",
                   default=".",
                   help="Where to create the repository." )

argsp = argsSubparsers.add_parser("cat-file",
                                  help = "Provide content of repository objects"  )

argsp.add_argument("type",
                    metavar="type",
                    choices=["blob", "commit", "tag","tree"],
                    help="Specify the type")

argsp.add_argument("object",
                    metavar="object",
                    help="The object to display")


argsp = argsubparsers.add_parser(
    "hash-object",
    help="Compute object ID and optionally creates a blob from a file")

argsp.add_argument("-t",
                   metavar="type",
                   dest="type",
                   choices=["blob", "commit", "tag", "tree"],
                   default="blob",
                   help="Specify the type")

argsp.add_argument("-w",
                   dest="write",
                   action="store_true",
                   help="Actually write the object into the database")

argsp.add_argument("path",
                   help="Read object from <file>")


def command_init(args):
    repoLib.repo_create(args.path)

def cat_file(repo,obj,object_type = None):
    obj = objectLib.object_read(repo,objectLib.object_find(repo,obj,object_type=object_type))
    sys.stdout.buffer.write(obj.serialize())

def command_cat_file(args):
    repo = repoLib.repo_find()
    cat_file(repo,args.object,object_type=args.type.encode())

def command_hash_object(args):
    if args.write:
        repo = repoLib.repo_find()
    else:
        repo = None 

    with open(args.path,"rb") as fd:
        sha = objectLib.object_Hash(fd,args.type.encode(),repo)
        print(sha)       

        

def main(argv=sys.argv[1:]):
    args = argparser.parse_args(argv)
    match args.command:
        case "add"              : command_add(args)
        case "cat-file"         : command_cat_file(args)
        case "check-ingore"     : command_check_ignore(args)
        case "checkout"         : command_checkout(args)
        case "commit"           : command_commit(args)
        case "hash-object"      : command_hash_object(args)
        case "init"             : command_init(args)
        case "log"              : command_log(args)
        case "ls-files"         : command_ls_files(args)
        case "ls-tree"          : command_ls_tree(args)
        case "rev-parse"        : command_rev_parse(args)
        case "rm"               : command_rm(args)
        case "show-ref"         : command_show_ref(args)
        case "status"           : command_status(args)
        case "tag"              : command_tag(args)
        case _                  : print("Bad comand.")