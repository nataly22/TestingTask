# TestingTask
Для заруска тестов необходимо установить Python 2.7.3 + Selenium
Web Driver _pyTest
Установка ПО для запуска автотестов:
1. Скачать и установить Python 2.7
я устанавливала на диск С в папку C:/Python27(можно взять здесь:
https://www.python.org/downloads/release/python-2714/)
2. Установить и добавить пути в переменную окружения:
C:\Python27;C:\Python27\Scripts;C:\Python27\Lib
3. Установить пакетный менеджер следующим образом:
В папку Python27 скопировать файл «easy_setup.py» - он будет
находиться в папке с файлом «readme»
4. Перейти в папку Python27 и в командной строке написать
команду:
python easy_setup.py install
Установятся все необходимые зависимости (делала по єтому видео:
https://www.youtube.com/watch?v=IKRumAagQ8U – тут
рассказывается где брать содержимое easy_setup.py, но я его уже
готовым кладу в проект)
5. Установить py.test как здесь указано:
https://docs.pytest.org/en/latest/getting-started.html
pip install -U pytest
6. Скачала chromedriver здесь
http://chromedriver.storage.googleapis.com/index.html?path=2.15/
И поместила файл в папку Python27\Scripts
7. Установить Slenium с помощью pip.
Скорее всего устанавливала так: pip install selenium:Запуск автотетстов в командной строке:
1. Перейти в папку проекта Tests
2. В командной строке запускаем тесты с помощью
Py.Test:
py.test test_registration.py test_validation_email.py test_validation_password.py
3. Можно запустить тесты в pyCharm при помощи unitTest
При запуске моих тестов видно, что используются такие
версии ПО:
platform: win32
Python 2.7.14
pyTest 3.3.1
py 1.5.2
pluggy 0.6.0
Могут быть проблемы с установками для 64 разрядных
ПК. Пробовала на компьютере сына, что-то между собой
не состыковалось.
