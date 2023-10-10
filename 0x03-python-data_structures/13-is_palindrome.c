#include "lists.h"

/**
 * is_palindrome - Function that checks if a singly linked list is a palindrome
 * @head: Pointer to the head of linked list.
 *
 * Return: 0 - If linked list is not a palindrome.
 *         1 - If list is a palindrome.
 */
int is_palindrome(listint_t **head)
{
	listint_t *current, *reversed, *mid;
	size_t size = 0, i;
	const size_t half = size / 2;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	current = *head;
	while (current)
	{
		size++;
		current = current->next;
	}

	current = *head;
	for (i = 0; i < (half) - 1; i++)
		current = current->next;

	if ((size % 2) == 0 && current->n != current->next->n)
		return (0);

	current = current->next->next;
	reversed = reverse_listint(&current);
	mid = reversed;

	current = *head;
	while (reversed)
	{
		if (current->n != reversed->n)
			return (0);
		current = current->next;
		reversed = reversed->next;
	}
	reverse_listint(&mid);

	return (1);
}
