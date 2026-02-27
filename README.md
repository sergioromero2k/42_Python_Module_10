# 42_Python_Module_10

## FuncMage Chronicles: The Path of Functional Programming

Welcome to **FuncMage**. In the year 2142, the digital kingdom is in chaos and only function mages can restore balance through mastery of the ancient arts of Python.

---

### Alliance Rules (Standards & Style)

For your spells to be accepted by the guild, you must follow these strict guidelines:

* **Environment:** Python 3.10 or higher.
* **Standard:** Code adhering to the `flakes` norm.
* **Robustness:** Exception handling is mandatory to prevent system crashes.
* **Clarity:** Use of **Type Hints** in all function signatures and return types.
* **Structure:** One file per exercise in its corresponding folder.
* **Focus:** Prioritize clear functional patterns over complex algorithms.

---

### Toolkit (Allowed vs. Forbidden)

#### Sacred Objects (Allowed)
* `functools`: The primary artifact for decorators and reduction.
* `typing`: For defining the nature of your data.
* `operator` and `itertools`: For advanced operations and iteration patterns.
* Built-in functions: `lambda`, `map`, `filter`, `sorted`, `callable`.

#### Dark Magic (Forbidden)
* **External libraries:** No `pip install`.
* **File I/O:** Everything must be in-memory processing.
* **Global Variables:** Forbidden; functional purity is required.
* **Forbidden Functions:** Do not use `eval()` or `exec()`.

---

### The 5 Kingdoms of Knowledge

| Challenge | File | Master Concept | Difficulty |
| :--- | :--- | :--- | :---: |
| **Ex 0** | `lambda_spells.py` | Anonymous functions and data sorting. | 🟢 3/10 |
| **Ex 1** | `higher_magic.py` | Higher-order functions (receiving/returning functions). | 🟡 5/10 |
| **Ex 2** | `scope_mysteries.py` | Lexical scope, closures and persistence (`nonlocal`). | 🟠 6/10 |
| **Ex 3** | `functools_artifacts.py` | `reduce`, `partial`, `lru_cache` and `singledispatch`. | 🔴 8/10 |
| **Ex 4** | `decorator_mastery.py` | Complex decorators, `@wraps` and static methods. | 🟣 9/10 |

---

### Exercise Overview

#### Lambda Sanctum
Master single-line functions. You will learn to sort artifacts by power, filter mages by level, and transform spell lists using `map` and `filter`.

#### 1. Higher Realm
Here functions are "first-class citizens". You will create spell combiners that merge two effects into one and amplifiers that multiply the results of other spells.

#### 2. Memory Depths
Explore closures. You will create functions that "remember" variables even after their original environment has disappeared, enabling private counters and memories without using globals.

#### 3. Ancient Library
Use the `functools` module to reduce power lists to a single value (`reduce`), pre-configure spells with fixed arguments (`partial`), and optimize performance with caching.

#### 4. Master's Tower
The final challenge. You will create decorators that measure execution time, automatically validate power levels, and retry spells that fail due to magical errors.

---

### Peer-Review Survival Guide

During evaluation, it is not enough for the code to work. You must be able to explain:

1. **Why use `lambda`?** For quick operations where defining a function with `def` would be excessive.
2. **What is a closure?** A function that retains access to the environment where it was created.
3. **What does `@wraps` do?** It prevents your decorators from "erasing" the original function's name and documentation.

---

### Testing

You can use the included `tools/data_generator.py` to generate themed test data (artifacts, mages, and spells) and verify your implementations.
