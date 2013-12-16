#!/usr/bin/env python

import sys

from pprint import pprint
from pick_lunch import read_luncher_prefs

def main(args):
    if len(args[1:]) != 1:
        sys.stderr.write("usage: %s <user.prefs>\n" % args[0])
        sys.stderr.write("makes sure your preferences are reasonable, shows adjusted weights if necessary\n")
        return 1

    prefs_filename = args[1]

    prefs = read_luncher_prefs(prefs_filename)
    pprint(prefs.preferences)
    print 'total:', sum([pref for pref in prefs.preferences.values()])

    return 0

if __name__ == '__main__':
    sys.exit(main(sys.argv))
