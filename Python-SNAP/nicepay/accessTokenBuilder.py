from variableBuilder import variableBuilder
from variables import variables

class AccessTokenBulder(variableBuilder) :
    def __init__ (self) :
        self.variable = variables()

    def setContentType (self, contentType) :
        self.variable.contentType = contentType
        return self

    def setEndPointAccessToken (self, endpointAccessToken) :
        self.variable.endpointAccessToken = endpointAccessToken
        return self
    
    def setXTimestampAccessToken (self, xTimestampAccessToken) :
        self.variable.xTimestampAccessToken = xTimestampAccessToken
        return self

    def setXClientKeyAccessToken (self, xClientKeyAccessToken) :
        self.variable.xClientKeyAccessToken = xClientKeyAccessToken
        return self

    def setXSignatureAccessToken (self, xSignatureAccessToken) :
        self.variable.xSignatureAccessToken = xSignatureAccessToken
        return self
    
    def setHeaderAccessToken (self, headerAccessToken) :
        self.variable.headerAccessToken = headerAccessToken
        return self
    
    def setBodyAccessToken (self, bodyAccessToken) :
        self.variable.bodyAccessToken = bodyAccessToken
        return self
    
    def setResponseAccessToken (self, responseAccessToken) :
        self.variable.responseAccessToken = responseAccessToken
        return self
    
    def getPrintAccessToken (self) :
        return self.variable.printAccessToken()
    
        # self.contentType = None
        # self.endpointAccessToken = None
        # self.xTimestampAccessToken = None
        # self.xClientKeyAccessToken = None
        # self.xSignatureAccessToken = None
        # self.headerAccessToken = None
        # self.bodyAccessToken =  None
        # self.responseAccessToken = None
    
