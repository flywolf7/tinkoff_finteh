from game.cell import Cell
import random
from copy import deepcopy


class Field:
    __height = 0
    __width = 0
    __game_field = []

    def __init__(self, height, width):
        assert height > 0 and width > 0
        self.__height = height
        self.__width = width
        self.__game_field = self.__get_default()
        return

    @property
    def game_field(self):
        return self.__game_field

    @property
    def height(self):
        return self.__height

    @property
    def width(self):
        return self.__width

    def next(self):
        new_list = self.__get_default()
        for i in range(0, self.height):
            for j in range(0, self.width):
                current = Cell(self.get_cell(i, j).alive)
                if current.alive:
                    new_list = self.__process_alive(i, j, new_list)
                else:
                    new_list = self.__process_dead(i, j, new_list)
        self.__game_field = new_list

    def get_neighbours(self, x, y):
        neighbours = []
        positions = [[-1, -1], [-1, 0], [-1, 1], [0, -1],
                     [0, 1], [1, -1], [1, 0], [1, 1]]
        for i in positions:
            if (0 <= i[0] + y < self.height) and (0 <= i[1] + x < self.width):
                neighbours.append(self.get_cell(x + i[1], y + i[0]))
        return neighbours

    def fill_random(self):
        self.__game_field = [[Cell(random.randint(0, 1))
                              for _ in range(self.height)]
                             for _ in range(self.width)]
        return

    def to_str(self):
        ret_str = ''
        for i in range(0, self.height):
            for j in range(0, self.width):
                ret_str += self.get_cell(i, j).to_str() + ' '
            ret_str += '\n'
        return ret_str

    def get_cell(self, x, y):
        assert 0 <= x <= self.width and 0 <= y <= self.height
        return self.game_field[y][x]

    def set_cell(self, x, y, query):
        assert 0 <= x <= self.width and 0 <= y <= self.height
        self.game_field[y][x] = query
        return

    def __process_alive(self, x, y, new_list):
        neighbours = self.get_neighbours(x, y)
        cnt = 0
        for cell in neighbours:
            if cell.alive:
                cnt += 1
        if cnt < 2 or cnt > 3:
            new_list[y][x] = self.get_cell(x, y).get_mutated()
        else:
            new_list[y][x] = self.get_cell(x, y)
        return new_list

    def __process_dead(self, x, y, new_list):
        neighbours = self.get_neighbours(x, y)
        cnt = 0
        for cell in neighbours:
            if Cell(cell).alive:
                cnt += 1
        if cnt == 3:
            new_list[y][x] = self.get_cell(x, y).get_mutated()
        else:
            new_list[y][x] = self.get_cell(x, y)
        return new_list

    def __get_default(self):
        new_field = [[Cell(False)
                      for _ in range(self.height)]
                     for _ in range(self.width)]
        return new_field
