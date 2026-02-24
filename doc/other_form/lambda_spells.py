#!/usr/bin/env python3

from data_generator import FuncMageDataGenerator


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    max_power = max(mages, key=lambda x: x["power"])["power"]
    min_power = min(mages, key=lambda x: x["power"])["power"]

    total_power = sum(map(lambda x: x["power"], mages))
    avg_power = round(total_power / len(mages), 2)

    return {
        "max_power": max_power, "min_power": min_power, "avg_power": avg_power}


def main() -> None:
    data = FuncMageDataGenerator()

    print("\nTesting artifact sorter...")
    raw_data_arti = data.generate_artifacts(4)

    sorted_artifacts = artifact_sorter(raw_data_arti)

    if len(sorted_artifacts) >= 2:
        print(
            f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']}"
            " power) comes before "
            f"{sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']} "
            "power)"
        )

    print("\nTesting spell transformer...")
    raw_data_spell = data.generate_spells(4)

    print(" ".join(spell_transformer(raw_data_spell)))


if __name__ == "__main__":
    main()
