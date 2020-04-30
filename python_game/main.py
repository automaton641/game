import os
import random
import json
import sys
import matplotlib.pyplot as plt


class Play:
    def __init__(self, name, plays_count):
        self.name = name
        self.index = plays_count

    def data(self):
        data = {"name": self.name, "index": self.index}
        return data


class Player:
    def __init__(self):
        self.max_health = 64.0
        self.health = 32.0
        self.energy = 4.0
        self.strength = 4.0
        self.intelligence = 8.0
        self.armor = 4.0
        self.resistance = 4.0
        self.courage = 4.0
        # self.discipline = 4.0

    def copy(self, other):
        self.max_health = other.max_health
        self.health = other.health
        self.energy = other.energy
        self.strength = other.strength
        self.intelligence = other.intelligence
        self.armor = other.armor
        self.resistance = other.resistance
        self.courage = other.courage

    def data(self):
        data = {"max_health": self.max_health, "health": self.health, "energy": self.energy, "strength": self.strength,
                "intelligence": self.intelligence, "armor": self.armor, "resistance": self.resistance,
                "courage": self.courage}
        return data

    def take_damage(self, damage):
        if damage >= self.health:
            self.health = 0
            return False
        self.health -= damage
        return True

    def tick(self):
        if self.health + 1 > self.max_health:
            self.health = self.max_health
        else:
            self.health += 1


class PlayType:
    attack = 0
    defend = 1
    think = 2
    breathe = 3
    pray = 4
    eat = 5
    forge = 6
    count = 7


def decide():
    return random.randrange(0, PlayType.count)


def load_data():
    is_empty = os.stat("data.json").st_size == 0
    if is_empty:
        return []
    with open('data.json') as json_file:
        data = json.load(json_file)
        return data


class PlayerController:
    def __init__(self, me: Player, rival: Player):
        self.me: me
        self.rival = rival
        self.memory = load_data()
        print_line("memory")
        # print(json.dumps(self.memory, indent=4))


def print_line(line):
    return
    print("<line> " + line + " </line>")


def skip_line():
    return
    print("")


def get_line():
    return input("<input> ")


def print_player_attributes(player: Player):
    print_line("health: " + str(player.health))
    print_line("max_health: " + str(player.max_health))
    print_line("strength: " + str(player.strength))
    print_line("armor: " + str(player.armor))
    print_line("resistance: " + str(player.resistance))
    print_line("intelligence: " + str(player.intelligence))
    print_line("energy: " + str(player.energy))
    print_line("courage: " + str(player.courage))


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
        self.data = []
        self.winner = 0

    def get_data(self):
        for index in range(len(self.turns)):
            item = {"attributes": self.states[index].data(), "plays": self.plays[index].data(),
                    "turn": self.turns[index],
                    "winner": self.winner}
            self.data.append(item)


def append_to_file(data_to_save):
    is_empty = os.stat("data.json").st_size == 0
    with open("data.json", "r+") as file:
        if is_empty:
            json.dump(data_to_save, file, indent=4)
        else:
            data = json.load(file)
            for block in data_to_save:
                data.append(block)
            file.seek(0)
            json.dump(data, file, indent=4)


def apply_play(player_1: Player, player_2: Player, chosen_play: Play):
    print_line("apply_play: " + chosen_play.name)
    print_line("chosen_play.index: " + str(chosen_play.index))
    if chosen_play.index == PlayType.attack:
        print_line("attacking...")
        balance = player_1.courage / player_2.courage
        if player_1.energy > 0.0:
            balance *= player_1.strength
        balance -= player_2.resistance + player_2.armor
        if balance >= 0.0:
            return player_2.take_damage(balance - player_2.intelligence)
        else:
            return player_1.take_damage((-1) * balance + player_2.intelligence)
    elif chosen_play.index == PlayType.defend:
        print_line("defending...")
        player_1.health += 1.0
        player_1.resistance += 1.0
    elif chosen_play.index == PlayType.eat:
        print_line("eating...")
        player_1.health += 1.0
        player_1.max_health += 1.0
    elif chosen_play.index == PlayType.forge:
        print_line("forging...")
        player_1.strength += 1.0
        player_1.armor += 1.0
    elif chosen_play.index == PlayType.breathe:
        print_line("breathing...")
        player_1.health += 1.0
        player_1.resistance += 1.0
    elif chosen_play.index == PlayType.pray:
        print_line("praying...")
        player_1.strength += 1.0 / 2.0
        player_1.courage += 1.0
    elif chosen_play.index == PlayType.think:
        print_line("thinking...")
        player_1.intelligence += 1.0
    return True


class PlayState:
    def __init__(self, play_a: Play, play_b: Play):
        self.play_a = play_a
        self.play_b = play_b

    def data(self):
        data = {"a": self.play_a.data(), "b": self.play_b.data()}
        return data

    pass


class Client:
    def __init__(self):
        self.game_log = GameLog()
        self.player_a = Player()
        self.player_b = Player()
        self.controller_a = PlayerController(self.player_a, self.player_b)
        self.controller_b = PlayerController(self.player_b, self.player_a)
        self.current_controller = self.controller_a
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
        self.turn = 0

    def choose_play(self):
        return self.plays[decide()]

    def play_turn(self):
        self.player_a.tick()
        self.player_b.tick()
        self.current_controller = self.controller_a
        chosen_play_a: Play = self.choose_play()
        self.current_controller = self.controller_b
        chosen_play_b: Play = self.choose_play()
        self.game_log.turns.append(self.turn)
        self.game_log.plays.append(PlayState(chosen_play_a, chosen_play_b))
        self.game_log.states.append(State(self.player_a, self.player_b))
        if chosen_play_a.index == PlayType.attack:
            b = apply_play(self.player_b, self.player_a, chosen_play_b)
            a = apply_play(self.player_a, self.player_b, chosen_play_a)
        else:
            a = apply_play(self.player_a, self.player_b, chosen_play_a)
            b = apply_play(self.player_b, self.player_a, chosen_play_b)
        return a and b

    def get_winner(self):
        if self.player_a.health == 0:
            if self.player_b.health == 0:
                return "e"
            return "b"
        elif self.player_b.health == 0:
            return "a"

    def play(self, save_game_log: bool):
        self.turn = 0
        playing: bool = True
        while playing:
            print_line(
                "==========================================================================================================================================")
            playing = self.play_turn()
            self.turn += 1
        self.game_log.winner = self.get_winner()
        self.game_log.get_data()


if True:
    client = Client()
    for i in range(256):
        client.play(True)
    my_data = client.game_log.data


def process_data(input_data):
    result = {"player_a_health": [], "player_b_health": [], "winner": []}
    for data_block in input_data:
        result["player_a_health"].append(data_block["attributes"]["a"]["health"])
        result["player_b_health"].append(data_block["attributes"]["b"]["health"])
        result["winner"].append(data_block["winner"])
    return result


data = my_data
processed_data = process_data(data)
# convert into JSON:
processed_data_json = json.dumps(processed_data, indent=4)
print(processed_data_json)
wins_a = 0
wins_b = 0
draws = 0
for winner in processed_data["winner"]:
    if winner == "a":
        wins_a += 1
    elif winner == "b":
        wins_b += 1
    else:
        draws += 1
print("wins_a: " + str(wins_a))
print("wins_b: " + str(wins_b))
print("draws: " + str(draws))
if False:
    plt.plot(processed_data["player_a_health"], "ro", processed_data["player_b_health"], "bo")
    plt.xlabel('player_a_health')
    plt.ylabel('turn')
    plt.show()

names = ['wins_a', 'wins_b', 'draws']
plt.bar(names, [wins_a, wins_b, draws])
plt.xlabel('results')
plt.ylabel('count')
plt.show()
# print(processed_data)
