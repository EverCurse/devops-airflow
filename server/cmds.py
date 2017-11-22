#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess

p = subprocess.Popen('df -h', shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print p.stdout.readlines()