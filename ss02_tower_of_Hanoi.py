A = [3, 2, 1]
B = []
C = []

def move(n, source, target, auxiliary):
    if n > 0:
        move(n - 1, source, auxiliary, target)
        #move n-1 disks from source to auxiliary, so they are out of the way

        target.append(source.pop())
        #move the nth disk from source to target

        print(A, B, C, '###', sep='\n')
        #display our progress

        move(n - 1, auxiliary, target, source)
        #move the n-1 disks that we left on auxiliary onto target

move(3, A, C, B)
#initiate call from source A to target C with auxiliary B   

    