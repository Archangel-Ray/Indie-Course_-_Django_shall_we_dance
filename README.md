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
первый проект. первое приложение для демонстрации. остальные создаются по заданию.
- [horoscope](my_page%2Fhoroscope) основное приложение. в нём предполагается сделать сайт со знаками Зодиака. 
на его примере демонстрируется:
  - как создавать приложение.
  - что такое роуты и как в них подключать представления.
  - как связывать роут с представлением. 
  - что такое представление и как оно создаётся. 
  - как подключить файл роутов приложения к основному списку роутов.
  - как создать динамический роут и передать с запросом часть данных введённых в адресе в виде переменной представлению.
  - применение [конвертеров](https://docs.djangoproject.com/en/5.1/topics/http/urls/#path-converters) в роуте.
  - перенаправление на другой адрес
  - как именовать адреса и формировать на основе этих имён пути с использованием функции `reverse`
  - использование html-тегов. создание ссылки в html-тексте.
  - как создать меню из списка.
  - как роут может принимать больше одного параметра. /_выполнено два задания: 1) дополнительное меню по 
стихиям. 2) определение знака зодиака по дате._/
- [week_days](my_page%2Fweek_days) проверочное приложение для выполнения заданий:
  - отобразить на странице строку соответствующую по названию дня недели в адресе.
  - применить конвертер числа в роуте.
  - выполнить перенаправление внутри сайта
  - сформировать пути функцией `reverse` с использованием имени адреса
  - создать конвертер четырёхзначного числа /_вообще-то было два других задания, но я не стал заморачиваться, потому-что
задания вырваны из контекста_/
- [geometry](my_page%2Fgeometry) выполнение задания:
  - создать это приложение.
  - создать файл роутов.
  - подключить этот файл к основному.
  - сделать три роута прямоугольник, квадрат и круг. которые должны принимать параметры для вычисления их площади.
  - прописать соответствующие представления для каждой фигуры.
  - добавить перенаправления для каждой фигуры.
  - применить функцию `reverse` для формирования пути в перенаправлениях всех фигур. для этого даны имена основным 
адресам приложения.

### [my_site](my_site) 
проект для выполнения заданий:
- создать этот проект.
- сделать файл конфигурации в ПайЧарме для запуска одновременно двух проектов на разных портах в режиме отладки. 
- приложение "блог" и в нём два роута: на главную страницу и на список постов.
- сделать роут динамическим, он должен принимать и выводить на странице текст введённый в адресе.
- следующий роут должен принимать номер поста и выводить строку с этим номером.