import os
import random
import time
from datetime import datetime
import telebot
from telebot import types
import gtts
import jdatetime
import qrcode


bot = telebot.TeleBot("6487625609:AAFEk4UqXVR1yg0FC59CEA1K9srDY_CFV84", parse_mode=None)

# Welcome message با نام کاربر، خوش آمدید چاپ کند. مثلا (sajjad خوش آمدی) 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username
    welcome_message = f"{username} خوش آمدی 😍"
    bot.reply_to(message, welcome_message)

# Help توضیحات بالا را نمایش دهد.

@bot.message_handler(commands=["help"])
def give_info(message):
    pass

# QRCode یک رشته از کاربر دریافت نماید و qrcode آن را تولید نماید.

@bot.message_handler(commands=["QRCode"])
def get_string(message):
    user_id = message.from_user.id
    markup = types.ForceReply(selective= False)
    bot.send_message(user_id, "لطفا یک رشته را وارد کنید: ", reply_markup= markup)
@bot.message_handler(func=lambda message: True, content_types=["text"])
def make_QRCode(message):
    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size = 10,
        border = 4,
)
    qr.add_data(message)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")
    img_path = ("1.Introduction/Assignment-9/database/qrcode/qrcode.png")
    img.save(img_path)
    user_id = message.from_user.id
    with open(img_path, "rb") as photo:
        bot.send_photo(user_id, photo)

    
# Age Calculator تاریخ تولد را به صورت هجری شمسی دریافت نماید و سن را محاسبه نماید. (برای راهنمایی به آدرس اینستاگرامی pylearn@ مراجعه نمایید)

@bot.message_handler(commands=["age"])
def get_birthday(message):
    user_id = message.from_user.id
    markup = types.ForceReply(selective= False)
    bot.send_message(user_id, "لطفا تاریخ تولد خود را وارد کنید : ", reply_markup= markup)
@bot.message_handler(func=lambda message: True, content_types=["text"])
def calculate_age(message):
    try:
        birthday = datetime.strptime(message.text, "%Y-%m-%d").date()
        current_date = datetime.now().date()
        age = current_date.year - birthday.year - ((current_date.month, current_date.day) < (birthday.month, birthday.day))
        shamsi_birthday = jdatetime.datetime.fromgregorian(date= birthday).strftime("%Y/%m/%d")
        bot.reply_to(message, f"Your Shamsi birthday: {shamsi_birthday}\nYour age: {age} years.")
    except ValueError:
        bot.reply_to(message, "Invalid date format. Please enter your birthday in the format YYYY-MM-DD.")

# Voice یک جمله به انگلیسی از کاربر دریافت نماید و آن را به صورت voice ارسال نماید.

@bot.message_handler(commands=["voice"])
def get_text(message):
    user_id = message.from_user.id
    markup = types.ForceReply(selective= False)
    bot.send_message(user_id, "لطفا آنچه را که قصد تبدیل به صدا دارید را به زبان انگلیسی تایپ کنید.", reply_markup= markup)
@bot.message_handler(func=lambda message: True, content_types=["text"])
def make_voice(message):
    user_id = message.from_user.id
    text_to_convert = message.text
    tts = gtts.gTTS(text_to_convert, lang= "en")
    directory_path = "1.Introduction/Assignment-9/database/Voice"
    os.makedirs(directory_path, exist_ok=True)
    file_name = f"{user_id}_{int(time.time())}.mp3"
    file_path = f"1.Introduction/Assignment-9/database/Voice/{file_name}"
    tts.save(file_path)
    audio_file = open(file_path, "rb")
    bot.send_audio(user_id, audio_file)

# Max یک آرایه به صورت 14,7,78,15,8,19,20 از کاربر دریافت نماید و بزرگترین مقدار را چاپ نماید.

@bot.message_handler(commands=["max"])
def get_number(message):
    user_id = message.from_user.id
    markup = types.ForceReply(selective= False)
    bot.send_message(user_id, "لطفا تعدادی عدد وارد کنید تا بزرگترین مقدار برایتان چاپ شود: ", reply_markup= markup)
@bot.message_handler(func=lambda message: True, content_types=["text"])
def return_max(message):
    numbers = [int(x) for x in message.text.split(",")]
    max_value = max(numbers)
    user_id = message.from_user.id
    bot.send_message(user_id, f"بزرگترین مقدار در آرایه : {max_value}")

# Argmax یک آرایه به صورت 14,7,78,15,8,19,20 از کاربر دریافت نماید و اندیس بزرگترین مقدار را چاپ نماید.

@bot.message_handler(commands=["argmax"])
def get_number(message):
    user_id = message.from_user.id
    markup = types.ForceReply(selective= False)
    bot.send_message(user_id, "لطفا تعدادی عدد وارد کنید تا اندیس بزرگترین مقدار برایتان چاپ شود: ", reply_markup= markup)
@bot.message_handler(func=lambda message:True, content_types=["text"])
def return_argmax(message):
    numbers = [int(x) for x in message.text.split(",")]
    argmax_value = max(range(len(numbers)), key=lambda i: numbers[i])
    user_id = message.from_user.id
    bot.send_message(user_id, f"بزرگترین مقدار در اندیس : {argmax_value}")

bot.infinity_polling()