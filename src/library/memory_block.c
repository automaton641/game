#include <library/memory_block.h>
#include <library/array.h>
#include <library/application.h>
#include <library/math.h>
#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

array_t *load_memory_array()
{
    FILE *file = fopen("memory.bin", "r");
    if (file == NULL)
    {
        return NULL;
    }
    array_t *array = array_create(sizeof(memory_block_t));
    memory_block_t *memory_block = malloc(sizeof(memory_block_t));
    while (true)
    {
        fread(memory_block, sizeof(memory_block_t), 1, file);
        if (ferror(file))
        {
            fclose(file);
            printf("%s\n", "ERROR LOADING MEMORY");
            free(memory_block);
            exit(EXIT_FAILURE);
        }
        if (feof(file))
        {
            fclose(file);
            free(memory_block);
            return array;;
        }
        array_add(array, memory_block);
    }
}

bool print_winrate(long long *compensator_a, long long *compensator_b)
{
    array_t *memory = load_memory_array();
    if (memory == NULL)
    {
        printf("MEMORY IS NULL");
        return false;
    }
    long long a_wins = 0.0;
    long long b_wins = 0.0;
    long long games_count = 0;
    long long average_turns = 0.0;
    long long plays_a[4];
    long long plays_b[4];
    for (size_t i = 0; i < PLAYS; i++)
    {
        plays_a[i] = 0;
        plays_b[i] = 0;
    }
    
    memory_block_t *memory_block;
    memory_block_t *last_memory_block;
    size_t i;
    for (i = 0; i < memory->size; i++)
    {
        memory_block = array_get(memory, i);
        if (memory_block->turn % 2 == 0)
        {
            plays_a[memory_block->play] += 1;
        }
        else
        {
            plays_b[memory_block->play] += 1;
        }
        
        
        if (memory_block->turn == 0)
        {
            if (i > 0)
            {
                last_memory_block = array_get(memory, i-1); 
                average_turns += last_memory_block->turn + 1.0;
            }
            
            games_count += 1;
            if (memory_block->winner == 0)
            {
                a_wins += 1;
            }
            else if (memory_block->winner == 1)
            {
                b_wins += 1;
            }
        }
    }
    last_memory_block = array_get(memory, i-1); 
    average_turns += last_memory_block->turn + 1.0;
    average_turns /= games_count;
    long long winrate = 100*a_wins/(a_wins+b_wins);
    long long real_winrate = 100*a_wins/(games_count);
    for (size_t i = 0; i < PLAYS; i++)
    {
        printf("%s: %zu - %lli\n", "a play", i, plays_a[i]);
    }
    for (size_t i = 0; i < PLAYS; i++)
    {
        printf("%s: %zu - %lli\n", "b play", i, plays_b[i]);
    }
    printf("\n%s: %lli\n", "games_count", games_count);
    printf("\n%s: %lli\n", "average_turns", average_turns);
    printf("\n%s: %lli\n", "a_wins", a_wins);
    printf("\n%s: %lli\n", "b_wins", b_wins);
    printf("\n%s: %lli\n", "draws", games_count - a_wins - b_wins);
    printf("\n%s: %lli\n", "winrate", winrate);
    printf("\n%s: %lli\n", "real winrate", real_winrate);
    array_destroy(memory);
    if (distance(winrate, 50) < 5)
    {
        printf("\nSUCCESS!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
        printf("\n%s: %lli\n", "winrate", winrate);
        return true;
    }
    else
    {
        //printf("%04x",a);
        printf("\nFAILURE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!\n");
        printf("\n%s: %lli\n", "winrate", winrate);        
    }
    return false;
}