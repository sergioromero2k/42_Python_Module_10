#!/usr/bin/env python3

"""
Lambda Sanctum - Functional programming with lambda expressions.
"""


# Sort artifacts by power in descending order
def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(artifacts, key=lambda x: x["power"], reverse=True)


# Filter mages whose power is greater than or equal to min_power
def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    return list(filter(lambda x: x["power"] >= min_power, mages))


# Transform spell names by adding prefix and suffix symbols
def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda x: f"* {x} *", spells))


# Calculate mage power statistics.
def mage_stats(mages: list[dict]) -> dict:
    if not mages:
        return {"max_power": 0, "min_power": 0, "avg_power": 0.0}

    # Find maximum and minimum power levels using lambda key selection
    max_power = max(mages, key=lambda x: x["power"])["power"]
    min_power = min(mages, key=lambda x: x["power"])["power"]

    total_power = sum(map(lambda x: x["power"], mages))
    avg_power = round(total_power / len(mages), 2)

    return {
        "max_power": max_power, "min_power": min_power, "avg_power": avg_power}


def main() -> None:
    # Sample artifacts data (for demonstration purposes)
    artifacts = [
        {"name": "Storm Crown", "power": 84, "type": "focus"},
        {"name": "Lightning Rod", "power": 83, "type": "armor"},
        {"name": "Wind Cloak", "power": 60, "type": "relic"},
        {"name": "Ice Wand", "power": 100, "type": "relic"},
    ]

    spells = ["darkness", "heal", "fireball", "flash"]

    print("\nTesting artifact sorter...")
    sorted_artifacts = artifact_sorter(artifacts)

    if len(sorted_artifacts) >= 2:
        print(
            f"{sorted_artifacts[0]['name']} ({sorted_artifacts[0]['power']}"
            " power) comes before "
            f"{sorted_artifacts[1]['name']} ({sorted_artifacts[1]['power']}"
            "power)"
        )

    print("\nTesting spell transformer...")
    print(" ".join(spell_transformer(spells)))


if __name__ == "__main__":
    main()
