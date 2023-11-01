#include "Python.h"

/**
 * print_python_string - function that prints Python strings
 * @p: A PyObject string object.
 */
void print_python_string(PyObject *p)
{
	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
	{
		printf("[ERROR] Invalid String Object\n");
		return;
	}

	printf("type: %s\n",
		 PyUnicode_IS_COMPACT_ASCII(p) ?
		"compact ascii" : "compact unicode object");
	printf("length: %ld\n", PyUnicode_GetLength(p));
	printf("value: %ls\n", PyUnicode_AsWideCharString(p, NULL));
}
