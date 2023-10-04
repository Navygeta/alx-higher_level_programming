#include "lists.h"
/**
 * insert_node - inserts number into sorted singly linked list
 * @head: pointer to head pointer of list
 * @number: number to insert into node
 * Return: address of node or NULL on failure
 */
listint_t *insert_node(listint_t **head, int number);
{
	listint_t *nu_node = *current, *prev;

	nu_node = malloc(sizeof(listint_t));
	if (nu_node == NULL)
	{
		return (NULL);
	}
	nu_node->n = number;
	nu_node->next = NULL;
	if (*head == NULL || (*head) ->n >= number)
	{
		nu_node->next = *head;
		*head = nu_node;
		return (nu_node);
	}
	current = *head;
	prev = NULL;

	while(current && current->n < number)
	{
		prev = current;
		current = current->next;
	}

	nu_node->next = current;
	prev->next = nu_node;

	return (nu_node);
}
