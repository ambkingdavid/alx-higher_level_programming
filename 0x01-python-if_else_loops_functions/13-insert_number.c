#include "list.h"

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

	while (node && node->next && node->n < number)
	{
		node = node->next;
	}

	new->next = node->next;
	node->next = new;

	return (new);

}
