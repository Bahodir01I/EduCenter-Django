import os
import polib

def create_translation(lang_code, translations):
    base_dir = os.path.dirname(os.path.abspath(__file__))
    locale_dir = os.path.join(base_dir, 'locale', lang_code, 'LC_MESSAGES')
    os.makedirs(locale_dir, exist_ok=True)
    
    po = polib.POFile()
    po.metadata = {
        'Project-Id-Version': '1.0',
        'Report-Msgid-Bugs-To': 'you@example.com',
        'POT-Creation-Date': '2007-10-18 14:00+0100',
        'PO-Revision-Date': '2007-10-18 14:00+0100',
        'Last-Translator': 'you <you@example.com>',
        'Language-Team': 'English <yourteam@example.com>',
        'MIME-Version': '1.0',
        'Content-Type': 'text/plain; charset=utf-8',
        'Content-Transfer-Encoding': '8bit',
    }

    for msgid, msgstr in translations.items():
        entry = polib.POEntry(msgid=msgid, msgstr=msgstr)
        po.append(entry)
    
    po_path = os.path.join(locale_dir, 'django.po')
    mo_path = os.path.join(locale_dir, 'django.mo')
    
    po.save(po_path)
    po.save_as_mofile(mo_path)
    print(f"✅ Generated {po_path} and {mo_path}")

# --- Russian Translations ---
ru_translations = {
    "Welcome to EduCenter": "Добро пожаловать в EduCenter",
    "Master Your Skills with EduCenter": "Улучшайте свои навыки с EduCenter",
    "Join thousands of students learning advanced techniques in web development, programming, and design.": "Присоединяйтесь к тысячам студентов, изучающих передовые методы веб-разработки, программирования и дизайна.",
    "Explore Courses": "Изучить курсы",
    "Sign Up for Free": "Зарегистрироваться бесплатно",
    "Expert Instructors": "Опытные преподаватели",
    "Learn directly from university academics and industry experts.": "Учитесь напрямую у университетских преподавателей и экспертов отрасли.",
    "Modern Technologies": "Современные технологии",
    "Stay up to date with the latest advanced web frameworks like Django and React.": "Будьте в курсе новейших передовых веб-фреймворков, таких как Django и React.",
    "Interactive Learning": "Интерактивное обучение",
    "Engage with dynamic content, coursework projects, and hands-on exercises.": "Развивайтесь с помощью динамичного контента, курсовых проектов и практических упражнений.",
    
    "Browse Courses": "Поиск курсов",
    "Language": "Язык",
    "Hello,": "Привет,",
    "Dashboard": "Панель управления",
    "Logout": "Выйти",
    "Login": "Войти",
    "Sign Up": "Регистрация",
    
    "Welcome Back": "С возвращением",
    "Ready to level up,": "Готовы поднять свой уровень,",
    "Dive back into your studies. Discover new advanced courses, or continue mastering your current skills.": "Возвращайтесь к учебе. Откройте для себя новые продвинутые курсы или продолжайте оттачивать свои навыки.",
    "My Dashboard": "Моя панель",
    "Why Choose EduCenter?": "Почему выбирают EduCenter?",

    "About Us": "О нас",
    "Courses": "Курсы",
    "Contact": "Контакты",
    "Contact Us": "Связаться с нами",
    "Tashkent, Uzbekistan": "Ташкент, Узбекистан",
    "All rights reserved.": "Все права защищены.",
    "What Our Students Say": "Что говорят наши студенты",
    "The Python course was amazing! The practical projects really helped me build a strong portfolio and land my first developer job.": "Курс Python был потрясающим! Практические проекты действительно помогли мне собрать сильное портфолио и найти первую работу.",
    "Very clear explanations and the instructors are extremely responsive. I highly recommend EduCenter to everyone!": "Очень четкие объяснения, и инструкторы всегда на связи. Очень рекомендую EduCenter всем!",
    "Learning React here was a breeze. The interactive exercises make a huge difference compared to just watching video lectures.": "Изучать React здесь было одно удовольствие. Интерактивные упражнения – это огромная разница по сравнению с простым просмотром.",
    "EduCenter is the best platform I've used. The material is very up-to-date with current industry standards.": "EduCenter – лучшая платформа, которую я использовал. Материал очень актуален и соответствует отраслевым стандартам.",
    "Master advanced techniques in web development, programming, and design with industry experts.": "Осваивайте передовые методы веб-разработки, программирования и дизайна вместе с экспертами.",
}

# --- Uzbek Translations ---
uz_translations = {
    "Welcome to EduCenter": "EduCenter'ga xush kelibsiz",
    "Master Your Skills with EduCenter": "EduCenter bilan malakangizni oshiring",
    "Join thousands of students learning advanced techniques in web development, programming, and design.": "Veb-dasturlash, dasturlash va dizayn bo'yicha ilg'or usullarni o'rganayotgan minglab talabalarga qo'shiling.",
    "Explore Courses": "Kurslarni ko'rish",
    "Sign Up for Free": "Bepul ro'yxatdan o'tish",
    "Expert Instructors": "Malakali o'qituvchilar",
    "Learn directly from university academics and industry experts.": "To'g'ridan-to'g'ri universitet akademiklari va soha mutaxassislaridan o'rganing.",
    "Modern Technologies": "Zamonaviy texnologiyalar",
    "Stay up to date with the latest advanced web frameworks like Django and React.": "Django va React kabi eng so'nggi ilg'or veb-freymvorklar bilan hamqadam bo'ling.",
    "Interactive Learning": "Interaktiv ta'lim",
    "Engage with dynamic content, coursework projects, and hands-on exercises.": "Dinamik kontent, kurs loyihalari va amaliy mashg'ulotlar bilan shug'ullaning.",

    "Browse Courses": "Kurslarni izlash",
    "Language": "Til",
    "Hello,": "Salom,",
    "Dashboard": "Boshqaruv paneli",
    "Logout": "Chiqish",
    "Login": "Tizimga kirish",
    "Sign Up": "Ro'yxatdan o'tish",

    "Welcome Back": "Xush kelibsiz",
    "Ready to level up,": "Bilimingizni oshirishga tayyormisiz,",
    "Dive back into your studies. Discover new advanced courses, or continue mastering your current skills.": "O'qishga qayting. Yangi ilg'or kurslarni kashf eting yoki joriy malakangizni oshirishda davom eting.",
    "My Dashboard": "Mening panelim",
    "Why Choose EduCenter?": "Nima uchun EduCenter?",

    "About Us": "Biz haqimizda",
    "Courses": "Kurslar",
    "Contact": "Aloqa",
    "Contact Us": "Biz bilan bog'lanish",
    "Tashkent, Uzbekistan": "Toshkent, O'zbekiston",
    "All rights reserved.": "Barcha huquqlar himoyalangan.",
    "What Our Students Say": "Talabalarimiz nima deydi",
    "The Python course was amazing! The practical projects really helped me build a strong portfolio and land my first developer job.": "Python kursi ajoyib edi! Amaliy loyihalar menga kuchli portfolio yaratishda va birinchi ishimni topishda juda yordam berdi.",
    "Very clear explanations and the instructors are extremely responsive. I highly recommend EduCenter to everyone!": "Juda aniq tushuntirishlar va o'qituvchilar doim yordamga tayyor. Men hammani EduCenter'ni tanlashga chaqiraman!",
    "Learning React here was a breeze. The interactive exercises make a huge difference compared to just watching video lectures.": "Bu yerda React'ni o'rganish juda oson kechdi. Interaktiv mashqlar faqat video ko'rishdan ko'ra katta farq qiladi.",
    "EduCenter is the best platform I've used. The material is very up-to-date with current industry standards.": "EduCenter men foydalangan eng yaxshi platforma. O'quv materiallari hozirgi bozor standartlariga juda mos keladi.",
    "Master advanced techniques in web development, programming, and design with industry experts.": "Veb dasturlash, dasturlash va dizayn bo'yicha ilg'or usullarni soha mutaxassislari bilan o'zlashtiring.",
}

create_translation('ru', ru_translations)
create_translation('uz', uz_translations)
