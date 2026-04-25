import sys

def solve():
    seq = sys.stdin.read().strip()
    if not seq : return 
    res,count = 1,1
    for i in range(1,len(seq)):
        if seq[i]==seq[i-1]:
            count+=1
        else:
            res = max(res,count)
            count =1 
    print(max(res,count))

if __name__ == "__main__":
    solve()