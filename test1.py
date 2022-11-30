from selenium import webdriver
from array import *
import time
import keyboard
import os



#try:
def main():
	driver = webdriver.Chrome()

	driver.get("") # убрал ссылку, чтобы не палить проект

	print("*********   TEST 1   *********")


	# ФУНКЦИЯ ДОБАВЛЕНИЯ ТОВАРА В КОРЗИНУ
	def product():
		tov = []
		tov = driver.find_elements_by_class_name("add-to-basket__button")
		tov[num_product].click()


	# ФУНКЦИЯ НАЖАТИЯ НА КНОПКУ ПЕРЕХОДА В КОРЗИНУ
	def basket():
		time.sleep(3)
		korz = driver.find_element_by_class_name("button--primary")
		korz.click()
		time.sleep(2)


	# ФУНКЦИЯ ОТКРЫТИЯ АККОРДИОНА В КОРЗИНЕ
	def search_accordeon():
		accordion = []
		accordion = driver.find_elements_by_class_name("js-accordion-block")
		accordion[num].click()


	# ФУНКЦИЯ ЗАКРЫТИЯ АЛЕРТА	
	def close_alert():
		time.sleep(4)
		btn_close = driver.find_element_by_class_name("js-modal-close-btn")
		btn_close.click()
		print("алерт закрыт")
		time.sleep(3)
	try:	

		# ДОБАВЛЯЕМ В КОРЗИНУ 1 ТОВАР	
		num_product = 1
		product()
		print("товар 1 в корзине")

		# НАЖИМАЕМ ЗАКРЫТЬ
		close_alert()

		# ДОБАВЛЯЕМ ТОВАР 2 В корзину
		num_product = 6
		product()
		print("товар 2 в корзине")

		#ПЕРЕХОДИМ В КОРЗИНУ
		basket()

	except Exception:
    #
    # попытки закрыть рандомно появляюзийся баннер
    #
		print(" СРАБОТАЛО ИСКЛЮЧЕНИЕ 1")
		time.sleep(15)
		keyboard.write("{ESC}")

		try:
			num_product = 0
			product()
			print("товар 3 (экстренный) в корзине")
			basket()

		except Exception:
			print(" СРАБОТАЛО ИСКЛЮЧЕНИЕ 2")

			try:
				close_alert()
				num_product = 7
				product()
				print("товар 4 (экстренный) в корзине")

				basket()

			except Exception:
				print(" СРАБОТАЛО ИСКЛЮЧЕНИЕ 3")
				keyboard.write("{ESC}")
				num_product = 7
				product()
				print("товар 5 (экстренный) в корзине")

				basket()




	finally:

		print("переход в корзину успешен")

		# ОТКРЫТИЕ АККОРДИОНА 1
		num = 0
		search_accordeon()
		time.sleep(1)
		print("аккордеон нажат")

		# ВВОД ЛОГИНА
		form_lodin = driver.find_element_by_id("desktop-inputEmailAuthorization")
		form_lodin.click()
		form_lodin.send_keys("yurij.strukov@nova-test.ru")
		print("логин введён")

		# ВВОД ПАРОЛЯ
		form_password = driver.find_element_by_id("desktop-inputPasswordAuthorization")
		form_password.click()
		form_password.clear()
		form_password.send_keys("Zzaaqq11")
		print("пароль введён")

		# НАЖАТИЕ НА КНОПКУ ВХОДА
		btn_entry = driver.find_element_by_class_name("form__entry-btn")
		btn_entry.click()
		time.sleep(4)
		print("вход успешен")

		# ОТКРЫТИЕ АККОРДИОНА 2
		num = 1
		search_accordeon()
		print("аккордеон 2 нажат")
		time.sleep(2)

		# НАЖАТИЕ НА КНОПКУ ПОИСКА ГОРОДА
		btn_search = driver.find_element_by_class_name("select-search__button")
		btn_search.click()
		time.sleep(2)


		# НАЖАТИЕ НА ФОРМУ ПОИСКА ГОРОДА
		form_search = driver.find_element_by_class_name("js-delivery-city-input")
		form_search.click()
		form_search.send_keys("Курс")
		print("поиск города осуществлён")
		time.sleep(2)


		# ФУНКЦИЯ ВЫБОРА ГОРОДА ИЗ СПИСКА
		def search_town():
			town_name = []
			town_name = driver.find_elements_by_class_name("dropdown-select__item")
			town_name[townNumber].click()
			print("город выбран")


		# ВЫБОР ГОРОДА ИЗ СПИСКА
		try:
			townNumber = 0
			search_town()

		except Exception():
			print(" ГОРОД ВЫБРАТЬ НЕ УДАЛОСЬ")
			town_name.location_once_scrolled_into_view 
			search_town()




		# УКАЗАНИЕ УЛИЦЫ
		form_street = driver.find_element_by_name("Street")
		form_street.click()
		form_street.send_keys("Тестовая")
		print("улица указана")

		# УКАЗАНИЕ ДОМА
		form_home = driver.find_element_by_name("Home")
		form_home.click()
		form_home.send_keys("1")
		print("дом указан")

		# НАПИСАНИЕ КОММЕНТАРИЯ
		form_comment = driver.find_element_by_name("delivery-comment")
		form_comment.click()
		form_comment.send_keys("Заказ создан автоматически и является тестовым, отмените его сразу, как увидете")
		print("комментарий написан")

		# НАПИСАНИЕ КОММЕНТАРИЯ
		btn_proceed = driver.find_element_by_class_name("checkout__section-submit--delivery")
		btn_proceed.click()
		print('кнопка "продолжить" нажата')
		time.sleep(2)


		# ОТКРЫТИЕ АККОРДИОНА 3
		num = 2
		search_accordeon()
		print("аккордеон 3 нажат")
		time.sleep(2)


		# ВЫБОР ДОСТАВКИ ПРИ ПОЛУЧЕНИИ
		def radio_blo():
			radio = []
			radio = driver.find_elements_by_class_name("radio-block--images")
			radio[1].click()
			print("доставка при получении выбрана")


		# УДАЛЕНИЕ ТОВАРА ИЗ КОРЗИНЫ
		def delete():
			btn_delete = []
			btn_delete = driver.find_elements_by_class_name("basket-item__delete-text")
			btn_delete[0].click()
			time.sleep(5)
			print(" ТОВАР УДАЛЁН ИЗ КОРЗИНЫ")

		flag = True


		# ФУНКЦИЯ ПОЛУЧЕНИЯ КОЛ-ВА ЭЛЕМЕНТОВ КОРЗИНЫ + ПРОВЕРКА КОЛ-ВА
		def quantity_basket():
			form_quantity = []
			form_quantity = driver.find_elements_by_name("result")
			print("В корзине " + str(len(form_quantity)) + " разных товара")

			if (len(form_quantity) > 2):
				delete()
				quantity_basket()
			else:
				flag = False
				return flag
				fun_test_price()

				


		# ФУНКЦИЯ ПОЛУЧЕНИЯ ИТОГОВОЙ СТОИМОСТИ БЕЗ ПРОБЕЛА
		def fun_test_price():

			try:
				if (flag == True):
					text_price = driver.find_element_by_class_name("js-checkout-total-price").text
					# УБИРАЕМ ПРОБЕЛ ТУТ
					text_price = ''.join(text_price.split())
					print(text_price)
					

					# ЕСЛИ ИТОГОВАЯ ЦЕНА МЕНЬШЕ 100 000
					if (int(text_price) < 100000):

						radio_blo()
						time.sleep(2)

					else:
						print(" СРАБОТАЛО ИСКЛЮЧЕНИЕ, СЛИШКОМ БОЛЬШАЯ ЦЕНА")	
						quantity_basket()


				elif (flag == False):
					form_quantity = []
					form_quantity = driver.find_elements_by_class_name("result").text
					form_quantity = input.split(", ")
					print("в корзине элементов " + form_quantity)

			except Exception:
				print(" ошибка")

			finally:
				text_price = driver.find_element_by_class_name("js-checkout-total-price").text
				# УБИРАЕМ ПРОБЕЛ ТУТ
				text_price = ''.join(text_price.split())
				print(text_price)

				if (int(text_price) > 100000):
					fun_test_price()
					
			

		
		fun_test_price()
		print(" ТЕСТ ВЫПОЛНЕН")
		time.sleep(25)




if __name__ == "__main__":
	main()

#except Exception:
	#print(" ТЕСТ ПРЕРВАН")
	#time.sleep(15)

	#os.startfile("test2.py")
