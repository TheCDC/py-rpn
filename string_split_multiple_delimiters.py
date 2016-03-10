#!/usr/bin/env python3

import re

def main():
	ex_str = "We hold these truths to be self-evident, that is they are obvious; they require no effort to see."
	delimiters = [' ',', ','\.\s*','; ','-']

	regex = "(" + '|'.join(delimiters) + ")"
	results = re.split(regex,ex_str)
	print(results)

def split_by_list(s,l):
	return re.split('|'.join(l),s)

if __name__ == '__main__':
	main()