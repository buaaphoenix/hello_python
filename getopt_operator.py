#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys, getopt

def main(argv):
    inputfile = ''
    outputfile = ''
    longopt = None
    conf_file = None
    try:
        opts, args = getopt.getopt(argv[1:], "hi:o:f:", ["ifile=", "ofile=", "longopt=", "conf_file="])
        print(opts, args)
    except getopt.GetoptError:
        print('xxxx.py -i <inputfile> -o <outputfile>')
        sys.exit(2)
        
    for opt,arg in opts:
        if opt == '-h':
            print('xxxx.py -i <inputfile> -o <outputfile>')
            sys.exit()
        if opt in ("-i", "--ifile"):
            inputfile = arg
        if opt in ("-o", "--ofile"):
            outputfile = arg
        if opt in ("--longopt"):
            longopt = arg
        if opt in ("-c", "--conf_file"):
            conf_file = arg
    
    print('Input file is : ', inputfile)
    print('Output file is : ', outputfile)
    if longopt is True:
        print("longopt is true")

if __name__ == '__main__':
    res = main(sys.argv)
    exit(res)

