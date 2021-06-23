import timeit

def nested_join(r, s):
    res = []
    for x in r:
        for y in s:
            if x == y:
                res.append([x,y])
    #print(res)

def sorted_merge_join(r, s):
    r.sort()
    s.sort()
    res = []
    i = 0
    j = 0
    while i < len(r) and j < len(s):
        cur = s[j]
        tmp = [cur]
        j += 1
        done = False
        while not done and j < len(s):
            newcur= s[j]
            if cur == newcur:
                tmp.append(newcur)
                j += 1
            else:
                done = True
        while i < len(r) and r[i] < cur:
            i += 1
        while i < len(r) and r[i] == cur:
            for e in tmp:
                res.append([r[i], e])
            i += 1

    #print(res)

def hash_join(r, s):
    res = []
    hashtabler = {}
    for x in r:
        if x%7 not in hashtabler: # 使用x%7来计算hash值
            hashtabler[x%7] = []
        hashtabler[x%7].append(x)

    hashtables = {}
    for x in s:
        if x % 7 not in hashtables:
            hashtables[x % 7] = []
        hashtables[x % 7].append(x)

    for x,y in hashtabler.items():
        for z in hashtables[x]:
            for t in y:
                if z == t: # 可能会发生冲突,所以一个分区里的值并不一定全部相同
                    res.append([t,t])
    #print(res)


if __name__ == '__main__':
    for i in range(1, 5):
        print("testcase"+str(i))
        print("-------------------------")
        with open("./testcase" + str(i),'r') as f:
            tmpr = f.readline().split(',')
            r = [int(x.strip()) for x in tmpr]
            tmps = f.readline().split(',')
            s = [int(x.strip()) for x in tmps]
            if len(r) > len(s) :
                r, s = s, r

            t1 = timeit.Timer('nested_join(r,s)', 'from __main__ import nested_join, r, s')
            print("run nested join time:     ", end='')
            print(t1.timeit())

            t2 = timeit.Timer('sorted_merge_join(r, s)', 'from __main__ import sorted_merge_join, r, s')
            print("run sorted merge join time: ", end='')
            print(t2.timeit())

            t3 = timeit.Timer('hash_join(r, s)', 'from __main__ import hash_join, r, s')
            print("run hash join time:       ", end='')
            print(t3.timeit())
        print("-------------------------")
