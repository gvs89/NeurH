from aiogram import types


def generate_main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(types.KeyboardButton("Записаться на прием к врачу"))
    keyboard.add(types.KeyboardButton("Узнать расписание работы клиники"))
    keyboard.add(types.KeyboardButton("Уточнить адрес и контактную информацию клиники"))
    return keyboard


def generate_directions_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add("Гепатология", "Гинекология", "Диагностика")
    keyboard.add("Неврология", "Онкология", "Урология")
    keyboard.add("Флебология", "Химиотерапия", "Хирургия")
    keyboard.add("Центр возрастной и эстетической медицины", "Эндоскопия")
    keyboard.add("Назад")
    return keyboard


def generate_doctors_keyboard(direction):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if direction == "hepatology":
        keyboard.add("Орлова Юлия Михайловна")
    elif direction == "gynecology":
        keyboard.add("Колесник Элина Владимировна", "Щамхалова Камилла Керимовна",
                     "Гумерова Динара Радиковна", "Строгонова Оксана Александровна")
    elif direction == "diagnostics":
        keyboard.add("Михайлова Людмила Кирилловна", "Бельцевич Михаил Дмитриевич",
                     "Мангутов Фарид Шамилевич", "Меринов Дмитрий Станиславович",
                     "Ким Мария Эмильевна", "Скипенко Тимофей Олегович")
    elif direction == "neurology":
        keyboard.add("Акарачкова Елена Сергеевна")
    elif direction == "oncology":
        keyboard.add("Разуваев Никита Владимирович", "Таривердиев Андрей Михайлович",
                     "Мангутов Фарид Шамилевич")
    elif direction == "urology":
        keyboard.add("Разуваев Никита Владимирович", "Меринов Дмитрий Станиславович",
                     "Щамхалова Камилла Керимовна")
    elif direction == "phlebology":
        keyboard.add("Разуваев Никита Владимирович")
    elif direction == "chemotherapy":
        keyboard.add("Таривердиев Андрей Михайлович")
    elif direction == "surgery":
        keyboard.add("Орлова Юлия Михайловна", "Гебуадзе Георгий", "Меринов Дмитрий Станиславович",
                     "Разуваев Никита Владимирович", "Вавин Вячеслав Валерьевич")
    elif direction == "age_esthetics":
        keyboard.add("Орлова Юлия Михайловна", "Бельцевич Михаил Дмитриевич", "Разуваев Никита Владимирович",
                     "Мангутов Фарид Шамилевич")
    elif direction == "endoscopy":
        keyboard.add("Иванов Сергей Сергеевич", "Давлетшина Алина Юрьевна")
    keyboard.add("Назад")
    return keyboard


def generate_start_menu():
    return None