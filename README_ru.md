**[🇺🇸 English](https://github.com/avrtt/telegram-autocomment-bot/blob/main/README.md)** &nbsp; • &nbsp; **🇷🇺 Русский** (последнее обновление перевода: [e961f8c](https://github.com/avrtt/telegram-autocomment-bot/tree/e961f8cc8f0b70f7108a1f4da16f872e587973db))

<br>

Данный репозиторий содержит код Python-приложения, позволяющего мониторить новые посты в Telegram-каналах и мгновенно комментировать их при публикации. Вы можете указать список каналов для мониторинга, а также поведение бота с помощью промпта. 

Разработано с использованием [Telethon](https://github.com/LonamiWebs/Telethon), [gpt4free](https://github.com/xtekky/gpt4free) и [Tenacity](https://github.com/jd/tenacity). Аккаунт OpenAI для работы не нужен.

Этот софт — публичная часть одного из моих фриланс-проектов. Если вам нужны услуги фрилансера, всю необходимую информацию вы сможете найти на [моём замечательном сайтике](https://avrtt.github.io/freelance/ru) 👈👀. 

## Предупреждение
Ради всего святого, не используйте этот софт для спама, потому что никто не любит спам. Ну, хотя бы порядочным админам жизнь не усложняйте. А вообще, вас забанят за репорты. Я предупредил. Используйте лучше для веселья в своих каналах или в образовательных целях (совмещайте).

## Структура

```
telegram-autocomment-bot/
│
├── config/
│   ├── settings.ini
│   ├── prompt.txt
│   └── config_loader.py
│
├── utils/
│   ├── gpt_utils.py
│   └── log_utils.py
│
├── bot/
│   ├── bot_logic.py (основной функционал)
│   └── event_handlers.py
│
├── tests/
│   ├── test_g4f.py
│   └── test_bing_provider.py
│
├── requirements.txt
└── start.py
```

## Установка
1. Копируем и переходим в папку репозитория:
    ```
    git clone git@github.com:avrtt/telegram-autocomment-bot.git
    cd telegram-autocomment-bot
    ```

2. Поскольку использование виртуальной среды — практика хорошая, я рекомендую её создать:
    ```
    python3 -m venv venv
    ```

    Не забываем активировать:
    - На Linux/macOS:
        ```
        source venv/bin/activate
        ```
    - На Windows:
        ```
        venv\Scripts\activate
        ```

3. Ставим зависимости:
    ```
    pip install -r requirements.txt
    ```

4. Создаём файл `config/settings.ini` следующего содержания:
    ```
    [Telegram]
    api_id = <айди_вашей_апишки*>
    api_hash = <хэш_вашей_апишки*>
    auto_join = true
    channel_usernames = <канал1, канал2, ... **>

    [GPT]
    provider = Bing

    [Debug]
    verbose = false

    [Proxy] # необязательно
    proxy_login =
    proxy_password =
    proxy_ip =
    proxy_port =

    [Metadata] # необязательно
    device_model =
    system_version =
    ```
    \* Получить ID и хэш API можно [здесь](https://my.telegram.org/auth). Необходимо войти по номеру телефона бот-аккаунта, перейти в "API development tools" и создать приложение. **Не разглашайте эти данные!**  
    \** Указывайте каналы без символа `@`. Ваши приватные каналы работать не будут.

5. Запускаем:
    ```
    python start.py
    ```

6. Telethon спросит тот же самый номер телефона. Необходимо снова ввести код подтверждения, который будет отправлен в Telegram-клиент.

7. Если у вас включена двухфакторная аутентификация, Telethon также потребует ввести пароль.

<br>

Теперь, если вы перейдете в активные сессии бот-аккаунта, то обнаружите новое, только что зарегистрированное устройство. Веселитесь!

## Конфигурация
### Поведение
Вероятно, первое, что вы захотите настроить, — промпт, задающий поведение бота. Вы можете написать свой в файле `prompt.txt`. Тут всё просто: используйте бота подобно ChatGPT.

Рекомендуется описывать поведение на языке, на котором будет говорить бот.

Добавьте в конце промта что-то вроде `Вот текст, который нужно прокомментировать:`, поскольку в коде тексты постов добавляются после основного текста промпта. 

### Настройки
Ниже представлены описания переменных, которые находятся в файле `settings.ini` (дефолтные значения <ins>подчёркнуты</ins>):  

- `auto_join`: Должен ли бот подписываться на каналы перед комментированием в начале сессии **(<ins>true</ins>/false)**  
- `provider`: Какого провайдера использовать **(<ins>Bing</ins>, Liaobots, Phind, etc.)**  
- `verbose`: Переключение режима отладки, который показывает в консоли сведения о соединении, полные тексты промптов и другую информацию **(true/<ins>false</ins>)**  

## Тестирование и исправление неполадок
### Тестирование соединения с провайдером
Запускаем изолированный скрипт для g4f:
```
python tests/test_g4f.py
```

Скорее всего, вы получите `Error: Bing is not working`, потому запускаем изолированный скрипт для проверки Bing:
```
python tests/test_bing_provider.py
```

Если Bing не работает, попробуйте сменить провайдера или использовать прокси.

### Мой интернет-провайдер заблокировал Bing/OpenAI
Если у вас нет доступа к этим сервисам без VPN, значит ~~вы скорее всего из России~~ следует попробовать прокси, либо, возможно, пропускать весь трафик компьютера через VPN, использовать утилиты для обхода DPI и т.д. Попробуйте [GreenTunnel](https://github.com/SadeghHayeri/GreenTunnel).

### Использование других провайдеров
Полный список провайдеров и их поддержки разных моделей указан в [репозитории g4f](https://github.com/techwithanirudh/g4f).

## To do
- Заменить `Bing` на `config['GPT']['verbose']` в `gpt_utils.py`
- Больше фич
- Юнит-тесты

## Вклад
Пул-реквесты, ишьюсы — велком.

## Лицензия
МИТя
