# work with these variables
eugene = set(input().split())
rose = set(input().split())

non_visit_1 = eugene.difference(rose)
non_visit_2 = rose.difference(eugene)
print(non_visit_1 | non_visit_2)
