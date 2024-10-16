class arrays:
    def __init__(self,a:list[int],k :int):
        self.a = a
        self.k = k
    def rotate(self)->list[int]:
        i = self.k%len(self.a) #O(1)
        ret = self.a[i:]+self.a[:i] #O(n) creating new list
        return ret
    
if __name__ == "__main__":
    a = [1,2,3,4,5]
    k = 2
    obj = arrays(a,k)
    print(obj.rotate())

    #TC : O(n) due to iterating and slicing of list of size n
    #SC : O(n) due to creation of new list

    
