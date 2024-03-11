<h1>0x02. Python - Async Comprehension</h1>

<h2> Overview </h2>
In this project I was introduced to Asynchronous comprehensions and generators in Python.

<h2> Concepts </h2>

I learnt:

- How to write an asynchronous generator.

- How to use async comprehensions.

- How to type-annotate generators.

<h2> Resources </h2>

- [PEP 530 – Asynchronous Comprehensions](https://peps.python.org/pep-0530/)

- [What’s New in Python: Asynchronous Comprehensions / Generators](https://www.blog.pythonlibrary.org/2017/02/14/whats-new-in-python-asynchronous-comprehensions-generators/)

- [Type-hints for generators
  ](https://stackoverflow.com/questions/42531143/how-to-type-hint-a-generator-in-python-3)

<h2> Tasks </h2>

<h3>Task 0 - Async Generator</h3>

Write a coroutine called `async_generator` that takes no arguments.

The coroutine will loop 10 times, each time asynchronously wait 1 second, then yield a random number between 0 and 10. Use the `random` module.

<b>File:</b> [0-async_generator.py](https://github.com/m-aishah/alx-backend-python/blob/master/0x02-python_async_comprehension/0-async_generator.py)

---

<h3>Task 1 - Async Comprehension</h3>

Import `async_generator` from the previous task and then write a coroutine called `async_comprehension` that takes no arguments.

The coroutine will collect 10 random numbers using an async comprehensing over `async_generator`, then return the 10 random numbers.

<b>File:</b> [1-async_comprehension](https://github.com/m-aishah/alx-backend-python/blob/master/0x02-python_async_comprehension/1-async_comprehension.py)

---

<h3>Task 2 -Run time for four parallel comprehensions</h3>

Import `async_comprehension` from the previous file and write a `measure_runtime` coroutine that will execute `async_comprehension` four times in parallel using `asyncio.gather`.

`measure_runtime` should measure the total runtime and return it.

Notice that the total runtime is roughly 10 seconds, explain it to yourself.

<b>File:</b> [2-measure_runtime.py](https://github.com/m-aishah/alx-backend-python/blob/master/0x02-python_async_comprehension/2-measure_runtime.py)
