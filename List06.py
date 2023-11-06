def main(l):
    """
    A list of units and zeros with a length of five is given. Replace one with True.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    for i in range(len(l)):
        
        if l[i]==1:
            l[i]=True
    return l

print(main(l=[1,1,1,0]))
