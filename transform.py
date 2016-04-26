#!/usr/bin/python

import re, sys

trans = {
        'base0': {'d16': 'colour12', 'd256': 'colour244', 'd16M': '#839496'},
        'base1': {'d16': 'colour14', 'd256': 'colour245', 'd16M': '#93a1a1'},
        'base2': {'d16': 'colour7', 'd256': 'colour254', 'd16M': '#eee8d5'},
        'base3': {'d16': 'colour15', 'd256': 'colour230', 'd16M': '#fdf6e3'},
        'yellow': {'d16': 'colour3', 'd256': 'colour136', 'd16M': '#b58900'},
        'magenta': {'d16': 'colour5', 'd256': 'colour125', 'd16M': '#d33682'},
        'red': {'d16': 'colour1', 'd256': 'colour160', 'd16M': '#dc322f'},
        'base01': {'d16': 'colour10', 'd256': 'colour240', 'd16M': '#586e75'},
        'base02': {'d16': 'colour0', 'd256': 'colour235', 'd16M': '#073642'},
        'base03': {'d16': 'colour8', 'd256': 'colour234', 'd16M': '#002b36'},
        'orange': {'d16': 'colour9', 'd256': 'colour166', 'd16M': '#cb4b16'},
        'green': {'d16': 'colour2', 'd256': 'colour64', 'd16M': '#859900'},
        'violet': {'d16': 'colour13', 'd256': 'colour61', 'd16M': '#6c71c4'},
        'blue': {'d16': 'colour4', 'd256': 'colour33', 'd16M': '#268bd2'},
        'cyan': {'d16': 'colour6', 'd256': 'colour37', 'd16M': '#2aa198'},
        'base00': {'d16': 'colour11', 'd256': 'colour241', 'd16M': '#657b83'},
}


pat = re.compile('#{(' + '|'.join(trans.keys()) + ')}')

def repl_func(depth, match):
    key = match.group(1)
    seq = trans[key][depth]
    return seq

def snr(infile, outfile, depth):
    out = open(outfile, 'w')
    for i, line in enumerate(open(infile)):
        out.write(pat.sub(lambda m: repl_func(depth, m), line))
    out.close()

if __name__ == '__main__':
    depth = 'd' + sys.argv[1]
    infile = sys.argv[2]
    outfile = sys.argv[3]
    snr(infile, outfile, depth)

