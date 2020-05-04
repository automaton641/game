#include <library/application.h>
#include <library/memory_block.h>
#include <stdio.h>
#include <stdbool.h>
int main(int argc, char const *argv[])
{
    //41.0/101.0
    long long compensator_a = 1;
    long long compensator_b = 0;
    //printf("Hello\n");
    //application_erase_memory();
    //printf("size: %zu\n", sizeof(unsigned long long long long));
    while (true)
    {
        application_t *application = application_create();
        for (size_t i = 0; i < 1024; i++)
        {
            //printf("run %zu\n", i);
            application_run(application, 1);
        }
        application_destroy(application);
        print_winrate(&compensator_a, &compensator_b);
        return 0;
    }
    
    

}
