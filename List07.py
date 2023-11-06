def main(l):
    """
    A list of units and zeros with a length of five is given. Replace zero with False.
    Args:
        list1 (list): parameter
    Returns:
        list: return answer
    """
    for i in range(len(l)):
        if l[i]==0:
            l[i]=False
    return l
print(main(l=[1,1,1,0,0,0,]))