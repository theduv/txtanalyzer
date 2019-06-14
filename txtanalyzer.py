import sys
import os

def print_usage() :
    print("txtanalyzer: ./txtanalyzer [file]")
if len(sys.argv) < 2 :
    print_usage()
    sys.exit(1)
content = []
for arg in sys.argv[1:] :
    if os.path.exists(arg) and os.path.isfile(arg):
        fd = open(arg, "r")
        if fd == -1 :
            sys.stderr.write("Error: could not open " + arg)
        else :
            content += list(filter(bool, fd.read().split('\n')))
            str = ' '.join(content)
            content += list(filter(bool, str.split(' ')))
if os.path.exists("./skiplist.txt") :
    fd2 = open("skiplist.txt", "r")
if 'fd2' in locals() and fd2 != -1 :
    skiplist = list(filter(bool, fd2.read().split('\n')))
terms = {}
for word in content :
    if word in terms.keys() :
        terms[word] += 1
    else :
        terms[word] = 1
for key, value in sorted(terms.items(), reverse=True, key=lambda item: item[1]) :
    if 'skiplist' not in locals() or key not in skiplist :
        print("%s : %s" % (key, terms[key]))
