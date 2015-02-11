## Python tricks


#### Default header

```python

import numpy as np
import scipy as sp
import matplotlib.pylab as pl


import time

# parallel computations
import multiprocessing as mp

```

#### Parallel computations

Example:

```python
import multiprocessing as mp

def func(c):
    return c**2
    
nproc=4
pool = mp.Pool(nproc)

l=[i for i in range(100)]

# parallel map
res=pool.map(func,l)
```

Note that the function func has to be declared in the root of the module (pickle problem if not)


#### Cython compile

```
$ cython -a yourmod.pyx
```

Final compilation:

```
$ gcc -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing \
      -I/usr/include/python2.7 -o yourmod.so yourmod.c
```

or create a setup.py of the form 
```python
from distutils.core import setup
from Cython.Build import cythonize

setup(
    name = "My hello app",
    ext_modules = cythonize('hello.pyx'),  # accepts a glob pattern
)
```

then compile using the command:

```
$ python setup.py build_ext --inplace 
```


#### Argument parser


Example


```python
import argparse

# initialise the parser
parser = argparse.ArgumentParser(description='Short description')  

# Add binary argument with default value
parser.add_argument('-v','--verbose', action='store_true',default=False,help='print informations')

# Add required argument
parser.add_argument('task',help='trask to perform',default='')

# Add positionnal argument (list)
parser.add_argument('list', metavar='filter', type=str, nargs='*', help='list of string')
# metavar: name of the variable in help
# nargs:
#   1 : 1 argument
#   + : 1 or more
#   ? : 0 or 1 (default if 0)
#   * : any number
          
# Add choice argument
parser.add_argument('move', choices=['rock', 'paper', 'scissors'])
# note no default possible
              
# Add subparser for command surch as svn
subparsers=parser.add_subparsers()
parser_foo = subparsers.add_parser('foo')
parser_bar = subparsers.add_parser('bar')


# parse
args = parser.parse_args()  
                

# list set values
print "Values in args:"
for name in args.__dict__:
    print name,' :\t',args.__dict__[name]

```

