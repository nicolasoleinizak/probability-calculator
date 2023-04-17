import copy
import random
# Consider using the modules imported above.

class Hat:
    def __init__(self, **kwargs) -> None:
        self.contents = []
        self.contents_copy = []
        for key, value in kwargs.items():
          for i in range(value):
            self.contents.append(key)

    def draw (self, number):
      if self.contents_copy:
        self.contents = self.contents_copy.copy()
      self.contents_copy = self.contents.copy()
      drawing_content = []
      for i in range(number):
        if len(self.contents) == 0:
          break
        random_index = random.randrange(0, len(self.contents))
        drawing_content.append(self.contents[random_index])
        del self.contents[random_index]
      return drawing_content

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  matches = 0
  for i in range(num_experiments):
    withdraw_balls = hat.draw(num_balls_drawn)
    match = all(withdraw_balls.count(key) >= value for key, value in expected_balls.items())
    if(match):
      matches += 1
  return matches / num_experiments
