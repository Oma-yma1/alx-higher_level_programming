#include "lists.h"
/**
 * check_cycle - check if a singly linked list has a cycle in int
 * @list: linked list
 * Return: 0 ifthere is no cycle or 1 if there is a cycle
 */
int check_cycle(listint_t *list)
{
listint_t *check0 = list, *check1 = list;
if (list == NULL)
return (0);
	while (check0 != NULL && check1 != NULL && check1->next != NULL)
	{
		check0 = check0->next;
		check1 = check1->next->next;
		if (check0 == check1)
			return (1);
	}
	return (0);
}
