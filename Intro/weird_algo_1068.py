import sys 

def solve():
    input_data = sys.stdin.read().split()
    if not input_data : return 
    num = int(input_data[0])
    res = [num]
    while num!=1:
        if num%2==0: num = num //2
        else: num = num*3+1
        res.append(num)
    sys.stdout.write(" ".join(map(str,res))+"\n")

if __name__ == "__main__":
    solve()