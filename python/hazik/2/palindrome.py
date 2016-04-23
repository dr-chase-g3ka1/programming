#!/usr/bin/python
# -*- coding: utf-8 -*-

# These functions will decide if a function is palindrome or NOT!

# First one - Trivial method
STRING1 = u"görög"
STRING2 = "deified"
STRING3 = "racecar"
STRING4 = "fasztudja"

def Trivial(string):
  if string[::-1] == string:
    return True
  else:
    return False

# Second one - Iterative

def Itearitve(String):
  length = len(String)
  
  
def Recursive(String):
  ispalindrome = True
  length = len(String) - 1
  if len(String) < 2:
    return ispalindrome
  if String[0] == String[length]:
    ispalindrome = True
    Recursive(String[1:length])
  else:
    ispalindrome = False
  return ispalindrome
    
def main():
  print "recursive " + STRING1 + " " + str(Recursive(STRING1))
  #print "eie"[1:len("eie")-1]
  print "recursive " + STRING2 + " " + str(Recursive(STRING2))
  print "recursive " + STRING3 + " " + str(Recursive(STRING3))
  print "recursive " + STRING4 + " " + str(Recursive(STRING4))
  
  print "trivial " + STRING1 + " " + str(Trivial(STRING1))
  print "trivial " + STRING2 + " " + str(Trivial(STRING2))
  print "trivial " + STRING3 + " " + str(Trivial(STRING3))
  print "trivial " + STRING4 + " " + str(Trivial(STRING4))
#############################################################################

if __name__ == '__main__':
  main()