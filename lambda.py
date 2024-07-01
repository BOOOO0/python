from functools import reduce

ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(list(map(lambda x: x * 2, ls)))

print(list(filter(lambda x: x < 5, ls)))

print(reduce(lambda x, y: x + y, ls, 0))

print(reduce(lambda x, y: x + y, ls, 10))

print("true" if True else "false")

ranked_users = ['jon', 'bob', 'jane', 'alice', 'chris']

user_details = [{'name': x, 'rank': i+1} for i, x in enumerate(ranked_users)]

print(user_details)
