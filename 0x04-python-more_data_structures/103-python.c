#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - function to print bytes information
 *
 * @p: Python Object
 * Return: No need to return in void function
 */
void print_python_bytes(PyObject *p)
{
	char *byt_string;
	long int byt_size, i, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	byt_size = ((PyVarObject *)(p))->ob_size;
	byt_string = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", byt_size);
	printf("  trying string: %s\n", byt_string);

	if (byt_size >= 10)
		limit = 10;
	else
		limit = byt_size + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
	if (byt_string[i] >= 0)
		printf(" %02x", (unsigned char)byt_string[i]);
	else
		printf(" %02x", 256 + (unsigned char)byt_string[i]);

	printf("\n");
}

/**
 * print_python_list - function to print list information
 *
 * @p: Python Object
 * Return: No need to return in void function
 */
void print_python_list(PyObject *p)
{
	long int list_size, i;
	PyListObject *list;
	PyObject *element_obj;

	list_size = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", list_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < list_size; i++)
	{
		element_obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, element_obj->ob_type->tp_name);
	if (PyBytes_Check(element_obj))
		print_python_bytes(element_obj);
	}
}

