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
glue('3_anti',im3,display=False)

## Part 1

- Here, you will need to derive a formula for $\pmb{\lambda}$ from L and n (number of antinodes).

- It is pretty straightforward if you could sketch out some cases. So, I did it for you. 

- Let's consider 3 scenarios (look closely!):


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


```{tip}
Antinodes are points of maximum amptitude! Look at each case and see which number is changing in response to each case.
```




## Part 2

- This one requires a little bit of algebra <font color= 'red'><b>(getting yourself really cuz its gonna get messy!)</b></font>

- Look at the graph below and we can summarize: 

![](../../images/lab2/pre_lab2_part2.jpg)

|Quantity|Value|
|:---------------:|:----------------:|
|$\pmb{L}$| $1.304\pm{0.005} m$
|$\pmb{f}$| $120.0\pm{0.1} Hz$|
|$\pmb{Slope}$| $-0.0013\pm{0.0004} $|


