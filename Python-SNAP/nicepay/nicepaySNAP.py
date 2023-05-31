import base64
import datetime
import requests
import json
import socket
import hashlib
import hmac
# import urllib.parse as urlparse
# import http.client as httplib
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256

global setContentType
global setPrivateKey
global setXClientIDAccessToken
global setXTimestampAccessToken
global setBodyAccessToken

global setAccessTokenCreateVA
global setXClientIDCreateVA
global setClientSecretCreateVA
global setXExternalIDCreateVA
global setXTimestampCreateVA
global setChannelIDCreateVA
global setBodyCreateVA

global setAccessTokenInquiryVA
global setXClientIDInquiryVA
global setClientSecretInquiryVA
global setXExternalIDInquiryVA
global setXTimestampInquiryVA
global setXSignatureInquiryVA
global setChannelIDInquiryVA
global setBodyInquiryVA


host                    = "https://dev.nicepay.co.id/nicepay"
accessTokenEndpoint     = "/v1.0/access-token/b2b"
createVAEndpoint        = "/api/v1.0/transfer-va/create-va"
inquiryVAEndpoint       = "/api/v1.0/transfer-va/status"
method                  = "POST"

def genAccessToken() :
    
    # PRIVATE KEY
    privateKeyString = f"""-----BEGIN RSA PRIVATE KEY-----
    {setPrivateKey}
    -----END RSA PRIVATE KEY-----"""
    privateKey = RSA.importKey(privateKeyString)

    # ASSIGN VALUE
    StringToSign = f"{setXClientIDAccessToken}|{setXTimestampAccessToken}"
    privateKeySigner = PKCS115_SigScheme(privateKey)
    xSignatureAccessToken = privateKeySigner.sign(SHA256.new(StringToSign.encode()))

    # DECLARE REQUEST
    url = host + accessTokenEndpoint
    header = {"Content-Type" : setContentType,
              "X-TIMESTAMP" : setXTimestampAccessToken,
              "X-CLIENT-KEY" : setXClientIDAccessToken,
              "X-SIGNATURE" : base64.b64encode(xSignatureAccessToken).decode(),
              }
    body = setBodyAccessToken
    response = requests.post(url = url, headers = header, json = body)

    # OUTPUT
    print("-----------------------------")
    print("REQUEST ACCESS TOKEN")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------") 

    return()
    
def createVA() :
    
    # SIGNATURE CREATE VIRTUAL ACCOUNT
    clientSecret = setClientSecretCreateVA
    authorization = "Bearer " + setAccessTokenCreateVA
    bodyCleanser = json.dumps(setBodyCreateVA)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{createVAEndpoint}:{setAccessTokenCreateVA}:{bodyHex}:{setXTimestampCreateVA}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + createVAEndpoint
    header = {"Content-Type" : setContentType,
              "Authorization" : authorization,
              "X-TIMESTAMP" : setXTimestampCreateVA,
              "X-SIGNATURE" : base64.b64encode(encryptToHmacSHA512).decode(),
              "X-PARTNER-ID" : setXClientIDCreateVA,
              "X-EXTERNAL-ID" : setXExternalIDCreateVA,
              "CHANNEL-ID" : setChannelIDCreateVA
              }
    body = setBodyCreateVA
    response = requests.post(url = url, headers = header, json = body)

    # OUTPUT
    print("-----------------------------")
    print("CREATE VIRTUAL ACCOUNT")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------") 

    return()

def inquiryVA() :

    # SIGNATURE INQUIRY VIRTUAL ACCOUNT
    clientSecret = setClientSecretInquiryVA
    authorization = "Bearer " + setAccessTokenInquiryVA
    bodyCleanser = json.dumps(setBodyInquiryVA)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{inquiryVAEndpoint}:{setAccessTokenInquiryVA}:{bodyHex}:{setXTimestampInquiryVA}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + inquiryVAEndpoint
    header = {"Content-Type": setContentType,
              "Authorization": authorization,
              "X-TIMESTAMP": setXTimestampInquiryVA,
              "X-SIGNATURE": base64.b64encode(encryptToHmacSHA512).decode(),
              "X-PARTNER-ID": setXClientIDInquiryVA,
              "X-EXTERNAL-ID": setXExternalIDInquiryVA,
              "CHANNEL-ID": setChannelIDInquiryVA
              }
    body = setBodyInquiryVA
    response = requests.post(url= url, headers= header, json = body)

    # OUTPUT
    print("-----------------------------")
    print("VIRTUAL ACCOUNT INQUIRY")
    print("-----------------------------")
    print(StringToSign)
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()

def directDebit() :
    print("NGENGGGGG!")