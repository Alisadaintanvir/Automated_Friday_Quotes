# Friday Quotes Email Sender

This Python script is designed to send an inspirational quote via email every Friday. It uses the `smtplib` library to handle the email sending and `datetime` and `random` modules to pick a random quote from the provided list of quotes.

## Prerequisites

Before running the script, make sure you have the following:

1. Python installed on your system.
2. A text file named `quotes.txt` containing a list of quotes, with each quote on a separate line.

## How to Use

1. Clone this repository to your local machine.
2. Place the `quotes.txt` file in the same directory as the Python script.
3. Make sure to have a Gmail account to use for sending the emails.
4. Enable the "Allow less secure apps" option in your Gmail account settings.
5. Update the `my_email`, `password`, and `receiver_email` variables with your Gmail account details.

## Usage

To run the script, execute the following command in your terminal or command prompt:

`python main.py`

## How it Works
The script checks the current day of the week using the datetime module.
If the current day is Friday (day number 4 in Python's weekday() function, where Monday is 0 and Sunday is 6), it proceeds to the next step.
It reads all the quotes from the quotes.txt file and selects a random quote using the random.choice() function.
The script then sends an email containing the selected quote to the specified receiver_email using the smtplib library.
Please note that it is important to handle your email credentials with care and avoid hardcoding them in the script directly. Instead, consider using environment variables or external configuration files to keep your sensitive information secure.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

Feel free to modify and use this script as you see fit!
