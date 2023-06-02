from nicepay import nicepaySNAP
import datetime

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
nicepaySNAP.setContentType = "Application/JSON"
nicepaySNAP.setAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJJT05QQVlURVNUIiwiaXNzIjoiTklDRVBBWSIsIm5hbWUiOiJCQkJBIiwiZXhwIjoiMjAyMy0wNi0wMlQwMTowMToxN1oifQ==.p66ooqmoRBEXUeefYU_WiQS5bp1W63y73ZTaMxh0Q5Q="
nicepaySNAP.setXTimestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
nicepaySNAP.setClientSecret = "1af9014925cab04606b2e77a7536cb0d5c51353924a966e503953e010234108a"
nicepaySNAP.setXPartnerID = "IONPAYTEST"
nicepaySNAP.setXExternalID = "OrdNo" + timestamp
nicepaySNAP.setChannelID = "NICE"
nicepaySNAP.setOrigin = "www.nicepay.co.id"
nicepaySNAP.setBody = {
        "merchantId" : "IONPAYTEST",
        "partnerReferenceNo" : "OrdNo" + timestamp,
        "storeId" : "NICEPAY",
        "validityPeriod" : "",
        "additionalInfo" : {
            "goodsNm" : "Merchant Goods 1",
            "billingNm" : "John Doe",
            "billingPhone" : "08123456789",
            "billingEmail" : "john.doe@example.com",
			"billingAddr" : "Jln. Raya Casablanka Kav.88",
            "billingCity" : "South Jakarta",
            "billingState" : "DKI Jakarta",
			"billingCountry" : "Indonesia",
			"billingPostCd" : "10200",
			"callBackUrl" : "https://www.nicepay.co.id/IONPAY_CLIENT/paymentResult.jsp",
			"dbProcessUrl" : "https://webhook.site/e15ef201-98a9-428c-85d4-a0c6458939c3",
			"userIP" : "127.0.0.1",
			"cartData" : "{\"count\":1,\"item\":[{\"img_url\":\"https://d3nevzfk7ii3be.cloudfront.net/igi/vOrGHXlovukA566A.medium\",\"goods_name\":\"Nokia 3360\",\"goods_detail\":\"Old Nokia 3360\",\"goods_amt\":\"100\",\"goods_quantity\":\"1\"}]}",
			"mitraCd" : "QSHP"
        },
		"amount" : {
			"value" : "100.00",
			"currency" : "IDR"
		}
}

nicepaySNAP.createQRIS()