from state import State


class Configuration:

    def __init__(self, startingSymbol):
        self.state = State.NORMAL
        self.index = 0
        self.workStack = []
        self.inputStack = [startingSymbol]
