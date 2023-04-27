#1
class A:
    def __init__(self, v1) -> None:
        self.f1 = "*" * v1
    
    def __add__(self, v1):
        return A(self.f1 + "*" * v1)
    
l=A(6)
ll= l + 6
print(ll)



