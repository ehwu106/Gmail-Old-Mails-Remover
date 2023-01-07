# Gmail: Old Email Remover Service
Python service that interacts with Gmail API to retrieve old emails 3 years ago from the date of runtime and archive them to Trash. A discord notification will be sent out with the amount of emails that were archived and how much days you'll have to retrieve them if you do so choose to keep them. Maximum amount of retrieval is 500 emails per request. I have this app running on a cloud run app in Google Cloud Console being trigger by a Cloud Scheduler to run bi-weekly to automate the process of cleaning out old emails within my inboxes. This is a good way of keeping your inboxes up to date and keep your Google storage from piling with garbages.

## Intructions
1.) Go to your Google Cloud Console. Hover to -> Credentials -> create Credentials -> OAuth client ID. Choose Desktop app for application type and click on create.

2.) After creation click on download credential Json file and save it in the same directory as this app and rename it as `credentials.json`.

3.) Enable Gmail API in Google Cloud Console.

4.) Configure an OAuth consent screen for authorization and add your gmail account as a test users.

5.) Configure the secrets in the codes accordingly to your own such as your discord serverID, channelID, Token etc. If you don't wish to include discord notification logs will also be written out to "logfile.txt".

6.) Install all the requirement libraries in requirements.txt: `pip install -r requirements.txt`

7.) Run `Python3 app.py` locally and authenticate and authorize to the consent screen to retrieve a `token.json` file with token informations in it.

## Local Docker

```bash
    $ docker build -t gmail-old-email-remover-app .
    $ docker run -it --rm -p 8080:8080 gmail-old-email-remover-app:latest
```
# License
[GNU General Public License v3.0](LICENSE)
