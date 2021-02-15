#!/usr/bin/env python
# -*- coding: UTF-8 -*-
"""
@Author  ：青竹红颜
@Date    ：2021/2/11 8:11 
"""
import sys
import os

currentdir = os.path.dirname(sys.argv[0])
libdir = os.path.join(currentdir, "lib")
print(currentdir)
sys.path.append(libdir)
os.environ['path'] += ';./lib'