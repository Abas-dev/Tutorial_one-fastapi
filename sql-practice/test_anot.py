#This file is to explain more about Annotation in python. https://docs.python.org/3/library/typing.html#typing.Annotated
from typing import Annotated, get_type_hints, get_args, get_origin
from functools import wraps 

def check_value_range(func):
    @wraps(func)
    def wrapped(x):
        type_hints = get_type_hints(double, include_extras=True)
        hint = type_hints['x']
        if get_origin(hint) is Annotated: 
            hint_type, *hint_args = get_args(hint)
            low, high = hint_args[0]

            if not low <= x <= high:
                raise ValueError(f"{x} falls outside boundary {low} - {high}")
        return func(x)
    return wrapped

 
def double(x: Annotated[int, (0,100)]) -> int:
    type_hints = get_type_hints(double, include_extras=True)
    hint = type_hints['x']
    if get_origin(hint) is Annotated: 
        hint_type, *hint_args = get_args(hint)
        low, high = hint_args[0]

        if not low <= x <= high:
            raise ValueError(f"{x} falls outside boundary {low} - {high}")
    return x * 2

result = double(80)

print(result)