s = "Hello World"

# Queue
# w
# o
# r
# l
# d

# h
# e
# l
# l
# o

def arr_app():

    result = [w for w in s.split()][::-1]

    print(" ".join(result))

# from queue import Queue

# def queue_app():
#     st = ""
#     q = Queue(maxsize=len(s))
#     for i in range(len(s), 0, -1):
#         q.put(s[i-1])
    
#     while not q.empty():
#         st += q.get()
    
#     print(st)


# queue_app()
