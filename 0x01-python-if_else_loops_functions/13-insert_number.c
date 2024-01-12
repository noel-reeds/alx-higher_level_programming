#include "lists.h"
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

	if (!number)
		return (NULL);
	new_node->n = number;
	if (!head)
	{
		*head = new_node;
		new_node->next = NULL;
		return (new_node);
	}
	temp = *head;
	if (temp) /* missing.. */
	{
		if (temp->n > new_node->n)
		{
			new_node->next = temp->next;
			*head = new_node;
		}
		temp->next = new_node;
		new_node->next = NULL;
	}
	while (temp)
	{
		if (temp->n > new_node->n)
		{
			new_node->next = temp;
			temp = new_node;
		}
		temp = new_node;
	}
}
