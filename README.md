## ConversationScript
Reads a qualtrics form and fills out conversation data with residents.
CURRENTLY ONLY WORKS FOR NAVE AND BSH.


# Setup and Usage
First, you must download Chrome Driver. Make sure to download the correct version. Your Google Chrome might need to be updated first.
If you are on Mac and probably Linux you will want to place this file as /usr/local/bin/chromedriver
So move it there after you have downloaded it. Windows should have a similar bin file to place this in but honestly I dont know.

https://chromedriver.chromium.org/downloads

Second, you must set up your excel spreedsheet that the script will pull the data from.
Most of this data only needs to be completed once. Below is the link to the master sheet.
Make a copy of the master sheet and put your data in. Note that the method and the key is currently not used so putting all as 1's will suffice.

https://docs.google.com/spreadsheets/d/11OUO7HHQl-Fs4Uou1oj1Yq1psZI96MdPdA3L9G5ibUY/edit?usp=sharing 

After you have filled out this data. Download this document as an .xlsx file. If you using a Mac or Linux 
simply placing this file in your downloads should work. If not you will need to change the "loc" variable in the 
excel_reader.py file to be the location of your file.

loc = "~/Downloads/MasterConvo.xlsx"

Afterwards simply run the convo-script.py python script. It is still a new script so it might throw an error at some point. 
If it fails delete all the rows that sucessfully ran and then download the file again.
If you need any help contact Brett.