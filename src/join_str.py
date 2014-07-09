#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 9, 2014

@author: anroco

In python how to join several strings into one?

En python ¿como concatenar varios strings en uno solo?
'''

#create a str
s = 'many years later'
print(s)

#create a new str result of using the + operator
s_join = s + ', as he faced the firing squad'
print(s_join)

#create a list with string items
l = ['strings', 'are', 'immutable', 'sequences', 'of', 'characters', 'unicode']

#generates a string which is the concatenation of the strings in itarable
#object, define the separator to use between elements.
s_join = ' '.join(l)
print(s_join)

#uses join() method of a str object. the separator is the '@' character
s_join = '@'.join(['username', 'domain.com'])
print(s_join)
