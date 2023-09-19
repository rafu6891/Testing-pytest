# Testing-pytest
Learning testing with pytest

This repository contains a simple set of Python functions and their corresponding tests using `pytest`.

## Contents

- `main.py`: Contains the primary functions including a greeting function.
- `test.py`: Houses all the pytest unit tests for the functions found in `main.py`.

## Features

- **Basic Functionality**: There's a simple function (`func()`) which increments a number by 1.
- **Random Number Generation**: The `number()` function generates a random number between 1 and 100.
- **Fixtures**: Utilizes pytest's fixture feature for generating a random number and for providing a fixed sum.
- **Parameterized Testing**: Uses pytest's `mark.parametrize` to test multiple input scenarios for mathematical operations.
- **Greeting Function Test**: A test for the greeting function imported from `main.py`.

## Running the tests

Ensure you have `pytest` installed:

```bash
pip install pytest


![Test results](https://github.com/rafu6891/Testing-pytest/blob/main/Testing-pytest.png)
