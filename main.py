import logging

from aiogram import Bot, Dispatcher, executor, types
from buttons import *
from config import API_TOKEN

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    
    await message.reply("""Tilni tanlang / Choose language""",reply_markup=menu)



 ############################################################
############################################################
#menuga qaytish
@dp.callback_query_handler(text="orqaga")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""👋Assalomu alaykum!""",reply_markup=uzb)
#
@dp.callback_query_handler(text="orqaga_1")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""👋 Loyixa haqida...""",reply_markup=loyixa_haqida)

#########################################################

@dp.callback_query_handler(text="uzb")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""👋Assalomu alaykum!

 Sizni kuzatuvchilarimiz safida ko'rganimizdan mamnunmiz!
    
 Yosh menejerlar dasturi Besh tashabbus loyihasi hamda MBM IT kompaniyasi vakillari hamkorligida tashkil etilgan maxsus dastur hisoblanadi!
    
 Ushbu loyiha orqali xalqaro doirada boshqaruv qobiliyatiga ega kadrlar tizimi shakllantiriladi.""",reply_markup=uzb)

@dp.callback_query_handler(text="loyixa_haqida")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""👋 Loyixa haqida...""",reply_markup=loyixa_haqida)

@dp.callback_query_handler(text="loyixa_maq")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""🔰 Yosh Menejerlar dasturi nima maqsadda tashkil etilmoqda?

  Mazkur loyiha 17 yoshdan 25 yoshgacha bo'lgan yoshlar 
  qatlamini loyihalar boshqaruvi bo'yicha 
  nazariy jihatdan o'qitish, amaliy jihatdan yoshlarga 
  ish tajribasini ulashish, turli fikr va 
  dunyoqarashga ega shaxslar orasida muloqot almashinuvini 
  yo'lga qo'yish maqsadida tashkil etilgan.""",reply_markup=loyixaning_maqsadi)

@dp.callback_query_handler(text="loyixa_vaz")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""🔰 Loyihaning vazifalari nimalardan iborat?

 • Boshqaruv sohasida malakaga ega, xalqaro doirada faoliyat yurita oladigan mutaxassislar tayyorlab, 
 davlat va nodavlat sektoridagi subyekt/obyektlar uchun salohiyatli kadrlar tizimini yaratib berish;

 • Yoshlarning bilim va ko'nikmasini oshirib, yuqori daromad keltiradigan ish bilan ta'minlash;

 • Kattalar va yoshlar orasida kommunikatsiya jarayonini shakllantirib, 
 o'rtadagi "jarlik"ka ma'lum ma'noda chek qo'yish, 
 ularning o'zaro hamkorligini ta'minlashga ko'maklashish.""",reply_markup=loyixaning_vazifasi)

@dp.callback_query_handler(text="o'tkazish_tar")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""🔰 Loyiha qancha vaqt davom etadi va o'tkazilish tartibi qanday?

 📝Yosh menejerlar dasturining o’tkazilish tartibi:

 Loyiha 10 hafta davomida bo'lib o'tadi: amaliy va nazariy darslar olib boriladi.

 📋 Avgust oyining 25-sanasidan boshlab 10-Sentabr kuniga qadar loyihada ishtirok etishga nomzod shaxslarni 
 ro'yxatdan o'tkazish va saralash jarayoni tashkil etiladi:

• 1-bosqichi saralashdan o’tganlar: 13 Sentabr e’lon qilinadi. (100 ta ishtirokchi);
• 2-saralash bosqichi: 15-16 Sentabr kuni bo’lib o’tadi;
• Javoblar: 18 Sentabr kuni e’lon qilinadi (50 ta ishtirokchi).

 💡 Nomzodlar ichidan 50 nafar kuchga to'la, ingliz tilini yaxshi biluvchi, 
 o'z ambitsiyalariga ega va kelajakda katta maqsadlari bor yoshlar 
 tanlab olinadi.""",reply_markup=utkazish_tartibi)

@dp.callback_query_handler(text="talablar")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""🔰 Loyihada qatnashish uchun nomzodlarga qanday talablar qo'yiladi?

 — ingliz, rus, o'zbek tilida ish yuritish: erkin so'zlashish va yoza olish;
 — IT texnologiyalari hamda mediasavodxonlik bo'yicha bilimga egalik;
 — 17-25 yosh orasida bo'lish;
 — Toshkent shahri va viloyati hududida istiqomat qilish.""",reply_markup=talablar)

@dp.callback_query_handler(text="ro'yxatdan_o'tosh")
async def echo(call: types.CallbackQuery):
	await call.answer("siz ro'yxatdan o'tdingiz",show_alert = True)	


############################################################################
@dp.callback_query_handler(text="Back_1")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""👋Assalomu alaykum!

 We are glad to see you among our observers! 
    
 The Young Managers Program is a special project organized in collaboration 
 with the Five Initiative Project and representatives of MBM IT Company! 
    
 Through this program personnel management skills system will be formed in 
 the international arena.""",reply_markup=english)

@dp.callback_query_handler(text="Back_2")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""About the project""",reply_markup=abaut_the_project)
##############################################################################
@dp.callback_query_handler(text="in")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""👋Assalomu alaykum!

 We are glad to see you among our observers! 
    
 The Young Managers Program is a special project organized in collaboration 
 with the Five Initiative Project and representatives of MBM IT Company! 
    
 Through this program personnel management skills system will be formed in 
 the international arena.""",reply_markup=english)

@dp.callback_query_handler(text="abaut_the")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""About the project""",reply_markup=abaut_the_project)

@dp.callback_query_handler(text="aim_of_the_project")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""🔰 What is the main purpose of the Young Managers Program?

 Project is designed to provide theoretical training in project management to young people
  from aged 17 to 25, to share practical work experience with young people, and to establish a community 
  between people with different ideas and worldviews.""",reply_markup=aim_of_the_project)

@dp.callback_query_handler(text="project_task")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""🔰 What are the objectives of project? 

 • Training of specialists with international qualifications in the field of management and creation 
 of a potential human resources system for entities and objects in the public and private sectors;

 • Providing high-paid jobs to increase the knowledge and skills of youth; 

 • To form a process of communication between the older and younger generations, 
 to put an end to the "cliff" between them, 
 to help them to ensure their interaction;""",reply_markup=project_task)

@dp.callback_query_handler(text="the_order_of_process")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""🔰 How long will the project last and what is the procedure?

  📝 Procedure for the Young Managers Program:

  The project will last for 10 weeks: practical and theoretical lessons will be conducted.

  📋 From August 25 to September 10, the process of registration and selection of candidates 
  for participation in the project will be organized:

• Round 1 qualifiers: September 13 will be announced. (100 participants);
• Qualifying Round 2: September 15-16;
• Answers: to be announced on September 18 (50 participants).

  💡 Out of the candidates, 50 young people who are strong, fluent in English, 
  have their own ambitions and have big goals 
  for the future will be selected""",reply_markup=the_order_of_process)

@dp.callback_query_handler(text="requirements")
async def echo(call: types.CallbackQuery):
	await call.message.answer("""🔰 What are the requirements for candidates to participate?

 — Office work in English, Russian, Uzbek: fluent speaking and writing skills;
 — Knowledge of IT and media; 
 — 17-25 years old;
 — Resident of Tashkent city and region.""",reply_markup=requirements)

@dp.callback_query_handler(text="registration")
async def echo(call: types.CallbackQuery):
	await call.answer("registration")	


##############################################################








if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
