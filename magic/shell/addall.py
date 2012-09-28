import itertools
import sys
import os
import numpy

def compress_feature(filename):
    feature_set = []
    with open(filename) as f:
        for line in f:
            feature = [int(i) for i in line.split(' ') if i.strip() != '']
            feature_set.append(feature)
    it = itertools.izip(*feature_set)
    count = len(feature_set)
    #count = len(feature_set) * 1.0
    result = []
    for item in it:
        result.append(sum(item) / count)
    return filename, result


if __name__ == '__main__':
    args = sys.argv
    #files = [i for i in os.listdir(args[1]) if not i.startswith('.')]
    files = [i for i in os.listdir(args[1]) if i.endswith('.mkv')]
    results = []
    for f in files:
        r = compress_feature(f)
        results.append(r)

    for fn1, r1 in results:
        for fn2, r2 in results:
            ra1 = numpy.array(r1)
            ra2 = numpy.array(r2)
            nr1 = numpy.linalg.norm(ra1)
            nr2 = numpy.linalg.norm(ra2)
            cos = ra1.dot(ra2) / (nr1 * nr2)
            print "%s, %s:" % (fn1, fn2), cos
            
