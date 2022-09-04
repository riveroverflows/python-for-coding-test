h, b, c, s = map(float, input().split())
print(format(h * b * c * s / 8 / 1024 / 1024, ".1f"), "MB")
