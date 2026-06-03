import time
from typing import Any
from functools import wraps
from collections.abc import Callable


def spell_timer(func: Callable[[], str]) -> Callable[[], str]:
    @wraps(func)
    def time_execution(*args: Any, **kargs: Any) -> str:
        print(f"Casting {func.__name__}...")
        start = time.time()
        result = func(*args, **kargs)
        end = time.time()
        print(f"Spell completed in {round(end - start, 3)} seconds")
        return result
    return time_execution


@spell_timer
def slow_fireball() -> str:
    time.sleep(0.101)
    return "Fireball cast!"


def power_validator(min_power: int) -> Callable[..., Callable[..., Any]]:
    def decorator(func: Callable[..., str]) -> Callable[..., Any]:
        @wraps(func)
        def validate_power(*args: Any, **kwargs: Any) -> Any:
            try:
                if isinstance(args[0], MageGuild):
                    power = args[2]
                else:
                    power = args[0]
                if power >= min_power:
                    return func(*args, **kwargs)
                else:
                    return "Insufficient power for this spell"
            except TypeError:
                raise ValueError("[ERROR] First argument must be an integer")
        return validate_power
    return decorator


@power_validator(10)
def fireball(power: int, target: str) -> str:
    return f"target: {target} power: {power}"


def retry_spell(max_attempts: int) -> Callable[..., Callable[..., str]]:
    def failed_decorator(func: Callable[..., str]) -> Callable[..., Any]:
        @wraps(func)
        def retry_spell(*args: Any, **kwargs: Any) -> Any:
            test: int = 0
            while test < max_attempts:
                try:
                    return func(*args, **kwargs)
                except Exception:
                    test += 1
                    print("Spell failed, retrying...(attempt "
                          f"{test}/{max_attempts})")
                    if test == max_attempts:
                        return "Spell casting failed after "
                    "max_attempts attempts"
        return retry_spell
    return failed_decorator


@retry_spell(3)
def raise_error() -> str:
    import random
    if random.choice([True, False]):
        raise Exception("An error")
    return ("Waaaaaaagh spelled !")


class MageGuild:
    def __init__(self) -> None:
        pass

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) > 3 and all(letter.isalpha() or letter == " "
                                 for letter in name):
            return True
        return False

    @power_validator(10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("Testing spell timer...")
    print("Result:", slow_fireball())

    print("\nTesting power validator...")
    try:
        print("Result:", fireball(20, "dragon"))
    except Exception as e:
        print(e)

    print("\nTesting retrying spell...")
    print(raise_error())

    print("\nTesting MageGuild...")
    mage = MageGuild()
    print(mage.validate_mage_name("Endevor Elenor"))
    print(mage.validate_mage_name("Endevor21"))
    print(mage.cast_spell("Lightning", 15))
    print(mage.cast_spell("Lightning", 7))


if __name__ == "__main__":
    main()
