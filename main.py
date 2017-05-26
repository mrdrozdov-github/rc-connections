from __future__ import print_function
import gspread
from oauth2client.client import SignedJwtAssertionCredentials
import pandas as pd
import json


SCOPE = ["https://spreadsheets.google.com/feeds"]
SECRETS_FILE = "./rc-mentor-97cc1526452c.json"
SPREADSHEET = "RC Mentor Demo (Mentee) (Responses)"

# Load Credentials from JSON file
json_key = json.load(open(SECRETS_FILE))

# Authenticate using the signed key
credentials = SignedJwtAssertionCredentials(json_key['client_email'],
                                            json_key['private_key'], SCOPE)

# Google Auth Access
gc = gspread.authorize(credentials)

print("The following sheets are available")
for sheet in gc.openall():
    print("{} - {}".format(sheet.title, sheet.id))

# Open spreadsheet using its name (can also use its id if available)
workbook = gc.open(SPREADSHEET)

# Get the first sheet
_sheet = workbook.sheet1

# Load into dataframe
data = pd.DataFrame(_sheet.get_all_records())

# Print to stdout
print(data)
