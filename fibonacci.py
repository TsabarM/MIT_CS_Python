# Efficient Fibonnaci

d = {1:1, 2:2} #base case

def fib_efficient(n, d):
    if n in d:
        return d[n]
    else:
        ans = fib_efficient(n-1, d) + fib_efficient(n-2, d)
        d[n] = ans
        return ans

if __name__ == "__main__":
    print(fib(6, d))