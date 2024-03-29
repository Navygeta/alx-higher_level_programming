#include "lists.h"
/**
 * insert_node - inserts number into sorted singly linked list
 * @head: pointer to head pointer of list
 * @number: number to insert into node
 * Return: address of node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *node = *head, *nu_node;

	nu_node = malloc(sizeof(listint_t));
	if (nu_node == NULL)
		return (NULL);
	nu_node->n = number;

	if (node == NULL || node->n >= number)
	{
		nu_node->next = node;
		*head = nu_node;
		return (nu_node);
	}

	while (node && node->next && node->next->n < number)
		node = node->next;

	nu_node->next = node->next;
	node->next = nu_node;

	return (nu_node);
}
