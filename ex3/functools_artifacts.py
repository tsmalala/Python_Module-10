from functools import reduce, lru_cache, partial, singledispatch
from collections.abc import Callable
from operator import add, mul
from typing import Any


def spell_reducer(spells: list[int], operation: str) -> int:
    final_reduce: int = 0
    if len(spells) == 0:
        return 0
    if operation == "add":
        final_reduce = reduce(add, spells)
        return final_reduce
    elif operation == "multiply":
        final_reduce = reduce(mul, spells)
        return final_reduce
    elif operation == "max":
        final_reduce = reduce(max, spells)
        return final_reduce
    elif operation == "min":
        final_reduce = reduce(min, spells)
        return final_reduce
    print("[ERROR] Unknown operation")
    return 0


def base_enchantment(power: int, element: str, target: str) -> str:
    return f"Enchanting {target} with {power} power of {element}"


def partial_enchanter(base_enchantment: Callable[[int, str, str], str]
                      ) -> dict[str, Callable[[str], str]]:
    return {
        "Dragon": partial(base_enchantment, 50, "fire"),
        "Sword": partial(base_enchantment, 50, "ice"),
        "Light": partial(base_enchantment, 50, "lightning")
        }


@lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def dispatcher(data: Any) -> str:
        return "Unknown spell type"

    @dispatcher.register(int)
    def _(data: int) -> str:
        return f"Damage spell: {data} damage"

    @dispatcher.register(str)
    def _(data: str) -> str:
        return f"Enchantment: {data}"

    @dispatcher.register(list)
    def _(data: list[Any]) -> str:
        return f"Multi-cast: {len(data)} spells"
    return dispatcher


def main() -> None:
    spell_powers = [41, 43, 29, 33, 29, 35]

    print("\nTesting spell reducer...")
    print(f"Sum: {spell_reducer(spell_powers, 'add')}")
    print(f"Product: {spell_reducer(spell_powers, 'multiply')}")
    print(f"Max: {spell_reducer(spell_powers, 'max')}")

    print("\nTesting partial enchanter...")
    partial_func = partial_enchanter(base_enchantment)
    print(partial_func["Dragon"]("dragon"))
    print(partial_func["Sword"]("sword"))
    print(partial_func["Light"]("armor"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    spell = spell_dispatcher()
    print(spell(42))
    print(spell("fireball"))
    print(spell([15, "hello", "hi"]))
    print(spell(1.5))


if __name__ == "__main__":
    main()
