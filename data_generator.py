import random

from faker import Faker


class DataGenerator:
    def __init__(self, num_rows=None, num_columns=10, min_value=0,
                 max_value=100):
        self.num_rows = num_rows
        self.num_columns = num_columns
        self.min_value = min_value
        self.max_value = max_value
        self.fake = Faker()

    def generate_data(self):
        if not self.num_rows:
            self.num_rows = random.randint(500000, 2000000)
        
        data = []
        for _ in range(self.num_rows):
            row = [self.fake.random_int(min=self.min_value, max=self.max_value)
                   for _ in range(self.num_columns)]
            data.append(row)
        
        return data