#pragma once
#include <stdbool.h>

typedef struct memory_block memory_block_t;

struct memory_block
{
    int play;
    int turn;
    int winner;
    long long attributes_a[4];
    long long attributes_b[4];
};

bool print_winrate(long long *compensator_a, long long *compensator_b);