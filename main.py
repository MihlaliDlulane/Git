import argparse,sys
from lib import library

argparser = argparse.ArgumentParser()
argsSubparsers = argparser.add_subparsers(title="Commands", dest="command")
argsSubparsers.required = True

argsp = argsSubparsers.add_parser("init", help= "Initialize a new, empty repository. ")
argsp.add_argument("path",
                   metavar="directory",
                   nargs="?",
                   default=".",
                   help="Where to create the repository." )   


def command_init(args):
    library.repo_create(args.path)

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