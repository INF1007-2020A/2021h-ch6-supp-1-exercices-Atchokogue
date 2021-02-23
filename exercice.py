#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy
import itertools


def get_maximums(numbers):
	liste_finale = []
	for listes in numbers:
		liste_ordre = sorted(listes, reverse=True)
		liste_finale += liste_ordre[0:1]

	return [liste_finale]


def join_integers(numbers):
	string_nbr = ""
	for elem in numbers:
		string_nbr += str(elem)
	return int(string_nbr)


def generate_prime_numbers(limit):
	premiers = []
	nombres = list(range(2, limit + 1))
	while len(nombres) != 0:
		premiers.append(nombres[0])
		nombres = [elem for elem in nombres if elem % nombres[0] != 0]

	return premiers


def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	return [""]


if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(77))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
