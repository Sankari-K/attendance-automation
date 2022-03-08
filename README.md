# attendance-automation
This is python script I wrote using selenium to automatically fill up google forms for one of my college courses.
I'm supposed to fill up the same google form with details such as my name, email and university id thrice a week. This program automates this task for me.

### Built With
* [Selenium](https://selenium-python.readthedocs.io/) - Tool used for automation
* [Chrome Driver](https://chromedriver.chromium.org/) - Used by selenium to control Chrome

#### Note:
* Make sure ```chromedriver.exe``` is in the ```C:\Program Files (x86)``` directory
* Create a file called ```secrets.py``` that looks like this:
```
    username = "your_email@gmail.com"
    password = "your_password"
```
* Run ```first_time.py``` once, to store login information in a ```cookies.pkl``` file. Whenever the form needs to be filled, run ```attendance_automation.py```
