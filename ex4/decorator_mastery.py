#!/usr/bin/env python3

from functools import wraps
import time


def spell_timer(func: callable) -> callable:
    """
    Measures and prints the execution time of a spell.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.perf_counter()
        # Execute original function
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        duration = end_time - start_time
        print(f"Spell completed in {duration: .3f} seconds")
        return result

    return wrapper


def power_validator(min_power: int) -> callable:
    """Validates if the provided power meets the minimun requirement."""

    def decorater(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            # If it's a method, powers is usually args[2] (self,name,power)
            # If it's a function, it might be args[0]
            # Let's check 'power' in kwatgs first, then positional args.
            power = kwargs.get("power")
            if power is None:
                # We skip 'self' (args[0]) if this is a method call
                power = args[2] if len(args) > 2 else args[0]

            if isinstance(power, (int, float)) and power >= min_power:
                return func(*args, **kwargs)
            return "Insufficient power for this spell"

        return wrapper

    return decorater


def retry_spell(max_attempts: int) -> callable:
    """Retries a function call if an exception occurs,"""

    def decorator(func):
        @wraps(func)
        def wrapper(*arg, **kwargs):
            for i in range(1, max_attempts + 1):
                try:
                    return func(*arg, **kwargs)
                except Exception:
                    print(
                        f"Spell failed, retrying... "
                        f"(attempt {i}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper

    return decorator


class MageGuild:
    """Manages mage validatio nand spell casting."""

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        """
        Checks if a name is at least 3 chars long and strictly alphabetic.
        """
        if len(name) >= 3 and name.replace(" ", "").isalpha():
            return True
        return False

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        """Executes a spell if power level is sufficient."""
        return f"Successfully cast {spell_name} with power {power}"


def main() -> None:
    # === Exercise 4 Test Data ===
    # Master's Tower Test Data
    test_powers = [20, 29, 24, 15]
    # spell_names = ["fireball", "meteor", "heal", "freeze"]
    mage_names = ["Riley", "Phoenix", "Ash", "Jordan", "Casey", "Nova"]
    invalid_names = ["Jo", "A", "Alex123", "Test@Name"]

    try:
        @spell_timer
        def fireball():
            time.sleep(0.1)
            return "Fireball cast!"
        print("\nTesting spell timer...")
        result = fireball()
        print(f"Result: {result}")
    except Exception as e:
        print(f"An error occurred during spell timing: {e}")

    # Testing MageGuild...
    print("\nTesting MageGuild...")
    try:
        guild = MageGuild()

        print(guild.validate_mage_name(mage_names[1]))
        print(guild.validate_mage_name(invalid_names[0]))
        print(guild.cast_spell("Lightning", test_powers[3]))
        print(guild.cast_spell("Spark", 5))
    except Exception as e:
        print(f"A guild error occurred: {e}")


if __name__ == "__main__":
    main()
