def count_partitions(n, m):
    """Count the ways to partition n using parts up to m."""
    if n == 0:
        return 1
    elif n < 0:
        return 0
    elif m == 0:
        return 1
    else:
        return count_partitions(n - 1, m) + count_partitions(n, m - 1)

result = count_partitions(6, 4)
print(result)

