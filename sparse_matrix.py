import prompt

class Sparse_Matrix:
    def __init__(self, row, col, *args):
        #print(row, col)
        self.args = args #(0,0,0)
        #print(self.args)
               
        if type(row) == int:
            if row > 0:
                self.rows = row 
            else: 
                raise AssertionError
        else:
            raise AssertionError
        
        if type(col) == int:
            if col > 0:
                self.cols = col
            else: 
                raise AssertionError
        else:
            raise AssertionError
        
        self._valid_rows = [i for i in range(0,row)]
        #print('row',self._valid_rows)
        self._valid_cols = [i for i in range(0,col)]
        #print('cols', self._valid_cols)
        
        self.matrix = {}
        self.matrixl = [[0 for x in range(col)] for y in range(row)]
        #print(self.matrixl)
        for x in args: 
            if (x[0], x[1]) not in self.matrix.keys():
                if (x[0] in self._valid_rows) and (x[1] in self._valid_cols) and (type(x[2]) == int or type(x[2]) == float): 
                    self.matrix[(x[0], x[1])] = x[2]
                    self.matrixl[x[0]][x[1]] = x[2]
                else: 
                    raise AssertionError
            else:
                raise AssertionError
        #self.matrix = {(x[0], x[1]):x[2] for x in args}
        #print('dict', self.matrix, 'list', self.matrixl)

    # I have written str(...) because it is used in the bsc.txt file and
    #   it is a bit subtle to get correct. This function does not depend
    #   on any other method in this class being written correctly, although
    #   it could be simplified by writing self[...] which calls __getitem__.   
    def __str__(self):
        size = str(self.rows)+'x'+str(self.cols)
        width = max(len(str(self.matrix.get((r,c),0))) for c in range(self.cols) for r in range(self.rows))
        return size+':['+('\n'+(2+len(size))*' ').join ('  '.join('{num: >{width}}'.format(num=self.matrix.get((r,c),0),width=width) for c in range(self.cols))\
                                                                                             for r in range(self.rows))+']'
    def __len__(self):
        #verify if type is SM or dict 
        return self.rows * self.cols
        
    def __bool__(self):
        return not self.matrix == {}
    
    def size(self):
        return (self.rows, self.cols)
    
    def __repr__(self):
        #return "Sparse_Matrix({})".format(','.join(str(self.rows) +',' +  str(self.cols) + str(x) for x in self.args))
        return "Sparse_Matrix(" + str(self.rows) +  "," + str(self.cols) + ',' + ','.join(str(x) for x in self.args) + ')'
    
    def __getitem__(self, t): 
        #print('t', t, len(t))
        #print(self._valid_rows, self._valid_rows)
        if type(t) == tuple and len(t) == 2:
            if t[0] <0 or t[1] < 0:
                raise TypeError
            else: 
                if t[0] in self._valid_rows and t[1] in self._valid_cols:
                    return self.matrixl[t[0]][t[1]]
                else: 
                    raise TypeError
        else:
            raise TypeError


    def __setitem__(self, t, value):
        #print(value)
        if type(value) == int or type(value) == float:   
            if type(t) == tuple and value == int or float and len(t) == 2:
                if t[0] in self._valid_rows and t[1] in self._valid_cols:
                    if value == 0:
                        self.matrixl[t[0]][t[1]] = value
                        self.__delitem__(t)
                    else:
                        self.matrixl[t[0]][t[1]] = value
                else:
                        raise TypeError
            else:
                raise TypeError
        else:
            raise TypeError


    def __delitem__(self, t):
        if type(t) == tuple:
            if t[0] in self._valid_rows or t[1] in self._valid_cols:
                self.matrixl[t[0]][t[1]] = 0
                self.matrix.pop(t)
                #self.matrix.del[(t[0],t[1])]
        else:
            raise TypeError
    
    def row(self, r):
        if r in self._valid_rows:
            return tuple([x for x in self.matrixl[r]])      
        else:
            raise AssertionError
        
    def col(self,c):
        if c in self._valid_cols:    
            lst = []
            for i in range(0, self.rows):
                lst.append(self.matrixl[i][c])
       
            return tuple(lst)
        else:
            raise AssertionError

    def details(self):
        det = str(self.rows) + 'x' + str(self.cols) + ' -> ' + str(self.matrix) + ' -> (' 
        for i in range(0, self.rows):
            det += str(self.row(i))
        det += ")"

        return det
    
    def __call__(self, int1, int2):
        #print('in call')
        #print(int1, int2)
        #print(self)
        if int1 > 0 and int2 > 0:
            matrix = {}
            matrixl = [[0 for x in range(int1)] for y in range(int2)]
            for i in range(0, int1):
                for j in range(0, int2):
                    if i >= self.rows or j >= self.cols: 
                        matrixl[i][j] = 0
                    else:#print(self.matrixl[i][j], self.matrix[(i,j)])
                        matrixl[i][j] = self.matrixl[i][j]
                        if (i,j) in self.matrix.keys():
                            matrix[(i,j)] = self.matrix[(i,j)]
                    
            self.matrix = matrix 
            self.matrixl = matrixl
            self._valid_cols = [x for x in range(0,int2)]
            self._valid_rows = [x for x in range(0, int1)]
            self.rows = int1 
            self.cols = int2
            
            args = []            
            for key in self.matrix:
                if self.matrix[key] != 0:
                    args.append((key[0], key[1], self.matrix[key]))
            self.args = args
        else:
            raise AssertionError
        
    def __pos__(self):
        #print('in pos')
        args =[]
        for key in self.matrix.keys():
            args.append((key[0], key[1], self.matrix[key]))
        
        return Sparse_Matrix(self.rows, self.cols, *args)
    
    def __neg__(self):
        args = []
        for key in self.matrix.keys():
            args.append((key[0], key[1], (-1)*self.matrix[key]))
        
        return Sparse_Matrix(self.rows, self.cols, *args)
        
    def __add__(self, matrix2):
        #print(matrix2, 'in add')
        if type(matrix2) == int: 
            args = []
            for i in range(0,self.rows):
                for j in range(0,self.cols):
                    args.append((i,j,self.matrix[i][j] + matrix2))
                    
            return Sparse_Matrix(self.rows, self.cols, args)
        elif type(matrix2) == Sparse_Matrix:   
            #print(self, '\n', matrix2)
            args = []
            if self.rows == matrix2.rows and self.cols == matrix2.cols: 
                for i in range(0, self.rows):
                    for j in range(0, self.cols):
                        if self.matrixl[i][j] + matrix2.matrixl[i][j] != 0:
                            args.append((i, j, self.matrixl[i][j] + matrix2.matrixl[i][j]))
                           
                return Sparse_Matrix(self.rows, self.cols, *args)
            else: 
                raise AssertionError
        else:
            raise TypeError
    
    def __sub__(self, matrix2):
        #print(matrix2, 'in sub')
        if type(matrix2) == int: 
            args = []
            for i in range(0,self.rows):
                for j in range(0,self.cols):
                    args.append((i,j,self.matrix[i][j] - 1))
                    
            return Sparse_Matrix(self.rows, self.cols, args)
        elif type(matrix2) == Sparse_Matrix:
            args = []
            if self.rows == matrix2.rows and self.cols == matrix2.cols: 
                for i in range(0, self.rows):
                    for j in range(0, self.cols):
                        if self.matrixl[i][j] - matrix2.matrixl[i][j] != 0:
                            args.append((i, j, self.matrixl[i][j] - matrix2.matrixl[i][j]))
                       
                return Sparse_Matrix(self.rows, self.cols, *args)
        else: 
            raise TypeError
        
    def __mul__(self, value):
        #print(self, value)
        args = []
        if type(value) == int: 
            #print('is int')
            for i in range(0, self.rows):
                for j in range(0, self.cols):
                    #print(self.matrixl[i][j]*value)
                    if self.matrixl[i][j]*value != 0:
                        args.append((i,j,self.matrixl[i][j]*value))
            print(args)
            x = Sparse_Matrix(self.rows, self.cols, *args)
            print(len(x.matrix))
            return Sparse_Matrix(self.rows, self.cols, *args)
        elif type(value) == Sparse_Matrix:  #### this is wrong come ack later and cry later TT_TT
            #print(self)
            #print(self.rows, value.cols, self.cols, value.rows)
            if self.rows == value.cols and self.cols == value.rows:
                for i in range(0, self.rows): #grab a row
                    for j in range(0, value.cols): #grab a column
                        num = 0
                        for k in range(0, len(self.row(i))):
                            #print(self.__row__(i)[k], value.__col__(j)[k])
                            num += self.row(i)[k] * value.col(j)[k]
                        if num != 0:
                            #print(num)
                            args.append((i,j, num))
                return Sparse_Matrix(self.rows, value.cols, *args)
            else:
                raise AssertionError
        else:
            raise TypeError
        
    def __abs__(self):
        #print('in abs')
        args =[]
        for i in range(0, self.rows):
            for j in range(0, self.cols):
                args.append((i,j,abs(self.matrixl[i][j])))
        return Sparse_Matrix(self.rows, self.cols, *args)
    
    def __eq__(self, arg):
        #print(arg)
        if type(arg) == Sparse_Matrix:
            if self.rows == arg.rows and self.cols == arg.cols:
                if len(self.args) == len(arg.args):
                    for i in range(0, len(self.args)):
                        if self.args[i] != arg.args[i]:
                            return False
                    return True
                else: 
                    return False
            else: 
                return False
        elif type(arg) == int or type(arg) == float: 
            if arg == 0: 
                if len(self.matrix) == 0:
                    return True
                else: 
                    return False
            else: #if any other value  
                #print('arg', arg)
                for i in range(0, self.rows):
                    for j in range(0, self.cols):
                        if self.matrixl[i][j] != arg: 
                            return False      
                return True
        else: 
            return False
        
    def __ne__(self, arg):
        if self.__eq__(arg)== True: 
            return False
        else: 
            return True
    
    def __pow__(self, value):
        if type(value) == int: 
            #print("is int")
            if self.rows == self.cols and value >= 1: #start recursion?                  
                #i cry 
                if value == 1:
                    return self
                else:
                    x = self
                    for i in range(value, 1, -1):
                        x *= self
                        #print(x)
                    return x
            else: 
                raise AssertionError
        else: 
            raise TypeError
        
if __name__ == '__main__':
    
    #Simple tests before running driver
    #Put your own test code here to test Sparse_Matrix before doing the bsc tests
    #Debugging problems with these tests is simpler

    print('Printing')
    m = Sparse_Matrix(3,3, (0,0,1),(1,1,3),(2,2,1))
    z = Sparse_Matrix(3,3, (0,0,2),(1,1,3),(2,2,2))
    y = z + m
    x = m- z

    #print('y', y)
    #print('x', x)

    m1 = Sparse_Matrix(2,2, (0,0,-1),(0,1,-6),(1,0,-1),(1,1,-6))
    m2 = Sparse_Matrix(2,2, (0,0,4),(0,1,1),(1,0,4),(1,1,1))
    #print('m1', m1)
    '''you = m1.__repr__()
    print('you' ,you)
    print(type(you))'''
    print(abs(m1))
    #print('m2', m2)
    m3 = m1*m2
    #print('m3', m3)
    m4 = m1*2
    #print('m4', m4)
    
    print('testing power')
    m5 = m1**4
    print('m5', m5)

    print(m)
    print(repr(m))
    print(m.details())
  
    print('\nlen and size')
    print(len(m), m.size())
    
    print('\ngetitem and setitem')
    print(m[1,1])
    m[1,1] = 0
    m[0,1] = 2
    print(m.details())

    '''print('\niterator')
    for r,c,v in m:
        print((r,c),v)
    
    print('\nm, m+m, m+1, m==m, m==1')
    print(m)
    print(m+m)
    print(m+1)
    print(m==m)
    print(m==1)
    print()'''
    
    import driver
    driver.default_file_name = 'bscp22F18.txt'
#     driver.default_show_exception = prompt.for_bool('Show exceptions when testing',True)
#     driver.default_show_exception_message = prompt.for_bool('Show exception messages when testing',True)
#     driver.default_show_traceback = prompt.for_bool('Show traceback when testing',True)
    driver.driver()
