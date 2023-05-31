import base64
import datetime
import requests
from nicepay.getVariabels import AccessTokenBulder
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256

builder = AccessTokenBulder()

#Declare Value Parameters
timeStamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
endPoint = "https://dev.nicepay.co.id/nicepay/v1.0/access-token/b2b"
contentType = "Application/JSON"
xClientKey = "TNICEVA022"
header = {"Content-Type" : contentType, "X-TIMESTAMP" : timeStamp, "X-CLIENT-KEY" : xClientKey}
body = {
    "grantType" : "client_credentials",
    "additionalInfo" : {
    }
}

builder.setendpointAccessToken(endPoint)
builder.setContentType(contentType)
builder.setxTimestampAccessToken(timeStamp)
builder.setxClientKeyAccessToken(xClientKey)
builder.setxSignatureAccessToken("ZfH0mZmrQseBaV5jzyA4K1CsMQPLBOPkJvgcT2Q/RKUNq2We4wzTZ/tmQinrkgKIqtyj/7JYKXP0xdhWjf4R4w==")
builder.setBodyAccessToken(body)

# builder = setResponseAccessToken(requests.post(url=endPoint))
# builder.buildProject()
print()
print(builder.getProject())