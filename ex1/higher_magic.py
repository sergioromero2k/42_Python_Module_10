#!/usr/bin/env python3

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> callable:
    def combined(*args, **kwargs):
        r1 = spell1(*args, **kwargs)
        r2 = spell2(*args, **kwargs)
        return (r1, r2)

    return combined


def power_amplifier(base_spell: callable, multiplier: int) -> callable: ...


def conditional_caster(condition: callable, spell: callable) -> callable: ...


def spell_sequence(spells: list[callable]) -> callable: ...


def main() -> None:
    fireball = lambda x: f"Fire {x}"
    heal = lambda x: f"heal {x}"

    combo = spell_combiner(fireball, heal)
    print(combo("Dragon"))


if __name__ == "__main__":
    main()
