// 2577 c

#include <stdio.h>

int    main(void)
{
    int arr[42];
    int input[10];
    int result = 0;

    for (int i = 0; i < 10; i++)
    {
        scanf_s("%d", &input[i]);
    }
    for (int i = 0; i < 10; i++)
        input[i] = input[i] % 42;
    for (int i = 0; i < 42; i++)
    {
        for (int j = 0; j < 10; j++)
        {
            if (input[j] == i)
            {
                result++;
                break;
            }
        }
    }
    printf("%d\n", result);
}
