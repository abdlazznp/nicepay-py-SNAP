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

    def getProject(self) :
        return self.project.getProject()