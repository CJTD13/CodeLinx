class fragment(object):
    def __init__(self, string):
        self.__string = string
        
    def __add__(self, other):
        if type(other) is link:
            return fragment(self.__string+'\n'+other.get_string())
    def __call__(self):
        return compile(self.__string,'<string>','exec')
    
    def get_string(self):
        return self.__string
    
    def set_string(self,newstring):
        self.__string = newstring
        
class link(object):
    def __init__(self,varlist):
        self.__vars = varlist
        self.__string = ''


    def __call__(self,**values):
        string = ''
        for x in self.__vars:
            if type(values[x]) is str:
                string += x+ ' = '+'"'+str(values[x])+'"'
            else:
                string += x +' = '+str(type(values[x]))[8:-2]+'('+ str(values[x])+')'
            string +='\n'
        init = fragment(string)
        executor = init+self
        return executor

    def __add__(self, other):
        if type(other) is link:
            return chain([self,other])
        elif type(other) is chain:
            return chain([self]+other.list)
        
    def get_string(self):
        return self.__string
    def get_vars(self):
        return self.__vars
    
    def set_string(self,newstring):
        self.__string = newstring
        
    def add_var(self,var):
        pass
    def remove_var(self,var):
        pass
    

class chain(object):
    def __init__(self,linklist):
        self.__list = linklist
        self.__varlist = []
        for i in self.__list:
            for j in i.get__vars():
                if j not in self.__list:
                    self.__varlist.append(j)

    def __call__(self, **values):
        init = ''
        for x in self.__varlist:
            init += x +' = '+ str(values[x])
            init +='\n'
        selfstring = ''
        for x in self.__list:
            selfstring+=x.get_string()
            selfstring +='\n'
        totstring = init+selfstring
        executor = fragment(totstring)
        return executor()
    
    def get_list(self):
        return self.__list
    def get_vars(self):
        return self.__varlist
    
    def add_link(self,link):
        pass
    def add_var(self,var):
        pass
    
    def remove_link(self,link):
        pass
    def remove_var(self,var):
        pass

class Bucket(object):
    def __init__(self):
        self.__funclist = {}

    def bindfunc(self,funcname,link):
        self.__funclist[funcname] = link
        setattr(self, funcname, link)

    def delfunc(self,func):
        delattr(self,func)

    def __call__(self,*funcs,**var):
        ans =[]
        for x in funcs:
            function = getattr(self,x)
            
    def get_funcs(self):
        return self.__funclist
             
