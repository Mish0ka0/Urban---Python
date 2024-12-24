import sys


def introspection_info(obj):
    type_obj = type(obj).__name__
    method_name = type.__name__
    attributes = [attr for attr in dir(obj) if not callable(getattr(obj, attr))]
    methods = [attr for attr in dir(obj) if callable(getattr(obj, attr))]
    modules = introspection_info.__module__
    ident = id(obj)
    sizes = sys.getsizeof(obj)
    return {method_name: type_obj, 'attributes': attributes, 'methods': methods, 'module': modules,
            'id': ident, 'size': sizes}


number_info = introspection_info(42)
print(number_info)
