from abc import abstractmethod, ABC


class AbstractCell(ABC):
    __alive = False

    @abstractmethod
    def get_mutated(self):
        pass

    @abstractmethod
    def to_str(self):
        pass

    @property
    def alive(self):
        return self.__alive

    def set_alive(self, alive):
        self.__alive = alive


class Cell(AbstractCell):
    def __init__(self, is_al):
        self.set_alive(is_al)

    def get_mutated(self):
        if self.alive:
            return Cell(False)
        else:
            return Cell(True)

    def to_str(self):
        if self.alive:
            return '*'
        else:
            return '.'
