import random
import pytest
from main import greeting

def func(x):
    """Return the input incremented by 1."""
    return x + 1

def test_answer():
    """Test if the func() increments the input by 1."""
    assert func(4) == 5

def number():
    """Return a random number between 1 and 100."""
    return random.randint(1, 100)

def test_random():
    """Test if the number() function returns a value between 1 and 100."""
    result = number()
    assert result >= 1 and result <= 100

@pytest.fixture(scope='function')
def random_number():
    """Fixture to generate a random number between 1 and 100."""
    return random.randint(1, 100)

def test_random_with_fixture(random_number):
    """Test using the random_number fixture."""
    assert 1 <= random_number <= 100

@pytest.fixture(scope="function")
def sum_result():
    """Fixture to provide a fixed sum result."""
    a = 1
    b = 2
    return a + b

def test_sum(sum_result, random_number):
    """Test the sum of sum_result and random_number."""
    final_result = sum_result + random_number
    assert final_result > 1

def test_rest(sum_result, random_number):
    """Test the difference between sum_result and random_number."""
    final_result = sum_result - random_number
    assert final_result < 100

def test_multi(sum_result, random_number):
    """Test the sum vs. multiplication of sum_result and random_number."""
    final_result = sum_result + random_number
    assert final_result != sum_result * random_number


@pytest.mark.parametrize('input1, expected', [('3+5', 8), ('2+4', 6), ('6*9', 54)])
def test_with_mark(input1, expected):
    """Test mathematical operations using parameterized testing."""
    assert eval(input1) == expected

def test_greeting():
    """Test the greeting function from the main module."""
    result = greeting()
    assert result == "Hello, I'm testing pytest!"