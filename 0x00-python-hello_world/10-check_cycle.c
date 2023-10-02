#include "lists.h"

/**
 * check_cycle - Checks if a list has a cycle
 * @list: List argument to be checked
 * Return: 0 if cycle is not found else 1
 */

int check_cycle(listint_t *list)
{
	listint_t *sl = list;
	int a = 0;

	if (list == NULL || list->next == NULL)
		return (0);

	while (sl != NULL)
	{
		if (a > 12)
			return (1);
		sl = sl->next;
		a++;
	}

	return (0);
}
