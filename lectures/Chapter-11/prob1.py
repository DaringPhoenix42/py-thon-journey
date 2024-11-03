class twoDVector:
      def __init__(self,i,j):
            self.i=i
            self.j=j
      def show(self):
            print(f"The vector is {self.i}i + {self.j}j")
      def __add__(self,other):
            return twoDVector(self.i+other.i,self.j+other.j)
        
class treeDvector(twoDVector):
    def __init__(self, i, j, k):
          super().__init__(i, j)
          self.k = k
    def show(self):
            print(f"The vector is {self.i}i + {self.j}j + {self.k}k")
    def __add__(self, other):
            return treeDvector(self.i + other.i, self.j + other.j, self.k + other.k)
        
v1=twoDVector(3,4)
v2=twoDVector(2,1)
v3=treeDvector(1,2,3)
v4=treeDvector(4,5,6)
v5=v1+v2
v6=v3+v4
v5.show()
v6.show()
