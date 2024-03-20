import random
import padder

class StatSim():
    def __init__(self, days, beginning_stats, options):
        self.days = days
        self.beginning_stats = beginning_stats
        self.options = options
        self.stat_change = {
            "level": 0,
            "hp": 0,
            "strength": 0,
            "defense": 0,
            "movement": 0
        }
        
    def change_stat(self, stat, value):
        self.stat_change[stat] += value

    def sim_zap(self):
        result = random.randint(1, 89)
        if result >= 1 and result <= 12:
            self.change_stat('level', -2)
        if result >= 13 and result <= 18:
            return
        if result >= 19 and result <= 30:
            self.change_stat('hp', random.randint(2,5))
        if result >= 31 and result <= 40:
            return
        if result >= 41 and result <= 50:
            self.change_stat('movement', random.randint(2,3))
        if result >= 51 and result <= 60:
            self.change_stat('strength', random.randint(2,3))
        if result >= 61 and result <= 65:
            self.change_stat('level', 2)
        if result >= 66 and result <= 70:
            self.change_stat('defense', random.randint(2,3))
        if result >= 71 and result <= 75:
            self.change_stat('strength', random.randint(-3,-2))
        if result >= 76 and result <= 82:
            self.change_stat('movement', random.randint(-3,-2))
        if result >= 83 and result <= 89:
            self.change_stat('defense', random.randint(-3,-2))
    
    def sim_kitchen_quest(self):
        result = random.randint(1,100)
        if result >= 1 and result <= 5:
            self.change_stat('level', 1)
        elif result >= 6 and result <= 17:
            self.change_stat('hp', 1)
        elif result >= 18 and result <= 25:
            self.change_stat('strength', 1)
        elif result >= 26 and result <= 32:
            self.change_stat('defense', 1)
        elif result >= 33 and result <= 40:
            self.change_stat('movement', 1)

    def sim_training_school(self):
        if self.beginning_stats['level'] + self.stat_change['level'] * 3 > self.beginning_stats['hp'] + self.stat_change['hp']:
            self.change_stat('hp', 1)
        else:
            self.change_stat('level', 1)
    
    def sim_faerie_quest(self):
        result = random.randint(1,100)
        # light faerie
        if result >= 1 and result <= 11:
            self.change_stat('level', 2)
        # dark faerie
        if result >= 12 and result <= 22:
            self.change_stat('hp', 3)
        # fire faerie
        if result >= 23 and result <= 33:
            self.change_stat('strength', 3)
        # water faerie
        if result >= 34 and result <= 44:
            self.change_stat('defense', 3)
        # air faerie
        if result >= 45 and result <= 55:
            self.change_stat('movement', 2)
        # earth faerie
        if result >= 56 and result <= 66:
            stat = random.choice(['strength', 'defense', 'movement'])
            self.change_stat(stat, 3)
        # grey faerie
        if result >= 67 and result <= 77:
            r = random.randint(0,100)
            # 13% for level
            if r >= 1 and r <= 13:
                self.change_stat('level', 2)
            # 17% for hp
            if r >= 14 and r <= 30:
                self.change_stat('hp', 3)
            # 23% for strength
            if r >= 31 and r <= 53:
                self.change_stat('strength', 3)
            # 23% for defense
            if r >= 54 and r <= 76:
                self.change_stat('defense', 3)
            # 24% for movement
            if r >= 77 and r <= 100:
                self.change_stat('movement', 3)
        # soup faerie
        if result >= 78 and result <= 88:
            r = random.randint(1,3)
            if r == 1:
                self.change_stat('hp', 2)
                self.change_stat('movement', 2)
            elif r == 2:
                self.change_stat('strength', 2)
                self.change_stat('level', 2)
            elif r == 3:
                self.change_stat('hp', 2)
                self.change_stat('defense', 2)
        # battle faerie
        if result >= 89 and result <= 94:
            self.change_stat('level', 3)
            self.change_stat('strength', 3)
            self.change_stat('defense', 3)
        # queen fyora
        if result >= 95 and result <= 98:
            self.change_stat('level', 2)
            self.change_stat('hp', 5)
            self.change_stat('strength', 5)

    def sim_days(self):
        options = self.options
        for i in range(self.days):
            if options['lab_ray'] == True:
                zap_count = 1
                # update zap count if using cookies
                if options['lab_cookies'] == True:
                    if i == 1 or i % 7 == 0:
                        zap_count = random.randint(2,4)
                for i in range(zap_count):
                    self.sim_zap()
            if options['kitchen_quests'] == True:
                for i in range(10):
                    self.sim_kitchen_quest()
            if options['training'] == True:
                self.sim_training_school()
            if options['faerie_quests'] == True:
                self.sim_faerie_quest()
    
        return self.stat_change.values()
    
    def reset_stat_change(self):
        self.stat_change = {
            "level": 0,
            "hp": 0,
            "strength": 0,
            "defense": 0,
            "movement": 0
        }

    def print_stats(self, stat_change):
        stats = self.beginning_stats
        selected_options = [o for o in self.options if self.options[o] != False]
        print(f"\nResults of {self.days} simulated days:")
        for o in selected_options:
            print(f"- {o.replace('_', ' ')}")
        print('-' * 30)
        lines = [f"{key} {stats[key]} -> {stats[key] + stat_change[key]} \t{'%+d' % stat_change[key]}" for key in stats.keys()]
        p = padder.Padder()
        p.pad_lines(lines)

    def get_stat_report(self):
        results = []
        # run sim 100 times and collect outputs
        for i in range(100):
            stat_change = self.sim_days()
            results.append(stat_change)
            self.reset_stat_change()
        averages = [round((sum(col) / len(col))) for col in zip(*results)]
        stat_averages = {
            "level": averages[0],
            "hp": averages[1],
            "strength": averages[2],
            "defense": averages[3],
            "movement": averages[4],
        }
        self.print_stats(stat_averages)
        return
        