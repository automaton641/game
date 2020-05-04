#include <library/player.h>
#include <library/application.h>
#include <stdlib.h>
#include <stdio.h>
#include <library/memory_block.h>
#include <library/math.h>

player_t *player_create(int number, bool use_memory) 
{
    player_t *player = malloc(sizeof(player_t));
    player->memory_is_empty = true;
    player->number = number;
    player->use_memory = use_memory;
    if (number == 0)
    {
        player->attributes[0] = 32;
        player->attributes[1] = 32;
        player->attributes[2] = 0;
        player->attributes[3] = 0;
    }
    else
    {
        long long compensator = 16;
        player->attributes[0] = 32 + compensator;
        player->attributes[1] = 32;
        player->attributes[2] = 0;
        player->attributes[3] = 0;
    }
    player_load_memory(player);
    return player;
}

void player_print_memory(player_t *player)
{
    
    printf("player no: %i, memory\n", player->number);
    if (player->memory_is_empty)
    {
        printf("empty memory\n");
        return;
    }
    memory_block_t *memory_block;
    for (size_t i = 0; i < player->memory->size; i++)
    {
        memory_block = array_get(player->memory, i);
        printf("%s: %zu\n", "memory block no", i);
        printf("%s: %i\n", "", memory_block->winner);
        printf("%s: %i\n", "", memory_block->turn);
        printf("%s: %i\n", "", memory_block->play);
        printf("%s", "attributes a\n");
        for (size_t j = 0; j < ATTRIBUTES; j++)
        {
            printf("%s: %lli\n", "", memory_block->attributes_a[j]);
        }
        printf("%s", "attributes b\n");
        for (size_t j = 0; j < ATTRIBUTES; j++)
        {
            printf("%s: %lli\n", "", memory_block->attributes_b[j]);
        }
    }
    
}

void player_load_memory(player_t *player)
{
    FILE *file = fopen("memory.bin", "r");
    if (file == NULL)
    {
        player->memory_is_empty = true;
        printf("%s\n", "memory is empty");
        return;
    }
    player->memory_is_empty = false;
    player->memory = array_create(sizeof(memory_block_t));
    memory_block_t *memory_block = malloc(sizeof(memory_block_t));
    while (true)
    {
        fread(memory_block, sizeof(memory_block_t), 1, file);
        if (ferror(file))
        {
            free(memory_block);
            fclose(file);
            printf("%s\n", "ERROR LOADING MEMORY");
            exit(EXIT_FAILURE);
        }
        if (feof(file))
        {
            free(memory_block);
            fclose(file);
            return;
        }
        array_add(player->memory, memory_block);
    }
}

void player_destroy(player_t *player)
{
    if (!player->memory_is_empty) 
    {
        array_destroy(player->memory);
    }
    free(player);
}

/*
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
*/

int player_play_from_memory(player_t *player)
{
    long long weights[PLAYS];
    for (size_t i = 0; i < PLAYS; i++)
    {
        weights[i] = 0;
    }
    
    memory_block_t *memory_block;
    long long w;
    for (size_t i = 0; i < player->memory->size; i++)
    {
        memory_block = array_get(player->memory, i);
        if (player->number == 0)
        {
            if (memory_block->turn % 2 == player->number)
            {
                if (memory_block->winner == 0) 
                {
                    w = 4;
                }
                else if (memory_block->winner == 1)
                {
                    w = -4;
                }
                else
                {
                    w = -1;
                }
                for (size_t j = 0; j < ATTRIBUTES; j++)
                {
                    weights[memory_block->play] += w*256/(distance(memory_block->attributes_a[j], player->attributes[j])+64);
                    weights[memory_block->play] += w*256/(distance(memory_block->attributes_b[j], player->enemy->attributes[j])+64);
                }
            }
            /*
            else
            {
                if (memory_block->winner == 0) 
                {
                    w = -4;
                }
                else if (memory_block->winner == 1)
                {
                    w = 4;
                }
                else
                {
                    w = -1;
                }
                for (size_t j = 0; j < ATTRIBUTES; j++)
                {
                    weights[memory_block->play] += w*256/(distance(memory_block->attributes_b[j], player->attributes[j])+64);
                    weights[memory_block->play] += w*256/(distance(memory_block->attributes_a[j], player->enemy->attributes[j])+64);
                }
            }
            */
            
        }
        else if (player->number == 1)
        {
            if (memory_block->turn % 2 == player->number)
            {
                if (memory_block->winner == 0) 
                {
                    w = -4;
                }
                else if (memory_block->winner == 1)
                {
                    w = 4;
                }
                else
                {
                    w = -1;
                }
                for (size_t j = 0; j < ATTRIBUTES; j++)
                {
                    weights[memory_block->play] += w*256/(distance(memory_block->attributes_b[j], player->attributes[j])+64);
                    weights[memory_block->play] += w*256/(distance(memory_block->attributes_a[j], player->enemy->attributes[j])+64);
                }
            }
            /*
            else
            {
                if (memory_block->winner == 0) 
                {
                    w = 4;
                }
                else if (memory_block->winner == 1)
                {
                    w = -4;
                }
                else
                {
                    w = -1;
                }
                for (size_t j = 0; j < ATTRIBUTES; j++)
                {
                    weights[memory_block->play] += w*256/(distance(memory_block->attributes_a[j], player->attributes[j])+64);
                    weights[memory_block->play] += w*256/(distance(memory_block->attributes_b[j], player->enemy->attributes[j])+64);
                }
            }
            */
        }
    }
    int best_play = 0;
    //printf("player %i\n", player->number);
    for (size_t i = 0; i < PLAYS; i++)
    {
        //printf("weights %zu = %li\n", i, weights[i]);
        if (weights[best_play] < weights[i])
        {
            best_play = i;
        }
    }
    return best_play;
}

int player_play(player_t *player)
{
    if (player->memory_is_empty || !player->use_memory)
    {
        return rand() % PLAYS;
    }
    else
    {
        return player_play_from_memory(player);
    }
    
}

void player_print_attributes(player_t *player)
{
    printf("%s: %i\n", "player no", player->number);
    for (size_t i = 0; i < ATTRIBUTES; i++)
    {
        printf("%s: %zu, %s: %lli\n", "attribute no: ", i, "value", player->attributes[i]);
    }
}