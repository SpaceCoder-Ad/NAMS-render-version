import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackContext, CallbackQueryHandler, MessageHandler, Filters

# Setup logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

# Function to handle the /start command
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
        "How can we assist you today?\n"
        # "- For *Course details*, type /services\n"
        # "- For *Application Process*, type /apply\n"
        # "- For *Contact Info*, type /contact\n"
        # "- For *Frequently Asked Questions*, type /faq\n"
        # "- For *Destinations*, type /destinations\n"
        # "- For *Our Achievements*, type /achievements"
    )
    # send_message(update, welcome_message)
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
# Function to handle the /services command
def services(update: Update, context: CallbackContext) -> None:
    services_message = (
        "*🚀 Unlock Your Potential and Achieve Your College Dreams*\n"
        "Start Your Journey With Us!\n\n"
        "Applying to college can be a stressful and overwhelming experience. With our application consulting services, you'll "
        "receive expert guidance to elevate your application and stand out to college admissions officers. Our experienced consultants will work with you one-on-one to craft a personalized strategy that showcases your unique qualities and achievements.\n\n"

        "*Why Choose Us?*\n"
        "01. *Guidance: Make it Personal* 🧑‍🏫\n"
        "We’ll help you find the best course for you and guide you through the complex foreign education system. Our expert consultants have years of experience to offer informed guidance.\n\n"

        "02. *Access: Make it Easier on Yourself* 🔑\n"
        "We have access to over 700 universities worldwide and stay up-to-date with their latest changes and opportunities.\n\n"

        "03. *Fees: Save Your Money for the Fun Stuff* 💰\n"
        "NAMS doesn’t charge agent fees for expert counseling, and there are no hidden charges. Some universities even waive their application fees when you apply through us!\n\n"

        "04. *Services: More Than Just Placement* 🌍\n"
        "We offer a full suite of services, including:\n"
        "- English language testing (IELTS)\n"
        "- Visa guidance\n"
        "- Pre-departure advice\n"
        "- Assistance with medical insurance, accommodation, and banking while living abroad.\n\n"

        "05. *Network: Part of a Living Network* 🤝\n"
        "We’ll connect you with alumni or current students who’ve been where you want to be and are eager to share their stories.\n\n"

        "06. *You're Not Alone: New in Town?* 🏙️\n"
        "NAMS is a vibrant network of students, alumni, and employers. We’ll connect you with other NAMS students through welcome events to help you settle in.\n\n"

        "*NAMS: Your One-Stop Solution for International Study*\n"
        "Established in Ethiopia, NAMS connects students with top-ranking educational institutions worldwide. Our firm is known for providing expert visa and informational guidance according to high commission requirements, boasting a strong reputation for securing student visas.\n\n"

        "*Our mission:* To help students compete globally and become productive members of society. We advise on educational opportunities in various countries, including:\n"
        "- 🇺🇸 US                         - 🇬🇧 UK                     - 🇨🇦 Canada\n"
        "- 🇦🇺 Australia              - 🇳🇿 New Zealand   - 🇮🇪 Ireland\n"
        "- 🇩🇪 Germany              - 🇫🇷 France             - 🇸🇪 Sweden\n"
        "- 🇩🇰 Denmark              - 🇳🇱 Netherlands   - 🇦🇹 Austria\n"
        "- 🇫🇮 Finland                  - 🇮🇹 Italy                 - 🇵🇱 Poland\n"
        "- 🇨🇿 Czech Republic    - 🇭🇺 Hungary         - 🇨🇭 Switzerland\n"
        "- 🇪🇸 Spain                     - 🇵🇹 Portugal         - 🇯🇵 Japan\n"
        "- 🇸🇬 Singapore             - 🇲🇾 Malaysia         - 🇦🇪 UAE\n"
        "- 🇹🇷 Turkey                   - 🇨🇾 Cyprus            - 🇨🇳 China\n"
        "- 🇷🇺 Russia                   - 🇻🇳 Vietnam\n\n"

        "*✨ Our Services Include:*\n"
        "1. *Application Consulting* 📄\n"
        "Personalized application strategies to help you stand out in the admissions process.\n\n"

        "2. *Interview Preparation* 🎤\n"
        "Coaching for entrance exams such as IELTS, TOEFL, PTE, GMAT, GRE, SAT, and ACT.\n\n"

        "3. *Test Prep & Tutoring* 📚\n"
        "Comprehensive coaching for entrance exams like IELTS, TOEFL, PTE, GMAT, GRE, SAT, and ACT.\n\n"

        "4. *Student Visas* ✈️\n"
        "Guidance in visa interview preparation, including mock interviews and much more!"
    )

    try:
        if update.callback_query:
            # Respond to the callback query if it's a button click
            update.callback_query.message.reply_text(services_message, parse_mode='Markdown')
        elif update.message:
            # Respond directly to the message if the command is typed
            update.message.reply_text(services_message, parse_mode='Markdown')
        else:
            # If neither callback_query nor message exists
            raise ValueError("No valid update type found")
    except Exception as e:
        # Log the error to see what happened
        print(f"Error in services function: {e}")
        # Inform the user that something went wrong
        if update.callback_query:
            update.callback_query.message.reply_text("An error occurred. Please try again.")
        elif update.message:
            update.message.reply_text("An error occurred. Please try again.")


# Function to handle the /destinations command
def destinations(update: Update, context: CallbackContext) -> None:
    destinations_message = (
        "*🌍 Our Destinations*\n"
        "Here are some of the exciting destinations you can choose for your study abroad experience:\n\n"
        "*🇺🇸 United States*\n"
        "Studying in the U.S.A. will exhilarate you and change your life forever.\n\n"

        "*🇬🇧 United Kingdom*\n"
        "The UK provides internationally recognized qualifications of the highest standard.\n\n"

        "*🇦🇺 Australia*\n"
        "Study in Australia for modern living and rich native culture.\n\n"

        "*🇳🇿 New Zealand*\n"
        "New Zealand offers a safe and secure environment with affordable tuition and living expenses.\n\n"

        "*🇮🇪 Ireland*\n"
        "Rich culture, breathtaking scenery, and friendly people make Ireland an ideal study destination.\n\n"

        "*🇨🇦 Canada*\n"
        "World-class education and a promising future await you in Canada.\n\n"

        "*🇨🇾 Cyprus*\n"
        "Cyprus is a stunning location with long summers, sunny beaches, and a diverse culture.\n\n"

        "*🇨🇿 Czech Republic*\n"
        "Czech universities provide a wide range of courses and well-established specializations.\n\n"

        "*🇩🇰 Denmark*\n"
        "Study in Denmark's energetic and unique educational environment.\n\n"

        "*🇫🇮 Finland*\n"
        "Finland is one of the best places in Europe for studying technology, business, and natural sciences.\n\n"

        "*🇫🇷 France*\n"
        "France offers high-level technology education and a rich cultural experience.\n\n"

        "*🇩🇪 Germany*\n"
        "Germany is a top choice for research opportunities and international study programs.\n\n"

        "*🇭🇺 Hungary*\n"
        "Hungary boasts over 650 years of academic excellence with courses offered in multiple languages.\n\n"

        "*🇪🇸 Spain*\n"
        "Friendly and laid-back, Spain offers an excellent education system and high standard of living.\n\n"

        "*🇮🇹 Italy*\n"
        "Italy is an economical choice for high-quality education at top public and private universities.\n\n"

        "*🇯🇵 Japan*\n"
        "Japan is ideal for students interested in technology and engineering fields.\n\n"

        "*🇲🇾 Malaysia*\n"
        "Affordable tuition fees with high-quality education make Malaysia a strong choice.\n\n"

        "*🇳🇱 Netherlands*\n"
        "Study in the Netherlands for top-quality education and a variety of English-language programs.\n\n"

        "*🇦🇹 Austria*\n"
        "Austria offers a rich cultural experience with high-quality education.\n\n"

        "*🇵🇱 Poland*\n"
        "Poland provides affordable study abroad experiences with worldwide recognition.\n\n"

        "*🇵🇹 Portugal*\n"
        "Enjoy picturesque villages and modern urban lifestyles while studying in Portugal.\n\n"

        "*🇷🇺 Russia*\n"
        "Russia offers a diverse educational experience in a culturally rich environment.\n\n"

        "*🇸🇬 Singapore*\n"
        "Singapore is an education hub in Asia, offering unique services in a safe environment.\n\n"

        "*🇸🇪 Sweden*\n"
        "Sweden's flexible education system encourages practical work alongside studies.\n\n"

        "*🇨🇭 Switzerland*\n"
        "Swiss universities rank among the best in the world for their innovative education systems.\n\n"

        "*🇹🇷 Turkey*\n"
        "Turkey offers affordable living costs and accommodation for students.\n\n"

        "*🇦🇪 United Arab Emirates*\n"
        "The UAE is a business hub, offering valuable networking opportunities alongside education."
    )
    # update.callback_query.message.reply_text(destinations_message, parse_mode='Markdown')
    if update.callback_query:
        # Respond to the callback query if it's a button click
        update.callback_query.message.reply_text(destinations_message, parse_mode='Markdown')
    else:
        # Respond directly to the message if the command is typed
        update.message.reply_text(destinations_message, parse_mode='Markdown')
    # send_message(update, destinations_message)

# Function to handle the /faq command
def faq(update: Update, context: CallbackContext) -> None:
    faq_message = (
        "*❓ Frequently Asked Questions*\n"
        "Any Questions? We are here to help you.\n\n"
        "*Help Desk Support* ☎️\n"
        "Feel free to call us or contact us for any information or questions.\n\n"

        "*Live Chat Support* 💬\n"
        "We are available here on the live chat bot for any information.\n\n"

        "*Here Are the Answers to Some Common Questions:*\n\n"

        "*Q1: Are you eligible to study abroad?* 🌏\n"
        "A1: Yes, as long as you meet the admission requirements and are ready to adapt to a new culture, education system, and environment.\n\n"

        "*Q2: Do I need to take an English test?* 📘\n"
        "A2: Most universities require proof of English proficiency through tests like IELTS or TOEFL.\n\n"

        "*Q3: What if I don't meet the requirements?* 🔄\n"
        "A3: Don't worry! We can guide you on alternative paths and preparations to meet your goals.\n\n"

        "*Q4: How can I stay updated on university changes?* 📰\n"
        "A4: We provide regular updates through our newsletters and counseling sessions.\n\n"

        "*Q5: Do I need to make an appointment to meet a counselor?* 📅\n"
        "A5: Yes, appointments can be scheduled online or by phone. Walk-ins are also welcome during business hours.\n\n"

        "*Q6: What documents should I bring to my appointment?* 📄\n"
        "A6: Bring your valid passport and academic transcripts to verify your identity and streamline the application process.\n\n"

        "*Q7: Which universities do you partner with?* 🌐\n"
        "A7: NAMS partners with over 700 universities in 29 countries, including top institutions in the USA, UK, Australia, Canada, and more.\n\n"

        "*Q8: Are there hidden service fees?* 🚫\n"
        "A8: No, we do not charge any student fees for consultations, and there are no hidden charges.\n\n"

        "*Q9: How long do applications take to process?* ⏳\n"
        "A9: Applications typically take between two to six weeks but may vary during peak periods."
    )
    # update.callback_query.message.reply_text(faq_message, parse_mode='Markdown')
    if update.callback_query:
        # Respond to the callback query if it's a button click
        update.callback_query.message.reply_text(faq_message, parse_mode='Markdown')
    else:
        # Respond directly to the message if the command is typed
        update.message.reply_text(faq_message, parse_mode='Markdown')
    # send_message(update, faq_message)

# Function to handle the /apply command
def apply(update: Update, context: CallbackContext) -> None:
    apply_message = (
        "*📝 How to Apply for University*\n"
        "Our experienced NAMS counselors will assist you in compiling your application and certifying the supporting documents. "
        "Your counselor will then submit your application on your behalf to your chosen university or institution.\n\n"

        "For more detailed guidance on the application process, /contact us directly, or schedule an appointment with one of our counselors."
    )
    # update.callback_query.message.reply_text(apply_message, parse_mode='Markdown')
    if update.callback_query:
        # Respond to the callback query if it's a button click
        update.callback_query.message.reply_text(apply_message, parse_mode='Markdown')
    else:
        # Respond directly to the message if the command is typed
        update.message.reply_text(apply_message, parse_mode='Markdown')
    # send_message(update, apply_message)

# Function to handle the /contact command
def contact(update: Update, context: CallbackContext) -> None:
    contact_message = (
        "*📞 Contact Us:*\n"
        "- For inquiries and more information:\n\n"
        "📞 Phone: \n       +251-929-444-144,\n       +251-911-764-507\n"
        "*📧 Email*: \n         Namsoneducation@gmail.com,\n         info@namsconsultancy.com\n"
        "*📍 Location*: [Bole Tropical Mall Next to Ramada Hotel, Office #405, Addis Ababa, Ethiopia](https://maps.google.com/?q=8.991310,38.783470)\n"
        "*📦 P.O. Box*: 2371\n\n"
        "*🔗 Social Media*:\n"
        "- **Instagram** 📸 [Namsedu02](https://www.instagram.com/Namsedu02/)\n"
        "- **TikTok** 🎵 [namseducation](https://www.tiktok.com/@namseducation)\n"
        "- **Telegram** 💬 [namsEdu](https://t.me/namsEdu)\n"
        "- **Facebook** 📘 [Namseducationalconsultancy](https://www.facebook.com/Namseducationalconsultancy)\n"
        "- **Website** 🌐 [namseducationalconsultancy.com](https://namseducationalconsultancy.com/)\n\n"
        # "🏢 Address: NAMS Educational Consultancy, Addis Ababa, Ethiopia\n\n"
        "We're here to help you achieve your academic goals! 🎓"
    )
    # update.callback_query.message.reply_text(contact_message, parse_mode='Markdown')
    if update.callback_query:
        # Respond to the callback query if it's a button click
        update.callback_query.message.reply_text(contact_message, parse_mode='Markdown')
    else:
        # Respond directly to the message if the command is typed
        update.message.reply_text(contact_message, parse_mode='Markdown')
    # send_message(update, contact_message)

# Function to handle the /achievements command
def achievements(update: Update, context: CallbackContext) -> None:
    achievements_message = (
        "*🏆 Our Achievements*\n"
        "We take pride in helping thousands of students reach their study abroad dreams. Our achievements include:\n"
        "- Successfully placed students in over 700 universities across 30 countries 🌍\n"
        "- Admitted Students: *250+* 🎓\n"
        "- Got VISA: *120+* ✈️\n"
        "- Achieved a high visa success rate for students applying to multiple destinations ✅\n"
        "- Provided students with scholarships and grants worth millions of dollars 💸\n"
        "- Helped students secure job placements after graduation in various industries 💼\n\n"
        "Let us help you be part of our success story! "
    )
    # update.callback_query.message.reply_text(achievements_message, parse_mode='Markdown')
    if update.callback_query:
        # Respond to the callback query if it's a button click
        update.callback_query.message.reply_text(achievements_message, parse_mode='Markdown')
    else:
        # Respond directly to the message if the command is typed
        update.message.reply_text(achievements_message, parse_mode='Markdown')
    # send_message(update, achievements_message)

# Function to handle messages not linked to a command
def handle_message(update: Update, context: CallbackContext) -> None:
    message_text = update.message.text.lower()

    # Check if the message contains "faq" or similar queries
    if "faq" in message_text or "frequently asked questions" in message_text:
        faq(update, context)
    else:
        fallback_message = (
            "I'm sorry, I didn't understand that. Please use one of the commands listed below:\n"
            "- FOR *Start* /start\n"
            "- For *Course details*, type /services\n"
            "- For *Application Process*, type /apply\n"
            "- For *Contact Info*, type /contact\n"
            "- For *Frequently Asked Questions*, type /faq\n"
            "- For *Destinations*, type /destinations\n"
            "- For *Our Achievements*, type /achievements"
        )
        update.message.reply_text(fallback_message, parse_mode='Markdown')

def main():
    # Replace 'YOUR_API_TOKEN' with the bot token from BotFather
    bot_token = '7859553921:AAHDfvkoNlX48XZg3dMQZyM7yIfwZMsZMow'
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
