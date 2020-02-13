import time


def decorator(func):
    def wrapper():
        print(f'running {func}')
        func()
        print('done')

    return wrapper


def timeit(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        output = func(*args, **kwargs)
        end = time.perf_counter() - start
        print(f"function took: {end}")
        return output
    return wrapper


@timeit
def compute(power):
    return 2 ** power


@timeit
def talk():
    print('some talk')


if __name__ == '__main__':
    output = compute(10)
    print(output)
    talk()
