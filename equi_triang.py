#This python scirpt print like below(triangle line == n)
#
#                   *
#                 *   *
#               *   *   *
#             *   *   *   *
#           *   *   *   *   *
#         *   *   *   *   *   *
#       *   *   *   *   *   *   *
#     *   *   *   *   *   *   *   *
#   *   *   *   *   *   *   *   *   *
def tri(n):
    s = 2*n
    for i in range(1,n+1):
        sp = s*" "
        for j in range(i):
            if j == 0:
               print(sp,"*",end='')
            else:
               print(" "*2,"*",end='')
        s=s-2
        print()
tri(9)
