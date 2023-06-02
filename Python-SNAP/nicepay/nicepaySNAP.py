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

global setAccessTokenInquiryVA
global setXClientIDInquiryVA
global setClientSecretInquiryVA
global setXExternalIDInquiryVA
global setXTimestampInquiryVA
global setXSignatureInquiryVA
global setChannelIDInquiryVA
global setBodyInquiryVA

global setAccessToken
global setXPartnerID
global setClientSecret
global setXExternalID
global setXTimestamp
global setXSignature
global setChannelID
global setOrigin
global setBody


host                        = "https://dev.nicepay.co.id/nicepay"
accessTokenEndpoint         = "/v1.0/access-token/b2b"
createVAEndpoint            = "/api/v1.0/transfer-va/create-va"
inquiryVAEndpoint           = "/api/v1.0/transfer-va/status"
directDebitEndpoint         = "/api/v1.0/debit/payment-host-to-host"
inquiryDirectDebitEndpoint  = "/api/v1.0/debit/status"
refundDirectDebitEndpoint   = "/api/v1.0/debit/refund"
createQRISEndpoint          = "/api/v1.0/qr/qr-mpm-generate"
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
    clientSecret = setClientSecret
    authorization = "Bearer " + setAccessToken
    bodyCleanser = json.dumps(setBody)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{createVAEndpoint}:{setAccessToken}:{bodyHex}:{setXTimestamp}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + createVAEndpoint
    header = {"Content-Type" : setContentType,
              "Authorization" : authorization,
              "X-TIMESTAMP" : setXTimestamp,
              "X-SIGNATURE" : base64.b64encode(encryptToHmacSHA512).decode(),
              "X-PARTNER-ID" : setXPartnerID,
              "X-EXTERNAL-ID" : setXExternalID,
              "CHANNEL-ID" : setChannelID
              }
    body = setBody
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
    clientSecret = setClientSecret
    authorization = "Bearer " + setAccessToken
    bodyCleanser = json.dumps(setBody)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{inquiryVAEndpoint}:{setAccessToken}:{bodyHex}:{setXTimestamp}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + inquiryVAEndpoint
    header = {"Content-Type": setContentType,
              "Authorization": authorization,
              "X-TIMESTAMP": setXTimestamp,
              "X-SIGNATURE": base64.b64encode(encryptToHmacSHA512).decode(),
              "X-PARTNER-ID": setXPartnerID,
              "X-EXTERNAL-ID": setXExternalID,
              "CHANNEL-ID": setChannelID
              }
    body = setBody
    response = requests.post(url= url, headers= header, json = body)

    # OUTPUT
    print("-----------------------------")
    print("VIRTUAL ACCOUNT INQUIRY")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()

def directDebit() :

    # SIGNATURE DIRECT DEBIT
    clientSecret = setClientSecret
    authorization = "Bearer " + setAccessToken
    bodyCleanser = json.dumps(setBody)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{directDebitEndpoint}:{setAccessToken}:{bodyHex}:{setXTimestamp}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + directDebitEndpoint
    header = {"Content-Type": setContentType,
              "Authorization": authorization,
              "X-TIMESTAMP": setXTimestamp,
              "X-SIGNATURE": base64.b64encode(encryptToHmacSHA512).decode(),
              "X-PARTNER-ID": setXPartnerID,
              "X-EXTERNAL-ID": setXExternalID,
              "CHANNEL-ID": setChannelID
              }
    body = setBody
    response = requests.post(url = url, headers = header, json = body)

    # OUTPUT
    print("-----------------------------")
    print("DIRECT DEBIT")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()

def inquiryDirectDebit() :

    # SIGNATURE DIRECT DEBIT
    clientSecret = setClientSecret
    authorization = "Bearer " + setAccessToken
    bodyCleanser = json.dumps(setBody)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{inquiryDirectDebitEndpoint}:{setAccessToken}:{bodyHex}:{setXTimestamp}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + inquiryDirectDebitEndpoint
    header = {"Content-Type": setContentType,
              "Authorization": authorization,
              "X-TIMESTAMP": setXTimestamp,
              "X-SIGNATURE": base64.b64encode(encryptToHmacSHA512).decode(),
              "X-PARTNER-ID": setXPartnerID,
              "X-EXTERNAL-ID": setXExternalID,
              "CHANNEL-ID": setChannelID
              }
    body = setBody
    response = requests.post(url=url, headers=header, json=body)

    # OUTPUT
    print("-----------------------------")
    print("DIRECT DEBIT")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()

def refundDirectDebit() :

    # SIGNATURE DIRECT DEBIT
    clientSecret = setClientSecret
    authorization = "Bearer " + setAccessToken
    bodyCleanser = json.dumps(setBody)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{refundDirectDebitEndpoint}:{setAccessToken}:{bodyHex}:{setXTimestamp}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + refundDirectDebitEndpoint
    header = {"Content-Type": setContentType,
              "Authorization": authorization,
              "X-TIMESTAMP": setXTimestamp,
              "X-SIGNATURE": base64.b64encode(encryptToHmacSHA512).decode(),
              "X-PARTNER-ID": setXPartnerID,
              "X-EXTERNAL-ID": setXExternalID,
              "CHANNEL-ID": setChannelID
              }
    body = setBody
    response = requests.post(url=url, headers=header, json=body)

    # OUTPUT
    print("-----------------------------")
    print("DIRECT DEBIT")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()


def createQRIS() :

    # SIGNATURE DIRECT DEBIT
    clientSecret = setClientSecret
    authorization = "Bearer " + setAccessToken
    bodyCleanser = json.dumps(setBody)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{createQRISEndpoint}:{setAccessToken}:{bodyHex}:{setXTimestamp}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + createQRISEndpoint
    header = {"Content-Type": setContentType,
              "Authorization": authorization,
              "X-TIMESTAMP": setXTimestamp,
              "X-SIGNATURE": base64.b64encode(encryptToHmacSHA512).decode(),
              "X-PARTNER-ID": setXPartnerID,
              "X-EXTERNAL-ID": setXExternalID,
              "CHANNEL-ID": setChannelID
              }
    body = setBody
    response = requests.post(url=url, headers=header, json=body)

    # OUTPUT
    print("-----------------------------")
    print("DIRECT DEBIT")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()