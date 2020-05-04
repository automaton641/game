#include <library/array.h>
#include <stdlib.h>
#include <string.h>

void array_add(array_t *array, void *element) 
{
    if (array->size == array->capacity) 
    {
        array->capacity *= 2;
        array->data = realloc(array->data, array->capacity*array->element_size);
    }
    memcpy(array->data+array->size*array->element_size, element, array->element_size);
    array->size++;
}

void array_destroy(array_t *array) 
{
    free(array->data);
    free(array);
}

array_t *array_create(size_t element_size) 
{
    array_t *array = malloc(sizeof(array_t));
    array->element_size = element_size;
    array->capacity = 16;
    array->size = 0;
    array->data = malloc(array->capacity*element_size);
    return array;
}

void *array_get(array_t *array, size_t index) 
{
    return (void*)(array->data+index*array->element_size);
}