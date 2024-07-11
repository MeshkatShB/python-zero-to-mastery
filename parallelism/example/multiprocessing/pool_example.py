import multiprocessing


def square(n):
    return n * n


if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        numbers = [1, 2, 3, 4, 5]
        results = pool.map(square, numbers)
        print(results)
