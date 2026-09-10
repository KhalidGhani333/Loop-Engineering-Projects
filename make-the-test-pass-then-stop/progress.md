# Progress

- 2026-09-11 | all three (add, is_even, largest) | fixed math_utils.py: `add` returned `a - b` -> `a + b`; `is_even` checked `n % 2 == 1` -> `n % 2 == 0`; `largest` returned `numbers[0]` -> `max(numbers)` | pytest: 3 passed

## Done

1. `add(a, b)` — changed `return a - b` to `return a + b` (was subtracting instead of adding).
2. `is_even(n)` — changed `return n % 2 == 1` to `return n % 2 == 0` (had the even/odd test inverted).
3. `largest(numbers)` — changed `return numbers[0]` to `return max(numbers)` (was returning the first element, not the biggest).

## Notes

- Only math_utils.py was changed; test_math.py is untouched.
- Final run: `python -m pytest -q` -> `3 passed in 0.02s`.
- Fixed on the first attempt; 5 attempts of the 6-attempt budget remain unused.
- `is_even` returns a real bool because `==` is used, which satisfies the `is True` / `is False` identity checks in the test.
