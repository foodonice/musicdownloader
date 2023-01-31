import subprocess
from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth
import spotdl
# For using listdir()
import os,shutil
# Below code does the authentication
# part of the code
gauth = GoogleAuth()
  
# Creates local webserver and auto
# handles authentication.
gauth.LocalWebserverAuth()       
drive = GoogleDrive(gauth)
path = "C:\\Users\\Krish\\OneDrive\\Desktop\\MusicDownlaoder\\songs"
cmd2 = "spotdl"

while True:
    print("Input a spotify link")
    songLink = input()
    if(songLink != "0"):

        p = subprocess.Popen([cmd2, songLink], cwd=path)
        p.wait()
        print("DOWNLOADED")

        songLink = "0"

        for x in os.listdir(path):
            f = drive.CreateFile({'title': x,'parents': [{'id': '1UCTvZJekMMt9bvtkph8D28aoDBt4CX7R'}]})
            f.SetContentFile(os.path.join(path, x))
            f.Upload()
        
            # Due to a known bug in pydrive if we 
            # don't empty the variable used to
            # upload the files to Google Drive the
            # file stays open in memory and causes a
            # memory leak, therefore preventing its 
            # deletion
            f = None

        print("UPLOADED")

        for filename in os.listdir(path):
            file_path = os.path.join(path, filename)
            try:
                if os.path.isfile(file_path) or os.path.islink(file_path):
                    os.unlink(file_path)
                elif os.path.isdir(file_path):
                    shutil.rmtree(file_path)
            except Exception as e:
                print('Failed to delete %s. Reason: %s' % (file_path, e))
        
        print("CLEARED")
        print("DONE")


