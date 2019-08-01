import re, traceback, keyword

def pnamedtuple(type_name, field_names, mutable= False):
    print(type_name, field_names)
    def show_listing(s):
        for line_num, line_text in enumerate(s.split('\n'), 1):
            print(f' {line_num: >3} {line_text.rstrip()}')

    # put your code here
    # bind class_definition (used below) to the string constructed for the class
    class_template = '''\
class {}: 
    def __init__(self, *args):
        self._arg = args
        
    def __repr__(self):
        return '{}(','.join(self._arg))'
        
    def __str__(self):
        return '{}(','.join(self._arg))'
        
    def __getitem__(self, arg):
        pass
        
    def __eq__(self, other):
        if type(other) == type(self): 
            return True
        return False
        
    def __replace(self, **kargs):
        if self._mutable: 
            print(kargs)
        else: 
            return blah 
        
    #def __setattr__(self, arg):
        #pass 
'''
            
    # While debugging, remove comment below showing source code for the class
    # show_listing(class_definition)
    class_definition = \
        class_template.format(type_name, type_name, type_name)
        
    #print(class_definition)
    
    # Execute this class_definition str in a local name space; then, bind the
    #   source_code attribute to class_defintion; after that try, return the
    #   class object created; if there is a syntax error, list the class and
    #   also show the error
    name_space = dict(__name__  =  f'pnamedtuple_{type_name}')
    try:
        exec(class_definition,name_space)
        name_space[type_name].source_code = class_definition
    except (TypeError,SyntaxError):   
        show_listing(class_definition)
        traceback.print_exc()
    #
    #print(name_space[type_name])
    return name_space[type_name]

    
if __name__ == '__main__':
    # Test pnamedtuple in script below: use Point = pnamedtuple('Point','x,y')

    Point = pnamedtuple('Point', 'x,y')
    #print(Point.__dict__)
    p = Point(0,0)
    print(p._arg)
    
    #driver tests
    import driver
    driver.default_file_name = 'bscp3S18.txt'
#     driver.default_show_exception= True
#     driver.default_show_exception_message= True
#     driver.default_show_traceback= True
    driver.driver()
