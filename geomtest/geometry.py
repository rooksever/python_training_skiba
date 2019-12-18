from geom2d.point import Point

# just sorting
# l1 = [Point(3, 1), Point(0, 0), Point(1, 2)]

# l2 = sorted(l1, key=lambda p: p.distance(Point(0, 0)))

# print(l1)
# print(l2)
# ______________

# list comprehention
# l = [Point(i, i*i) for i in range(-5, 6)]

# cycle
# l2 = []

# for el in l:
    # upward parabola
#     l2.append(Point(el.x, -el.y))

# print(l)
# print(l2)
# ___________________

# map way
# l = list(map(lambda i: Point(i, i*i), range(-5, 6)))

# l2 = list(map(lambda p: Point(p.x, -p.y), l))

# print(l)
# print(l2)

# filter
l = list(map(lambda i: Point(i, i*i), range(-5, 6)))

# x>0
# l2 = list(filter(lambda p: p.x > 0, l))
# x is even
l2 = list(filter(lambda p: p.x % 2 == 0, l))


print(l)
print(l2)