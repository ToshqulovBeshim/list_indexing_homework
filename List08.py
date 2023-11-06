def main(l):
    """
    A list of ones and zeros, five in length, is given. replace one with True, replace zeros with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    for i in range(len(l)):
        if l[i]==1:
            l[i]=True
        else:
            l[i]=False
    return l
print(main([1,1,1,0,0,0]))