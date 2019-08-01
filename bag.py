from collections import defaultdict
from goody import type_as_str
import prompt

# Submitter: whsieh2(Hsieh, Wesley)
# Partner  : chanycl(Cho, Chan)
# We certify that we worked cooperatively on this programming
#   assignment, according to the rules for pair programming

class Bag:
    def __init__(self, values: [str]):
        self.values = values
        self.dict = {}
        for x in values: 
            if x in self.dict.keys():
                self.dict[x] += 1
            else:
                self.dict[x] = 1
        #print(self.dict)
        
    def __repr__(self):
        yolo = ''
        for x in self.dict.keys():
            for i in range(0,self.dict[x]):
                yolo += '\'' + str(x) + '\''
                
        #print(yolo)
        return yolo
                
    def __str__(self):
        #yolo2 = 'Bag({}[{}])'.format(self.dict.keys(), self.dict[value])
        '''yolo2 = 'Bag('
        for key in self.dict.keys():
            yolo2 += str(key) + '[' + str(self.dict[key]) + ']'
        yolo2 += ')'
        return yolo2'''
    
        return "Bag({})".format(','.join(str(c) + '[' + str(v) + ']' for c,v in self.dict.items()))
    
    def __len__(self):
        return len(self.values)
        '''count = 0   
        for i in self.values:
            count += 1  
        return count'''

    def __contains__(self, arg):
        return (arg in self.values)
    
    def __eq__(self, Bag):
        return (self.dict() == Bag.dict())
    
    def __ne__(self, Bag):
        return (self.dict() != Bag.dict())
    
    def __iter__(self):
        pass 
    
    #come back to this later ??

    def __add__(self, bag1): 
        b3 = Bag([])       
        lst = b3.add(self.values, bag1.values)
        b3.__init__(lst)

        return b3
    
    def unique(self):
        return len(self.dict.keys())

    def count(self,arg):
        if self.dict[arg] != 0:
            return self.dict[arg]
        else:
            return 0
            
    def add(self, arg1, arg2):
        return arg1+arg2
    
    def remove(self, arg):
        self.values.remove(arg)
        
        self.dict[arg] -= 1
        if self.dict[arg] == 0:
            del self.dict[arg]
        else: 
            #create new list 
            #re-initialize self.values
            pass
    
if __name__ == '__main__':
    
    #Simple tests before running driver
    #Put your own test code here to test Bag before doing the bsc tests
    #Debugging problems with these tests is simpler

    b = Bag(['d','a','d','b','c','b','d'])
    print(b.__str__())
    print(repr(b))
    #v = value, c = count
    print(all((repr(b).count('\''+v+'\'')==c for v,c in dict(a=1,b=2,c=1,d=3).items())))
    for i in b:
        print(i)

    b2 = Bag(['a','a','b','x','d'])
    print(repr(b2+b2))
    print(str(b2+b2))
    print([repr(b2+b2).count('\''+v+'\'') for v in 'abdx'])
    b = Bag(['a','b','a'])
    print(repr(b))
    print()
    
    import driver
    driver.default_file_name = 'bscp21F18.txt'
#     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
#     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
#     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
