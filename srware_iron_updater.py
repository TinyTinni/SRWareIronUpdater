''' 
author: Matthias Moeller
date: 2016

    Updates/installs SRWare Iron browser
    Default install path:
        - "$ProgramFiles$/SRWare Iron" for 32-bit
        - "$ProgramFiles$/SRWare Iron (64-bit)" for 64-bit

    Command lines:
    (optional): "-p <path>" Specify SRWare Iron Install Path (Default: C:\Program Files\SRWare Iron (64-bit)" (64-bit prefix just for 64-bit windows, if you use 32-bit browser on a 64-bit os, please specify install path) 
    (optional): "-x86" Use 32-bit binary instead of 64-bit. NOTE: You may have to change the install path
    
    For windows, you can install this script as a service.
    Please have a look to "srware_iron_updater_install_task.bat"
    Maybe you have to change the python directory
'''

import urllib.request
import re
import pathlib
import tempfile
import subprocess
import os
import shutil
import argparse

def getOnlineVersion():
    res = urllib.request.urlopen("https://www.srware.net/software_srware_iron_download.php")
    html = str(res.read())
    html = "Version: <strong>50.0.2650.0</strong><br><br>"
    p = re.compile("Version: <strong>(\d+.\d+.\d+.\d+)</strong><br><br>")
    m = p.match(html)
    result = m.group(1)
    print("Online Version: " + result)
    return result

def getInstalledVersion(inPath):

    print("Search for Versions in: " + inPath)
    
    inPath = pathlib.Path(inPath)
    
    files = [ f.stem for f in inPath.glob("**/*.manifest") ]
    print("Offline Versions: ")
    print(files)

    return files

def installUpdate(exeName):
    print("Download installer")
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix="."+exeName.split(".")[-1])
    with urllib.request.urlopen("https://www.srware.net/downloads/"+exeName) as res:
        shutil.copyfileobj(res,tmp)   
    tmp.close()
    print("Download finished")
    exe = subprocess.Popen(tmp.name)
    exe.wait()
    os.remove(tmp.name)

def is64Windows():
    return 'PROGRAMFILES(X86)' in os.environ

def getExeName(use64bit):
    if use64bit:
        return "srware_iron64.exe" #64-bit
    else:
        return "srware_iron.exe" #32-bit
        
def getInstallPath():
    result = os.environ['ProgramW6432']+"\\SRWare Iron"
    if is64Windows():
        result += " (64-Bit)"
    return result

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Updates/installs SRWare Iron browser")
    parser.add_argument("-p", action="store", dest="installpath", 
                        default = getInstallPath(),
                        help="Specify SRWare Iron Install Path  (Default: "+getInstallPath()+")")
    parser.add_argument("-x86", action="store_true",dest="archix86", default= not is64Windows(),
                        help="Use 32-bit Iron (Default: " + str(not is64Windows()) + ")")
    parsedArgs = parser.parse_args()
    
    use64bit = not parsedArgs.archix86
    downloadExeName = getExeName(use64bit)
    installedVersion = getInstalledVersion(parsedArgs.installpath )
    onlineVersion = getOnlineVersion()

    needUpdate = onlineVersion not in installedVersion
    print("Needs Update: " + str(needUpdate))
    if needUpdate:
        installUpdate(downloadExeName)
