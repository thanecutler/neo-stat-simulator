import statsim.statsim as statsim

if __name__ == "__main__":

    beginning_stats = {
        "level": 0,
        "hp": 0,
        "strength": 0,
        "defense": 0,
        "movement": 0
    }

    for stat in beginning_stats.keys():
        while beginning_stats[stat] == 0:
            try:
                beginning_stats[stat] = int(input(f"Input current {stat}: "))
            except ValueError:
                print("Please enter your pet's stat in numerical format (ex. 200)")

    run = "y"
    while run == "y":
        options = {
            "lab_ray": None,
            "lab_cookies": None,
            "training": None,
            "faerie_quests": None,
            "kitchen_quests": None
        }

        days = 0
        while days == 0:
            try:
                days = int(input("Number of days to simulate: "))
            except ValueError:
                print("Error: Please enter the number of days in numerical format (ex. 365)")

        for option in options.keys():
            while options[option] == None:
                response = str(input(f"Simulate daily {option.replace('_', ' ')}? (y/n) ")).lower()
                if response == "y":
                    options[option] = True
                elif response == "n":
                    options[option] = False
                else:
                    options[option] = None

        s = statsim.StatSim(
            days=days, 
            beginning_stats=beginning_stats, 
            options=options
        )

        s.get_stat_report()
        run = input("Run again? (y): ").lower()
