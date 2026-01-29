#!/usr/bin/env python3
"""
test.py

Simple palindrome checker utilities.

Provides:
- is_palindrome(s): returns True if s is a palindrome (ignoring case and non-alphanumeric chars)
- CLI usage: pass words/phrases as arguments or run with no args to read a line from stdin
- Basic self-tests when run with --test
"""

from __future__ import annotations
import sys
import re

def normalize(text: str) -> str:
    """Return a lowercased string containing only alphanumeric characters from text."""
    return re.sub(r'[^a-z0-9]', '', text.lower())

def is_palindrome(s: str) -> bool:
    """
    Return True if s is a palindrome, ignoring non-alphanumeric characters and case.

    Examples:
    >>> is_palindrome("A man, a plan, a canal: Panama")
    True
    >>> is_palindrome("race a car")
    False
    >>> is_palindrome("")
    True
    """
    n = normalize(s)
    return n == n[::-1]

def _run_tests() -> None:
    # Simple assertions; replace or extend with unittest/pytest if desired.
    assert is_palindrome("A man, a plan, a canal: Panama")
    assert is_palindrome("No 'x' in Nixon")
    assert not is_palindrome("Hello, world!")
    assert is_palindrome("")  # empty string is a palindrome by convention
    assert is_palindrome("12321")
    assert not is_palindrome("12345")
    print("All self-tests passed.")

def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        # No args: read one line from stdin
        try:
            line = input().rstrip("\n")
        except EOFError:
            print("No input provided.", file=sys.stderr)
            return 1
        print(is_palindrome(line))
        return 0

    if argv and argv[0] == "--test":
        _run_tests()
        return 0

    # Treat each argument as a separate string to check; print results line by line
    for item in argv:
        print(f"{item!r} -> {is_palindrome(item)}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())