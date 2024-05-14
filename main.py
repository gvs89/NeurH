import logging
import executor
from aiogram import Bot, Dispatcher, types
from config import token
from keyboards import generate_start_menu, generate_main_menu, generate_directions_keyboard, generate_doctors_keyboard

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

# Инициализация бота и диспетчера
Bot = Bot(token)
dp = Dispatcher()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer("Добрый день, Вас приветствует Международная Академическая Клиника МАК!",
                         reply_markup=generate_start_menu())


@dp.message_handler(lambda message: message.text == "Начать общение")
async def greeting_handler(message: types.Message):
    await message.answer("Какой у Вас вопрос?", reply_markup=generate_main_menu())


@dp.message_handler(lambda message: message.text == "Записаться на прием к врачу")
async def appointment_handler(message: types.Message):
    await message.answer("Выберите направление:", reply_markup=generate_directions_keyboard())


@dp.message_handler(lambda message: message.text == "Узнать расписание работы клиники")
async def schedule_handler(message: types.Message):
    await message.answer("Режим работы: Поликлиника: 08:00-21:00, Стационар: круглосуточно")


@dp.message_handler(lambda message: message.text == "Уточнить адрес и контактную информацию клиники")
async def address_handler(message: types.Message):
    await message.answer("Адрес клиники: г. Москва, ул. Автозаводская, д. 16, корпус 2, М. Автозаводская, МЦК ЗИЛ. "
                         "Телефон: +7 (495) 492-17-21")


@dp.message_handler(lambda message: message.text == "Назад")
async def back_handler(message: types.Message):
    await message.answer("Какой у Вас вопрос?", reply_markup=generate_main_menu())


@dp.message_handler(lambda message: message.text in ["Гепатология", "Гинекология", "Диагностика",
                                                     "Неврология", "Онкология", "Урология",
                                                     "Флебология", "Химиотерапия", "Хирургия",
                                                     "Центр возрастной и эстетической медицины",
                                                     "Эндоскопия"])
async def directions_handler(message: types.Message):
    doctors = {
        "Гепатология": "hepatology",
        "Гинекология": "gynecology",
        "Диагностика": "diagnostics",
        "Неврология": "neurology",
        "Онкология": "oncology",
        "Урология": "urology",
        "Флебология": "phlebology",
        "Химиотерапия": "chemotherapy",
        "Хирургия": "surgery",
        "Центр возрастной и эстетической медицины": "age_esthetics",
        "Эндоскопия": "endoscopy"
    }
    direction = doctors.get(message.text)
    await message.answer("Выберите врача:", reply_markup=generate_doctors_keyboard(direction))


@dp.message_handler(lambda message: message.text == "Назад")
async def back_to_main_handler(message: types.Message):
    await message.answer("Какой у Вас вопрос?", reply_markup=generate_main_menu())


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
