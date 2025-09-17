import json
import sys
from flask import Flask, render_template, jsonify
from flask_frozen import Freezer
from flask_flatpages import pygments_style_defs

app = Flask(__name__)
app.config.from_pyfile('config.py')
freezer = Freezer(app)


def _get_settings():
    with open(app.config['SETTINGS_FILE'], encoding='utf8') as config_file:
        return json.load(config_file)


def clean_settings(settings, *seo_keys):
    """
    Удаляет из settings все ключи, которые явно передаются в render_template (site_url, site_title, description, keywords).
    """
    settings_clean = dict(settings)
    for key in ("site_url", "site_title", "description", "keywords") + seo_keys:
        settings_clean.pop(key, None)
    return settings_clean


@app.route("/")
def index():
    settings = _get_settings()
    seo = {
        "site_title": "Военный адвокат в Волгоградской и Астраханской области, Ахтубинске, Волгограде, Волжском — юридическая помощь военнослужащим",
        "description": "Юридическая помощь военнослужащим, участникам СВО, ветеранам и их семьям в Волгоградской и Астраханской области, Ахтубинске, Волгограде, Волжском. Консультации, защита прав, военный адвокат с опытом более 12 лет.",
        "keywords": "военный адвокат Волгоград, военный юрист Волгоградская область, адвокат Ахтубинск, адвокат Волжский, адвокат Астраханская область, юридическая помощь военнослужащим, СВО, военное право, консультация адвоката"
    }
    breadcrumbs = [
        {"name": "Главная", "url": settings.get("site_url", "/")}
    ]
    return render_template(
        'index.html',
        breadcrumbs=breadcrumbs,
        site_url=settings.get("site_url", "/"),
        site_title=seo["site_title"],
        description=seo["description"],
        keywords=seo["keywords"],
        **clean_settings(settings, *seo.keys())
    )

@app.route('/contacts')
def contacts():
    settings = _get_settings()
    seo = {
        "site_title": "Контакты военного адвоката — Волгоград, Астраханская область, Ахтубинск, Волжский",
        "description": "Контакты военного адвоката и юриста в Волгоградской и Астраханской области, Ахтубинске, Волгограде, Волжском. Телефон, email, адрес, соцсети. Запишитесь на консультацию по вопросам военного права.",
        "keywords": "контакты военный адвокат Волгоград, юрист Ахтубинск, адвокат Волжский, консультация, телефон, адрес, юридическая помощь"
    }
    breadcrumbs = [
        {"name": "Главная", "url": settings.get("site_url", "/")},
        {"name": "Контакты", "url": settings.get("site_url", "/contacts")}
    ]
    return render_template(
        'contacts.html',
        breadcrumbs=breadcrumbs,
        site_url=settings.get("site_url", "/contacts"),
        site_title=seo["site_title"],
        description=seo["description"],
        keywords=seo["keywords"],
        **clean_settings(settings, *seo.keys())
    )

@app.route('/resume')
def resume():
    settings = _get_settings()
    seo = {
        "site_title": "Резюме — Военный адвокат Волгоград, Астраханская область, Ахтубинск, Волжский",
        "description": "Резюме и опыт военного адвоката: более 12 лет юридической практики, специализация на защите прав военнослужащих, участников СВО, ветеранов в Волгоградской и Астраханской области.",
        "keywords": "резюме военный адвокат Волгоград, опыт юриста, военное право, адвокат Ахтубинск, адвокат Волжский, юридическая практика"
    }
    breadcrumbs = [
        {"name": "Главная", "url": settings.get("site_url", "/")},
        {"name": "Резюме", "url": settings.get("site_url", "/resume")}
    ]
    return render_template(
        'resume.html',
        breadcrumbs=breadcrumbs,
        site_url=settings.get("site_url", "/resume"),
        site_title=seo["site_title"],
        description=seo["description"],
        keywords=seo["keywords"],
        **clean_settings(settings, *seo.keys())
    )

@app.route('/skills')
def skills():
    settings = _get_settings()
    seo = {
        "site_title": "Навыки военного адвоката — Волгоград, Астраханская область, Ахтубинск, Волжский",
        "description": "Навыки и специализация военного адвоката: воинские преступления, дисциплинарные взыскания, военные пенсии, льготы, жилищные вопросы, помощь участникам СВО.",
        "keywords": "навыки военный адвокат Волгоград, военное право, адвокат Ахтубинск, льготы военнослужащим, юридическая помощь"
    }
    breadcrumbs = [
        {"name": "Главная", "url": settings.get("site_url", "/")},
        {"name": "Навыки", "url": settings.get("site_url", "/skills")}
    ]
    return render_template(
        'skills.html',
        breadcrumbs=breadcrumbs,
        site_url=settings.get("site_url", "/skills"),
        site_title=seo["site_title"],
        description=seo["description"],
        keywords=seo["keywords"],
        **clean_settings(settings, *seo.keys())
    )

@app.route('/interests')
def interests():
    settings = _get_settings()
    seo = {
        "site_title": "Интересы — Военное право, помощь военнослужащим, Волгоград, Астраханская область",
        "description": "Профессиональные интересы военного адвоката: воинские преступления, дисциплинарные взыскания, жилищные вопросы, пенсии, льготы, помощь участникам СВО.",
        "keywords": "интересы военный адвокат Волгоград, военное право, адвокат Ахтубинск, помощь СВО, юридическая помощь"
    }
    breadcrumbs = [
        {"name": "Главная", "url": settings.get("site_url", "/")},
        {"name": "Интересы", "url": settings.get("site_url", "/interests")}
    ]
    return render_template(
        'interests.html',
        breadcrumbs=breadcrumbs,
        site_url=settings.get("site_url", "/interests"),
        site_title=seo["site_title"],
        description=seo["description"],
        keywords=seo["keywords"],
        **clean_settings(settings, *seo.keys())
    )

@app.route('/counters')
def counters():
    settings = _get_settings()
    seo = {
        "site_title": "Статистика и достижения — Военный адвокат Волгоград, Астраханская область",
        "description": "Достижения и статистика: более 12 лет опыта, десятки успешных дел, сотни консультаций по вопросам военного права, СВО, пенсий, льгот.",
        "keywords": "статистика военный адвокат Волгоград, достижения, опыт, юридическая помощь, адвокат Ахтубинск, Волжский"
    }
    breadcrumbs = [
        {"name": "Главная", "url": settings.get("site_url", "/")},
        {"name": "Достижения", "url": settings.get("site_url", "/counters")}
    ]
    return render_template(
        'counters.html',
        breadcrumbs=breadcrumbs,
        site_url=settings.get("site_url", "/counters"),
        site_title=seo["site_title"],
        description=seo["description"],
        keywords=seo["keywords"],
        **clean_settings(settings, *seo.keys())
    )

@app.route('/post/<slug>')
def post(slug):
    settings = _get_settings()
    # Здесь предполагается, что вы получаете пост из базы или файла по slug
    # post = get_post_by_slug(slug)
    post = {"title": "Публикация", "description": "Описание публикации", "tag": "военное право", "project": "Проект", "date": "2024-01-01", "platform": "Платформа", "link": "#", "html": "<p>Текст публикации</p>"}
    seo = {
        "site_title": f"{post['title']} — Публикации военного адвоката, Волгоград, Астраханская область",
        "description": post.get("description", "Публикация военного адвоката по вопросам военного права, СВО, льгот, пенсий, Волгоград, Астраханская область."),
        "keywords": f"{post.get('tag', '')}, публикация, военный адвокат, Волгоград, Астраханская область, Ахтубинск, Волжский"
    }
    breadcrumbs = [
        {"name": "Главная", "url": settings.get("site_url", "/")},
        {"name": "Публикации", "url": settings.get("site_url", "/post")},
        {"name": post['title'], "url": settings.get("site_url", f'/post/{slug}')}
    ]
    return render_template(
        'post.html',
        post=post,
        breadcrumbs=breadcrumbs,
        site_url=settings.get("site_url", f"/post/{slug}"),
        site_title=seo["site_title"],
        description=seo["description"],
        keywords=seo["keywords"],
        **clean_settings(settings, *seo.keys())
    )

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('monokai'), 200, {'Content-Type': 'text/css'}


@app.route('/chatbot_scenario')
def chatbot_scenario():
    with open('static/data/chatbot_texts.json', encoding='utf8') as f:
        data = json.load(f)
    return jsonify(data)


@app.route('/yandex_bfabf8125b1b6900.html')
def yandex_verification():
    return render_template('yandex_bfabf8125b1b6900.html')


@app.errorhandler(404)
def page_not_found(e):
    seo = {
        "site_title": "Страница не найдена — Военный адвокат Волгоград, Астраханская область, Ахтубинск, Волжский",
        "description": "Ошибка 404. Страница не найдена. Юридическая помощь военнослужащим, участникам СВО, ветеранам и их семьям в Волгоградской и Астраханской области.",
        "keywords": "404, страница не найдена, военный адвокат Волгоград, юридическая помощь военнослужащим"
    }
    return render_template(
        '404.html',
        site_url=_get_settings().get("site_url", "/"),
        site_title=seo["site_title"],
        description=seo["description"],
        keywords=seo["keywords"]
    ), 404

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "build":
        freezer.freeze()
    else:
        app.run(host=app.config['HOST'], port=app.config['PORT'], debug=app.config['DEBUG'])
