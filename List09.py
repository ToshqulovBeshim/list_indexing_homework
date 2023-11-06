def main(l):
    """
    A list of several elements is given. True if all items are the same, otherwise return False.
    Args:
        list1 (list): parameter
    Returns:
        bool: return answer
    """
    a=0
    for i in range(len(l)-1):
        
        if l[i]==l[i+1]:
            a+=1
    a==len(l)
    if a==(len(l)-1):
        return True      
    else :
        return False
print(main([1,0,1,1,1]))
        
            