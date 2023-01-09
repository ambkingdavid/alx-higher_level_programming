#include <stdlib.h>
#include <stdio.h>
#include "lists.h"

/**
 * is_palindrome - checks if a linked list is palindrome
 * @head: address of the linked list
 *
 * Return: 1 if palindrome and 0 otherwise
 */


int is_palindrome(listint_t **head)
{
	listint_t *tmp, *start;
	int len, i, list_len, list_val[50];

	tmp = *head;
	start = *head;
	len = 0;
	list_len = 0;

	while (tmp)
	{
		list_val[len] = tmp->n;
		tmp = tmp->next;
		len++;
	}
	len = len - 1;

	for (i = 0; i <= len; i++)
	{
		if (start->n == list_val[len - i])
			list_len++;
		start = start->next;
	}

	if (list_len == len + 1)
		return (1);
	return (0);
}
