#include <library/game.h>
#include <stdlib.h>
#include <stdio.h>
#include <library/math.h>
#include <library/application.h>
#include <library/memory_block.h>
#include <errno.h>

int attributes_limit = 1024;

game_t *game_create(long long compensator) 
{
    game_t *game = malloc(sizeof(game_t));
    game->memory = array_create(sizeof(memory_block_t));
    game->turn = 0;
    game->winner = -1;
    game->play_a = 0;
    game->play_b = 0;
    game->player_a = player_create(0, true);
    game->player_b = player_create(1, true);
    game->player_a->enemy = game->player_b;
    game->player_b->enemy = game->player_a;
    for (size_t i = 0; i < ATTRIBUTES; i++)
    {
        game->attributes_a[i] = &game->player_a->attributes[i];
        game->attributes_b[i] = &game->player_b->attributes[i];
    }
    return game;
}

void game_destroy(game_t *game) 
{
    array_destroy(game->memory);
    player_destroy(game->player_a);
    player_destroy(game->player_b);
    free(game);
}

void game_print_players_attributes(game_t *game)
{
    player_print_attributes(game->player_a);
    player_print_attributes(game->player_b);
}

void game_save_memory(game_t *game)
{
    FILE *file = fopen("memory.bin","a");
    if (file == NULL)
    {
        printf("%s\n", "ERROR: FILE IS NULL");
        perror("fopen: Could not open file");
        fclose(file);
        exit(EXIT_FAILURE);
    }
    fwrite(game->memory->data, game->memory->element_size, game->memory->size, file);
    fclose(file);
}

void game_print_players_memory(game_t *game)
{
    player_print_memory(game->player_a);
    player_print_memory(game->player_b);
}

bool game_play(game_t *game) {
    memory_block_t memory_block;
    memory_block.turn = game->turn;
    memory_block.winner = game->winner;
    for (size_t i = 0; i < ATTRIBUTES; i++)
    {
        memory_block.attributes_a[i] = game->player_a->attributes[i];
        memory_block.attributes_b[i] = game->player_b->attributes[i];
    }
    if (game->turn % 2 == 0)
    {
        game->play_a = player_play(game->player_a);
        //printf("%s: %i\n", "play_a", game->play_a);
        memory_block.play = game->play_a;
        game_apply_play(game->play_a, game->attributes_a, game->attributes_b);
    }
    else
    {
        game->play_b = player_play(game->player_b);
        //printf("%s: %i\n", "play_b", game->play_b);
        memory_block.play = game->play_b;
        game_apply_play(game->play_b, game->attributes_b, game->attributes_a);
    }
    array_add(game->memory, &memory_block);
    game->turn++;
    //game_print_players_attributes(game);
    game_check_winner(game);
    if (game->winner > -1)
    {
        for (size_t i = 0; i < game->turn; i++)
        {
            memory_block_t *mem_block = array_get(game->memory, i);
            mem_block->winner = game->winner;
        }
        return true;
    }
    return false;
}

void game_fight_draw(game_t *game) 
{
    long long life_a = *game->attributes_a[0];
    long long life_b = *game->attributes_b[0];
    if (life_a == life_b)
    {
        long sum_a = 0;
        long sum_b = 0;
        for (size_t i = 1; i < ATTRIBUTES; i++)
        {
            sum_a += *game->attributes_a[i];
            sum_b += *game->attributes_b[i];
        }
        if (sum_a == sum_b)
        {
            game->winner = 2;
            return;
        }
        else
        {
            if (sum_a > sum_b)
            {
                game->winner = 0;
                return;
            }
            else
            {
                game->winner = 1;
                return;
            }
        }
    }
    else
    {
        if (life_a > life_b)
        {
            game->winner = 0;
            return;
        }
        else
        {
            game->winner = 1;
            return;
        }
    }
}

void game_check_winner(game_t *game)
{
    long long life_a = *game->attributes_a[0];
    long long life_b = *game->attributes_b[0];
    if (life_a <= 0)
    {
        if (life_b <= 0)
        {
            game_fight_draw(game);
            return;
        }
        else
        {
            game->winner = 1;
            return;
        }
    }
    else if (life_b <= 0)
    {
        game->winner = 0;
        return;
    }
    else if (game->turn >= 16)
    {
        game_fight_draw(game);
        return;
    }
}

void change_attribute(long long *attribute, long long offset)
{
    *attribute += offset;
    if (*attribute > attributes_limit)
    {
        *attribute = attributes_limit;
    }
    else if (*attribute < 0)
    {
        *attribute = 0;
    }
}

void game_apply_play(int play, long long* source[4], long long* target[4]) 
{
    long long d;
    long long a;
    switch (play)
    {
    case 0:
        d = 64*distance(*source[0], *target[0]);
        change_attribute(source[0], d + 256);
        change_attribute(target[2], -32);
        //change_attribute(source[3], 1);
        change_attribute(target[3], -32);
        break;
    case 1:
        //change_attribute(source[1], 1*distance(*target[2], *target[3]));
        //change_attribute(source[2], 1);
        change_attribute(source[3], 32+4);
        change_attribute(source[2], 16);
        break;
    case 2:
        change_attribute(source[1], 8);
        change_attribute(source[2], 32);
        change_attribute(target[1], -8);
        //change_attribute(target[2], -1);
        //change_attribute(target[3], -1);
        break;
    case 3:
        a = (*source[3] * 24 + (*source[2]) * 24) * 32-(*target[1]* 12 + (*target[2]* 12)) * 16;
        change_attribute(target[0], -a*(64+32));  
        break;
    
    default:
        printf("ERROR: unknown play\n");
        exit(EXIT_FAILURE);
    }
}


    

