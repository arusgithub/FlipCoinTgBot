from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, ContextTypes, filters
import random
import os



# Приветствие и кнопка
async def welcome_with_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Создаем кнопку
    keyboard = [["Бросить монету"]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    # Отправляем приветственное сообщение с кнопкой
    await update.message.reply_text(
        "🎰 Привет!\nЯ бот для подбрасывания монеты.\n\nНе можешь сделать выбор?\nНажмите кнопку ниже, чтобы бросить монету:",
        reply_markup=reply_markup
    )

# Обработка кнопки "Бросить монету"
async def flip_coin(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Проверяем текст, отправленный пользователем 🪙
    if update.message.text == "Бросить монету":
        result = "Орёл" if random.choice([True, False]) else "Решка"
        await update.message.reply_text(f"Выпало: {result}")

# Основная функция для запуска бота
def main():
    # Вставьте токен вашего бота
    TOKEN = os.getenv("TG_COIN_BOT_TOKEN")

    # Создаем объект Application
    application = Application.builder().token(TOKEN).build()

    # Регистрируем команду /start для приветствия
    application.add_handler(CommandHandler("start", welcome_with_buttons))

    # Регистрируем обработчик для кнопки "Бросить монету"
    application.add_handler(MessageHandler(filters.TEXT & filters.Regex("^Бросить монету$"), flip_coin))

    # Запускаем бота
    application.run_polling()

if __name__ == "__main__":
    main()

