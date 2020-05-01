import json
import os
import random


class Assignation:
    def __init__(self, x, state, index):
        self.state = state
        self.index = index
        self.x = x

    def execute(self):
        self.state[self.index] = self.x

    def __str__(self):
        return "Assignation "


class Instruction:
    def __init__(self, x, state, negate, code_blocks):
        self.x = x
        self.negate = negate
        self.state = state
        self.code_blocks = code_blocks

    def execute(self):
        if self.negate:
            if not self.x:
                for code_block in self.code_blocks:
                    code_block.execute()
        else:
            if self.x:
                for code_block in self.code_blocks:
                    code_block.execute()

    def __str__(self):
        rep = "Instruction: ["
        for block in self.code_blocks:
            rep += str(block)
        rep += "] "
        return rep


def generate_code_block(state, max_list_size, depth, max_depth):
    is_assignation = bool(random.getrandbits(1))
    if is_assignation or depth == max_depth:
        is_constant = bool(random.getrandbits(1))
        if is_constant:
            x = bool(random.getrandbits(1))
        else:
            x = state[random.randrange(len(state))]
        index = random.randrange(len(state))
        return Assignation(x, state, index)
    else:
        x = state[random.randrange(len(state))]
        negate = bool(random.getrandbits(1))
        instruction_list = []
        for i in range(max_list_size):
            instruction_list.append(generate_code_block(state, max_list_size - 1, depth + 1, max_depth))
        return Instruction(x, state, negate, instruction_list)


class Game:
    def __init__(self):
        self.state = []
        self.rule = []
        self.state_size = 8
        self.rule_size = 12
        self.depth = 4
        self.random_state()
        self.random_rule()

    def random_state(self):
        for i in range(self.state_size):
            self.state.append(bool(random.getrandbits(1)))

    def random_rule(self):
        for i in range(self.rule_size):
            self.rule.append(generate_code_block(self.state, self.rule_size - 1, 0, self.depth))

    def play(self):
        for code_block in self.rule:
            code_block.execute()

    def print_rule(self):
        for code_block in self.rule:
            print(code_block)


game = Game()
print(game.state)
game.play()
print(game.state)

game.print_rule()
