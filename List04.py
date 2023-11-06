# def main(*l):
#     """
#     A list of several elements is given. Return the last item.
#     Args:
#         list1 (list): parameter
#     Returns:
#         list: return answer
#     """
#     return list(l)[-1]
# print(main(1,2,3,4,5,6,7))
print((lambda *l: list(l)[-1])(1,2,3,4,5,6,7))