from scipy import stats


def get_stat(data):
    return stats.kstest(data, "norm").statistic


if __name__ == '__main__':
    print(get_stat([1, 2, 3, 4, 5, 6]))
