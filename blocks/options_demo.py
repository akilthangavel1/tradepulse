from fyers_apiv3 import fyersModel


client_id = "MMKQTWNJH3-100"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE3MzIyNjcyNDEsImV4cCI6MTczMjMyMTg0MSwibmJmIjoxNzMyMjY3MjQxLCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCblFFenBiNTdldG1FNmRTMEkzMGVSMWNyZ2c5dEpmV0cxUU1ScG9Wd1VBLW9iNGJYMlRlWlcwaTU0VEZsSGRYTFdvOWlJWk5ETnQtSGJXYjN5eXJZZ1FQTTlnejg3bWlBOVVOSHgyaDhzbFoydDJiVT0iLCJkaXNwbGF5X25hbWUiOiJBS0lMIFRIQU5HQVZFTCIsIm9tcyI6IksxIiwiaHNtX2tleSI6ImJlY2M0NDU4NmZjN2MyOTFhMWZjYTAwZmVjMjA2YmQ0MjNiOThlZDRiYWY4Mjc3YjZhMWI5Y2U2IiwiZnlfaWQiOiJZQTI5Mzk2IiwiYXBwVHlwZSI6MTAwLCJwb2FfZmxhZyI6Ik4ifQ.2VpaWj-Nf6nwwQrsiZDj9Pp_VILLR6eVzPjWSCBDe3k"
# Initialize the FyersModel instance with your client_id, access_token, and enable async mode
fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")
data = {
    "symbol":"NSE:SBIN-EQ",
    "strikecount":1,
    "timestamp": ""
}
response = fyers.optionchain(data=data);
print(response)
