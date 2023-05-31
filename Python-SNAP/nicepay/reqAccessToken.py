from accessTokenBuilder import AccessTokenBulder

builder = AccessTokenBulder()
builder.setContentType("") \
        .setEndPointAccessToken("") \
        .setXTimestampAccessToken("") \
        .setXClientKeyAccessToken("") \
        .setXSignatureAccessToken("") \
        .setBodyAccessToken("") \
        .setResponseAccessToken("")
print(builder.getPrintAccessToken())