#!/usr/bin/python
# -*- coding: utf-8 -*-

def szam_forditottja(integer):
  sztring = str(integer)
  outteger = int(sztring[::-1])
  return outteger

def main():
  INT1 = 1234
  INT2 = 453436
  
  print str(INT1)+ "\t" + str( szam_forditottja(INT1))
  print str(INT2)+ "\t" + str(szam_forditottja(INT2))
    


#############################################################################

if __name__ == '__main__':
  main()