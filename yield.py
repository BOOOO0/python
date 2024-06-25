def yield_abc():
    yield "a"
    yield "b"
    yield "c"


abc = yield_abc()
print(abc)
print(type(abc))

for a in abc:
    print(a)

tp = ("a", "b", "c")
print(tp[0])
