# Problem 72:
#     Counting Fractions
#
# Description:
#     Consider the fraction, n/d, where n and d are positive integers.
#     If n < d and HCF(n,d) = 1, it is called a reduced proper fraction.
#
#     If we list the set of reduced proper fractions for d ≤ 8 in ascending order of size, we get:
#         1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
#
#     It can be seen that there are 21 elements in this set.
#
#     How many elements would be contained in the set of reduced proper fractions for d ≤ 1,000,000?

def main(d_max: int) -> int:
    """
    Returns the number of distinct proper reduced fractions having denominator at most `d_max`, which are
      fractions `n/d` (where n,d are natural numbers),
      such that n < d, and
      n,d are relatively prime.

    Args:
        d_max (int): Natural number, greater than 1

    Returns:
        (int): Count of distinct proper reduced fractions n/d, where d ≤ `d_max`.

    Raises:
        AssertError: if incorrect args are given
    """
    assert type(d_max) == int and d_max > 1

    # Idea:
    #     For some fixed denominator `d`, a proper fraction can only be formed
    #       when we have numerator `n` such that 0 < n < d (d-1 possible numerators).
    #     That fraction `n/d` will only be considered 'reduced' if n and d are relatively prime.
    #     The count of valid numerators, i.e. those satisfying these constraints for our fixed `d`,
    #       is given by Euler's totient function `φ(d)`.
    #
    #     Thus, we simply need to compute the totient for all possible denominators `d`,
    #       which can be done by using a method nearly identical to the Sieve of Eratosthenes.

    # Totient values for all possible denominators.
    # Denominators 0 and 1 aren't necessary here,
    #   but just including for code readability while iterating.
    phi = list(range(d_max+1))

    # Technically, φ(1) = 1, but 1/1 is not a fraction of interest here as we want n < d.
    phi[1] = 0

    for d in range(2, d_max+1):
        if phi[d] == d:
            # `d` is prime, so discount all multiples of `d` from later denominators
            for m in range(d, d_max+1, d):
                phi[m] -= phi[m] // d
        else:
            continue

    return sum(phi)


if __name__ == '__main__':
    max_denominator = int(input('Enter a natural number (greater than 1): '))
    fraction_count = main(max_denominator)
    print('Number of distinct reduced proper fractions for d ≤ {}:'.format(max_denominator))
    print('  {}'.format(fraction_count))
