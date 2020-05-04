#pragma once

typedef struct array array_t;

#include <stddef.h>

array_t *array_create(size_t element_size);

void array_add(array_t *array, void *element);

void *array_get(array_t *array, size_t index);

void array_destroy(array_t *array);

struct array 
{
    unsigned char *data;
    size_t capacity;
    size_t size;
    size_t element_size;
};