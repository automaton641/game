#include <library/application.h>
#include <stdlib.h>
#include <stdbool.h>
#include <stdio.h>
#include <time.h>

void application_print_winner(application_t *application)
{
    switch (application->game->winner)
    {
    case 0:
        printf("%s\n", "a wins");
        break;
    case 1:
        printf("%s\n", "b wins");
        break;
    case 2:
        printf("%s\n", "draw");
        break;
    default:
        printf("%s\n", "ERROR: WINNING");
        break;
    }
    printf("%s: %i\n", "turn", application->game->turn);
}

void application_run(application_t *application, long long compensator) 
{
    application->game = game_create(compensator);
    //game_print_players_memory(application->game);
    
    while (true)
    {
        if (game_play(application->game))
        {
            break;
        }        
    }
    game_save_memory(application->game);
    game_destroy(application->game);
    //game_print_players_attributes(application->game);
    //application_print_winner(application);
    
}

application_t *application_create() 
{
    application_t *application = malloc(sizeof(application_t));
    srand(time(0)); 
    return application;
}

void application_destroy(application_t *application) 
{
    free(application);
}

void application_erase_memory()
{
    if (remove("memory.bin"))
    {
        printf("Unable to delete the file\n"); 
    }
}