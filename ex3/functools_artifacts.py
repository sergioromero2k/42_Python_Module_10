#!/usr/bin/env python3
from functools import reduce, partial, lru_cache, singledispatch
from operator import add, mul


def spell_reducer(spells: list[int], operation: str) -> int:
    """
    Reduce a list of spell powers into a single value.
    """
    if not spells:
        raise ValueError("The spell list is empty. No power to reduce!")
    # Mapping operation names to operator functions
    operations = {
        "add": add,
        "multiply": mul,
        "max": max,
        "min": min
    }
    if operation not in operations:
        raise ValueError(f"Unsuspported operation: {operation}")

    # Select reduction function and apply reduce
    return reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    """
    Create specialized enchantment functions using partial application.
    """
    # We verify that it is callable vefore proceeding.
    if not callable(base_enchantment):
        raise TypeError("The base_enchantment must be a callable function.")
    return {
            'fire_enchant': partial(
                base_enchantment, power=50, element="fire"),
            'ice_enchant': partial(base_enchantment, power=50, element="ice"),
            'lightning_enchant': partial(
                base_enchantment, power=50, element="lightning")
        }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    """Recursive Fibonacci with memoization to prevent exponential slowdown."""
    # Base case: stop recursion
    if not isinstance(n, int) or n < 0:
        raise ValueError(
            "Fibonacci is only defined for non-negative integers.")
    if n < 2:
        return n
    # Recursive Fibonacci computation with caching
    return memoized_fibonacci(n-1) + memoized_fibonacci(n-2)


def spell_dispatcher() -> callable:
    """
    Creates a single-dispatch system for different spell types.
    """
    @singledispatch
    def dispatcher(spell):
        return f"Unknown spell type: {spell}"

    @dispatcher.register(int)
    def _(spell: int):
        return f"Casting Danage Spell: {spell} HP"

    @dispatcher.register(str)
    def _(spell: str):
        return f"Casting Enchantment: {spell}"

    @dispatcher.register(list)
    def _(spell: list):
        return f"Multi-casting: {', '.join(map(str, spell))}"
    return dispatcher


def main() -> None:
    """Executing with Ancient Library Test Data"""
    spell_powers = [48, 34, 21, 31, 46, 11]
    operations = ['add', 'multiply', 'max', 'min']
    fibonacci_tests = [19, 11, 8]

    print("\nTesting spell reducer...")
    for op in operations:
        result = spell_reducer(spell_powers, op)
        print(f"{op.capitalize()}: {result}")

    print("\nTesting memoized fibonacci...")
    for n in fibonacci_tests:
        print(f"Fib({n}): {memoized_fibonacci(n)}")

    # print("\n--- Dispatcher Demonstration ---")
    # cast = spell_dispatcher()
    # print(cast(100))
    # print(cast("Frost Nova"))
    # print(cast([10, "Shield", 20]))


if __name__ == "__main__":
    main()
