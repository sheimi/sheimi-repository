#!/usr/bin/env python
"""
video.py
~~~~~~~
This file contains some shell command to cope with video.

:copyright: (c) 2012 by sheimi.
:license: BSD, see LISENSE for more details.

"""

import os
import argparse
from shell import ShellExec
from itertools import izip


class Video(ShellExec):

    def __init__(self, args=None):
        self.args = args
        self.subfixes = ['.mkv']
        self.cwd = os.getcwd()

    def __call__(self):
        method = args.method or 'split'
        return getattr(self, method)()

    def check_subfix(self, filename):
        for subfix in self.subfixes:
            if filename.endswith(subfix):
                return True
        return False

    def split(self):

        # get the args
        srcdir = args.src
        desdir = args.des if args.des else self.cwd
        interval = args.interval if args.interval else '1'

        # generate the srcs path
        if os.path.isdir(srcdir):
            srcs = ['/'.join([srcdir, src]) for src in os.listdir(srcdir)
                    if self.check_subfix(src)]
        else:
            srcs = [srcdir]

        # generate the deses path and make dirs
        filenames = [os.path.basename(src) for src in srcs]
        if not os.path.isdir(desdir):
            os.mkdir(desdir)
        desdirs = ['/'.join([desdir, filename])
                   for filename in filenames]
        [os.mkdir(desdir) for desdir in desdirs if not os.path.isdir(desdir)]
        deses = [desdir + '/image%d.png' for desdir in desdirs]

        # construct command and execute it
        command = (['ffmpeg', '-i', src, '-f',
                   'image2', '-r', interval, des]
                   for src, des in izip(srcs, deses))
        subs = self.exec_cmd(*command)
        for sub in subs:
            if sub.wait() != 0:
                print sub.stderr.read()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Process some integers.')

    parser.add_argument('--method')
    parser.add_argument('--src')
    parser.add_argument('--des')
    parser.add_argument('--interval')

    args = parser.parse_args()

    vs = Video(args)
    vs()
