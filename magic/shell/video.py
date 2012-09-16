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


class Video(object):

    def __init__(self, args=None):
        self.args = args

    def __call__(self):
        method = args.method or 'split'
        return getattr(self, method)()

    def split(self):
        src = args.src
        des = args.des
        filename = src.split('/')[-1]
        if des is None:
            des = '/'.join([os.getcwd(), filename, ''])
        if not os.path.isdir(des):
            os.mkdir(des)
        des += 'image%d.png'
        command = ['ffmpeg', '-i', src, '-f',
                   'image2', '-r', '1', des]
        print ' '.join(command)
        os.system(' '.join(command))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Process some integers.')

    parser.add_argument('--method')
    parser.add_argument('--src')
    parser.add_argument('--des')

    args = parser.parse_args()

    vs = Video(args)
    vs()
