import random
import copy

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, quantity in kwargs.items():
            self.contents += [color] * quantity

    def draw(self, num_balls_drawn):
        drawn_balls = []
        if num_balls_drawn >= len(self.contents):
            return self.contents
        for _ in range(num_balls_drawn):
            ball_index = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(ball_index))
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    num_success = 0
    for _ in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        drawn_balls = hat_copy.draw(num_balls_drawn)
        drawn_dict = {color: drawn_balls.count(color) for color in set(drawn_balls)}
        success = True
        for color, count in expected_balls.items():
            if color not in drawn_dict or drawn_dict[color] < count:
                success = False
                break
        if success:
            num_success += 1
    return num_success / num_experiments

# Example usage:
hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat,
                         expected_balls={"red":1,"green":2},
                         num_balls_drawn=4,
                         num_experiments=10000)
print(probability)
