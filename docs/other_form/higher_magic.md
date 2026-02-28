def main() -> None:

    === 1: spell_combiner ===
    fireball = lambda x: f"Fire {x}"
    heal = lambda x: f"heal {x}"

    combo = spell_combiner(fireball, heal)
    print(combo("Dragon"))

    === 2: power_amplifier ===
    fireball = lambda x: f"{x}"

    boosted = power_amplifier(fireball, 3)
    print(boosted(10))

    === 3: conditional_caster ===
    def fireball_2(x):
        return x * 2

    def is_positive(x):
        return x > 0

    conditional_spell = conditional_caster(is_positive, fireball_2)
    print(conditional_spell(10))
    print(conditional_spell(-5))

    === 4: Spell Sequence ===

    def fireball(x):
        return x * 2

    def heal(x):
        return x + 5

    def shield(x):
        return x + 3

    spells = [fireball, heal, shield]
    combo = spell_sequence(spells)
    print(combo(10))
    """

if __name__ == "__main__":
    main()
