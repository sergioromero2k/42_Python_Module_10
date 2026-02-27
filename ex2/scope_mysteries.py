#!/usr/bin/env python3


def mage_counter() -> callable:
    """Return a functio that counts its calls using a closure."""
    n = 0

    def counter() -> int:
        nonlocal n
        n += 1
        return n
    return counter


def spell_accumulator(initial_power: int) -> callable:
    """Return a function that accumulates power values."""
    total_power = initial_power

    def accumulator(amount: int) -> int:
        nonlocal total_power
        try:
            total_power += amount
            return total_power
        except TypeError as e:
            print(f"Accumulation error: {e}")
            return total_power
    return accumulator


def enchantment_factory(enchantment_type: str) -> callable:
    """Return a function that applies a specific enchantment string."""
    def enchant(item_name: str) -> str:
        try:
            return f"{enchantment_type} {item_name}"
        except Exception as e:
            print(f"Enchantment error: {e}")
            return "Failed enchantment"
    return enchant


def memory_vault() -> dict[str, callable]:
    """Return a dictionary with store and recall closure functions."""
    _storage = {}

    def store(key: str, value: any) -> None:
        try:
            _storage[key] = value
        except Exception as e:
            print(f"Vault storage error: {e}")

    def recall(key: str) -> any:
        try:
            return _storage.get(key, "Memory not found")
        except Exception as e:
            print(f"Vault recall error: {e}")
            return "Memory error"

    return {
        "store": store,
        "recall": recall
    }


def main() -> None:
    """Demonstrate closure functionality with the provided test cases."""

    # initial_powers = [34, 51, 45]
    # power_additions = [5, 15, 9, 19, 11]
    # enchantment_types = ['Earthen', 'Windy', 'Dark']
    # items_to_enchant = ['Sword', 'Ring', 'Staff', 'Shield']

    print("Testing mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting enchantment factory...")
    flaming_factory = enchantment_factory("Flaming")
    frozen_factory = enchantment_factory("Frozen")
    print(flaming_factory("Sword"))
    print(frozen_factory("Shield"))


if __name__ == "__main__":
    main()
