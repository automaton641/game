#pragma once
#include <stdbool.h>

typedef struct player player_t;

player_t *player_create(int number, bool use_memory);
void player_destroy(player_t *player);
int player_play(player_t *player);
int player_play_from_memory(player_t *player);
void player_load_memory(player_t *player);
void player_print_attributes(player_t *player);
void player_print_memory(player_t *player);

#include <library/array.h>

struct player
{
    player_t *enemy;
    bool use_memory;
    bool memory_is_empty;
    array_t *memory;
    int number;
    long long attributes[4];
};
//cb3f7807ffff01fe