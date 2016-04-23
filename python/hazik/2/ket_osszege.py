#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys


def main():
  if len(sys.argv) == 3:
    print int(sys.argv[1]) + int(sys.argv[2])
  if len(sys.argv) == 1:
    Integer1 = raw_input('-->')
    Integer2 = raw_input('-->')
    print int(Integer1) + int(Integer2)




#############################################################################

if __name__ == '__main__':
  main()