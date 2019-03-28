'''write a function that gets 3 numbers and finds out the largest among the 3 numbers'''
# here we are testing your knowledge of comparing 2 numbers

def check_power(N, k):
    if N == k:
        return True
    try:
        return N == k**int(round(math.log(N, k)))
    except Exception:
        return False

check_power(25,30)