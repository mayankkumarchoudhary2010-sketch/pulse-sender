from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler
)

BOT_TOKEN = "8631125046:AAH2vAr9ZpHGSy0nqsdk2CBr98S386fs0uo"

CHANNELS = [
    "LEGEND_MARKETt",
    "PulseSenderUpdates"
]

PRIVATE_GROUP = "https://t.me/+ojvio8vThl0yNWE1"

async def check_user(user_id, bot):
    try:
        for channel in CHANNELS:
            member = await bot.get_chat_member(
                chat_id=f"@{channel}",
                user_id=user_id
            )

            if member.status not in [
                "member",
                "administrator",
                "creator"
            ]:
                return False

        return True

    except:
        return False

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    verified = await check_user(user_id, context.bot)

    if verified:

        await update.message.reply_text(
            "✅ Verified!\n\nWelcome to Pulse Sender 🔥"
        )

        return

    buttons = [
        [
            InlineKeyboardButton(
                "📢 Join Channel 1",
                url="https://t.me/LEGEND_MARKETt"
            )
        ],
        [
            InlineKeyboardButton(
                "📢 Join Channel 2",
                url="https://t.me/PulseSenderUpdates"
            )
        ],
        [
            InlineKeyboardButton(
                "👥 Join Group",
                url=PRIVATE_GROUP
            )
        ],
        [
            InlineKeyboardButton(
                "✅ I've Joined",
                callback_data="check"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(
        "⚠️ Please join all required channels/groups first.",
        reply_markup=reply_markup
    )

async def button_click(update: Update, context: ContextTypes.DEFAULT_TYPE):

    query = update.callback_query

    await query.answer()

    user_id = query.from_user.id

    verified = await check_user(user_id, context.bot)

    if verified:

        await query.message.reply_text(
            "✅ Verification Successful!\n\nWelcome to Pulse Sender 🔥"
        )

    else:

        await query.message.reply_text(
            "❌ You haven't joined all channels/groups yet."
        )

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(button_click))

print("Bot Running 🔥")

app.run_polling()
