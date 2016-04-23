#!/usr/bin/python
# -*- coding: utf-8 -*-

SZTRINGBAZMEG = """123. 12. 54.73: 
8000"""


# írjunk függvényt ami kap egy sztringet oszt kiszedi belőle a whitespace karaktereket
def NoMoreWhiteSpace(sztring):
  Listah = []
  for betu in sztring:
    if ((betu == "\n") or (betu == "\t") or (betu == " ")):
      continue
    Listah.append(betu)
  return ''.join(Listah)

def main():
  kicsistring = NoMoreWhiteSpace(SZTRINGBAZMEG)
  print kicsistring

#############################################################################

if __name__ == '__main__':
  main()