import itertools


def solution(relation):
    row_len = len(relation)
    col_len = len(relation[0])
    generated_keys = []
    col_nums = [i for i in range(col_len)]
    for i in range(1, col_len + 1):
        for column_numbers in itertools.combinations(col_nums, i):
            candidate_keys = set()
            is_minimal = True
            for key in generated_keys:
                if key.issubset(column_numbers):
                    is_minimal = False
                    break
            if not is_minimal:
                continue

            for r in relation:
                key = ""
                for c in column_numbers:
                    key += r[c]
                candidate_keys.add(key)
            if len(candidate_keys) == row_len:
                generated_keys.append(set(column_numbers))

    return len(generated_keys)


print(
    solution(
        [
            ["100", "ryan", "music", "2"],
            ["200", "apeach", "math", "2"],
            ["300", "tube", "computer", "3"],
            ["400", "con", "computer", "4"],
            ["500", "muzi", "music", "3"],
            ["600", "apeach", "music", "2"],
        ]
    )
)
