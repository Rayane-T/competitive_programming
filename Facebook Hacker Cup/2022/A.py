def sol(K,N,S):
    l1, l2, l_v1, l_v2 = [], [], [], []
    if (K < N/2):
        return False
    for e in range(0,K):    # Put elements in 2 lists (cases)
        l1.append(S[e])
    for k in range(K,N):
        l2.append(S[k])
    l1.sort()
    l2.sort()
    l1_init_len = len(l1)
    l2_init_len = len(l2)
    #Check if occurence in l1
    for i in range(l1_init_len):
        if l1.count(l1[i]) > 2: #Check if more than 2 occurences
            return False
        elif l1.count(l1[i]) > 1:
            if l1[i] not in l2:
                l2.append(l1[i])
                l1.pop(i)
        else:
            l_v1.append(l1[i])
    #Check if occurence in l2
    for j in range(l2_init_len):
        if l2.count(l2[j]) > 2: #Check if more than 2 occurences
            return False
        elif l2.count(l2[j]) > 1:
            if l2[j] not in l1: #check sup to exchange element from l2 to l1
                l1.append(l2[j])
                l2.pop(j)
        else:
            l_v2.append(l2[j])
    return True

with open('second_hands_input.txt', 'r') as f:
    S, N, K, k, T, Lines = [], 0, 0, 0, f.readline(), f.readlines()
    for i in range(len(Lines)):
        if (i%2 == 0):
            tmp = Lines[i].split()
            N = int(tmp[0])
            K = int(tmp[1])
        elif(i%2 == 1):
            k += 1
            S = [eval(i) for i in Lines[i].split()]
            if sol(K,N,S) == True:
                print("Case #"+str(k)+": YES")
            if sol(K,N,S) == False:
                print("Case #"+str(k)+": NO")
