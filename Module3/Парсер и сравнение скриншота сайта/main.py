import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from PIL import Image
import numpy as np

def take_screenshot(url, screenshot_path):
    # Настройки браузера
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Запуск в фоновом режиме
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)

    try:
        driver.get(url)

        # Явное ожидание, пока элемент с тегом 'body' не станет доступным
        WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Небольшая задержка перед сохранением скриншота
        time.sleep(2)

        driver.save_screenshot(screenshot_path)
        print(f"Скриншот сохранен как {screenshot_path}")
    finally:
        driver.quit()

def compare_images(image1_path, image2_path):
    # Открытие изображений
    img1 = Image.open(image1_path)
    img2 = Image.open(image2_path)

    # Преобразование изображений в массивы
    arr1 = np.array(img1)
    arr2 = np.array(img2)

    # Сравнение размеров изображений
    if arr1.shape != arr2.shape:
        print("Изображения имеют разные размеры.")
        return False

    # Сравнение изображений
    difference = np.sum(arr1 != arr2)
    total_pixels = arr1.size
    similarity = (total_pixels - difference) / total_pixels

    if similarity == 1.0:
        print("Изображения идентичны.")
        return True
    elif similarity >= 0.5:
        print("Сходство найдено на 50% или более.")
        # continue_work = input("Хотите продолжить работу? (да/нет): ")
        # if continue_work.lower() == 'да':
        #     print("Продолжаем работу...")
        #     return True
        # else:
        #     print("Остановка работы.")
        #     return False
    else:
        print(f"Изображения различаются в {difference} пикселях.")
        os.remove(screenshot_path)

        return False
        
# Пример использования
base_url = "https://kinescope.io/embed/"  # Замените на нужный базовый URL
start_number = 204820000  # Начальное число
end_number = 1     # Конечное число
screenshot_path_template = "screenshot_{}.png"
reference_image_path = "image.png"

for number in range(start_number, end_number - 1, -1):
    url = f"{base_url}{number}"
    screenshot_path = screenshot_path_template.format(number)

    # Снимаем скриншот
    take_screenshot(url, screenshot_path)

    # Сравниваем с существующим изображением
    if compare_images(screenshot_path, reference_image_path):
        print(f"Сравнение для {url} завершено.")
        # maybeexit = input('Вы хотите завершить работу? Да/Нет: ')
        # if maybeexit.lower() == 'да':
        #     break
    else:
        print(f"Сравнение для {url} завершено с различиями.")


