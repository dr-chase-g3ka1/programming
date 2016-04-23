#!/usr/bin/python
# -*- coding: utf-8 -*-

BIGINTEGER = 2**256

def szamjegyek_szama(BigInt):
  return len(str(BigInt))

def main():
  print BIGINTEGER
  print szamjegyek_szama(BIGINTEGER)


#############################################################################

if __name__ == '__main__':
  main()