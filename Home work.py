import inspect

def introspection_info(obj):
    info = {}


    info['type'] = type(obj).__name__


    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr)) and not attr.startswith("__")]
    info['attributes'] = attributes


    methods = [method for method in dir(obj) if callable(getattr(obj, method)) and not method.startswith("__")]
    info['methods'] = methods


    info['module'] = obj.__module__ if hasattr(obj, '__module__') else 'N/A'


    if inspect.isclass(obj):
        info['is_class'] = True
        info['base_classes'] = [base.__name__ for base in inspect.getmro(obj)[1:]]
    elif inspect.isfunction(obj):
        info['is_function'] = True
        info['signature'] = inspect.signature(obj)
    elif inspect.ismethod(obj):
        info['is_method'] = True
        info['signature'] = inspect.signature(obj)
    elif inspect.ismodule(obj):
        info['is_module'] = True
        info['file'] = inspect.getfile(obj)
    elif inspect.isbuiltin(obj):
        info['is_builtin'] = True

    return info


number_info = introspection_info(42)
print(number_info)

class MyClass:
    def __init__(self, value):
        self.value = value

    def my_method(self):
        pass

my_object = MyClass(10)
object_info = introspection_info(my_object)
print(object_info)
