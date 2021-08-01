import telebot # importamos la libreria de telebot

# token = os.getenv['TOKEN']
bot = telebot.TeleBot('') #anadimos el token
updates = bot.get_updates()
message = updates[0].message
from_user = message.from_user
id = from_user.id
get_me = bot.get_me()

@bot.message_handler(commands=['info','hola']) #definimos el comando
def hola(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id,  "Envia 1 o GB para ver formula Gigabytes a Megabytes \n Envia 2 o TB para ver formula Terabytes a Gigabytes \n Envia 3 o MB para ver formula Megabytes a Kilobytes \n Envia 4 o b para ver formula Bytes a bits \n ")
    print("Mandaron info")

@bot.message_handler(commands=['1','GB']) 
def GB(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "multiplica el valor de tamaño de datos por 1024")
    print("Mandaron 1")

@bot.message_handler(commands=['2','TB'])
def TB(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "multiplica el valor de tamaño de datos por 1024")
    print("Mandaron 2")

@bot.message_handler(commands=['3','MB'])
def MB(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "multiplica el valor de tamaño de datos por 1024")
    print("Mandaron 3")

@bot.message_handler(commands=['4','b'])
def b(mensaje):
    bot.send_chat_action(id, 'typing')
    bot.send_message(id, "multiplica el valor de tamaño de datos por 8")
    print("Mandaron 4")

bot.polling()