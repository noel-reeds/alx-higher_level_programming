#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
/**
 * insert_node - inserts a number into a sorted singly linked list.
 *@head: head pointer
 *@number: number to be inserted in the linked list.
 *Return: pointer to the newly inserted node or NULL if failed.
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *new_node = malloc(sizeof(listint_t));
	listint_t *temp;

	if (!new_node)
		return (NULL);
	new_node->n = number;
	if (!head) /* empty list..*/
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	temp = *head;
	if (!temp->next)
	{
		if (temp->n < new_node->n)
		{
			temp = new_node;
			new_node->next = NULL;
		}
		new_node->next = temp;
		new_node = temp;
	}
	while (temp)
	{
		if (temp->n < new_node->n)
		{
			new_node->next = temp->next;
			temp = new_node;
		}
		else
			new_node = temp;
		temp = temp->next;
	}
	return (new_node);
}
