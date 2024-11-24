from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import CommandStart, Command

router = Router()

@router.message(CommandStart())
async def echo(message: Message):
    await message.answer('Привет!')

@router.message(Command('balance'))
async def balance(message: Message):
    await message.answer('Your Balance: 100$')


@router.message(Command('chanell'))
async def balance(message: Message):
    await message.answer('Лучший челик по программированию - @xaxiNotF')

@router.message(F.text == 'как дела')
async def nice(message: Message):
    await message.answer('nice')