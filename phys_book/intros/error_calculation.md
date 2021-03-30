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

# Error Calculation

Here are some tips for error calculations!

___

+++

## Terminology

- **Absolute error $\delta{A}$**: The error in a quantity A that has the same units as the quantity.

- **Relative error $\frac{\delta{A}}{A}$**: The error expressed as a fractional or percentage.

```{caution}
These terms has confused a lot of students. So please be careful!
```

+++

## Rules with errors

```{tabbed} Addition Rule
<p style="font-size:25px"><b>Explanation</b></p>

The maximum possible error  of  a  sum  or  difference  is  calculated  by  adding  the  absolute  errors  in  the  quantities  to  be added or subtracted.

$$\delta{A+B} = \delta{A} + \delta{B}$$
```

```{tabbed} Product Rule
<p style="font-size:25px"><b>Explanation</b></p>

The relative maximum possible error of a product or quotient is equal to the sum of the relativeerrors in the quantities being multiplied or divided.

$$
\frac{\delta{(AB)}}{AB} = \frac{\delta{(A/B)}}{A/B}= (\frac{\delta{A}}{A} + \frac{\delta{B}}{B})
$$
```

```{tabbed} Power Rule
<p style="font-size:25px"><b>Explanation</b></p>

If a number x is raised to some power n then the relative error in the result is $|n|$ times the relative error in x.

$$
\frac{\delta{x^n}}{x^n} = |n| \frac{\delta{x}}{x}
$$
```

```{attention}
All formula above are to calculate the maximum error associated with the calculations.
```

+++

## Tips for applying rules

- Here are the helpful steps that I went through all the pains to gather:
  - **Step 1**: Identify the operators. This helps find which rules will be applied.
  - **Step 2**: Identify large component. For example, in $X = a^3 b^{-2} c$, $a^3$ and $b^{-2}$ are large component while c (only itself) is a small one. In this case, c is also the simplest/smallest component.
  - **Step 3**: Apply the rules above with large components as if they are small.
  - **Step 4**: Move into each large component. Identify the smaller components and operators inside it.
  - **Step 5**: Apply the rules for those smaller components you just identify.
  - **Step 6**: Continue until the you see the smallest/simplest components in your calculation.

+++

## Challenges

- Try to solve these formula. Assume a, b, c, d are arbitrary terms with corresponding error $\delta{a}$, $\delta{b}$, $\delta{c}$, $\delta{d}$.
  - Problem 1: $X = abcd$
  - Problem 2: $X = a+bcd$
  - Problem 3: $X = \frac{a^3 b^-2}{c} + d$
  - Problem 4: $X = \frac{c+d}{a^2 b^-1} + d$

+++

## Danger of the Internet

- When searching on the internet, there are many interpretation of the error calculations. Most of them are nowhere near similar to that of our physics labs.
- However, they are not wrong. The only problem is that **those cannot be applied in the context of our physics labs**.

```{warning}
Always evaluate your findings. For example, check the source website, or contact your Profs/TAs. **Do not ever trust anything on first sight**.
```
