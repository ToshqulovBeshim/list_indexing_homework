# def main(l,i):
#     """
#     A list of several elements is given. i Return the item in the index.
#     Args:
#         list1 (list): parameter
#         i (int): parameter
#     Returns:
#         list: return answer
#     """
#     return l[i]
# l=[1,2,3,4,5,6,7]
# i=3
# print(main(l,i))
print((lambda i, *l: list(l)[i])(3, 1,2,3,4,5,6,7))