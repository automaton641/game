#include <library/math.h>

long long distance(long long a, long long b)
{
    long long c = a - b;
    if (c < 0.0)
    {
        return -c;
    }
    return c;
}