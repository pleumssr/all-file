def putQueen(r,b,colFree,upFree,downFree):
    global N
    global numSol
    for c in range(N):
        if colFree[c] and upFree[r+c] and downFree[r-c+(N-1)]:
            b[r] = c
            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 0
            if r == N-1:
                print(b)
                numSol +=1
            else:
                putQueen(r+1,b,colFree,upFree,downFree)
            colFree[c] = upFree[r+c] = downFree[r-c+N-1] = 1

N = int(input('enter n:'))
numSol = 0
colFree = N*[1] #(c) check
upFree =(2*N-1)*[1] #(r+c) check
downFree =(2*N-1)*[1] #(r-c+(N-1)) check
board=N*[-1] #board array[1]

putQueen(0,board,colFree,upFree,downFree)



