from multiprocessing import Pool

# A sample function for squaring numbers


def square(n):
    return n * n


if __name__ == "__main__":
    # Creating a pool of 4 processes
    with Pool(4) as p:
        results = p.map(square, [1, 2, 3, 4])
    print(results)