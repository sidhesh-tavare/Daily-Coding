import sys

def solve():
    input_data = sys.stdin.read().split()
    if not input_data : return 
    t = int(input_data[0]) # no of test cases
    res = []
    for i in range(1,t*2,2):
        a,b = int(input_data[i]),int(input_data[i+1])

        if (a+b)%3 == 0 and min(a,b)*2>=max(a,b):
            res.append("YES")
        else: res.append("NO")
    sys.stdout.write("\n".join(res)+"\n")

if __name__ == "__main__":
    solve()

