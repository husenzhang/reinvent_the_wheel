def top_k(num_list, k):
    """return largest k numbers from a list"""
    from collections import Counter
    res = [item for item, _ in Counter(num_list).most_common(k)]
    return res

if __name__ == '__main__':
    from random import randint
    for _ in range(3):
        lst = [randint(1, 5) for _ in range(10)]
        print(lst,top_k(lst, 3))
         
    
        
    
