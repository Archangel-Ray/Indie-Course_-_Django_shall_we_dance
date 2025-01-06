# Репозиторий курса ["Django, потанцуем?"](https://stepik.org/course/114288/info) ([Артема Егорова](https://stepik.org/users/4877629/teach))

    я не вёл историю этого курса с начала. 
    очень торопился, потому что надо было успеть до начала другого курса. 
    Но, всё равно не успел. 
    прошёл больше семидесяти процентов, но пришлось на долго прерваться. 
    прошло полгода. тот курс я закончил и пришло время вернуться сюда.
    я уже не помню, что я здесь делал. пожалел, что не писал историю. 
    теперь сложно разобраться что, где и зачем оно там. 
    начал весь курс с самого начала. 
    сейчас подключу ГИТа и буду записывать в чём разобрался, а что не понятно.

### [my_page](my_page)
первый проект: первое приложение для демонстрации, а остальные созданы по заданиям курса.
- [horoscope](my_page%2Fhoroscope) демонстрационное приложение. в нём предполагается сделать сайт со знаками Зодиака. 
на его примере демонстрируется:
  - создание приложения.
  - что такое роуты и как в них подключать представления.
  - связывание роута с представлением. 
  - что такое представление и как оно создаётся. 
  - подключение файла роутов приложения к основному списку роутов.
  - создание динамического роута и передача с запросом части данных введённых в адресе в виде переменной представлению.
  - применение [конвертеров](https://docs.djangoproject.com/en/5.1/topics/http/urls/#path-converters) в роуте.
  - перенаправление на другой адрес
  - именование адреса и формирование на основе этих имён пути с использованием функции `reverse`
  - использование html-тегов. создание ссылки в html-тексте.
  - создание меню из списка.
  - передача роуту больше одного параметра. /_выполнено два задания: 1) дополнительное меню по стихиям. 2) определение 
знака зодиака по дате._/
  - создание тестов в приложении.
  - создание html-шаблонов.
  - передача шаблона в виде строки в представлении.
  - размещение шаблонов в проекте.
  - подключение и вставка внешних шаблонов.
  - подключение статических файлов.
  - настройка css-файла. /_бонусное видео. повторил всё, что делал Артём. я уже записался на его курс по html и css. так 
что обязательно изучу следом за Джанго._/
  - создание собственного фильтра.
- [week_days](my_page%2Fweek_days) проверочное приложение для выполнения заданий:
  - отобразить на странице строку соответствующую по названию дня недели в адресе.
  - применить конвертер числа в роуте.
  - выполнить перенаправление внутри сайта.
  - сформировать пути функцией `reverse` с использованием имени адреса.
  - создать конвертер четырёхзначного числа /_вообще-то было два других задания, но я не стал заморачиваться, потому-что
задания вырваны из контекста_/.
  - создать статичный шаблон стартовой страницы.
- [geometry](my_page%2Fgeometry) выполнение задания:
  - создать это приложение.
  - создать файл роутов.
  - подключить этот файл к основному.
  - сделать три роута прямоугольник, квадрат и круг. которые должны принимать параметры для вычисления их площади.
  - прописать соответствующие представления для каждой фигуры.
  - добавить перенаправления для каждой фигуры.
  - применить функцию `reverse` для формирования пути в перенаправлениях всех фигур. для этого даны имена основным 
адресам приложения.
  - создать, по образцу, шаблоны для каждой фигуры.
- [actors](my_page%2Factors) 
ещё одно приложение для выполнения заданий. задания, которые выпадают из общего контекста я делал здесь:
  - скопировать шаблон и передать ему данные из представления.
  - сделать шаблон с заданным текстом, скопировать представление и совместить их, передав данные из представления в 
шаблон.
  - скопировать шаблон и список людей. передать список в шаблон и вывести циклом.
  - скопировать шаблон с таблицей. скопировать статический css-файл и подключить его к шаблону.

### [my_site](my_site) 
проект для выполнения заданий:
- создать этот проект.
- сделать файл конфигурации в ПайЧарме для запуска одновременно двух проектов на разных портах в режиме отладки. 
- приложение "блог" и в нём два роута: на главную страницу и на список постов.
- сделать роут динамическим, он должен принимать и выводить на странице текст введённый в адресе.
- следующий роут должен принимать номер поста и выводить строку с этим номером.
- создать папку для шаблонов, шаблон для основной страницы и подключить его в представлении.
- создать шаблон где должен будет отображаться список всех постов.
- добавить два шаблона по образцу, сделать для них роуты и передать в шаблон данные, которые будут вводиться в адресе.
- /_на этом задании началось самое интересное_/ скопировать страницу готового блога. разбить его на блоки в 
разные шаблоны. скопировать словарь с несколькими постами /_я их немного отредактировал для красоты_/. передать посты 
в шаблон и отображать три случайных поста на основной странице.
- подключить статику в проекте. создать css-файл. сделать блок подключения статики в базовом шаблоне и подключить 
css-файл в шаблоне основной страницы.
### [movie_proj](movie_proj)
проект для демонстрации работы с базами данных:
- создание БД.
- создание моделей.
- миграции.
- работа с консолью в терминале.
- переопределение магических методов модели.
- получение QuerySet - всех записей.
- работа со списком QuerySet.
- изменение модели.
- изменение и удаление записей в таблице.
- фильтрация и исключения. получение QuerySet по условию.
### [bookshop](bookshop)
создан по заданию для проверки полученных знаний. работа с БД:
- создать модель таблицы с двумя полями.
- создать и накатить миграции.
- добавить пять записей в таблицу базы данных через консоль shell_plus.
- переопределить метод \_\_str__ в модели.
- сохранить QuerySet - список всех записей в переменную.
- посмотреть значение атрибута одной из записей.
- добавить логическое поле в модель. сделать миграции.
- добавить колонку в таблицу которая может быть пустой. заполнить поля данными через консоль.