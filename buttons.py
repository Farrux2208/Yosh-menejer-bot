from aiogram.types import *

bosh_sahifa = ReplyKeyboardMarkup(
	keyboard=[
		[
			KeyboardButton(text="Buyurtma berish 👩‍💻")
		],
		[
			KeyboardButton(text="Sozlamalar"),
			KeyboardButton(text="Biz bilan aloqa")
		],
	],resize_keyboard=True
)

menu = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="🇺🇿 uzbekcha",callback_data="uzb"),
			InlineKeyboardButton(text="🇺🇸 English",callback_data="in"),
		],
	],
)

uzb = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Loyixa haqida",callback_data="loyixa_haqida"),
			InlineKeyboardButton(text="Ro'yxatdan o'tosh",callback_data="ro'yxatdan_o'tosh"),
		],
		[
			InlineKeyboardButton(text="Savollar yo'llansh",callback_data="savollar_yo'llansh"),
		],
	],
)

loyixa_haqida = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="loyixa maqsadi",callback_data="loyixa_maq"),
			InlineKeyboardButton(text="Loyiza vazifasi",callback_data="loyixa_vaz"),
		],
		[
			InlineKeyboardButton(text="O'tkazilish tartibi",callback_data="o'tkazish_tar"),
			InlineKeyboardButton(text="Talablar",callback_data="talablar"),
		],
		[
			InlineKeyboardButton(text="orqaga",callback_data="orqaga"),
		],
	],
)

loyixaning_maqsadi = InlineKeyboardMarkup(
	inline_keyboard=[
		
		[
			InlineKeyboardButton(text="orqaga",callback_data="orqaga_1"),
		],
	],
)

loyixaning_vazifasi = InlineKeyboardMarkup(
	inline_keyboard=[
		
		[
			InlineKeyboardButton(text="orqaga",callback_data="orqaga_1"),
		],
	],
)

utkazish_tartibi = InlineKeyboardMarkup(
	inline_keyboard=[
		
		[
			InlineKeyboardButton(text="orqaga",callback_data="orqaga_1"),
		],
	],
)

talablar = InlineKeyboardMarkup(
	inline_keyboard=[
		
		[
			InlineKeyboardButton(text="orqaga",callback_data="orqaga_1"),
		],
	],
)

###################################################
english = InlineKeyboardMarkup(
	inline_keyboard=[
		[
			InlineKeyboardButton(text="Abaut the project",callback_data="abaut_the"),
			InlineKeyboardButton(text="Registration",callback_data="registration"),
		],
		[
			InlineKeyboardButton(text="Send questions",callback_data="send_q"),
		],
	],
)

abaut_the_project = InlineKeyboardMarkup(
	inline_keyboard=[

		[
			InlineKeyboardButton(text="Aim of the project",callback_data="aim_of_the_project"),
			InlineKeyboardButton(text="project task ",callback_data="project_task"),
		],
		[
			InlineKeyboardButton(text="The order of process",callback_data="the_order_of_process"),
			InlineKeyboardButton(text="Requirements",callback_data="requirements"),
		],
		[
			InlineKeyboardButton(text="Back",callback_data="Back_1"),
		],
	],
)

aim_of_the_project = InlineKeyboardMarkup(
	inline_keyboard=[
		
		[
			InlineKeyboardButton(text="Back",callback_data="Back_2"),
		],
	],
)

project_task = InlineKeyboardMarkup(
	inline_keyboard=[
		
		[
			InlineKeyboardButton(text="Back",callback_data="Back_2"),
		],
	],
)

the_order_of_process = InlineKeyboardMarkup(
	inline_keyboard=[
		
		[
			InlineKeyboardButton(text="Back",callback_data="Back_2"),
		],
	],
)

requirements = InlineKeyboardMarkup(
	inline_keyboard=[
		
		[
			InlineKeyboardButton(text="Back",callback_data="Back_2"),
		],
	],
)
##############################################################
