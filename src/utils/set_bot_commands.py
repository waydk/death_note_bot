from aiogram import types


async def set_default_commands(dp):
    await dp.bot.set_my_commands([
        types.BotCommand("help", "Gather information"),
        types.BotCommand("rules", "Show the rules"),
        types.BotCommand("write", "Simplified write_down command"),
        types.BotCommand("write_down", "Write in the death note"),
        types.BotCommand("death_list", "Show death note"),
        types.BotCommand("settings", "Open settings"),
        types.BotCommand("top", "top users by apples"),
        types.BotCommand("shop", "buy something"),
    ])
