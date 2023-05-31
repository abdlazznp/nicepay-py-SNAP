from abc import ABC, abstractstaticmethod
from variables import variable

class accessTokenBulder() :

    def __init__(self) :
        self.project = variable()
        self.contentType = None
        self.endpointAccessToken = None
        self.xTimestampAccessToken = None
        self.xClientKeyAccessToken = None
        self.xSignatureAccessToken = None
        self.headerAccessToken = None
        self.bodyAccessToken =  None
    
    @abstractstaticmethod
    def item() :
        return accessTokenBulder()
    
    @abstractstaticmethod
    def setContentType (self, contentType) :
        self.contentType = contentType
        return self

    @abstractstaticmethod
    def setEndpointAccessToken (self, endpointAccessToken) :
        self.endpointAccessToken = endpointAccessToken
        return self
    
    @abstractstaticmethod
    def setXTimestampAccessToken (self, xTimestampAccessToken) :
        self.xTimestampAccessToken = xTimestampAccessToken
        return self
    
    @abstractstaticmethod
    def setXClientKeyAccessToken (self, xClientKeyAccessToken) :
        self.xClientKeyAccessToken = xClientKeyAccessToken
        return self
    
    @abstractstaticmethod
    def setXSignatureAccessToken (self, xSignatureAccessToken) :
        self.xSignatureAccessToken = xSignatureAccessToken
        return self
    
    @abstractstaticmethod
    def setHeaderAccessToken (self, headerAccessToken) :
        self.headerAccessToken = headerAccessToken
        return self
    
    @abstractstaticmethod
    def setBodyAccessToken (self, bodyAccessToken) :
        self.bodyAccessToken = bodyAccessToken
        return self
    
    def build(self) :
        return accessTokenBulder(self.contentType,
                                 self.endpointAccessToken,
                                 self.xTimestampAccessToken,
                                 self.xClientKeyAccessToken,
                                 self.xSignatureAccessToken,
                                 self.headerAccessToken,
                                 self.bodyAccessToken)