# cProfile - A built-in module to profile the time spent on different parts of the code.
import cProfile


def example_function():
    sum([i for i in range(1000000)])


cProfile.run('example_function()')
# timeit: A module to measure the execution time of small code snippets.
import timeit

time_taken = timeit.timeit('sum([i for i in range(100)])', number=1000)
print(f"Time taken: {time_taken}")


