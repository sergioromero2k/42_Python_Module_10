#!/usr/bin/env python3


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    """Combines two spells: returns a tuple with the results of both."""
    def wrapper(*args, **kwargs):
        try:
            return (spell1(*args, **kwargs), spell2(*args, **kwargs))
        except Exception as e:
            print(f"Error combining spells: {e}")
            return (None, None)
    return wrapper


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    """Amplify the power: multiply the numerical result of the spell."""
    def wrapper(*args, **kwargs):
        try:
            return base_spell(*args, **kwargs) * multiplier
        except Exception as e:
            print(f"Power amplification failed: {e}")
            return 0
    return wrapper


def conditional_caster(condition: callable, spell: callable) -> callable:
    """Conditional casting: only cast the spell if the condition is True."""
    def wrapper(*args, **kwargs):
        try:
            if condition(*args, **kwargs):
                return spell(*args, **kwargs)
            return "Spell fizzled"
        except Exception as e:
            print(f"Condition check failed: {e}")
            return "Spell fizzled"
    return wrapper


def spell_sequence(spells: list) -> callable:
    """Spell sequence: executes a list and returns a list of results."""
    def wrapper(*args, **kwargs):
        results = []
        for spell in spells:
            try:
                results.append(spell(*args, **kwargs))
            except Exception as e:
                print(f"Sequence step failed: {e}")
                results.append(None)
        return results
    return wrapper


def main() -> None:
    # --- Test to validate the code ---
    # Provided test values and targets
    # test_values = [21, 14, 23]
    test_targets = ['Dragon', 'Goblin', 'Wizard', 'Knight']

    # Sample spells for testing
    def fireball(target: str) -> str:
        return f"Fireball hits {target}"

    def heal(target: str) -> str:
        return f"Heals {target}"

    def get_damage(target: str) -> int:
        return 10

    # Requirement demonstration
    print("\nTesting spell combiner...")
    combined = spell_combiner(fireball, heal)
    res = combined(test_targets[0])
    print(f"Combined spell result: {res[0]}, {res[1]}")

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(get_damage, 3)
    print(f"Original: 10, Amplified: {mega_fireball(test_targets[0])}")


if __name__ == "__main__":
    main()
