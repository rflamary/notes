#!/usr/bin/python
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 21 14:56:10 2015

@author: rflamary
"""

import argparse

# initialise the parser
parser = argparse.ArgumentParser(description='Short description')  

# Add binary argument with default value
parser.add_argument('-v','--verbose', action='store_true',default=False,help='print informations')

# Add required argument
#parser.add_argument('task',help='trask to perform',default='')

# Add positionnal argument (list)
parser.add_argument('list', metavar='filter', type=str, nargs='*', help='list of string')
# metavar: name of the variable in help
# nargs:
#   1 : 1 argument
#   + : 1 or more
#   ? : 0 or 1 (default if 0)
#   * : any number
          
# Add choice argument
#parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
# note no default possible
              
# Add subparser for command surch as svn
#subparsers=parser.add_subparsers()
#parser_foo = subparsers.add_parser('foo')
#parser_bar = subparsers.add_parser('bar')


# parse
args = parser.parse_args()  
                

# list set values
print "Values in args:"
for name in args.__dict__:
    print name,' :\t',args.__dict__[name]