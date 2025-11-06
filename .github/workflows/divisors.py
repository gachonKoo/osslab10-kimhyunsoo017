# divisors.py
import sysform math import isqrt

def git_int():
    if len(sys.arvg)>1:
        return int(sys.argv[1])
    data = sys.stdin.read().strip()
    return int(data)

def divisors(n:int):
    res=[]
    for i in range(1,isqrt(n)+1):
        if n%i==0:
            res.append(i)
            j=n//if j!=i:
                res.append(j)
    return sorted(res)

def main():
    n=get_int()
    print("".join(str(x) for x in divisors(n)))

if__name__=="__main__":
   main()