# search.py
'''
Hypothetical command line tool for searching a collection of
files for one or more text patterns.
'''


# [yangdong@centos7 ~]$ python3 search.py -v -p spam --pat=eggs foo.txt bar.txt
# filenames = ['foo.txt', 'bar.txt']
# patterns  = ['spam', 'eggs']
# verbose   = True
# outfile   = None
# speed     = slow
#
# [yangdong@centos7 ~]$ python3 search.py -v -p spam --pat=eggs foo.txt bar.txt -o results
# filenames = ['foo.txt', 'bar.txt']
# patterns  = ['spam', 'eggs']
# verbose   = True
# outfile   = results
# speed     = slow
#
# [yangdong@centos7 ~]$ python3 search.py -v -p spam --pat=eggs foo.txt bar.txt -o results
#              --speed=fast
# filenames = ['foo.txt', 'bar.txt']
# patterns  = ['spam', 'eggs']
# verbose   = True
# outfile   = results
# speed     = fast


import argparse
parser = argparse.ArgumentParser(description='Search some files')

parser.add_argument(dest='filenames',metavar='filename', nargs='*')

parser.add_argument('-p', '--pat',metavar='pattern', required=True,
                    dest='patterns', action='append',
                    help='text pattern to search for')

parser.add_argument('-v', dest='verbose', action='store_true', 
                    help='verbose mode')

parser.add_argument('-o', dest='outfile', action='store',
                    help='output file')

parser.add_argument('--speed', dest='speed', action='store',
                    choices={'slow','fast'}, default='slow',
                    help='search speed')

args = parser.parse_args()

# Output the collected arguments
print(args.filenames)
print(args.patterns)
print(args.verbose)
print(args.outfile)
print(args.speed)
