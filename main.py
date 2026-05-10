import os

from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    CallbackQueryHandler
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

CHANNELS = [
    "LEGEND_MARKETt",
    "PulseSenderUpdates"
]

PRIVATE_GROUP_LINK = "https://t.me/+ojvio8vThl0yNWE1"


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

    verified = await check_user(
        user_id,
        context.bot
    )

    if verified:

        await update.message.reply_text(
            "✅ Verification Successful!\n\nWelcome to Pulse Sender 🔥"
        )

        return

    buttons = [

        [
            InlineKeyboardButton(
                "📢 Join LEGEND MARKET",
                url="https://t.me/LEGEND_MARKETt"
            )
        ],

        [
            InlineKeyboardButton(
                "📢 Join Updates Channel",
                url="https://t.me/PulseSenderUpdates"
            )
        ],

        [
            InlineKeyboardButton(
                "👥 Join Private Group",
                url=PRIVATE_GROUP_LINK
            )
        ],

        [
            InlineKeyboardButton(
                "✅ I've Joined",
                callback_data="check_join"
            )
        ]
    ]

    reply_markup = InlineKeyboardMarkup(buttons)

    await update.message.reply_text(
        "⚠️ Please join all required channels first to continue.",
        reply_markup=reply_markup
    )


async def button_click(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    query = update.callback_query

    await query.answer()

    user_id = query.from_user.id

    verified = await check_user(
        user_id,
        context.bot
    )

    if verified:

        await query.message.reply_text(
            "✅ Access Granted!\n\nWelcome to Pulse Sender 🔥"
        )

    else:

        await query.message.reply_text(
            "❌ Please join all required channels first."
        )


app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(
    CommandHandler("start", start)
)

app.add_handler(
    CallbackQueryHandler(button_click)
)

print("Bot Running 🔥")

app.run_polling()
