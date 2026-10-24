#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright Chems eddine h1t8re 6.2.1996 After Jesus Christ'e

import math as math
import cmath as cmath
import numpy as numpy
import sympy as sympy
from mpmath import mp
import operator as operator

def get_math_functions():
	libraries_functions = []
	libraries_functions.append(("math", [x for x in dir(math) if "__" not in x]))
	libraries_functions.append(("cmath", [x for x in dir(cmath) if "__" not in x]))
	libraries_functions.append(("numpy", [x for x in dir(numpy) if "__" not in x]))
	libraries_functions.append(("sympy", [x for x in dir(sympy) if "__" not in x]))
	libraries_functions.append(("mp", [x for x in dir(mp) if "__" not in x]))
	libraries_functions.append(("operators", [x for x in dir(operator) if "__" not in x]))
	return libraries_functions

def make_function_callable(library_name, function_name):
	if library_name == "math":
		function_call = getattr(math, function_name)
	elif library_name == "cmath":
		function_call = getattr(cmath, function_name)
	elif library_name == "numpy":
		function_call = getattr(numpy, function_name)
	elif library_name == "sympy":
		function_call = getattr(sympy, function_name)
	elif library_name == "mp":
		function_call = getattr(mp, function_name)
	elif library_name == "operators":
		function_call = getattr(operator, function_name)
	return function_call

def yellowing_functions(func, libraries_of_functions):
	for library_name, library_of_functions in libraries_of_functions:
		for function_name in library_of_functions:
			function = make_function_callable(library_name, function_name)
			yield func(function)
			for f in yellowing_functions(func(function), libraries_of_functions):
				yield f

def yellowing_math_to_world(libraries_of_functions):
	for f in yellowing_functions(None, libraries_of_functions):
		for g in yellowing_functions(None, libraries_of_functions):
			equality = (f == g)
			yield equality

def main():
	while True:
		libraries_of_functions = get_math_functions()
		for equality in yellowing_math_to_world(libraries_of_functions):
			yield equality

if __name__ == "__main__":
	main()
