
### Default header

```python

import numpy as np
import scipy as sp
import matplotlib.pylab as pl


import time

# parallel computations
import multiprocessing as mp

```

### Parallel computations

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
