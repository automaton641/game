#pragma once

#include <stdbool.h>

typedef struct game game_t;

game_t *game_create(long long compensator);

void game_destroy(game_t *game);

bool game_play(game_t *game);

void game_apply_play(int play, long long* source[4], long long* target[4]);

void game_apply_plays(game_t *game);

void game_check_winner(game_t *game);

void game_print_players_attributes(game_t *game);

void game_save_memory(game_t *game);

void game_print_players_memory(game_t *game);

#include <library/player.h>
#include <library/array.h>

struct game
{
    array_t *memory;
    int turn;
    int winner;
    player_t *player_a;
    player_t *player_b;
    int play_a;
    int play_b;
    long long* attributes_a[4];
    long long* attributes_b[4];
};