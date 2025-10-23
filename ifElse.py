#!/usr/bin/env python3

#if else

x= 10
y= 20 

def probe(wert1, wert2):
  if wert1 > wert2:
    print(wert1, "ist größer als", wert2)
  elif wert1<wert2:
    print(wert1, "ist kleiner als", wert2)
  else:
    print("Beide Werte sind gleich groß!!!")

probe(x,y)

x= 3.5
y= 4.75

def ifelse(a,b):
  if a>b:
    print(a, "größer als", b)
  elif a<b:
    print(a, "kleiner als", b)
  else:
    print(a, "gleich groß wie", b)

ifelse(x,y)