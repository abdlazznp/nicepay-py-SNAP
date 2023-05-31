from abc import ABC, abstractstaticmethod

class variableBuilder(ABC) :

    @abstractstaticmethod
    def setendpointAccessToken (self, endpointAccessToken) :
        pass

    @abstractstaticmethod
    def setContentType (self, contentType) :
        pass

    @abstractstaticmethod
    def setxTimestampAccessToken (self, xTimestampAccessToken) :
        pass

    @abstractstaticmethod
    def setxClientKeyAccessToken (self, xClientKeyAccessToken) :
        pass

    @abstractstaticmethod
    def setxSignatureAccessToken (self, xSignatureAccessToken) :
        pass
    
    @abstractstaticmethod
    def setHeaderAccessToken (self, headerAccessToken) :
        pass
    
    @abstractstaticmethod
    def setBodyAccessToken (self, bodyAccessToken) :
        pass

    @abstractstaticmethod
    def setResponseAccessToken (self, responseAccessToken) :
        pass