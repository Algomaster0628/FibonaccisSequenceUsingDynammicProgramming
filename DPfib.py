# Calculate fibonaccis number using memoization and recursion.
memo = {}
def fib(n):
  if n in memo:
    return memo[n]
  if n == 1 or n == 2:
    result = 1
  else:
    result = fib(n - 1) + fib(n - 2)
  memo[n] = result
  return result
x = fib(99)
print(x)
print(memo)
