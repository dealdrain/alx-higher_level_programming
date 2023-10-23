#include <Python.h>

void plist_print(PyObject *p);
void pbytes_print(PyObject *p);
void pfloat_print(PyObject *p);

/**
 * plist_print - Print info about P list.
 * @p: PyObject list object.
 */
void plist_print(PyObject *p)
{
	Py_ssize_t size;
	PyListObject *list;
	PyVarObject *var;

	if (!PyList_Check(p))
	{
		printf("  [ERROR] Invalid List Object\n");
		return;
	}

	list = (PyListObject *)p;
	var = (PyVarObject *)p;
	size = var->ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (Py_ssize_t i = 0; i < size; i++)
	{
		PyObject *item = list->ob_item[i];
		const char *type = item->ob_type->tp_name;

		printf("Element %ld: %s\n", i, type);

		if (strcmp(type, "bytes") == 0)
			pbytes_print(item);
		else if (strcmp(type, "float") == 0)
			pfloat_print(item);
	}
}

/**
 * pbytes_print - Print info on bytess.
 * @p: PyObject byte object.
 */
void pbytes_print(PyObject *p)
{
	PyBytesObject *bytes;

	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes = (PyBytesObject *)p;

	printf("[.] bytes object info\n");
	printf("  size: %ld\n", PyBytes_Size(p));
	printf("  trying string: %s\n", bytes->ob_sval);

	Py_ssize_t size = PyBytes_Size(p) >= 10 ? 10 : PyBytes_Size(p) + 1;

	printf("  first %ld bytes: ", size);
	for (Py_ssize_t i = 0; i < size; i++)
	{
		printf("%02hhx%s", bytes->ob_sval[i], i == size - 1 ? "\n" : " ");
	}
}

/**
 * pfloat_print - Print basic info on float.
 * @p: float object.
 */
void pfloat_print(PyObject *p)
{
	PyFloatObject *float_obj;

	if (!PyFloat_Check(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	float_obj = (PyFloatObject *)p;
	printf("[.] float object info\n");
	printf("  value: %s\n", PyOS_double_to_string(float_obj->ob_fval, 'r', 0, Py_DTSF_ADD_DOT_0, NULL));
}
