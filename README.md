# Каталог автомобилей
Страница с данными автомобилей.  
Список полей:
* производитель
* модель
* год
* коробка передач
* цвет

![](https://i.imgur.com/qRpwYQk.png)

Автомобили можно фильтровать с помощью формы в шапке страницы: достаточно ввести нужные значения в поля и нажать на кнопку «Найти автомобили». Заполнять все поля необязательно. Фильтрация учитывает подстроки: например, сочетание **BM** в поле «Производитель» выведет все модели **BMW**.

### Как развернуть 
#### Windows
1. Склонируйте репозиторий и создайте внутри папки виртуальное окружение:
```
git clone https://github.com/charlieplanka/D10-django-car-filter.git
cd D10-django-car-filter
virtualenv venv
```
2. Активируйте окружение и установите зависимости:
```
.\venv\Scripts\activate
pip install -r requirements.txt
```
3. Запустите сервер (по умолчанию поднимется на 8000 порту):
```
python manage.py runserver
```

#### Linux
1. Склонируйте репозиторий и создайте внутри папки виртуальное окружение:
```
git clone https://github.com/charlieplanka/D10-django-car-filter.git
cd D10-django-car-filter
python3 -m venv venv
```
2. Активируйте окружение и установите зависимости:
```
source venv/bin/activate
pip install -r requirements.txt
```
3. Запустите сервер (по умолчанию поднимется на 8000 порту):
```
python manage.py runserver
```
