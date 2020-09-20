class fragment(object):
    def __init__(self, string):
        self.string = string
    def __add__(self, other):
        if type(other) is link:
            return fragment(self.string+'\n'+other.string)
    def __call__(self):
        return compile(self.string,'<string>','exec')
        
class link(object):
    def __init__(self,varlist):
        self.vars = varlist
        self.string = ''


    def __call__(self,**values):
        string = ''
        for x in self.vars:
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

class chain(object):
    def __init__(self,linklist):
        self.list = linklist
        self.varlist = []
        for i in self.list:
            for j in i.varlist:
                if j not in self.list:
                    self.varlist.append(j)

    def __call__(self, **values):
        init = ''
        for x in self.varlist:
            init += x +' = '+ str(values[x])
            init +='\n'
        selfstring = ''
        for x in self.list:
            self.string+=x.string
            self.string +='\n'
        totstring = init+selfstring
        executor = fragment(totstring)
        return executor()

class Bucket(object):
    def __init__(self):
        self.list = {}

    def bindfunc(self,funcname,link):
        self.list[funcname] = link
        setattr(self, funcname, link)

    def delfunc(self,func):
        delattr(self,func)

    def __call__(self,*funcs,**var):
        ans =[]
        for x in funcs:
            function = getattr(self,x)
             
