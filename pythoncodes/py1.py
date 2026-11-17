import time

N = 5000000

def sum_array(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

def sum_squares(n):
    total = 0
    for i in range(1, n + 1):
        total += i * i
    return total

def alternating_sum(n):
    total = 0
    for i in range(1, n + 1):
        if i % 2 == 0:
            total += i
        else:
            total -= i
    return total

if __name__ == "__main__":
    start = time.perf_counter()
    print(f"Sum: {sum_array(N)} (Time: {time.perf_counter() - start:.4f}s)")

    start = time.perf_counter()
    for k in range(10):
        res_sq = sum_squares(N)
    print(f"Sum of squares (called 10 times): {res_sq} (Total Time: {time.perf_counter() - start:.4f}s)")

    start = time.perf_counter()
    print(f"Alternating sum: {alternating_sum(N)} (Time: {time.perf_counter() - start:.4f}s)")