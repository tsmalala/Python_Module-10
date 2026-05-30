from collections.abc import Callable


def fireball(target: str, power: int) -> str:
    return f"Fireball hits {target} for {power} HP"


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def lumos(taget: str, power: int) -> str:
    return f"Lumos light up {taget} for {power} HP"


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def spell(target: str, power: int) -> tuple[str, str]:
        return (spell1(target, power), spell2(target, power))
    return spell


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def new_spell(target: str, power: int) -> str:
        return (base_spell(target, power * multiplier))
    return new_spell


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(target: str, power: int) -> str:
        if condition(target, power):
            return (spell(target, power))
        else:
            return "Spell fizzled"
    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def cast_spell(target: str, power: int) -> list[Callable]:
        spell_list: list[Callable] = []
        for iter_spell in spells:
            spell_list.append(iter_spell(target, power))
        return spell_list
    return cast_spell


def main() -> None:
    print("Testing spell combiner...")
    combined_spell = spell_combiner(fireball, heal)
    print("Combined spell result:",
          combined_spell("Dragon", 24))

    print("\nTesting power amplifier...")
    mega_fireball = power_amplifier(fireball, 3)
    print("Original:", fireball("Knight", 6),
          "\nAmplified:", mega_fireball("Knight", 6))

    print("\nTesting conditional caster...")

    def is_strong(target, power):
        return power > 10
    conditional_example = conditional_caster(is_strong, fireball)
    print(conditional_example("Dragon", 6))

    print("\nTesting spell sequence...")
    spell = spell_sequence([fireball, heal, lumos])
    print(spell("Wizard", 24))


if __name__ == "__main__":
    main()
