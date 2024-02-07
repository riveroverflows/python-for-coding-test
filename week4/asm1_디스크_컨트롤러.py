import heapq


def solution(jobs):
    jobs.sort()
    jobs_qty = len(jobs)
    current_time, total_duration = 0, 0
    completed_qty = 0
    job_idx = 0
    min_heap = []
    while completed_qty < jobs_qty:
        while job_idx < jobs_qty and jobs[job_idx][0] <= current_time:
            req_time, duration = jobs[job_idx]
            heapq.heappush(min_heap, (duration, req_time))
            job_idx += 1

        if not min_heap:
            current_time = jobs[job_idx][0]
            continue

        duration, req_time = heapq.heappop(min_heap)
        current_time += duration
        total_duration += current_time - req_time
        completed_qty += 1

    return total_duration // jobs_qty


print(solution([[0, 3], [1, 9], [2, 6]]))
print(solution([[2, 3], [3, 5], [4, 2]]))
print(solution([[2, 3], [0, 9], [2, 6]]))
