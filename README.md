# An Efficient Algorithm to find (A Power M) Modulo N

Given the following expressions:

```
7^2 MOD 5
3^3 MOD 8
```

We can easily guess the answers. They are 4 and 3 respectively.

But what if, the three integers **a**, **m** and **n** are as large as possible. Example:

```
3^383 MOD 7
115^4589 MOD 124
```

Now, it is not trivial to find the answer.

The brute force technique to find the answer is also very time consuming.

The improved algorithm takes O(log m base 2) time to calculate the power modulo n.

The idea is to convert the exponent **m** into its binary equivalent.

Now, starting from L.S.B. we keep updating two other variables **a** and **y** as per the below algorithm:

```python
def power_mod(a, m, n):
    y = 1
    bin_m = get_binary(m)
    for i in reversed(bin_m):
        if int(i) == 1:
            y = (y * a) % n
        a = pow(a, 2) % n
    return y
```

The returned value of **y** is the answer.
