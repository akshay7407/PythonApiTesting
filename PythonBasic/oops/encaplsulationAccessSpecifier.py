class MyClass:
    def __init__(self):
        self.public_var = 10       # Public attribute
        self._protected_var = 20   # Protected attribute
        self.__private_var = 30    # Private attribute

    def public_method(self):
        pass  # Public method

    def _protected_method(self):
        pass  # Protected method

    def __private_method(self):
        pass  # Private method

    # Access Modifiers:
    # Python doesn't have strict access modifiers like some other languages (e.g., public, private, protected). However, it uses naming conventions to indicate the visibility of attributes and methods.
    #
    # Public: No special symbol. Accessible from anywhere.
    # Protected: Use a single underscore _ prefix. Suggests that an attribute or method should not be accessed directly from outside the class, but it's not enforced.
    # Private: Use a double underscore __ prefix. The attribute or method name gets name-mangled to include the class name, making it more difficult to accidentally override in subclasses.