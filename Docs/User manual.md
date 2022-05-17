# User manual

## HOW TO INSTALL
This installation is designed for the linux ubuntu 64 operating system
### Install Python  
- Start by updating the packages list and installing the prerequisite \
**$ sudo apt update** \
**$ sudo apt install software-properties-common** 
- Next, add the deadsnakes PPA to your sources list: \
**$ sudo add-apt-repository ppa:deadsnakes/ppa**
- Once the repository is enabled, install Python 3.7 with: \
**$ sudo apt install python3.7**
- At this point, Python 3.7 is installed on your Ubuntu system and ready to be used. You can verify it by typing: \
**$ python3.7 --version**

### Clone git
- Open the Ubuntu terminal window.
- Ensure an Ubuntu Git installation exists.
- **Run the following commands**:
  - **$ git clone** https://github.com/BelkisVasquez0609/002Assigment-SSN
  - **$ cd my-github-repo**

## HOW IT IS EXECUTED
- Open the terminal by searching for it in the dashboard or pressing **Ctrl + Alt + T.**
- Navigate the terminal to the directory where the script is located using the **cd command.**
- Type python **main.py** in the terminal to execute the script.
  - If the script is **python3**, use python3 in the terminal command:**python3 main.py**
 
## HOW TO USE THE APP
- When entering the application, the system will show a welcome message and then you will be asked to press the enter key.
- Then you will be asked to enter a 9-digit social security number
- You must enter this number made up of 3 sections and you must separate these by hyphens (-) as shown below:
   - 023-24-7567
 - If it is an incorrect number, a corresponding message will be displayed indicating the error, otherwise the message: **Registered successfully** will be displayed.
