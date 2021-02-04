# Lab 2

Here are some stuffs for lab2

____

## Part 1: Tension Calculation

```{tip}
Excel will help you calculate all in a few seconds!
```

## Part 2: Frequency & Pitch?


### Coming soon!


## Part 3:

- Now, there are <font color='red'><b>6 videos</b></font> corresponding to the number of anti-nodes in each case.

## Part 4: 

### Coming Soon

## Part 5: Plot and linear Fit

- In this part, you will have to plot your data in Logger Pro.
- <mark>Steps to plot your data</mark>:
    - Enter values of "n" to X column. Enter the values of frequency to Y column. (go back to Pre lab 1)
    - Create a new column: 
        - **Select Data > New Manual Column > Options header**
        - **Check Error bar calculations**
        - **Select Fixed value**

![](../../images/lab2/add_column.png)


- Here is an demonstration of what your graph might look like:

import altair as alt
import pandas as pd
import numpy as np

data = pd.read_csv('./lab2.csv', delimiter=',').rename(columns={'Number of Anti_nodes': 'n', 'f (Hz)': 'f','f error (Hz)': 'f_error'})

chart = alt.Chart(data, height=300, width=300).mark_circle(
    color='teal', 
    size = 70, 
    opacity=0.6,
).encode(
    x=alt.X('n:Q', title='Number of antinodes',scale=alt.Scale(domain=(0, 7))),
    y=alt.Y('f:Q', title='Frequency (Hz)',scale=alt.Scale(domain=(0, 100)))
).properties(
    title='Frequency vs Number of antinodes'
)

# Generate regression line
linear_fit=chart.transform_regression('n', 'f', method='linear').mark_line(color="red",strokeDash=np.array([3,3]))

# # generate the error bars
errorbars = chart.mark_errorbar(extent='stderr').encode(
    x=alt.X('x:Q'),
    yError=alt.YError(field='f_error:Q')
)

# Display the chart
alt.layer(chart,linear_fit, errorbars).interactive()

```{caution}
This is just a demo. Your graph should be in Logger Pro, which might look different! But it might give u a sense of what the values should be!
```

## Data Collection and Analysis

-  
- [Download Excel Template](https://docs.google.com/spreadsheets/d/e/2PACX-1vRAQbU1WT9LTW74JDTUguWd6Vcxvokxwkpgg5uOfV9XhA0Z3NokKYqnrwWIyuTdEVlFbwMzPE9xcfkF/pub?output=xlsx)



## Discussion Question

- 
![](../../images/lab2/discussion_lab2.jpg)








```{toctree}
:hidden:
:titlesonly:


Pre Lab 2 <pre_lab2>
```
