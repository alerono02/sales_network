# Sales Network

----------------------------------------------------

## Описание:

Данная работа представляет собой разработку онлайн платформы торговой сети электроники.
<p>

------------------------------------------------------------------------------------------------

## Функционал:
- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- CRUD для продуктов.
- CRUD для поставщиков.

----------------------------------------------------------------

## Технологии:
- Python
- Django
- Django REST framework
- django-filter
- psycopg2-binary
- JWT 
- DRF-YASG
- Djoser
- Docker
- Docker Compose

------------------------------------------------------------------------------------------------

## Запуск проекта 

**Клонируем проект по ссылке:**
> https://github.com/alerono02/sales_network.git

### Через docker
Создаем контейнер:
> docker build -t my-python-app .

Запускаем:
> docker run my-python-app


### Через docker compose
- Сборка и запуск контейнера в фоновом режиме:
> docker-compose up -d --build

----------------------------------------------------------------

## Краткое техническое задание:

- Создайте веб-приложение, с API интерфейсом и админ-панелью.

- Создайте базу данных используя миграции Django.

**Требования к реализации:**

1) Необходимо реализовать модель сети по продаже электроники.
Сеть должна представлять собой иерархическую структуру из 3 уровней:
- Завод
- Розничная сеть
- Индивидуальный предприниматель

Каждое звено сети ссылается только на одного поставщика оборудования (не обязательно предыдущего по иерархии). Важно отметить, что уровень иерархии определяется не названием звена, а отношением к остальным элементам сети, т.е. завод всегда находится на 0 уровне, а если розничная сеть относится напрямую к заводу, минуя остальные звенья - её уровень - 1.

2) Каждое звено сети должно обладать следующими элементами:

- Название;
- Контакты:
- - Email;
- - Страна;
- - Город;
- - Улица;
- - Номер дома;
- Продукты:
- - Название;
- - Модель;
- - Дата выхода продукта на рынок;
- Поставщик (предыдущий по иерархии объект сети);
- Задолженность перед поставщиком в денежном выражении с точностью до копеек;
- Время создания (заполняется автоматически при создании).

3) Сделать вывод в админ-панели созданных объектов
На странице объекта сети добавить:

- ссылку на «Поставщика»;
- фильтр по названию города;
- «admin action», очищающий задолженность перед поставщиком у выбранных объектов.

4) Используя DRF, создать набор представлений:
CRUD для модели поставщика (запретить обновление через API поля «Задолженность перед поставщиком»);
Добавить возможность фильтрации объектов по определенной стране.

5) Настроить права доступа к API так, чтобы только активные сотрудники имели доступ к API.

--------------------------