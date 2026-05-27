from typing import Any


def artifact_sorter(artifacts: list[dict[str, Any]]) -> list[dict[str, Any]]:
    power = sorted(artifacts, key=lambda artifact: artifact['power'],
                   reverse=True)
    return power


def power_filter(mages: list[dict[str, Any]], min_power: int
                 ) -> list[dict[str, Any]]:
    mage_filter = list(filter(lambda mage: mage['power'] >= min_power, mages))
    return mage_filter


def spell_transformer(spells: list[str]) -> list[str]:
    transformed_spell: list[str] = list(
        map(lambda spell: f"* {spell} *", spells)
    )
    return transformed_spell


def mage_stats(mages: list[dict[str, Any]]) -> dict[str, Any]:
    mage_power = [mage['power'] for mage in mages]
    max_power = max(mage_power)
    min_power = min(mage_power)
    average = round(sum(mage_power) / len(mage_power), 2)
    return {"max_power": max_power, "min_power": min_power,
            "avg_power": average}


def main() -> None:
    artifacts = [{'name': 'Crystal Orb', 'power': 72, 'type': 'relic'},
                 {'name': 'Fire Staff', 'power': 114, 'type': 'accessory'},
                 {'name': 'Storm Crown', 'power': 88, 'type': 'accessory'},
                 {'name': 'Wind Cloak', 'power': 115, 'type': 'accessory'}]
    mages = [{'name': 'Kai', 'power': 97, 'element': 'water'},
             {'name': 'Riley', 'power': 76, 'element': 'lightning'},
             {'name': 'Sage', 'power': 55, 'element': 'water'},
             {'name': 'Rowan', 'power': 73, 'element': 'wind'},
             {'name': 'Sage', 'power': 99, 'element': 'shadow'}]
    spells = ['earthquake', 'heal', 'darkness', 'freeze']

    print(f"artifact_sorter: {artifact_sorter(artifacts)}\n")
    print(f"power_filter: {power_filter(mages, 50)}\n")
    print(f"spell_transformer: {spell_transformer(spells)}\n")
    print(f"mage_stats: {mage_stats(mages)}\n")


if __name__ == "__main__":
    main()
