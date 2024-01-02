import httplib2
import apiclient.discovery
from oauth2client.service_account import ServiceAccountCredentials

CREDENTIALS_FILE = 'nanostroi/creds.json'
# spreadsheet_id = '1EIYCsVrtzEXBanFAov3b0xK1nJNjAy2SWl_P4HXXS6w'
spreadsheet_id = '17Wp4QmlaSk65Z1x_irI_KqHFzmYkEhfWxFQafTPXgKQ'

credentials = ServiceAccountCredentials.from_json_keyfile_name(
    CREDENTIALS_FILE,
    ['https://www.googleapis.com/auth/spreadsheets',
     'https://www.googleapis.com/auth/drive']
)
httpAuth = credentials.authorize(httplib2.Http())
service = apiclient.discovery.build('sheets', 'v4', http = httpAuth)

values = service.spreadsheets().values().get(
    spreadsheetId = spreadsheet_id,
    range = "'Roland бытовые'!F8",
    majorDimension = 'ROWS'
).execute()
print(values)
# exit()
