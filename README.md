## ConversationScript
Reads a qualtrics form and fills out conversation data with residents.
CURRENTLY ONLY WORKS FOR NORTH AVE AREA AND EAST CAMPUS

The only two files that you would need to modify is the convo_script.py or
the excel_reader.py and the locations are all marked with the comment of "#TODO"

- is_nav in the convo_script.py is true for the nav area and false for the east campus dorms

- want_email in the convo_script.py is personal preference. Set this value to true if you would like to recieve a confirmation email, but make sure you actually have an email in the corresponding column of your spreadsheet otherwise it will send the email to Kevin :)...

- loc in excel_reader will change where the directory is for the excel file containing the list of residents and information


# Setup and Usage

First, you need to install all these libraries using pip/pip3 or you can set up a virtual environment with these libraries.

- seleium
- xlrd2
- service
- datetime

For the chrome driver, you first need to check your chrome version or if you dont have chrome install it or look into the option
of downloading the appropiate driver. After finding the version, use this command to download the driver for the specific version of chrome that you have:

pip install chromedriver-py==YOUR VERSION  (or pip3 if that is the installed version of pip)

Second, you must set up your excel spreedsheet that the script will pull the data from.
Most of this data only needs to be completed once. Below is a link to an example sheet.

https://docs.google.com/spreadsheets/d/16Dz5gRLQUqZ6qLrWjEvd_B2steo0TlQLvCoelLU0BR8/edit?usp=sharing

After you have filled out this data. Download this document as an .xlsx file and place it in the same directory as the script and run convo_script.py