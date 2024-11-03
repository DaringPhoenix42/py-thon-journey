# def pattern(n):
#     for i in range(1, n+1):
#         for j in range(1, i+1):
#             print(i, end=' ')
#         print()

# pattern(5)

def pat2(n):

  def pattern(n):
    for i in range(1, n+1):
        print(" " * (n-i) + str(i) + " " * i)

def pat2(n):
    for i in range(1, n+1):
        print(" " * (n-i) + "* " * i)

def patt3(n):
    for i in range(1, n+1):
        print(" * " * (n-i) )

patt3(4)
# pat2(5)
