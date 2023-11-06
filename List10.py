def main(list_num):
    """
    A list of numbers consisting of several elements is given. Return the largest between the first and last elements.
    Args:
        list_num (list): parameter
    Returns:
        int: return answer
    """
    ma=0
    for i in range(1,len(list_num)-1):
        if ma<=list_num[i]:
            ma=list_num[i]
    return ma
print(main([78,3,42,5,6,7,234]))