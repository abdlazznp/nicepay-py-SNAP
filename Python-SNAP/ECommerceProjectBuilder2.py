from ProjectBuilder import ProjectBuilder
from Project import Project

class AccessTokenBulder(ProjectBuilder) :
    def __init__(self) :
        self.project = Project()

    def setendpointAccessToken (self, endpointAccessToken) :
        self.project.endpointAccessToken = endpointAccessToken
        return self
    
    def setContentType (self, contentType) :
        self.project.contentType = contentType
        return self

    def setxTimestampAccessToken (self, xTimestampAccessToken) :
        self.project.xTimestampAccessToken = xTimestampAccessToken
        return self
    
    def setxClientKeyAccessToken (self, xClientKeyAccessToken) :
        self.project.xClientKeyAccessToken = xClientKeyAccessToken
        return self

    def setxSignatureAccessToken (self, xSignatureAccessToken) :
        self.project.xSignatureAccessToken = xSignatureAccessToken
        return self
    
    def setBodyAccessToken (self, bodyAccessToken) :
        self.project.bodyAccessToken = bodyAccessToken
        return self
    
    def setResponseAccessToken (self, responseAccessToken) :
        self.project.responseAccessToken = responseAccessToken
        return self
    
    # def setName(self) :
    #     self.project.name = "E-Commerce Web App"
    #     return self
    
    # def setDescription(self) :
    #     self.project.description = "Blablablabla Gitu Lah"
    #     return self
    
    # def setFramework(self, framework) :
    #     self.project.framework = framework
    #     return self
    
    # def setLanguage(self, language) :
    #     self.project.lang = language
    #     return self
    
    # def setPattern(self, pattern) : 
    #     self.project.pattern = pattern
    #     return self
    
    # def buildProject(self) :
    #     self.setName()
    #     self.setDescription()

    def getProject(self) :
        return self.project.getProject()