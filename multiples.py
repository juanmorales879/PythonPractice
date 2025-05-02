def count_by(x, n):
    """
    Return a sequence of numbers counting by `x` `n` times.
    """
    multiples = []
    for i in range(1,n+1):
        double = i*x
        multiples.append(double)
    return multiples
#  return [i * x for i in range(1, n + 1)]