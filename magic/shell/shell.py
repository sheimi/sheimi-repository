#!/usr/bin/env python
"""
shell.py
~~~~~~~
This file contains some shell command parent.

:copyright: (c) 2012 by sheimi.
:license: BSD, see LISENSE for more details.

"""

import subprocess as sp


class ShellExec(object):

    def exec_cmd(self, *commands):
        #print commands
        #outs = [sp.Popen(command) for command in commands]
        outs = [sp.Popen(command, stdout=sp.PIPE,
                         stdin=sp.PIPE, stderr=sp.PIPE)
                for command in commands]
        return outs
