from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, ConversationHandler, MessageHandler, filters
import logging
from secrets import TOKEN
from telegram import Update, ReplyKeyboardMarkup



logging.basicConfig(
    format='%(asctime)s - %(name)s - %(message)s',
    level=logging.INFO
)  # модуль ведения журнала логов

logging.getLogger("httpx").setLevel(logging.WARNING)
logger = logging.getLogger(__name__)

DATE_CURRENCY, CHECK_DATE, SHOW_RESULT = range(3)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    "Приветствие бота и выбор валюты"
    user = update.message.from_user
    logger.info(f"{user.first_name} starts our bot")
    await context.bot.send_message(chat_id=update.effective_chat.id,
                             text="Добро пожаловать в бот определения цен валют!")
    curr_list = [["USD", "EUR", "CNY"]]  # список из валют
    await update.message.reply_text("Выберите валюту из представленных ниже",
                                    reply_markup=ReplyKeyboardMarkup(
                                        curr_list,
                                        input_field_placeholder="Выберите валюту",
                                        one_time_keyboard=True))
    return DATE_CURRENCY


async def date_currency(update: Update, context: ContextTypes.DEFAULT_TYPE):
    "Выбор даты"
    user = update.message.from_user
    logger.info(f"{user.first_name} selected {update.message.text}")
    logger.info(f"{user.first_name} inputs date")
    await update.message.reply_text("Напишите дату в формате YYYY-MM-DD, например, 2023-01-05")
    return CHECK_DATE

async def show_result(update: Update, context: ContextTypes.DEFAULT_TYPE):
    "Вывод результата поиска"
    user = update.message.from_user
    logger.info(f"{user.first_name} selected {update.message.text}")
    logger.info(f"{user.first_name} shows result")
    await update.message.reply_text("Результаты поиска")


async def exit_callback(update: Update, context: ContextTypes.DEFAULT_TYPE):
    "Завершение работы бота"
    user = update.message.from_user
    logger.info(f"{user.first_name} finishes our bot")
    await update.message.reply_text("Спасибо за выбор нашего бота!")
    return ConversationHandler.END

if __name__ == "__main__":
    app_b = ApplicationBuilder()
    app_b.token(TOKEN)
    app = app_b.build()

    start_conversation_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            DATE_CURRENCY: [MessageHandler(filters.Regex("^(USD|EUR|CNY)$"), date_currency)],
            CHECK_DATE: [MessageHandler(filters.Regex("^(19|20)\d{2}-(0[1-9]|1[1,2])-(0[1-9]|[12][0-9]|3[01])$"),
                                         show_result),
                          MessageHandler(filters.Regex("^((?!exit).)*$"),
                                         date_currency)
                          ],
        },
        fallbacks=[CommandHandler("exit", exit_callback)]
    )
    app.add_handler(start_conversation_handler)

    app.run_polling()
