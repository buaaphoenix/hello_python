#!/usr/bin/env python3

import subprocess

def popen_pipe():
    child1 = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)
    child2 = subprocess.Popen(['wc'], stdin=child1.stdout, stdout=subprocess.PIPE)
    out, err = child2.communicate() # Func_communicate returns the tuple (out, err)
    print(out.decode())

def popen_input():
    child = subprocess.Popen(['mysql','-uroot','-pxxxxxxx'], stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    out, err = child.communicate(input=b'use test;\n show tables;\nexit\n')
    print(out.decode())

if __name__ == '__main__':
    popen_pipe()

