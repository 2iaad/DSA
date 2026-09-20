import time

""" Testing performance Global vs Function scope """

# -> Global Scope
# -----------------------------------
t0 = time.perf_counter()
n = 10_000_000
while n > 0:
    n -= 1
t_global = time.perf_counter() - t0
# -----------------------------------

# -> Inside a Function
# -----------------------------------
def run_local():
    n = 10_000_000
    while n > 0:
        n -= 1

t0 = time.perf_counter()
run_local()
t_local = time.perf_counter() - t0
# -----------------------------------

print(f"Function: {t_local:.4f}s")
print(f"Global:   {t_global:.4f}s")
print(f"Speedup:  {t_global / t_local:.2f}x faster")
