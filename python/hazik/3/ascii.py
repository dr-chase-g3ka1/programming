#!/usr/bin/python
# -*- coding: utf-8 -*-

def ascii_iras():
  iterator = 32
  while iterator < 128:
    print str(iterator) + ":\t" + chr(iterator)
    iterator += 1
    
def main():
  ascii_iras()


#############################################################################

if __name__ == '__main__':
  main()