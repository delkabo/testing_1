from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes
from app.config import settings

# Инициализация бота
application = Application.builder().token(settings.BOT_TOKEN).build()

# Обработчик команды /start
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user
    await update.message.reply_html(
        f"Привет, {user.mention_html()}! 👋\n"
        f"Я бот, работающий на FastAPI!\n"
        f"Используй /help для списка команд"
        )

# Обработчик команды /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    help_text = """
📝 **Доступные команды:**

/start - Начать работу
/help - Помощь
/about - О боте

💬 **Просто отправь мне любое сообщение, и я отвечу!**
    """
    await update.message.reply_text(help_text)

# Обработчик команды /about
async def about_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    about_text = """
🤖 **FastAPI Telegram Bot**

Это демонстрационный бот, показывающий интеграцию:
• FastAPI как высокопроизводительный backend
• Telegram Bot API через вебхуки
• Асинхронную обработку сообщений

🛠 Технологии: Python, FastAPI, python-telegram-bot
    """
    await update.message.reply_text(about_text)

# Обработчик текстовых сообщений (эхо)
async def echo_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = f" Вы сказали: {user_message}"
    await update.message.reply_text(response)

# Обработчик неизвестных команд
async def unknown_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("x Неизвестная команда. Используй /help для списка команд.")

# Регистрируем обработчики
def setup_handlers():
    # Команды
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("about", about_command))

    # Текстовые сообщения
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo_handler))

    # Неизвестные команды (должен быть последним)
    application.add_handler(MessageHandler(filters.COMMAND, unknown_command))

def initialize_bot():
    setup_handlers()
    return application