import os
import random
import json
import matplotlib.pyplot as plt
import os.path
import sys


class Play:
    def __init__(self, name, index):
        self.name = name
        self.index = index

    def data(self):
        return {"name": self.name, "index": self.index}


class Limits:
    limit = 64


class Player:
    def __init__(self):
        self.max_health = 0.0
        self.health = 0.0
        self.energy = 0.0
        self.strength = 0.0
        self.intelligence = 0.0
        self.armor = 0.0
        self.resistance = 0.0
        self.courage = 0.0

    def reset(self):
        self.max_health = 4.0
        self.health = 4.0
        self.energy = 4.0
        self.strength = 4.0
        self.intelligence = 4.0
        self.armor = 4.0
        self.resistance = 4.0
        self.courage = 4.0

    def copy(self, other):
        self.max_health = other.max_health
        self.health = other.health
        self.energy = other.energy
        self.strength = other.strength
        self.intelligence = other.intelligence
        self.armor = other.armor
        self.resistance = other.resistance
        self.courage = other.courage

    def health_inc(self, value):
        balance = self.health + value
        if balance >= Limits.limit:
            self.health = Limits.limit
        else:
            self.health = balance

    def resistance_inc(self, value):
        balance = self.resistance + value
        if balance >= Limits.limit:
            self.resistance = Limits.limit
        else:
            self.resistance = balance

    def courage_inc(self, value):
        balance = self.courage + value
        if balance >= Limits.limit:
            self.courage = Limits.limit
        else:
            self.courage = balance

    def armor_inc(self, value):
        balance = self.armor + value
        if balance >= Limits.limit:
            self.armor = Limits.limit
        else:
            self.armor = balance

    def intelligence_inc(self, value):
        balance = self.intelligence + value
        if balance >= Limits.limit:
            self.intelligence = Limits.limit
        else:
            self.intelligence = balance

    def strength_inc(self, value):
        balance = self.strength + value
        if balance >= Limits.limit:
            self.strength = Limits.limit
        else:
            self.strength = balance

    def energy_inc(self, value):
        balance = self.energy + value
        if balance >= Limits.limit:
            self.energy = Limits.limit
        else:
            self.energy = balance

    def max_health_inc(self, value):
        balance = self.max_health + value
        if balance >= Limits.limit:
            self.max_health = Limits.limit
        else:
            self.max_health = balance

    def data(self):
        return {"max_health": self.max_health, "health": self.health, "energy": self.energy, "strength": self.strength,
                "intelligence": self.intelligence, "armor": self.armor, "resistance": self.resistance,
                "courage": self.courage}

    def take_damage(self, damage):
        if damage >= self.health:
            self.health = 0.0
            return False
        self.health -= damage
        return True

    def tick(self):
        if self.health + 1.0 > self.max_health:
            self.health = self.max_health
        else:
            self.health_inc(1.0)


class PlayType:
    attack = 0
    defend = 1
    think = 2
    breathe = 3
    pray = 4
    eat = 5
    forge = 6
    count = 7


class Attributes:
    list = ["max_health", "health", "energy", "strength", "intelligence", "armor", "resistance", "courage"]
    max_health = 0
    health = 1
    energy = 2
    strength = 3
    intelligence = 4
    armor = 5
    resistance = 6
    courage = 7
    count = 8


class Labels:
    list = ["my_max_health", "enemy_max_health", "my_health", "enemy_health", "my_energy", "enemy_energy",
            "my_strength", "enemy_strength", "my_intelligence", "enemy_intelligence", "my_armor", "enemy_armor",
            "my_resistance", "enemy_resistance", "my_courage", "enemy_courage", "turn"]


class Plays:
    list = ["attack", "defend", "forge", "think", "breathe", "pray", "eat"]


def load_data(file_name):
    if os.path.isfile(file_name):
        is_empty = os.stat(file_name).st_size == 0
        if is_empty:
            return []
        f = open(file_name, "r")
        result = json.load(f)
        f.close()
        return result
    return []


def get_blocks(data):
    blocks = []
    for game in data:
        for game_element in game["game_elements"]:
            block_a = {}
            block_b = {}
            for i in range(Attributes.count):
                block_a["my_" + Attributes.list[i]] = game_element["attributes"]["a"][Attributes.list[i]]
                block_a["enemy_" + Attributes.list[i]] = game_element["attributes"]["b"][Attributes.list[i]]
                block_b["my_" + Attributes.list[i]] = game_element["attributes"]["b"][Attributes.list[i]]
                block_b["enemy_" + Attributes.list[i]] = game_element["attributes"]["a"][Attributes.list[i]]
            if game["winner"] == "a":
                block_a["winner"] = 1
                block_b["winner"] = -1
            elif game["winner"] == "b":
                block_a["winner"] = -1
                block_b["winner"] = 1
            else:
                block_a["winner"] = 0
                block_b["winner"] = 0
            block_a["my_play"] = game_element["plays"]["a"]
            block_b["my_play"] = game_element["plays"]["b"]
            block_a["turn"] = game_element["turn"]
            block_b["turn"] = game_element["turn"]
            blocks.append(block_a)
            blocks.append(block_b)
    return blocks


def distance(a, b):
    c = a - b
    if c < 0:
        return (-1.0) * c
    return c


class PlayerController:
    def __init__(self, me: Player, rival: Player, use_memory):
        self.me = me
        self.rival = rival
        if use_memory:
            self.memory_data = load_data("data.json")
            self.memory_blocks = get_blocks(self.memory_data)
        else:
            self.memory_data = []
            self.memory_blocks = []
        self.turn = 0
        self.use_memory = use_memory
        self.weighs = {}
        for label in Labels.list:
            self.weighs[label] = random.uniform(0.0, 1.0)

    def get_label(self, label):
        if label == "turn":
            return self.turn
        if label == "my_" + "health":
            return self.me.health
        if label == "my_" + "max_health":
            return self.me.max_health
        if label == "my_" + "energy":
            return self.me.energy
        if label == "my_" + "courage":
            return self.me.courage
        if label == "my_" + "intelligence":
            return self.me.intelligence
        if label == "my_" + "resistance":
            return self.me.resistance
        if label == "my_" + "armor":
            return self.me.armor
        if label == "my_" + "strength":
            return self.me.strength
        if label == "enemy_" + "health":
            return self.rival.health
        if label == "enemy_" + "max_health":
            return self.rival.max_health
        if label == "enemy_" + "energy":
            return self.rival.energy
        if label == "enemy_" + "courage":
            return self.rival.courage
        if label == "enemy_" + "intelligence":
            return self.rival.intelligence
        if label == "enemy_" + "resistance":
            return self.rival.resistance
        if label == "enemy_" + "armor":
            return self.rival.armor
        if label == "enemy_" + "strength":
            return self.rival.strength

    def decide(self):
        if len(self.memory_blocks) > 0 and self.use_memory:
            pre = {}
            odds = {}
            for play in Plays.list:
                odds[play] = 0.0
                pre[play] = {}
                for label in Labels.list:
                    pre[play][label] = 0.0
            for memory_block in self.memory_blocks:
                for label in Labels.list:
                    my_label = self.get_label(label)
                    pre[memory_block["my_play"]][label] += memory_block["winner"] / (
                            1 + distance(memory_block[label], my_label))
            for play in Plays.list:
                for label in Labels.list:
                    odds[play] += pre[play][label]
            best_play = Plays.list[0]
            best_odd = odds[best_play]
            for play in Plays.list:
                if best_odd < odds[play]:
                    best_odd = odds[play]
                    best_play = play
            # print("best_odd: " + str(best_odd))
            return best_play
        else:
            return Plays.list[random.randrange(0, len(Plays.list))]


class State:
    def __init__(self, player_a: Player, player_b: Player):
        self.player_a = Player()
        self.player_a.copy(player_a)
        self.player_b = Player()
        self.player_b.copy(player_b)

    def data(self):
        return {"a": self.player_a.data(), "b": self.player_b.data()}


class GameLog:
    def __init__(self):
        self.plays = []
        self.turns = []
        self.states = []

    def get_data(self, player_a, player_b, turns, winner):
        full_game_data = {"winner": winner, "turns": turns,
                          "final_attributes": {"a": player_a.data(), "b": player_b.data()}, "game_elements": []}
        for index in range(len(self.turns)):
            item = {"attributes": self.states[index].data(), "plays": self.plays[index].data(),
                    "turn": self.turns[index]}
            full_game_data["game_elements"].append(item)
        self.plays = []
        self.turns = []
        self.states = []
        return full_game_data


def append_to_file(file_name, data_to_save):
    if os.path.isfile(file_name):
        is_empty = os.stat(file_name).st_size == 0
        if is_empty:
            f = open(file_name, "w")
            json.dump(data_to_save, f, indent=4)
            f.close()
        else:
            f = open(file_name, "r")
            data = json.load(f)
            for game in data_to_save:
                data.append(game)
            f.close()
            f = open(file_name, "w")
            json.dump(data, f, indent=4)
            f.close()
    else:
        f = open(file_name, "w")
        json.dump(data_to_save, f, indent=4)
        f.close()


def write_to_file(file_name, data_to_save):
    if os.path.exists(file_name):
        os.remove(file_name)
    f = open(file_name, "w")
    json.dump(data_to_save, f, indent=4)
    f.close()



def apply_play(player_1: Player, player_2: Player, chosen_play: Play):
    if chosen_play == "attack":
        balance = player_1.courage / player_2.courage
        if player_1.energy > 0.0:
            balance *= player_1.strength
        balance -= player_2.armor
        balance *= 1/(player_2.intelligence/player_1.resistance + 1)
        if balance >= 0.0:
            return player_2.take_damage(balance-player_2.resistance)
    elif chosen_play == "defend":
        player_1.health_inc(0.5)
        player_1.resistance_inc(0.5)
    elif chosen_play == "eat":
        player_1.health_inc(0.5)
        player_1.max_health_inc(0.5)
    elif chosen_play == "forge":
        player_1.strength_inc(0.5)
        player_1.armor_inc(0.5)
    elif chosen_play == "breathe":
        player_1.energy_inc(1.0)
    elif chosen_play == "pray":
        player_1.strength_inc(0.5)
        player_1.courage_inc(0.5)
    elif chosen_play == "think":
        player_1.intelligence_inc(1.0)
    return True


class PlayState:
    def __init__(self, play_a, play_b):
        self.play_a = play_a
        self.play_b = play_b

    def data(self):
        return {"a": self.play_a, "b": self.play_b}


def choose_play(controller):
    return controller.decide()


class Client:
    def __init__(self, use_memory, use_memory_b):
        self.turn = 0
        self.player_a = Player()
        self.player_b = Player()
        self.game_log = GameLog()
        self.controller_a = PlayerController(self.player_a, self.player_b, use_memory)
        self.controller_b = PlayerController(self.player_b, self.player_a, use_memory_b)
        self.plays = []
        self.plays_count = 0
        self.plays.append(Play("attack", self.plays_count))
        self.plays_count += 1
        self.plays.append(Play("defend", self.plays_count))
        self.plays_count += 1
        self.plays.append(Play("think", self.plays_count))
        self.plays_count += 1
        self.plays.append(Play("breathe", self.plays_count))
        self.plays_count += 1
        self.plays.append(Play("pray", self.plays_count))
        self.plays_count += 1
        self.plays.append(Play("eat", self.plays_count))
        self.plays_count += 1
        self.plays.append(Play("forge", self.plays_count))
        self.plays_count += 1

    def print_player_attributes(self, player: Player, label):
        print(label, "health", player.health)
        print(label, "max_health", player.max_health)
        print(label, "strength", player.strength)
        print(label, "energy", player.energy)
        print(label, "armor", player.armor)
        print(label, "resistance", player.resistance)
        print(label, "intelligence", player.intelligence)
        print(label, "courage", player.courage)

    def play_turn(self):
        self.controller_b.turn = self.turn
        chosen_play_a = choose_play(self.controller_a)
        print("A PLAY", chosen_play_a)
        chosen_play_b = choose_play(self.controller_b)
        print("B PLAY", chosen_play_b)
        self.game_log.turns.append(self.turn)
        self.game_log.plays.append(PlayState(chosen_play_a, chosen_play_b))
        self.game_log.states.append(State(self.player_a, self.player_b))
        if chosen_play_a == "attack":
            b = apply_play(self.player_b, self.player_a, chosen_play_b)
            a = apply_play(self.player_a, self.player_b, chosen_play_a)
        else:
            a = apply_play(self.player_a, self.player_b, chosen_play_a)
            b = apply_play(self.player_b, self.player_a, chosen_play_b)
        return a and b

    def get_winner(self):
        distance_a = distance(self.player_a.health, 0.0)
        distance_b = distance(self.player_b.health, 0.0)
        if distance_a < 0.01:
            if distance_b < 0.01:
                return "d"
            return "b"
        if distance_b < 0.01:
            return "a"
        return "d"

    def play(self, iteration):
        self.player_a.reset()
        self.player_b.reset()
        self.turn = 0
        playing: bool = True
        print("iteration", iteration)
        while playing:
            print("AAAAAAAAAAAAAAAAAAAAAA")
            self.print_player_attributes(self.player_a, "A")
            print("BBBBBBBBBBBBBBBBBBBBB")
            self.print_player_attributes(self.player_b, "B")
            playing = self.play_turn()
            self.turn += 1
            print(iteration + 1, "turn", self.turn)
        return [self.game_log.get_data(self.player_a, self.player_b, self.turn, self.get_winner())]


def play(n):

    client = Client(True, False)
    whole_data = load_data("data.json")
    for i in range(n):
        data = client.play(i)
        for game in data:
            whole_data.append(game)
        client.controller_a.memory_blocks = get_blocks(whole_data)
    write_to_file("data.json", whole_data)
    a_wins = 0
    b_wins = 0
    draws = 0
    average_game_duration = 0
    for game in whole_data:
        average_game_duration += game["turns"]
        if game["winner"] == "a":
            a_wins += 1
        elif game["winner"] == "b":
            b_wins += 1
        else:
            draws += 1
    average_game_duration /= len(whole_data)
    print("------------------------")
    print(whole_data[-1]["winner"], "winner")
    print("a_wins", a_wins)
    print("b_wins", b_wins)
    print("winrate", a_wins/(a_wins+b_wins))
    print("draws", draws)
    print("games", a_wins+b_wins+draws)
    print("average_game_duration", average_game_duration)
    write_to_file("last.json", whole_data[-1])

def write_memory():
    memory_data = load_data("data.json")
    memory_blocks = get_blocks(memory_data)
    write_to_file("memory.json", memory_blocks)


def delete_blocks(n):
    data = load_data("data.json")
    new_data = []
    i = 0
    for game in data:
        if i > n-1:
            new_data.append(data[i])
        i+=1
    write_to_file("data.json", new_data)

def graph_plays_count(file_name):
    data = load_data(file_name)
    values = []
    val_dictionary = {}
    names = Plays.list
    for play in names:
        val_dictionary[play] = 0
    for game in data:
        for game_element in game["game_elements"]:
            for play in names:
                val_dictionary[game_element["plays"]["a"]] += 1
    for play in names:
        values.append(val_dictionary[play])
    plt.bar(names, values)
    plt.show()

def iteration():
    iterate = True
    while iterate:
        play(1)
        delete_blocks(1)
        if not load_data("iterate.json"):
            iterate = False

iteration()

graph_plays_count("data.json")
