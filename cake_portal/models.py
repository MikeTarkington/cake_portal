# from django.db import models
# from __future__ import print_function
# from datetime import timedelta
# import datetime
# import pprint
# import pickle
# import os.path
# from googleapiclient.discovery import build
# from google_auth_oauthlib.flow import InstalledAppFlow
# from google.auth.transport.requests import Request

# class Googlecal(models.Model):
#     # api call to check someone's availability at a particular time frame


#     # api call to pull all of someone's calendar events from a time range
#     # If modifying these scopes, delete the file token.pickle.
#     SCOPES = ['https://www.googleapis.com/auth/calendar.readonly']


#     def main():

#         # prettier priting of json
#         pp = pprint.PrettyPrinter(indent=4)

#         creds = None
#         # The file token.pickle stores the user's access and refresh tokens, and is
#         # created automatically when the authorization flow completes for the first
#         # time.
#         if os.path.exists('token.pickle'):
#             with open('token.pickle', 'rb') as token:
#                 creds = pickle.load(token)
#         # If there are no (valid) credentials available, let the user log in.
#         if not creds or not creds.valid:
#             if creds and creds.expired and creds.refresh_token:
#                 creds.refresh(Request())
#             else:
#                 flow = InstalledAppFlow.from_client_secrets_file(
#                     'credentials.json', SCOPES)
#                 creds = flow.run_local_server(port=0)
#             # Save the credentials for the next run
#             with open('token.pickle', 'wb') as token:
#                 pickle.dump(creds, token)

#         cal_list_service = build('calendar', 'v3', credentials=creds)
#         # event_list_service = build('calendar', 'v3', credentials=creds)
#         free_busy_service = build('calendar', 'v3', credentials=creds)

#         # will need to account for non user specific calendars somehow...
#         # perhaps by checking the id for @datadoghq.com domain using regex
#         # theoretically, this could be a moot point if the subset of email domains
#         # filtered by SE timezone and MRR etc, will narrow this call and have us search
#         # calendar IDs based on their emails (assuming that's how their cal IDS are assigned)
#         calendars = cal_list_service.calendarList().list().execute()
#         # pp.pprint(calendars['items'])
#         # now = datetime.datetime.utcnow().isoformat() + 'Z'  # 'Z' indicates UTC time
#         now = datetime.datetime.utcnow()
#         later = now + timedelta(hours=4)
#         now = now.isoformat() + 'Z'
#         later = later.isoformat() + 'Z'

#         print(now)
#         print(later)

#         # for each calendar check if the user has events during that time frame
#         for cal in calendars['items']:
#             cal_id = cal['id'].encode('utf8')
#             req_body = {
#                 "timeMin": now,
#                 "timeMax": later,
#                 "items": [
#                     {
#                         "id": cal_id
#                     }
#                 ]
#             }
#             available = free_busy_service.freebusy().query(body=req_body).execute()
#             print(available)

            # events = event_list_service.events().list(
            #     calenderId=cal_id,
            #     timeMin=).execute()
