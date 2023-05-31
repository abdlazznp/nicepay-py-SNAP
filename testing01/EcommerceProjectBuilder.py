from ProjectBuilder import ProjectBuilder
from Project import Project

class ECommerceProjectBulder(ProjectBuilder) :
    def __init__(self):
        self.project = Project()
    
    def setName(self):
        self.project.name = "E-Commerce Web Apps"
        return self
    
    def setDescription(self):
        self.project.description = "E-Commerce Web App With Cool Features!"
        return self
    
    def setFramework(self, framework):
        self.project.framework = framework
        return self
    
    def setLanguage(self, language):
        self.project.lang = language
        return self
    
    def setPattern(self, pattern):
        self.project.pattern = pattern
        return self
    
    def buildProject(self):
        self.setName()
        self.setDescription()
    
    def getProject(self):
        return self.project.getProject()
    
