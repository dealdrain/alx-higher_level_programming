#include "lists.h"

/**
 * insert_node - Ins a node
 * @head: linked list head
 * @number: addition to the list
 * Return: Ptr to node or null
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *now = *ini;
	listint_t *fut = NULL;
	listint_t *temp = NULL;

	(void)number;

	fut = malloc(sizeof(listint_t));
	if (fut == NULL)
		return (NULL);

	if (ini == NULL || *ini == NULL)
	{
		fut->n = number;
		fut->next = NULL;
		*ini = fut;
		return (fut);
	}

	if (now->n > number)
	{
		fut->n = number;
		fut->next = now;
		*ini = fut;
		return (*ini);
	}

	/* Traverse the list to find where current->n > number*/
	while (now->n < number && now->next != NULL)
	{
		if (now->next->n >= number)
			break;
		now = now->next;
	}
	fut->n = number;
	temp = now->next;
	now->next = fut;
	fut->next = temp;

	return (NULL);
}
