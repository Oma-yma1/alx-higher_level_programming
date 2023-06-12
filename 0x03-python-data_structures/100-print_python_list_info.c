#include <Python.h>
/**
 *print_python_list_info - prints some basic info about Python
 *@p: a pointer
 */
void print_python_list_info(PyObject *p)
{
Py_ssize_t ssize = Py_SIZE(p), i;
PyObject *object;
printf("[*] Size of the Python List = %zd\n", ssize);
printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);
for (i = 0; i < ssize; i++)
{
object = PyList_GetItem(p, i);
printf("Element %zd: ", i);
printf("%s\n", Py_TYPE(object)->tp_name);
}
}
