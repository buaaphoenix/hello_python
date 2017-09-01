#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import re
import subprocess

def pvc_match():
    with open('pvc-list', 'r') as fd_pvc:
        for pvc_line in fd_pvc:
            pvc0= pvc_line.strip('\n').split('\t\t\t')[1].split('-')[1][:3]
            pvc1= pvc_line.strip('\n').split('\t\t\t')[1].split('-')[2][:4]
            result, data = subprocess.getstatusoutput('grep {} {} | grep {}'.format(pvc0, 'wiki-list', pvc1))
            if result == 0:
                with open('final', 'a') as fd_final:
                    fd_final.write(data + '\n')

if __name__ == '__main__':
    pvc_match()
