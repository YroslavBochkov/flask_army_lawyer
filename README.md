
**Пояснения:**

* **Заголовок:**  

Сайт адвокатского кабинета Садикова А.А., создающий иллюзию многостраничного сайта.

[![Netlify Status](https://api.netlify.com/api/v1/badges/e5bfe431-250a-41ab-a7c0-b464e6d7e24d/deploy-status)](https://app.netlify.com/projects/armylawer/deploys)

* **Описание:**

Сайт адвокатского кабинета Садикова А.А. представляет собой одностраничник, выполненный для целей презентации услуг адвоката и контактной информации. Имеет форму обратной связи.

* **Особенности:**  

Легкий одностраничник с иллюзией переходов на другие страницы.

---

## Чат-бот по военному праву

На сайте реализован современный чат-бот для консультаций по вопросам военного права, защиты прав военнослужащих, участников СВО и их семей.

**Возможности чат-бота:**
- Быстрый выбор темы: увольнение, дисциплинарные взыскания, выплаты, мобилизация, СВО, другое.
- В разделе "Вопросы СВО" — отдельные подразделы по льготам, выплатам и другим вопросам.
- Мгновенный доступ к контактам адвоката (телефон, WhatsApp, Telegram) по любому вопросу.
- Нет сбора персональных данных: бот не просит оставить номер телефона.
- Современный дизайн в фирменных цветах сайта, адаптивность для мобильных устройств.
- Легко расширяется и редактируется через файл `static/data/chatbot_texts.json`.

**Как работает чат-бот:**
- Кнопка 💬 всегда доступна в правом нижнем углу сайта.
- После нажатия открывается окно с выбором темы.
- Для каждой темы — краткая справка и кнопки для связи с адвокатом.
- В разделе "Вопросы СВО" — выбор между льготами, выплатами и другими вопросами, далее также доступны контакты для консультации.

**Технологии:**
- Чистый JavaScript, Flask, хранение сценария в JSON.
- Стилизация через отдельный CSS-файл, интеграция с шаблонами Jinja2.

---

* **Установка и запуск:**  

Сайт можно установить и запустить на любом веб-сервере. Адаптивная верстка позволяет сайту отлично смотреться на всех типах устройств. 

1. **Клонируйте репозиторий:**

```bash
git clone https://github.com/ваш_github/ваш_репозиторий.git
```
2.  **Создайте и активируйте виртуальное окружение:**

```
python3 -m venv venv
source [venv/bin/activate](VALID_FILE)  # Linux/macOS
venv\Scripts\activate  # Windows
```

3. **Установите зависисмости:**

```
pip install -r requirements.txt
```

4. **Запустите сайт:**

```
python mysite.py
```
Сайт будет доступен по адресу http://127.0.0.1:8000/.

* **Используемые технологии**

## Используемые технологии

[![Python](https://img.shields.io/badge/Python-3.9-blue)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-1.1.1-blue)](https://flask.palletsprojects.com/en/1.1.x/)
[![Flask-FlatPages](https://img.shields.io/badge/Flask--FlatPages-0.7.1-blue)](https://flask-flatpages.readthedocs.io/en/latest/)
[![Frozen-Flask](https://img.shields.io/badge/Frozen--Flask-0.15-blue)](https://pythonhosted.org/Frozen-Flask/)
[![Jinja2](https://img.shields.io/badge/Jinja2-2.10.3-blue)](https://jinja.palletsprojects.com/en/2.10.x/)
[![Markdown](https://img.shields.io/badge/Markdown-3.1.1-blue)](https://python-markdown.github.io/reference/)
[![Pygments](https://img.shields.io/badge/Pygments-2.4.2-blue)](https://pygments.org/)
[![PyYAML](https://img.shields.io/badge/PyYAML-5.1.2-blue)](https://pyyaml.org/en/stable/)
[![Click](https://img.shields.io/badge/Click-7.0-blue)](https://click.palletsprojects.com/en/7.x/)
[![Werkzeug](https://img.shields.io/badge/Werkzeug-0.16.0-blue)](https://werkzeug.palletsprojects.com/en/0.16.x/)
* **Лицензия:**  Информация о лицензии проекта.

Этот проект распространяется под лицензией [MIT](LICENSE).

* **Автор:**  

[YroslavBochkov](https://github.com/YroslavBochkov)
