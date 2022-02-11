
# An Efficient Algorithm to find Power Modulo N

# @author: ABHISHEK
# @github: https://github.com/abhishek-bits

# given a decimal number,
# returns a binary string representation
def get_binary(n):
    s = ""
    while n > 0:
        if (n & 1) == 1:
            s = "1" + s
        else:
            s = "0" + s
        n = n >> 1
    return s


# the efficient algorithm to find a^m MOD n
# Time Complexity: O(log m base 2)
def power_mod(a, m, n):
    # initialize y
    y = 1
    # first let us convert m into binary
    bin_m = get_binary(m)
    # now we need to iterate and find out 'a' and 'y'
    for i in reversed(bin_m):
        if i == '1':
            y = (y * a) % n
        a = pow(a, 2) % n
    return y


if __name__ == '__main__':
    print('17^22 MOD 21:', power_mod(17, 22, 21))
    print('3^383 MOD 7:', power_mod(3, 383, 7))
