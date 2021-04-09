---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Pre Lab 2

Help on pre lab 2 is here
___

```{code-cell} ipython3 
:tags: [hide-input]

from PIL import Image
from myst_nb import glue

im1 = Image.open("../../images/lab2/one_anti.jpg")
im2=Image.open("../../images/lab2/two_anti.jpg")
im3=Image.open("../../images/lab2/three_anti.jpg")
graph=Image.open("../../images/lab2/pre_lab2_part2.jpg")
glue('1_anti',im1, display=False)
glue('2_anti',im2,display=False)
glue('3_anti',im3,display=False)
glue('graph', graph,display=False)
```

<!-- #region -->
## Part 1

- Here, you will need to derive a formula for $\pmb{\lambda}$ from L and n (number of antinodes).

- Let's consider 3 scenarios:

| 1 Antinode | 2 Antinodes | 3 Antinodes |
|:----:|:----:|:----:|
|{glue:}`1_anti`|{glue:}`2_anti`|{glue:}`3_anti`|


```{tip}
Antinodes are points of maximum amptitude! Look to see which quantity is changing according to each case.
```

<!-- #endregion -->



<!-- #region -->
## Part 2

- This one requires a little bit of algebra <font color= 'red'><b>(getting yourself really cuz its gonna get messy!)</b></font>

- We can summarize from the graph {glue:}`graph`: 

````{panels} 
Graph
^^^
```{glue:figure} graph
:figwidth: 300px
```

---

Summary
^^^
|  $\pmb{L}$      | $1.304\pm{0.005} m$     |
|:---------------:|:-----------------------:|
|$\pmb{f}$        | $120.0\pm{0.1} Hz$      |
|$\pmb{slope}$    | $-0.0013\pm{0.0004}$   |


````


- $v = \sqrt{\frac{T}{\mu}} = f * \lambda$ (1) where: 

    - $\lambda$ = **your findings in part 1**
    - $T = m * g$ (2), mass hanging on a spring right?

- Now, look back at the graph. Ask yourself this question: <mark>Which one is the ***independent variable*** and which is the ***dependent variable***?</mark>

- Then your next step is to isolate the ***independent*** on one side and the ***dependent*** multiplying with a bunch of terms on the other.

```{tip}
Your bunch of terms that multiplies with the independent variable (not including the variable) is the slope! 
```
<!-- #endregion -->
