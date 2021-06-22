import timeit


def nested_join(r, s):
    pass

def sort_merge_join(r, s):
    pass

def hash_join(r, s):
    pass


if __name__ == '__main__':
    for i in range(1, 5):
        print("testcase"+str(i))
        print("-------------------------")
        with open("./testcase" + str(i),'r') as f:
            r = f.readline().split(',')
            s = f.readline().split(',')
            t1 = timeit.Timer('nested_join(r,s)', 'from __main__ import nested_join, r, s')
            t2 = timeit.Timer('sort_merge_join(r, s)', 'from __main__ import sort_merge_join, r, s')
            t3 = timeit.Timer('hash_join(r, s)', 'from __main__ import hash_join, r, s')
            print("run nested join time : ")
            print(t1.timeit())
            print("run sort merge join time: ")
            print(t2.timeit())
            print("run hash join time: ")
            print(t3.timeit())
        print("-------------------------")
