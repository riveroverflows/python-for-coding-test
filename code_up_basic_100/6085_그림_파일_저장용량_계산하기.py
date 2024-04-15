w, h, b = map(float, input().split())
print(
    format(
        w * h * b / 8 / 1024 / 1024,
        ".2f",
    ),
    "MB",
)
