def create_class(class_name, secrets=None):

    class MetaClass(type):
        def __new__(mcs, name, bases, cls_dict):
            name = class_name
            if secrets:
                cls_dict.update(**secrets)
            cls = super().__new__(mcs, name, bases, cls_dict)
            return cls

    class NewClass(metaclass=MetaClass):
        pass

    if not class_name:
        return None
    return NewClass
