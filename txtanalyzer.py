import sys
import os

def print_usage() :
    print("txtanalyzer: ./txtanalyzer [file]")
if len(sys.argv) != 2 :
    print_usage()
    sys.exit(1)
if os.path.exists(sys.argv[1]) :
    fd1 = open(sys.argv[1], "r")
if os.path.exists("./skiplist.txt") :
    fd2 = open("skiplist.txt", "r")
if fd1 == -1 :
    sys.stderr.write("Error: could not open " + sys.argv[1])
if 'fd2' in locals() and fd2 != -1 :
    skiplist = list(filter(bool, fd2.read().split('\n')))
terms = {}
content = list(filter(bool, fd1.read().split('\n')))
str = ' '.join(content)
content = list(filter(bool, str.split(' ')))
for word in content :
    if word in terms.keys() :
        terms[word] += 1
    else :
        terms[word] = 1
for key, value in sorted(terms.items(), reverse=True, key=lambda item: item[1]) :
    if 'skiplist' not in locals() or key not in skiplist :
        print("%s : %s" % (key, value))
