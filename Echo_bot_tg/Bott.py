import asyncio
from aiogram import Bot, Dispatcher
from Handlers import router




async def main():
    bot = Bot(token='********************')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

asyncio.run(main())