from Google import Create_Service
from googleapiclient.errors import HttpError
from datetime import datetime,timedelta
import pytz
from pytz import timezone
import discord

def run_bot(notification):
    try:
        TOKEN = "{YOUR_TOKEN}"
        client = discord.Client(intents=discord.Intents.default())
        @client.event
        async def on_ready():
            print(f'{client.user} is now running!')
            server = client.get_guild("{YOUR_SERVER_ID}")
            channel = server.get_channel("{YOUR_CHANNEL_ID}")
            await channel.send("```"+notification+"```")
            await client.close()
        client.run(TOKEN)
    except:
        print("Unable to Send Discord Message")

def audit_log(num_old_emails, before):
    date_format='%m/%d/%Y %H:%M:%S %Z'
    date = datetime.now(tz=pytz.utc)
    date = date.astimezone(timezone('US/Pacific'))
    fd = open("logfile.txt", 'a')
    fd.writelines(f'{date.strftime(date_format)} | You have '+str(num_old_emails)+' emails before the date: '+before+' archived to Trash. These will be deleted forever in 30 days.\n')
    fd.close()
    run_bot(f'{date.strftime(date_format)} | You have '+str(num_old_emails)+' emails before the date: '+before+' archived to Trash. These will be deleted forever in 30 days.\n')

def create_Google_service():
    SCOPES = ['https://mail.google.com/']
    return Create_Service(SCOPES)

def handler():
    try:
        service = create_Google_service()
        now = datetime.now(pytz.timezone('US/Pacific'))
        lasty = now - timedelta(hours=26298)
        next_page = None
        message_ids =[]
        while True:
            emails = service.users().messages().list(userId='me', pageToken=next_page, q='in:all before:{}'.format(lasty.strftime('%Y/%m/%d'))).execute()
            for messages in emails['messages']:
                if len(message_ids)<500:
                    message_ids.append(messages.get('id'))
                else:
                    break
            if len(message_ids)>=500:
                break
            next_page = emails.get('nextPageToken')
            if not next_page:
                break
        if message_ids:
            body={
                    'addLabelIds': ['TRASH'],
                    'ids':message_ids
                }
            service.users().messages().batchModify(userId='me', body=body).execute()
        audit_log(len(message_ids), format(lasty.strftime('%Y/%m/%d')))
        
    except HttpError as error:
        print("Error: "+f'{error}')

if __name__ == "__main__":
    handler()
