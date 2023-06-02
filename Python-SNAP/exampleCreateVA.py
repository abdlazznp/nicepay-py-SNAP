from nicepay import nicepaySNAP
import datetime

nicepaySNAP.setContentType = "Application/JSON"
nicepaySNAP.setAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUTklDRVZBMDIyIiwiaXNzIjoiTklDRVBBWSIsIm5hbWUiOiJUTklDRVZBMDIyIiwiZXhwIjoiMjAyMy0wNi0wMlQwMToxMDo1MVoifQ==.64-GnyUzO-zCRInZYZhd5ljcvFtKg141xe2omAsy-KQ="
nicepaySNAP.setXTimestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
nicepaySNAP.setClientSecret = "1af9014925cab04606b2e77a7536cb0d5c51353924a966e503953e010234108a"
nicepaySNAP.setXPartnerID = "TNICEVA022"
nicepaySNAP.setXExternalID = "OrdNo" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
nicepaySNAP.setChannelID = "NICE"
nicepaySNAP.setBody = {
    "partnerServiceId":"",
    "customerNo":"000666",
    "virtualAccountNo":"",
    "virtualAccountName":"John Doe",
    "trxId":"MerchantReferenceNo001",
    "totalAmount":{
        "value":"10000.00",
        "currency":"IDR"
    },
    "additionalInfo":{
        "bankCd": "CENA",
        "goodsNm": "Merchant Goods 1",
        "dbProcessUrl": "https://webhook.site/e15ef201-98a9-428c-85d4-a0c6458939c3",
        "vacctValidDt":"",
        "vacctValidTm":"",
        "msId":"",
        "msFee":"",
        "msFeeType":"",
        "mbFee":"",
        "mbFeeType":""
    }
}

nicepaySNAP.createVA()