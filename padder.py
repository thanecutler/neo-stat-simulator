class Padder():
    def __init__(self):
        self.width_at_index = {}

    def get_widths(self, lines):
        for line in lines:
            line = line.split(" ")
            for index, word in enumerate(line):
                if index not in self.width_at_index.keys():
                    self.width_at_index[index] = len(word) + 1
                else:
                    if len(word) + 1 > self.width_at_index[index]:
                        self.width_at_index[index] = len(word) + 1

    def pad_lines(self, lines):
        self.get_widths(lines)
        for line in lines:
            new_string = ""
            line = line.split()
            for index, word in enumerate(line):
                if index == 0:
                    new_word = word + " " * (self.width_at_index[index] - len(word))
                    new_string += new_word
                else:
                    new_word = " " * (self.width_at_index[index] - len(word)) + word
                    new_string += new_word
            print(new_string)
        return