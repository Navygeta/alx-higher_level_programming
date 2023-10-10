#include <Python.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: pointer to a Python object of type PyObject.
 */
void print_python_list_info(PyObject *p)
{
	int size, alloced, i;
	PyObject *object;

	size = Py_SIZE(p);
	alloced = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*] Allocated = %d\n", alloced);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: ", i);

		object = PyList_GetItem(p, i);
		printf("%s\n", Py_TYPE(object)->tp_name);
	}
}
