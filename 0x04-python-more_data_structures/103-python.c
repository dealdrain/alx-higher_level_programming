#include "/usr/include/python3.4/Python.h"
#include <stdio.h>

void print_hexn(const char *str, int n) {
	for (int i = 0; i < n; ++i) {
		printf("%02x ", (unsigned char)str[i]);
	}
	printf("\n");
}

void print_python_bytes(PyObject *p) {
	printf("[.] bytes object info\n");
	if (PyBytes_Check(p)) {
		int size = PyBytes_Size(p);
		int calc_bytes = size < 10 ? size : 10;
		
		printf("  size: %d\n", size);
		printf("  trying string: %s\n", PyBytes_AsString(p));
		printf("  first %d bytes: ", calc_bytes);
		print_hexn(PyBytes_AsString(p), calc_bytes);
	} else {
		printf("  [ERROR] Invalid Bytes Object\n");
	}
}

void print_python_list(PyObject *p) {
	printf("[*] Python list info\n");
	int list_len = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", list_len);
	printf("[*] Allocated = %d\n", (int)((PyListObject *)p)->allocated);

	for (int i = 0; i < list_len; ++i) {
		PyObject *item = PyList_GetItem(p, i);
		printf("Element %d: %s\n", i, item->ob_type->tp_name);
		
		if (PyBytes_Check(item)) {
			print_python_bytes(item);
		}
	}
}
