import sys
import dropbox
from dropbox.files import WriteMode
from dropbox.exceptions import ApiError, AuthError

'''dbx = dropbox.Dropbox('hED4sqJ7nVAAAAAAAAABGK9yMe5CsjWNjMlo_PWTYY4YfmwTho5xLYK_2yhTsDem')
dbx.users_get_current_account()
for entry in dbx.files_list_folder('').entries:	
	print(entry.name)'''

TOKEN = 'hED4sqJ7nVAAAAAAAAABGK9yMe5CsjWNjMlo_PWTYY4YfmwTho5xLYK_2yhTsDem'


def backup(LOCALFILE, BACKUPPATH):
    with open(LOCALFILE, 'rb') as f:
        # We use WriteMode=overwrite to make sure that the settings in the file
        # are changed on upload
        print("Uploading " + LOCALFILE + " to Dropbox as " + BACKUPPATH + "...")
        try:
            dbx.files_upload(f.read(), BACKUPPATH, mode=WriteMode('overwrite'))
        except ApiError as err:
            # This checks for the specific error where a user doesn't have
            # enough Dropbox space quota to upload this file
            if (err.error.is_path() and
                    err.error.get_path().reason.is_insufficient_space()):
                sys.exit("ERROR: Cannot back up; insufficient space.")
            elif err.user_message_text:
                print(err.user_message_text)
                sys.exit()
            else:
                print(err)
                sys.exit()

if __name__ == '__main__':
    # Check for an access token
    print('y')
    if (len(TOKEN) == 0):
        sys.exit("ERROR: Looks like you didn't add your access token. "
            "Open up backup-and-restore-example.py in a text editor and "
            "paste in your token in line 14.")

    # Create an instance of a Dropbox class, which can make requests to the API.
    print("Creating a Dropbox object...")
    dbx = dropbox.Dropbox(TOKEN)

    # Check that the access token is valid
    try:
        dbx.users_get_current_account()
    except AuthError as err:
        sys.exit("ERROR: Invalid access token; try re-generating an "
            "access token from the app console on the web.")

    # Create a backup of the current settings file
    backup('a.txt','//mnt/c/users/jm796/Dropbox/Apps/Pictopia/a.txt')
    backup('paragraph.txt','//mnt/c/users/jm796/Dropbox/Apps/Pictopia/paragraph.txt')