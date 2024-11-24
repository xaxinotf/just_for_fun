import asyncio
from aiogram import Bot, Dispatcher
from Handlers import router




async def main():
    bot = Bot(token='7408957680:AAGlhaBOpe-DEvdLqVn49Zxx33pvwwL5qzY')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

asyncio.run(main())