from abc import ABC, abstractstaticmethod

class ProjectBuilder(ABC):
    
    @abstractstaticmethod
    def setName(self, name) :
        pass

    @abstractstaticmethod
    def setDescription(self, description) :
        pass

    @abstractstaticmethod
    def setFramework(self, framework) :
        pass

    @abstractstaticmethod
    def setLanguage(self, language) : 
        pass

    @abstractstaticmethod
    def setPattern(self, pattern) : 
        pass
