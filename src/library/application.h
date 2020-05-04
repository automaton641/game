#pragma once

#define PLAYS 4
#define ATTRIBUTES 4

typedef struct application application_t;

application_t *application_create();

void application_run(application_t *application, long long compensator);

void application_destroy(application_t *application);

void application_print_winner(application_t *application);

void application_erase_memory();


#include <library/game.h>

struct application
{
    game_t *game;
};