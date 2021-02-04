# Pre Lab 2

Help on pre lab 2 is here
___

from PIL import Image
from myst_nb import glue

im1 = Image.open("../../images/lab2/one_anti.jpg")
im2=Image.open("../../images/lab2/two_anti.jpg")
im3=Image.open("../../images/lab2/three_anti.jpg")
glue('1_anti',im1, display=False)
glue('2_anti',im2,display=False)
glue('3_anti',im3)

## Part 1

- Here, you will need to derive a formula for $\pmb{\lambda}$ from


- Let's consider 3 scenarios:


````{tabbed} 1 Anti-node
```{glue:figure} 1_anti
```
````

````{tabbed} 2 Anti-nodes
```{glue:figure} 2_anti
```
````

````{tabbed} 3 Anti-nodes
```{glue:figure} 3_anti
```
````


import sys, os
os.path.dirname(sys.executable)




## Part 2

import sys, os
os.path.dirname(sys.executable)

