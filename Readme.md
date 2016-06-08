#Simple SRWare Iron Updater
Provides a simple Python script for installing and updating [SRWare Iron Webbrowser](https://www.srware.net/software_srware_iron_download.php).
Tested with Python 3.4 and 3.5.1.

Two addtional scripts provide easy script registration as a service for windows.
Service will be executed on a daily base.

##How-To Use
Execute the script using python.

    Default install path:
    - "%ProgramFiles%/SRWare Iron" for 32-bit
    - "%ProgramFiles%/SRWare Iron (64-bit)" for 64-bit

    Command lines:
    - (optional): "-p <path>" Specify SRWare Iron Install Path (Default: C:\Program Files\SRWare Iron (64-bit)" (64-bit prefix just for 64-bit windows, if you use 32-bit browser on a 64-bit os, please specify install path) 
    - (optional): "-x86" Use 32-bit binary instead of 64-bit. NOTE: You may have to change the install path
    
The provided "register" scripts automatically registers the update-script to the windows task scheduler as a service.
Make sure, your python was installed with path variables, otherwise you have to define the path to your python executable manually.

## License

[MIT License](./LICENSE) © Matthias Möller. Made with ♥ in Germany.
