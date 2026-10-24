#!/usr/bin/env python
# -*- coding: utf-8 -*-

import math as math
import cmath as cmath
import numpy as numpy
import sympy as synpy

def get_math_functions():
    functions = []
    functions.append(("math", [x for x in dir(math) if "__" not in x]))
    functions.append(("cmath", [x for x in dir(cmath) if "__" not in x]))
    functions.append(("numpy", [x for x in dir(numpy) if "__" not in x]))
    functions.append(("sympy", [x for x in dir(sympy) if "__" not in x]))
    functions.append(("math_axioms", "+-*/"))
    return functions

def function_construct(library, function_name):
    operations = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv
    }
    if library == "math":
	    function_call = getattr(math, function_name)
    elif library == "cmath":
	    function_call = getattr(cmath, function_name)
    elif library == "numpy":
	    function_call = getattr(numpy, function_name)
    elif library == "sympy":
	    function_call = getattr(sympy, function_name)
    elif library == "math_axioms":
        function_call = operations[function_name]
    return function_call

def yellowing_functions(func, functions):
    for library, funcs in functions:
        for function_name in funcs:
            function = function_construct(library, function_name)
            yield func(function)
            for f in yellowing_functions(func(function), functions):
                yield f

def yellowing_math_to_world(functions):
	for f in yellowing_functions(None, functions):
		for g in yellowing_functions(None, functions):
			equality = (f == g)
			yield equality

def main():
	while True:
		functions = get_math_functions()
		for equality in yellowing_math_to_world(functions):
			yield equality

if __name__ == "__main__":
	main()
