import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, MessageHandler, Filters

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

def start(update: Update, context: CallbackContext) -> None:
    keyboard = [
        [InlineKeyboardButton("Apply", callback_data='apply')],
        [InlineKeyboardButton("Service Info", callback_data='services')],
        [InlineKeyboardButton("Destinations", callback_data='destinations')],
        [InlineKeyboardButton("Achievements", callback_data='achievements')],
        [InlineKeyboardButton("Contact Us", callback_data='contact')],
        [InlineKeyboardButton("FAQ", callback_data='faq')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    welcome_message = (
        "*🌟 Welcome to NAMS Educational Consultancy!*\n\n"
        "How can we assist you today?"
    )
    update.message.reply_text(welcome_message, parse_mode='Markdown', reply_markup=reply_markup)

def button_click(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.answer()
    
    if query.data == 'services':
        services(update, context)
    elif query.data == 'apply':
        apply(update, context)
    elif query.data == 'contact':
        contact(update, context)
    elif query.data == 'faq':
        faq(update, context)
    elif query.data == 'destinations':
        destinations(update, context)
    elif query.data == 'achievements':
        achievements(update, context)
    else:
        query.message.reply_text("Unknown command. Please try again.")

# Define your other functions here (services, destinations, apply, etc.) as per your original code

def main():
    # Replace 'YOUR_API_TOKEN' with the bot token from BotFather
    bot_token = 'YOUR_API_TOKEN'
    updater = Updater(bot_token, use_context=True)
    dp = updater.dispatcher

    # Register command handlers
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("services", services))
    dp.add_handler(CommandHandler("apply", apply))
    dp.add_handler(CommandHandler("contact", contact))
    dp.add_handler(CommandHandler("faq", faq))
    dp.add_handler(CommandHandler("destinations", destinations))
    dp.add_handler(CommandHandler("achievements", achievements))

    # Register callback handler
    dp.add_handler(CallbackQueryHandler(button_click))

    # Start the bot
    updater.start_polling()

    # Run the bot until you press Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
