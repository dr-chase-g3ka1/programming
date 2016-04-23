#!/usr/bin/python
# -*- coding: utf-8 -*-

INTEGER = 1234

def binarissa(integer):
  it = integer
  maradek = 0
  maradekok = []
  while it != 0:
    maradek = it % 2
    maradekok.append(maradek)
    it = it / 2
  strmaradekok = []
  for szamjegy in maradekok:
    strmaradekok.append(str(szamjegy))
  
  return int("".join(strmaradekok[::-1]))

def main():
  binaris = binarissa(INTEGER)
  print str(INTEGER)+ "\t" + str(binaris)+ "\t" + str(bin(INTEGER))
  

#############################################################################

if __name__ == '__main__':
  main()