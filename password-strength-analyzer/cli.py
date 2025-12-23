import argparse
from analyzer.strength import analyze_password
from analyzer.wordlist import generate_wordlist

parser = argparse.ArgumentParser()
sub = parser.add_subparsers(dest="command")

a = sub.add_parser("analyze")
a.add_argument("--password", required=True)

g = sub.add_parser("generate")
g.add_argument("--name")
g.add_argument("--pet")
g.add_argument("--year")
g.add_argument("--out", default="wordlist.txt")

args = parser.parse_args()

if args.command == "analyze":
    analyze_password(args.password)

elif args.command == "generate":
    generate_wordlist(args, args.out)