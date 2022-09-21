Welcome to Royal Retailers Pvt Ltd Billing and Stock Management Software.

This setup will guide you how to install our software. Read Documentation for detailed steps with pictures.

Feel Free to skip any step below (if done already).

-------------------------------------------------------------------------------------------------

Step 1: Install Python 3.7.3 from the below links:
		64bit - https://www.python.org/ftp/python/3.7.3/python-3.7.3-amd64.exe
		32bit - https://www.python.org/ftp/python/3.7.3/python-3.7.3.exe
	Remember to set python as PATH file in installer.

Step 2: Install MySQL 8.0 GPL Community Server from https://dev.mysql.com/downloads/installer/
	Remember the password.

Step 3: Unzip and Place the Royal folder in a drive (for eg. C:\\). 				 (IMPORTANT STEP)

Step 4: Run The File named 'Backend Creation Utility.py' in C:\\Royal\_Setup folder
	independently.
	Note: You can keep any available drive instead of C:\\.

Step 5: Activate the venv scripts required for django.
	Use "pip3 install mysql-connector-python mysql-connector-python" as normal pip mysql is 
	unsupported for django.

Step 6: Navigate to C:\\Royal by using the same command window.
	Note: Give the above used drive instead of C:\\ here.
	After this, Open C:\\Royal\DOME\views.py (in file explorer; ONE TIME STEP) and in Django Path Configuration section, Edit the drive and pre-folder in 
	a similar fashion. Do not close the CMD Window.
	Save views.py and close it. DO NOT MAKE ANY OTHER CHANGES THERE.

Step 7: Enter into the command window: "py manage.py runserver" and Wait for some time.

Step 8: In Your browser, type URL "http://localhost:8000"
	Remember, https will not work. Else Download Chrome Browser which is supported.

Step 9: Login The Portal which pops up automatically if the URL is entered correctly.

Step 10: The Login details will be shared by the Developers with you.