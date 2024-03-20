def sim_days(days, stats):
    stat_change = {
        "level": 0,
        "hp": 0,
        "strength": 0,
        "defense": 0,
        "movement": 0
    }
    total_zaps = 0
    zap_count = 1
    # random number of zaps per day between 2 and 4
    if options['lab_cookies'] == True:
        zap_count = random.randint(2,4)
    # simulate stat changes for each day supplied
    for i in range(days):
        if options['kitchen_quests'] == True:
            for i in range(10):
                result = random.randint(1,100)
                if result >= 1 and result <= 5:
                    stat_change['level'] += 1
                elif result >= 6 and result <= 17:
                    stat_change['hp'] += 1
                elif result >= 18 and result <= 25:
                    stat_change['strength'] += 1
                elif result >= 26 and result <= 32:
                    stat_change['defense'] += 1
                elif result >= 33 and result <= 40:
                    stat_change['movement'] += 1
        if options['training'] == True:
            if (stats['level'] + stat_change['level']) * 3 > stats['hp'] + stat_change['hp']:
                stat_change['hp'] += 1
            else:
                stat_change['level'] += 1
        if options['lab_cookies'] == True:
            if i % 7 == 0:
                zap_count = random.randint(2,4)
        
        for i in range(zap_count):
            result = random.randint(1, 89)
            if result >= 1 and result <= 12:
                stat_change['level'] -= 2
            if result >= 13 and result <= 18:
                continue
            if result >= 19 and result <= 30:
                stat_change['hp'] += random.randint(2,5)
            if result >= 31 and result <= 40:
                continue
            if result >= 41 and result <= 50:
                stat_change['movement'] += random.randint(2,3)
            if result >= 51 and result <= 60:
                stat_change['strength'] += random.randint(2,3)
            if result >= 61 and result <= 65:
                stat_change['level'] += 2
            if result >= 66 and result <= 70:
                stat_change['defense'] += random.randint(2,3)
            if result >= 71 and result <= 75:
                stat_change['strength'] -= random.randint(2,3)
            if result >= 76 and result <= 82:
                stat_change['movement'] -= random.randint(2,3)
            if result >= 83 and result <= 89:
                stat_change['defense'] -= random.randint(2,3)
            total_zaps += 1
    return stat_change
    
def print_stats(stats, stat_change):
    print(f"\nResults of {days} simulated days:")
    lines = [f"{key} {stats[key]} -> {stats[key] + stat_change[key]} \t{'%+d' % stat_change[key]}" for key in stats.keys()]
    p = padder.Padder()
    p.pad_lines(lines)
        
results = []
for i in range(100):
    stat_change = sim_days(days, beginning_stats)
    results.append(list(stat_change.values()))
averages = [round(sum(col) / len(col)) for col in zip(*results)]

stat_averages = {
    "level": averages[0],
    "hp": averages[1],
    "strength": averages[2],
    "defense": averages[3],
    "movement": averages[4],
}

print_stats(beginning_stats, stat_averages)
