import base64
import datetime
import requests
import json
import socket
import urllib.parse as urlparse
import http.client as httplib
from Crypto.PublicKey import RSA
from Crypto.Signature.pkcs1_15 import PKCS115_SigScheme
from Crypto.Hash import SHA256

class genSignatureAccessToken :

    # NICEPAY PRIVATE KEY
    nicepayPrivateKey = "MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAInJe1G22R2fMchIE6BjtYRqyMj6lurP/zq6vy79WaiGKt0Fxs4q3Ab4ifmOXd97ynS5f0JRfIqakXDcV/e2rx9bFdsS2HORY7o5At7D5E3tkyNM9smI/7dk8d3O0fyeZyrmPMySghzgkR3oMEDW1TCD5q63Hh/oq0LKZ/4Jjcb9AgMBAAECgYA4Boz2NPsjaE+9uFECrohoR2NNFVe4Msr8/mIuoSWLuMJFDMxBmHvO+dBggNr6vEMeIy7zsF6LnT32PiImv0mFRY5fRD5iLAAlIdh8ux9NXDIHgyera/PW4nyMaz2uC67MRm7uhCTKfDAJK7LXqrNVDlIBFdweH5uzmrPBn77foQJBAMPCnCzR9vIfqbk7gQaA0hVnXL3qBQPMmHaeIk0BMAfXTVq37PUfryo+80XXgEP1mN/e7f10GDUPFiVw6Wfwz38CQQC0L+xoxraftGnwFcVN1cK/MwqGS+DYNXnddo7Hu3+RShUjCz5E5NzVWH5yHu0E0Zt3sdYD2t7u7HSr9wn96OeDAkEApzB6eb0JD1kDd3PeilNTGXyhtIE9rzT5sbT0zpeJEelL44LaGa/pxkblNm0K2v/ShMC8uY6Bbi9oVqnMbj04uQJAJDIgTmfkla5bPZRR/zG6nkf1jEa/0w7i/R7szaiXlqsIFfMTPimvRtgxBmG6ASbOETxTHpEgCWTMhyLoCe54WwJATmPDSXk4APUQNvX5rr5OSfGWEOo67cKBvp5Wst+tpvc6AbIJeiRFlKF4fXYTb6HtiuulgwQNePuvlzlt2Q8hqQ=="
    privateKeyString = f"""-----BEGIN RSA PRIVATE KEY-----
    {nicepayPrivateKey}
    -----END RSA PRIVATE KEY-----"""

    # READING PRIVATE KEY TO LIB
    privateKey = RSA.importKey(privateKeyString)

    # GET VALUE VARIABLES
    xClientId = "TNICEVA022"
    print("X-CLIENT-ID      : " + xClientId)
    xTimestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
    print("X-TIMESTAMP      : " + xTimestamp)
    stringToSign = f"{xClientId}|{xTimestamp}"
    print("StringToSign     : " + stringToSign)
    privateKeySigner = PKCS115_SigScheme(privateKey)
    xSignature = privateKeySigner.sign(SHA256.new(stringToSign.encode()))
    print("Signature        : " + base64.b64encode(xSignature).decode())


    # REQUEST ACCESS TOKEN
    host = "https://dev.nicepay.co.id"
    endpoint = "/nicepay/v1.0/access-token/b2b"
    url = host + endpoint
    header = {"Content-Type" : "Application/JSON",
              "X-TIMESTAMP" : xTimestamp,
              "X-CLIENT-KEY" : xClientId,
              "X-SIGNATURE" : base64.b64encode(xSignature).decode(),
              }
    body = {
            "grantType" : "client_credentials"
            }
    
    print("Header       : ") 
    print(header)
    print("Body         : ") 
    print(body.items())
    
    response = requests.post(url = url, headers = header, json = body)
    nResponse = response.json()
    print(nResponse)

# data = f"{clientId}|{timestamp}"
# hash = SHA256.new(data.encode())
# signer = PKCS115_SigScheme(private_key)
# signature = signer.sign(hash)
# print("Signature:", base64.b64encode(signature).decode())
    