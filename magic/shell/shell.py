#!/usr/bin/env python
"""
shell.py
~~~~~~~
This file contains some shell command parent.

:copyright: (c) 2012 by sheimi.
:license: BSD, see LISENSE for more details.

"""

import subprocess as sp
from itertools import izip


def yield_PIPE():
    while 1:
        yield sp.PIPE


class ShellExec(object):

    def exec_cmd(self, commands, stdouts=yield_PIPE(),
                 stdins=yield_PIPE(), stderrs=yield_PIPE()):
        #print commands
        #outs = [sp.Popen(command) for command in commands]
        outs = [sp.Popen(command, stdout=stdout,
                         stdin=stdin, stderr=stderr)
                for command, stdout, stdin, stderr
                in izip(commands, stdouts, stdins, stderrs)]
        return outs
