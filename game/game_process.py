from game.field import Field
from game.cell import Cell
from game import my_util
from typing import Final
import random

WELCOME_STR: Final = 'Начало работы программы\nВведите размеры поля'


class GameProcessor:
    fld = None

    def start(self):
        print(WELCOME_STR)
        self.__input_params()
        nsteps = self.__input_steps()
        for i in range(0, int(nsteps)):
            print(self.fld.to_str())
            self.fld.next()

    def __input_params(self):
        x = self.__input_x('ширин')
        y = self.__input_x('длин')
        self.fld = Field(int(x), int(y))
        self.fld.fill_random()

    def __input_steps(self):
        self.__welcome_x('количество шагов')
        input_str = input()
        if my_util.is_int(input_str) and int(input_str) > 0:
            return int(input_str)
        else:
            self.__error_x('количества шагов')
            self.__input_steps()

    def __input_x(self, x):
        self.__welcome_x(x + 'у')
        input_str = input()
        if my_util.is_int(input_str) and int(input_str) > 0:
            return int(input_str)
        else:
            self.__error_x(x + 'ы')
            self.__input_x(x)

    def __welcome_x(self, x):
        print('Введите ' + x + ': ')

    def __error_x(self, x):
        print('Произошла ошибка при вводе ' + x + ' должно быть положительным числом')
