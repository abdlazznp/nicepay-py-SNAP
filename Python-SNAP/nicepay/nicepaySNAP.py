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
inquiryQRISEndpoint         = "/api/v1.0/qr/qr-mpm-query"
refundQRISEndpoint          = "/api/v1.0/qr/qr-mpm-refund"
createPayoutEndpoint        = "/api/v1.0/transfer/registration"
approvePayoutEndpoint       = "/api/v1.0/transfer/approve"
inquiryPayoutEndpoint       = "/api/v1.0/transfer/inquiry"
refundPayoutEndpoint        = "/api/v1.0/transfer/cancel"
rejectPayoutEndpoint        = "/api/v1.0/transfer/reject"
balanceInquiryPayoutEndpoint= "/api/v1.0/transfer/balance-inquiry"
method                      = "POST"

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

    # SIGNATURE CREATE DIRECT DEBIT
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

    # SIGNATURE INQUIRY DIRECT DEBIT
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
    print("INQUIRY DIRECT DEBIT")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()

def refundDirectDebit() :

    # SIGNATURE REFUND DIRECT DEBIT
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
    print("REFUND DIRECT DEBIT")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()


def createQRIS() :

    # SIGNATURE CREATE QRIS
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
    print("CREATE QRIS")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()

def inquiryQRIS() :

    # SIGNATURE INQUIRY QRIS
    clientSecret = setClientSecret
    authorization = "Bearer " + setAccessToken
    bodyCleanser = json.dumps(setBody)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{inquiryQRISEndpoint}:{setAccessToken}:{bodyHex}:{setXTimestamp}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + inquiryQRISEndpoint
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
    print("INQUIRY QRIS")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()

def refundQRIS() :

    # SIGNATURE REFUND QRIS
    clientSecret = setClientSecret
    authorization = "Bearer " + setAccessToken
    bodyCleanser = json.dumps(setBody)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{refundQRISEndpoint}:{setAccessToken}:{bodyHex}:{setXTimestamp}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + refundQRISEndpoint
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
    print("REFUND QRIS")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()

def createPayout() :

    # SIGNATURE CREATE PAYOUT
    clientSecret = setClientSecret
    authorization = "Bearer " + setAccessToken
    bodyCleanser = json.dumps(setBody)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{createPayoutEndpoint}:{setAccessToken}:{bodyHex}:{setXTimestamp}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + createPayoutEndpoint
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
    print("REQUEST PAYOUT")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()

def approvePayout() :

    # SIGNATURE APPROVE PAYOUT
    clientSecret = setClientSecret
    authorization = "Bearer " + setAccessToken
    bodyCleanser = json.dumps(setBody)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{approvePayoutEndpoint}:{setAccessToken}:{bodyHex}:{setXTimestamp}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + approvePayoutEndpoint
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
    print("APPROVE PAYOUT")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()


def inquiryPayout() :

    # SIGNATURE INQUIRY PAYOUT
    clientSecret = setClientSecret
    authorization = "Bearer " + setAccessToken
    bodyCleanser = json.dumps(setBody)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{inquiryPayoutEndpoint}:{setAccessToken}:{bodyHex}:{setXTimestamp}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + inquiryPayoutEndpoint
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
    print("INQUIRY PAYOUT")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()


def refundPayout() :

    # SIGNATURE REFUND PAYOUT
    clientSecret = setClientSecret
    authorization = "Bearer " + setAccessToken
    bodyCleanser = json.dumps(setBody)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{refundPayoutEndpoint}:{setAccessToken}:{bodyHex}:{setXTimestamp}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + refundPayoutEndpoint
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
    print("REFUND PAYOUT")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()

def rejectPayout() :

    # SIGNATURE REJECT PAYOUT
    clientSecret = setClientSecret
    authorization = "Bearer " + setAccessToken
    bodyCleanser = json.dumps(setBody)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{rejectPayoutEndpoint}:{setAccessToken}:{bodyHex}:{setXTimestamp}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + rejectPayoutEndpoint
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
    print("REJECT PAYOUT")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()


def balanceInquiryPayout() :

    # SIGNATURE BALANCE INQUIRY PAYOUT
    clientSecret = setClientSecret
    authorization = "Bearer " + setAccessToken
    bodyCleanser = json.dumps(setBody)
    bodyHashing = hashlib.sha256(bodyCleanser.encode())
    bodyHex = bodyHashing.hexdigest()

    StringToSign = f"{method}:{balanceInquiryPayoutEndpoint}:{setAccessToken}:{bodyHex}:{setXTimestamp}"
    encryptToHmacSHA512 = hmac.new(clientSecret.encode(), StringToSign.encode(), hashlib.sha512).digest()

    # DECLARE REQUEST
    url = host + balanceInquiryPayoutEndpoint
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
    print("BALANCE INQUIRY PAYOUT")
    print("-----------------------------")
    print(f"Header       : {header}")
    print("-----------------------------")
    print(f"Body         : {body}")
    print("-----------------------------")
    print(f"Response     : {response.json()}")
    print("-----------------------------")

    return ()