from ftplib import FTP
import os
import zipfile
import json
import ConfigParser

config = ConfigParser.ConfigParser()
config.read('config.ini')

username = config.get('login', 'username')
password = config.get('login', 'password')
currentPath = config.get('config', 'filepath')

ftp = FTP('ftp.rescuegroups.org')

ftp.login(username, password)

files = ftp.nlst()

unzipPath = os.path.join(currentPath, 'RGFilesUnzipped')

for fileNum in range(len(files)):
    filename = files[fileNum]

    localFilename = os.path.join(currentPath, 'RGFiles', filename)
    with open(localFilename, 'wb') as f:
        def callback(data):
            f.write(data)

        print 'downloading=>', filename

        ftp.retrbinary('RETR %s' % filename, callback)

    zipF = zipfile.ZipFile(localFilename)
    zipF.extractall(unzipPath)

with open(os.path.join(unzipPath, 'QltdwQc9_pets_1.json'), 'r') as dataFile:
    for line in dataFile:
        jsonData = json.loads(line)
        print jsonData
