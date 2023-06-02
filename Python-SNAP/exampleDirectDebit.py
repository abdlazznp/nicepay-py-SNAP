from nicepay import nicepaySNAP
import datetime

nicepaySNAP.setContentType = "Application/JSON"
nicepaySNAP.setAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJUTklDRUVXMDUxIiwiaXNzIjoiTklDRVBBWSIsIm5hbWUiOiJUTklDRUVXMDUxIiwiZXhwIjoiMjAyMy0wNi0wMVQwMzoyNTowNFoifQ==.QgWdY4ld-ZQry3NEfp7XGGmHFP6RGa00D2QXI6_bFmo="
nicepaySNAP.setXTimestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
nicepaySNAP.setClientSecret = "1af9014925cab04606b2e77a7536cb0d5c51353924a966e503953e010234108a"
nicepaySNAP.setXPartnerID = "TNICEEW051"
nicepaySNAP.setXExternalID = "OrdNo" + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
nicepaySNAP.setChannelID = "NICE"
nicepaySNAP.setBody = {
    "partnerReferenceNo": "ref202305081205331683522921",
    "merchantId": "TNICEEW051",
    "subMerchantId": "",
    "externalStoreId": "",
    "validUpTo": "",
    "pointOfInitiation": "Mobile App",
    "amount": {
        "value": "100.00",
        "currency": "IDR"
    },
    "urlParam": [
        {
            "url": "https://webhook.site/e15ef201-98a9-428c-85d4-a0c6458939c3",
            "type": "PAY_NOTIFY",
            "isDeeplink": "Y"
        },
        {
            "url": "https://www.nicepay.co.id/IONPAY_CLIENT/paymentResult.jsp",
            "type": "PAY_RETURN",
            "isDeeplink": "Y"
        }
    ],
    "additionalInfo": {
        "mitraCd": "DANA",
        "goodsNm": "Merchant Goods 1",
        "billingNm": "John Doe",
        "billingPhone": "08123456789",
        "cartData": "{\"count\":\"2\",\"item\":[{\"img_url\":\"http://img.aaa.com/ima1.jpg\",\"goods_name\":\"Item 1 Name\",\"goods_detail\":\"Item 1 Detail\",\"goods_amt\":\"0.00\",\"goods_quantity\":\"1\"},{\"img_url\":\"http://img.aaa.com/ima2.jpg\",\"goods_name\":\"Item 2 Name\",\"goods_detail\":\"Item 2 Detail\",\"goods_amt\":\"100.00\",\"goods_quantity\":\"1\"}]}",
        "dbProcessUrl": "https://webhook.site/e15ef201-98a9-428c-85d4-a0c6458939c3",
        "callBackUrl": "https://www.nicepay.co.id/IONPAY_CLIENT/paymentResult.jsp",
        "msId" : "data"
    }
}

nicepaySNAP.directDebit()