#include "lists.h"

/**
 * insert_node - inserts a node in a sorted list
 * @head: pointer to the linked list
 * @number: value of the new node
 *
 * Return: address of the new node or NULL if it fails
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new, *current;

	current = *head;

	new = malloc(sizeof(listint_t));

	if (new == NULL)
		return (NULL);
	new->n = number;

	if (current == NULL || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}

	while (current && current->next && current->n < number)
	{
		current = current->next;
	}

	new->next = current->next;
	current->next = new;

	return (new);

}
