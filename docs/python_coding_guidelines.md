# Introduction

- Author: Miguel Ortuño
- Date: August 2026

This document specifies how to develop Python programs. It is
intended for use by LLMs.

# Source Code Format

- Identifiers and comments in English.

- Maximum line length of 80 columns.

- The program will start with:

  `#!/usr/bin/env python3`

- Next, it will include a comment indicating:

  - Name, date, and time of the file(s) containing the
    specification.
  - Name and version of the LLM that generated it.
  - Date and CEST time of generation.

## Programming Style

- Sequential, simple, and direct style.

- Modular: use functions of appropriate length. Neither too long
  nor too short. They should do one thing well. Typically a
  function will fit on a screen, with a few commonly accepted
  exceptions.

- A programmer with experience in C, Pascal, or Java should be
  able to understand the code without knowing advanced Python
  features.

- Prefer control structures equivalent to those available in C or
  Pascal:

  - Sequence.
  - Selection (`if`, `elif`, `else`).
  - Iteration (`for`, `while`).

- Avoid overly idiomatic or compact Python constructs.

- When multiple correct solutions exist, choose the most explicit
  and easy-to-read option, even if it is not the briefest or most
  idiomatic Python code.

## Python Features That Should Be Used

- Format strings using `str.format()`.

- Use loops like:

  ``` python
  for item in items:
      ...
  ```

  when explicit access to the index is not necessary.

- Use keyword arguments in function calls when there are more
  than two arguments:

  ``` python
  f(x=1, y=2, z=4)
  ```

- Use lists, dictionaries, tuples, and sets when they are the
  most natural data structure for the problem.

## Python Features That Should Be Avoided

- Object-oriented programming unless it provides a clear and
  significant advantage.

- Decorators.

- Metaclasses.

- Complex inheritance.

- Asynchronous programming (`async`, `await`).

- List, dictionary, and set comprehensions.

- Generator expressions.

- Anonymous functions (`lambda`) except for trivial cases.

- Functional programming based on `map()`, `filter()`, or
  `reduce()`.

- Advanced introspection.

- Operator overloading.

- Context managers (`with`).

- Features introduced after Python 3.6 unless explicitly
  requested.

- Unnecessary use of exceptions for controlling normal program
  flow.

# Dependencies

- Exclusively use the Python standard library unless it provides
  a major advantage or is explicitly stated otherwise.

# Error Codes

- The program will return 0 if execution was successful.

- The program will return non-zero values in case of error.
