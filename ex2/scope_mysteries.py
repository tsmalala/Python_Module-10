from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    mage = 0

    def counter() -> int:
        nonlocal mage
        mage += 1
        return mage
    return counter


def spell_accumulator(initial_power: int) -> Callable:
    total_power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total_power
        total_power += amount
        return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    memory: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        memory[key] = value

    def recall(key: str) -> str:
        if key not in memory:
            # return f"'{key}': Memory not found"
            return "Memory not found"
        # return f"'{key}' : {memory[key]}"
        return memory[key]

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    print("Testing mage counter...")
    counter_a = mage_counter()
    print("counter_a call 1:", counter_a())
    print("counter_a call 2:", counter_a())
    counter_b = mage_counter()
    print("counter_b call 1:", counter_b())

    print("\nTesting spell accumulator...")
    base = spell_accumulator(100)
    print("Base 100, add 20:", base(20))
    print("Base 100, add 30:", base(30))

    print("\nTesting enchantment factory...")
    factory = enchantment_factory("Flaming")
    print(factory("Sword"))
    factory = enchantment_factory("Frozen")
    print(factory("Shield"))

    print("\nTesting memory vault...")
    vault = memory_vault()
    print("Store 'secret' = 42")
    vault["store"]("secret", 42)
    # print("Recall", vault["recall"]("secret"))
    print(f"Recall 'secret': {vault['recall']('secret')}")
    print(f"Recall 'unknown': {vault['recall']('unknown')}")
    # print("Recall", vault["recall"]("unknown"))


if __name__ == "__main__":
    main()
