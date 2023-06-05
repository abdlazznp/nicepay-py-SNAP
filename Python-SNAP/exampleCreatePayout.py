from nicepay import nicepaySNAP
import datetime

timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
nicepaySNAP.setContentType = "Application/JSON"
nicepaySNAP.setAccessToken = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJJT05QQVlURVNUIiwiaXNzIjoiTklDRVBBWSIsIm5hbWUiOiJCTVJJIiwiZXhwIjoiMjAyMy0wNi0wNVQwMjo0MzoxNVoifQ==.ds3KKBRkZ-d5PcPTSnIhDO5m1sldqHfhxHihiqHiJrI="
nicepaySNAP.setXTimestamp = datetime.datetime.now().strftime("%Y-%m-%dT%H:%M:%S")+"+07:00"
nicepaySNAP.setClientSecret = "33F49GnCMS1mFYlGXisbUDzVf2ATWCl9k3R++d5hDd3Frmuos/XLx8XhXpe+LDYAbpGKZYSwtlyyLOtS/8aD7A=="
nicepaySNAP.setXPartnerID = "IONPAYTEST"
nicepaySNAP.setXExternalID = "OrdNo" + timestamp
nicepaySNAP.setChannelID = "NICE"
nicepaySNAP.setOrigin = "www.nicepay.co.id"
nicepaySNAP.setBody = {
 "merchantId":"IONPAYTEST",
 "msId":"",
 "beneficiaryAccountNo":"12355874912",
 "beneficiaryName":"tes",
 "beneficiaryPhone":"084124899843",
 "beneficiaryCustomerResidence":"1",
 "beneficiaryCustomerType":"1",
 "beneficiaryPostalCode":"123456",
 "payoutMethod":"1",
 "beneficiaryBankCode":"BBBA",
  "amount":{
     "value":"30000.00",
     "currency":"IDR"
   },
 "partnerReferenceNo":"1233456467412e213",
 "reservedDt":"",
 "reservedTm":"",
 "deliveryId":"",
 "deliveryName":"Ciki",
 "description":"This is test Request",
  "beneficiaryPOE": "Kota Administrasi Jakarta Selatan",
  "beneficiaryDOE": "220101",
  "beneficiaryCoNo": "12345JP",
  "beneficiaryAddress": "Jl. Hong Gil Dong 88",
  "beneficiaryAuthPhoneNumber": "081623516151725378",
  "beneficiaryMerCategory": "01",
  "beneficiaryCoMgmtName": "John Doe",
  "beneficiaryCoShName": ""
}

nicepaySNAP.createPayout()