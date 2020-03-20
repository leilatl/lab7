#1
print("Hello, World!")

#2
if __name__ == '__main__':
    n = int(input().strip())
if(n%2!=0): print("Weird")
elif(n>2 and n<5): print("Not Weird")
elif(n>6 and n<=20): print("Weird")
else: print("Not Weird")

#3
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a+b)
print(a-b)
print(a*b)

#4
if __name__ == '__main__':
    a = int(input())
    b = int(input())
print(a//b)
print(a/b)

if __name__ == '__main__':
    n = int(input())
for i in range (0, n):
    print(i*i)

#5
if __name__ == '__main__':
    n = int(input())

print(*range(1, n+1), sep='')

#6
if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())
print ([[a,b,c] for a in range(0,x+1) 
                for b in range(0,y+1) 
                for c in range(0,z+1) 
                if a + b + c != n ])

#7
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())


listnew=[]

for i in arr:

     if i not in listnew:

                listnew.append(i)

listnew.sort(reverse=True)

print(listnew[1])

#8
marksheet = []
for _ in range(0,int(input())):
    marksheet.append([input(), float(input())])

#9
second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
print('\n'.join([a for a,b in sorted(marksheet) if b == second_highest]))

#10
def print_full_name(a, b):
    print("Hello "+a+" "+b+"! You just delved into python.")
