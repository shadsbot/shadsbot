class User(object):
        def __init__(self, name, pl=0):
                self.name = name
                self.pl = pl
        def powerlevel(self):
                return self.pl
        def setpl(self, pl):
                self.pl = pl
#                print('%(name)s\'s powerlevel was set to %(level)i' % \
#                      {"name": self.name, "level": self.pl})
                return self.pl
        def addpl(self):
                self.pl = self.pl + 1
                return self.pl
