def root(x, n):
    return x**(1.0/n)


def md_nre_single_sample(y, y_hat, n, p):
    # assumed valid inputs
    return (root(y, n) - root(y_hat, n))**p