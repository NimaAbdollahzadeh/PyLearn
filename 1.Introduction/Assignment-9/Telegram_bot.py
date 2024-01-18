import os
import random
import time
from datetime import datetime
import telebot
from telebot import types
import gtts
import jdatetime
import qrcode


bot = telebot.TeleBot(#TOKEN_plecement, parse_mode=None)

# Welcome message با نام کاربر، خوش آمدید چاپ کند. مثلا (sajjad خوش آمدی) 

@bot.message_handler(commands=['start'])
def send_welcome(message):
    username = message.from_user.username
    welcome_message = f"{username} خوش آمدی 😍"
    bot.reply_to(message, welcome_message)

# Help توضیحات بالا را نمایش دهد.

@bot.message_handler(commands=["help"])
def give_info(message):
    user_id = message.from_user.id
    help_message = (
        "راهنما:\n"
        "/start - شروع چت با ربات\n"
        "/QRCode - تولید کد QR از یک رشته\n"
        "/age - محاسبه سن به صورت هجری شمسی\n"
        "/voice - تبدیل یک متن به صدا\n"
        "/max - یافتن بزرگترین عدد در یک آرایه\n"
        "/argmax - یافتن اندیس بزرگترین عدد در یک آرایه\n"
        "/game - بازی حدس عدد"
    )

    bot.send_message(user_id, help_message)

    markup = types.ReplyKeyboardMarkup(row_width=2)
    start_btn = types.KeyboardButton("/start")
    qrcode_btn = types.KeyboardButton("/QRCode")
    age_btn = types.KeyboardButton("/age")
    voice_btn = types.KeyboardButton("/voice")
    max_btn = types.KeyboardButton("/max")
    argmax_btn = types.KeyboardButton("/argmax")
    game_btn = types.KeyboardButton("/game")
    markup.add(start_btn, qrcode_btn, age_btn, voice_btn, max_btn, argmax_btn, game_btn)

    bot.send_message(user_id, help_message, reply_markup=markup)

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

# game بازی حدس عدد اجرا شود. کاربر یک عدد حدس میزند و بات راهنمایی می‌کند (برو بالا، برو پایین، برنده شدی) - در هنگام بازی، یک دکمه new game در پایین بات مشاهده شود.

@bot.message_handler(commands=["game"])
def start_game(message):
    user_id = message.from_user.id
    global target_number, attempts, user_guess
    target_number = random.randint(1, 100)
    attempts = 0
    user_guess = 0
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton("برو بالا"))
    markup.add(types.KeyboardButton("برو پایین"))
    markup.add(types.KeyboardButton("برنده شدی"))
    bot.send_message(user_id, f"بازی حدس عدد شروع شد! عددی بین 1 تا 100 را حدس بزنید.", reply_markup=markup)
@bot.message_handler(func=lambda message: message.text in ["برو بالا", "برو پایین", "برنده شدی"])
def check_guess(message):
    global target_number, attempts, user_guess
    user_id = message.from_user.id
    user_guess = 0
    try:
        if message.text == "برو بالا" :
            user_guess = random.randint(user_guess + 1, 100)
        elif message.text == "برو پایین":
            user_guess =  random.randint(1, user_guess - 1)
        else:
            bot.send_message(user_id, f"تبریک! شما با {attempts} تلاش برنده شدید.")
            return
    except Exception as e:
        bot.send_message(user_id, "متاسفانه خطایی رخ داده است. لطفاً دوباره تلاش کنید.")
        return
    attempts += 1
    bot.send_message(user_id, f"آیا عدد حدس زده شده توسط بات برابر با {user_guess} است؟", reply_markup= types.ReplyKeyboardRemove())
@bot.message_handler(func = lambda message: message.text.lower() == "new game")
def new_game(message):
    user_id = message.from_user.id
    bot.send_message(user_id, "بازی جدید شروع شد! عدد جدیدی بین 1 تا 100 را حدس بزنید.")
    start_game(message)

bot.infinity_polling()
