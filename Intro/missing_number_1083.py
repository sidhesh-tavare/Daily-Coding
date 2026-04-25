import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data : return 
    n = int(input_data[0])
    exp_sum = (n*(n+1))//2
    act_sum = sum(map(int,input_data[1:]))
    print(exp_sum-act_sum)

if __name__ == "__main__":
    solve()