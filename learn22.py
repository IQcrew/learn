x=2*int(input())
print(*[(" x"*i*2).center(x*2) if i<=x/2 else (" x"*((x-i+1)*2)).center(x*2) for i in range(1,x+1)],sep="\n")