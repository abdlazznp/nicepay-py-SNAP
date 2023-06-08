from nicepay import nicepaySNAP
import datetime

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
nicepaySNAP.setContentType = "Application/JSON"
nicepaySNAP.setAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJJT05QQVlURVNUIiwiaXNzIjoiTklDRVBBWSIsIm5hbWUiOiJCTVJJIiwiZXhwIjoiMjAyMy0wNi0wOFQwMzoyNjowOFoifQ==.B1L7pzqRZWz7lY_10XqMyNKyO6Mj59WZL5-TY3sfqWY="
nicepaySNAP.setXTimestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
nicepaySNAP.setClientSecret = "33F49GnCMS1mFYlGXisbUDzVf2ATWCl9k3R++d5hDd3Frmuos/XLx8XhXpe+LDYAbpGKZYSwtlyyLOtS/8aD7A=="
nicepaySNAP.setXPartnerID = "IONPAYTEST"
nicepaySNAP.setXExternalID = "OrdNo" + timestamp
nicepaySNAP.setChannelID = "NICE"
nicepaySNAP.setOrigin = "www.nicepay.co.id"
nicepaySNAP.setBody = {
           "merchantId" : "IONPAYTEST",
           "msId" : "",
           "beneficiaryAccountNo" : "12355874912",
           "beneficiaryName" : "John Doe",
           "beneficiaryPhone" : "08123456789",
           "beneficiaryCustomerResidence" : "1",
           "beneficiaryCustomerType" : "1",
           "beneficiaryPostalCode" : "10200",
           "beneficiaryBankCode" : "BBBA",
           "payoutMethod" : "1",
           "amount" : {
               "value" : "10000.00",
               "currency" : "IDR"
           },
           "partnerReferenceNo" : "OrdNo" + timestamp,
           "reservedDt" : "",
           "reservedTm" : "",
           "deliveryId" : "",
           "deliveryName" : "Merchant's Name",
           "description" : "This Is The Description Of The Payment",
           "beneficiaryPOE" : "South Jakarta",
           "beneficiaryDOE" : "220101",
           "beneficiaryCoNo" : "12345JP",
           "beneficiaryAddress" : "Jln.Raya Kasablanka Kav.88",
           "beneficiaryAuthPhoneNumber" : "081623516151725378",
           "beneficiaryMerCategory" : "01",
           "beneficiaryCoMgmtName" : "John Doe",
           "beneficiaryCoShName" : ""
}

nicepaySNAP.createPayout()