# Automated-Birthday-Wisher
A comprehensive program that sends birthday wishes to people's email if it's their birthday.

Key information required are the below:
* Update the "birthdays" csv file with name, email, year, month, and day for an individual. Refer to the example in the file.
	* Note that "name" should be a single string name.
	* "year" is not utilized for determining birthday and can be any year.
	* "month" and "day" fields are required.
* Update the "letter_#" text files with your desired message. 1 will be selected at random when sending an email.
	* Make sure the "[NAME]" placeholder field is not changed.
* Update the "n" value if you add new letter templates.
	* Make sure the new templates follow the same naming convention for the files (letter_#).
* Dependent on your email provider, you may need to adjust the "smtp_pv" variable.
	* Gmail(smtp.gmail.com), Yahoo(smtp.mail.yahoo.com), Hotmail(smtp.live.com), Outlook(smtp-mail.outlook.com)
	* Additionally, you may need to find out the port number for your email provider and replace the "smtp_port" value if it is not gmail.
* Your email information.
	* Note that the "my_password" field for gmail is your App Password from gmail (you will need to set this up yourself).