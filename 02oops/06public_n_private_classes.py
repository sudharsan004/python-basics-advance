# There is not really a public or private class in python, but we may do it in a pseudo way
# _className is private
class _privateClass(object):
    def __init__(self,name) :
        self.name = name


# normal class
class publicClass(object):
    def __init__(self,name) :
        self.name = name
