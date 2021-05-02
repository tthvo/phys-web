---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

# Lab 6

Here are some stuffs for lab 6!
___

+++

## Overview

- This lab is probably the easiest and shortest lab so far.

- Only error calculations are the majority of the work.

- It requires a look-up for mapping resistivity and material type.

- Plotting is required for submission.

+++

## Part 1: Calculations

- Let's have a look at the setup first:

```{figure} ../../images/lab6/demo_lab6.jpg
:scale: 70
Exmperimental setup
```

````{margin}
```{hint}
The caption gave you everything!
```
````

- Your task is to collect values of $V$, and $I$ from the figures in lab manual.

- There are **5 wires of increasing diameter** of the **same material** corresponding to 5 figures. so, make sure to <mark> keep track on the figure label</mark>.

- Next, you need to calculate other quantities such as:

$$R = \frac{V}{I}\ and\ \rho = \frac{RA}{L}\ (resistivity)$$

```{caution}
The lab uses $V$ as a replacement for $\Delta{V}$ as we assume $V_0$ = 0. Instead, $\Delta{V}$ represents its uncertainty.
```

### Uncertainty Calculations

- Now, the manual says there is a special error measurement for $\Delta{V}$ and $I$.

|Quantity   |Error Specifications              |
|:---------:|:-------------------------------:|
|$\Delta{V}$|0.5% of the reading plus 2 digits|
|$\Delta{I}$|1% of the reading plus 3 digits  |

```{note}
Those '2' and '3' digits are added to the last decimal places. The number of decimal places depends on your references. For the lab, three are enough.
```

- Let's have an example. You have found $V = 9.321 V$. So its error is:

$$\Delta{V} = (9.321 V) \times 0.005 + 0.002 = 0.049 V$$

- Note that we <mark>add 0.002 because we choose to keep 3 decimal place.</mark>

+++

## Part 2: Plotting $R$ vs $A^{-1}$

- Once you have all data ready, extract the R and x columns for plotting.

- Now, you have 2 choices:
  - Logger Pro: Same steps as lab 1-5.
  - Excel: Use Scatter Plot with column R and x. 

```{attention}
Make sure to add errors in the graph for either method!
```

- Here is a demo for you to follow:

```{code-cell} ipython3
:tags: [hide-input]

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Loading data set 
df = pd.read_csv("../../data/lab6.csv", delimiter=",")

# Setting for plot
sns.set_theme("notebook", style="darkgrid", font_scale=1.3)
sns.set_palette("husl", 5)
plot = sns.lmplot(x="x",
                  y="R",
                  data=df,
                  scatter_kws={'s':70, 'edgecolor':'w'})
plot.despine()
plot.set_axis_labels(r"$A^{-1} (mm^{-2})$",r"$R (\Omega)$")
plot.ax.set_title(r"$R\ vs\ A^{-1}$")

# Now plot the error bar
plot.ax.errorbar(x=df["x"], y=df["R"], xerr=df["x error"], yerr=df["R error"], fmt='none', capsize=4)

# Show plot
plt.show()
```

## Discussion

- One question asks you to identify the wire material. This requires **resistivity table** to do the look-up.

- Last question asks you to evaluate the relationship between R and $A^{-1}$. Either use $R^2$ (Excel) or **Slope** to justify your claim.

```{tip}
For resistivity, be careful as some metal is in form of liquid at room temperature!
```

+++

## Recordings

[Click Here](https://ubc.zoom.us/rec/share/xlvKeFe-5KUgzWthDJtImWno2EsDNj6TFNs_Qoqz3_byYk3TkwoPGqDtgX98n499.L7Xr0gHKDgA6-LKP)
