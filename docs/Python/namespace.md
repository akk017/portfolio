---
title: Namespaces
---


A Python namespaces is a mapping from names to objects. It works like a dictionary where keys are object names and values are the objects themselves.

A `namespace` is a container that holds the currently defined symbolic names and the objects each name references.

These namespaces have differing lifetimes. As Python executes a program, it creates namespaces as necessary and removes them when it no longer needs them.


Four Different Namespace Available:

1. Built-in
2. Local
3. Gobal
4. Enclosing or nonlocal



### Built-In Namespace
-  ex. Exception, Primitive Types, sort, reverse etc.
```python
>>> dir(__builtins__)
[
    'ArithmeticError',
    'AssertionError',
    'AttributeError',
    'BaseException',
    ...
    'super',
    'tuple',
    'type',
    'vars',
    'zip'
]
```

### Global Namespace
- The global namespace contains the names defined at the module level.
- Python creates a main global namespace when the main program’s body starts.

- `Globals are seperate to module`

### Local Namespace
- function level namespace
- on enter of function -> create a namespace, on exit of a function -> delete the namespace.

### Enclosing or Non Local Namespace
```py
>>> global_variable = "global"

>>> def outer_func():
...     # Nonlocal scope
...     nonlocal_variable = "nonlocal"
...     def inner_func():
...         # Local scope
...         local_variable = "local"
...         print(f"Hi from the '{local_variable}' scope!")
...         print(f"Hi from the '{nonlocal_variable}' scope!")
...         print(f"Hi from the '{global_variable}' scope!")
...     inner_func()
...

>>> outer_func()
Hi from the 'local' scope!
Hi from the 'nonlocal' scope!
Hi from the 'global' scope!
```

### The LEGB Rule for Searching Name
`LOCAL > ENCLOSING > GLOBAL > BUILTIN

