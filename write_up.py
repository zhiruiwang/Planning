#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 18 20:50:58 2017

@author: zhirui
"""
import os
with open('writeup.txt','w') as f:
	f.write(os.popen('python run_search.py -p1 -s 1').read())
	f.write(os.popen('python run_search.py -p1 -s 3').read())
	f.write(os.popen('python run_search.py -p1 -s 8').read())

	f.write(os.popen('python run_search.py -p2 -s 1').read())
	f.write(os.popen('python run_search.py -p2 -s 3').read())
	f.write(os.popen('python run_search.py -p2 -s 8').read())

	f.write(os.popen('python run_search.py -p3 -s 1').read())
	f.write(os.popen('python run_search.py -p3 -s 3').read())
	f.write(os.popen('python run_search.py -p3 -s 8').read())

	f.write(os.popen('python run_search.py -p1 -s 9').read())
	f.write(os.popen('python run_search.py -p1 -s 10').read())

	f.write(os.popen('python run_search.py -p2 -s 9').read())
	f.write(os.popen('python run_search.py -p2 -s 10').read())

	f.write(os.popen('python run_search.py -p3 -s 9').read())
	f.write(os.popen('python run_search.py -p3 -s 10').read())