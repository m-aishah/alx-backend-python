<h1> Overview </h1>
In this project I was introduced to Asyncio in Python.

<h2> Concepts </h2>

I learnt:

- async and await syntax.

- How to execute an async program with asyncio.

- How to run concurrent coroutines.

- How to create asyncio tasks.

- How to use the random module.

<h2> Resources </h2>

- [Async IO in Python: A Complete Walkthrough](https://realpython.com/async-io-python/)

- [asyncio - Asynchronous I/O](https://docs.python.org/3/library/asyncio.html)

- [random.uniform](https://docs.python.org/3/library/random.html#random.uniform)

<h2> Tasks </h2>

<h3>Task 0 - The basics of async</h3>

Write an asynchronous coroutine that takes in an integer argument (`max_delay`, with a default value of `10`) named wait_random that waits for a random delay between `0` and `max_delay` (included and float value) seconds and eventually returns it.

Use the random module.

<b>File:</b> [0-basic_async_syntax.py](https://github.com/m-aishah/alx-backend-python/blob/master/0x01-python_async_function/0-basic_async_syntax.py)

<h3>Task 1 - Let's execute multiple coroutines at the same time with async</h3>

Import `wait_random` from the previous python file that you’ve written and write an async routine called `wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. You will spawn `wait_random` `n` times with the specified `max_delay`.

`wait_n` should return the list of all the delays (float values). The list of the delays should be in ascending order without using `sort()` because of concurrency.

<b>File:,
</b> [1-concurrent_coroutines.py](https://github.com/m-aishah/alx-backend-python/blob/master/0x01-python_async_function/1-concurrent_coroutines.py)

<h3>Task 2 - Measure the runtime</h3>

From the previous file, import `wait_n` into `2-measure_runtime.py`.

Create a `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay) and returns `total_time / n`. Your function should return a float.

Use the `time` module to measure an approximate elapsed time.

<b>File:</b> [2-measure_runtime.py](https://github.com/m-aishah/alx-backend-python/blob/master/0x01-python_async_function/2-measure_runtime.py)

<h3>Task 3 - Tasks</h3>

Import `wait_random` from `0-basic_async_syntax`.

Write a function (do not create an async function, use the regular function syntax to do this) `task_wait_random` that takes an integer `max_delay` and returns a `asyncio.Task`.

<b>File:</b> [3-tasks.py](https://github.com/m-aishah/alx-backend-python/blob/master/0x01-python_async_function/3-tasks.py)

<h3>Task 4 - Tasks</h3>

Take the code from `wait_n` and alter it into a new function `task_wait_n`. The code is nearly identical to `wait_n` except `task_wait_random` is being called.

<b>File:</b> [4-tasks.py](https://github.com/m-aishah/alx-backend-python/blob/master/0x01-python_async_function/4-tasks.py)
