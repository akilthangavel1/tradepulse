from fyers_apiv3 import fyersModel


client_id = "MMKQTWNJH3-100"
access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJhcGkuZnllcnMuaW4iLCJpYXQiOjE3MzI2MTU4MDYsImV4cCI6MTczMjY2NzQwNiwibmJmIjoxNzMyNjE1ODA2LCJhdWQiOlsieDowIiwieDoxIiwieDoyIiwiZDoxIiwiZDoyIiwieDoxIiwieDowIl0sInN1YiI6ImFjY2Vzc190b2tlbiIsImF0X2hhc2giOiJnQUFBQUFCblJaNS1TalB3YjRJZDBFc2FiQmxXa055aXcySF9RcHl3RThOSWVaUnhaN2Njd2dPZnpFU20zNU1NYndoTFdLNGowd1RmSV9ZcndNcmdmRkRJRktfbnh6ZDZRak9FNnRUS3Q3Rm9YTTRIcUhtd2daST0iLCJkaXNwbGF5X25hbWUiOiJBS0lMIFRIQU5HQVZFTCIsIm9tcyI6IksxIiwiaHNtX2tleSI6ImJlY2M0NDU4NmZjN2MyOTFhMWZjYTAwZmVjMjA2YmQ0MjNiOThlZDRiYWY4Mjc3YjZhMWI5Y2U2IiwiZnlfaWQiOiJZQTI5Mzk2IiwiYXBwVHlwZSI6MTAwLCJwb2FfZmxhZyI6Ik4ifQ.0cK5wI5E2LswjtSnv7oqrXxSYcTpCUQg1FhZd-7rzhA"
    
def get_option_chain_data(symbol):
    fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")
    data = {
        "symbol":symbol,
        "strikecount":25,
        "timestamp": ""
    }
    response = fyers.optionchain(data=data);
    return response


def get_option_quotes(symbol_quotes):
    fyers = fyersModel.FyersModel(client_id=client_id, token=access_token,is_async=False, log_path="")

    data = {
        "symbols":symbol_quotes
    }

    response = fyers.quotes(data=data)
    return response
