def push(a,n):
    a.append(n)
    print('ok')

def pop(a):
    if len(a)>0:
        print(a.pop([0]))
    else:
        print('error')

def front(a):
    if len(a)>0:
        print(a[0])
    else:
        print('error')
    
def size(a):
    print(len(a))

def clear(a):
    a.clear()
    print('ok')
a=[]
word=list(iter(input, 'exit'))

for i in word:
    if 'size' in i:
        size(a)
    elif 'pop' in i:
        pop(a)
    elif 'front' in i:
        front(a)
    elif 'clear' in i:
        clear(a)
    else:        
        push(a,i.split()[-1])
    
print('bye')