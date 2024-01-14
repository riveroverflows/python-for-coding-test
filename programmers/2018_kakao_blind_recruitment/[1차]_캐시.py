from math import inf


def solution(cacheSize, cities):
    answer = 0
    cache = {}
    if cacheSize == 0:
        return len(cities) * 5

    for i, city in enumerate(cities):
        city_lower = city.lower()
        if len(cache) + 1 <= cacheSize:
            cache[city_lower] = (i, 1)
            answer += 5
        else:
            if city_lower in cache:
                index, hits = cache.get(city_lower)
                hits += 1
                cache[city_lower] = (index, hits)
                answer += 1
            else:
                # hits 수가 제일 작은 것 중에 제일 빨리 추가된 거
                min_hits = inf
                min_idx = inf
                min_city = ''
                for k, v in cache.items():
                    idx, hits = v
                    if min_hits > hits:
                        min_hits = hits
                        min_idx = idx
                        min_city = k
                        continue
                    if min_hits == hits:
                        if min_idx > idx:
                            min_idx = idx
                            min_city = k

                del cache[min_city]
                cache[city_lower] = (i, 1)
                answer += 5

    return answer

"""
print(solution(3, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 50
print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))  # 21
print(solution(2,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))  # 60
"""
print(solution(5,
               ["Jeju", "Pangyo", "Seoul", "NewYork", "LA", "SanFrancisco", "Seoul", "Rome", "Paris", "Jeju", "NewYork",
                "Rome"]))  # 52
# print(solution(2, ["Jeju", "Pangyo", "NewYork", "newyork"]))  # 16
# print(solution(0, ["Jeju", "Pangyo", "Seoul", "NewYork", "LA"]))  # 25