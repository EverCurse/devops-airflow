#!/usr/bin/env python
# -*- coding: utf-8 -*-

import commands

cmds='ls'

print commands.getstatusoutput(cmd=cmds)[1].split()