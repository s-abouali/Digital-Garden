import random
import time

garden = []

print("🌱 Welcome to your Digital Garden!")
print("Type anything to plant a seed.")
print("Type 'quit' to leave your garden.\n")

while True:
    word = input("Plant a seed: ")

    if word.lower() == "quit":
        break

    # Growth depends on the length of what you typed
    growth = len(word) + random.randint(1, 10)

    plant = {
        "name": random.choice([
            "Moonflower", "Star Fern", "Pixel Rose",
            "Thunder Tree", "Neon Mushroom", "Dream Vine"
        ]),
        "growth": growth
    }

    garden.append(plant)

    print(f"\n🌱 You planted a {plant['name']}!")
    print("Growing", end="", flush=True)

    for _ in range(3):
        time.sleep(0.4)
        print(".", end="", flush=True)

    print(f"\n✨ It grew {growth} points!\n")

    # Random garden event
    event = random.choice([
        "A butterfly visited your garden. 🦋",
        "It started raining pixels. 🌧️",
        "A mysterious glow appeared. ✨",
        "A tiny fairy watered your plants. 🧚",
        "Nothing happened... suspicious. 👀"
    ])

    print(event)

    print("\n🌿 YOUR GARDEN")
    print("-" * 30)

    for plant in garden:
        level = "🌱" if plant["growth"] < 10 else \
                "🌿" if plant["growth"] < 20 else \
                "🌳"

        print(f"{level} {plant['name']} — {plant['growth']} growth")

    print("-" * 30 + "\n")

print("\n🌙 Your garden is going to sleep...")
print(f"You grew {len(garden)} plant(s).")
print("Thanks for visiting! 🌌")
