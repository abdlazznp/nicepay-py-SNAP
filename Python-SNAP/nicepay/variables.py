class variables() :

    def __init__(self) :
        self.contentType = None
        self.endpointAccessToken = None
        self.xTimestampAccessToken = None
        self.xClientKeyAccessToken = None
        self.xSignatureAccessToken = None
        self.headerAccessToken = None
        self.bodyAccessToken =  None
        self.responseAccessToken = None
    
    def printAccessToken(self) :
        str = "\n------------------------------\n"
        str += "REQUEST ACCESS TOKEN"
        str += "------------------------------\n"
        str += f"\n Endpoint         : {self.endpointAccessToken}\n"
        str += "------------------------------\n"
        str += "Header \n"
        str += f"Content-Type         : {self.contentType}\n"
        str += f"X-TIMESTAMP          : {self.xTimestampAccessToken}\n"
        str += f"X-CLIENT-KEY         : {self.xClientKeyAccessToken}\n"
        str += f"X-SIGNATURE          : {self.xSignatureAccessToken}\n"
        str += "------------------------------\n"
        str += "Body \n"
        str += f"{self.bodyAccessToken}\n"
        str += "------------------------------\n"
        str += "RESPONSE ACCESS TOKEN\n"
        str += "------------------------------\n"
        str += "Response \n"
        str += f"{self.responseAccessToken}\n"
        str += "------------------------------\n"

        return str
    
    def printCreateVA(self) :
        str = "\n------------------------------\n"
        str += "REQUEST CREATE VIRTUAL ACCOUNT"
        str += "------------------------------\n"

    # def getContentType (self) :
    #     return self.contentType
    
    # def setContentType (self, contentType) :
    #     self.contentType = contentType

    # def getEndpointAccessToken (self) :
    #     return self.endpointAccessToken
    
    # def setEndpointAccessToken (self, endpointAccessToken) :
    #     self.endpointAccessToken = endpointAccessToken
    
    # def getXTimestampAccessToken (self) :
    #     return self.xTimestampAccessToken
    
    # def setXTimestampAccessToken (self, xTimestampAccessToken) :
    #     self.xTimestampAccessToken = xTimestampAccessToken
    
    # def getXClientKeyAccessToken (self) :
    #     return self.xClientKeyAccessToken
    
    # def setXClientKeyAccessToken (self, xClientKeyAccessToken) :
    #     self.xClientKeyAccessToken = xClientKeyAccessToken
    
    # def getXSignatureAccessToken (self) :
    #     return self.xSignatureAccessToken
    
    # def setXSignatureAccessToken (self, xSignatureAccessToken) :
    #     self.xSignatureAccessToken = xSignatureAccessToken

    # def getHeaderAccessToken (self) :
    #     return self.headerAccessToken
    
    # def setHeaderAccessToken (self, headerAccessToken) :
    #     self.headerAccessToken = headerAccessToken

    # def getBodyAccessToken (self) :
    #     return self.bodyAccessToken
    
    # def setBodyAccessToken (self, bodyAccessToken) :
    #     self.bodyAccessToken = bodyAccessToken

    