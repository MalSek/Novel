# Определение персонажей игры.
define e = Character('Эйлин', color="#c8ffc8", image="e")
define l = Character('Лео', color="#024bde", image="l")
define player = Character('[pname]', color='31d422', image='p')

define introvert = False
define toxic = False

define mon=1000

define audio.s="music/sad.mp3"
define audio.hap="music/happy.mp3"
define audio.st="main-menu-theme.ogg"
# Позиции персонажей
init:
    $ left1 = Position(xalign=0.2, yalign=1.1)
    $ right1 = Position(xalign=0.8, yalign=1.1)

# Игра начинается здесь
label start:

    scene bg class
    with fade

    $ pname = renpy.input("Как тебя зовут?", length=12, default="Олег", allow="йцукенгшщзхъэждлорпавыфячсмитьбю-ЙЦУКЕНГШЩЗХЪЭЖДЛОРПАВЫФЯЧСМИТЬБЮ").strip()
    if pname == "":
       $ pname="Олег"
    
    show e norm
    with moveinleft 

    e "{cps=10}{size=+10}{color=05f}Привет{/size}{/color}, {s}давно не виделись,{/s} [pname]. {w}{i}Есть ещё{/i} {b}кое-кто{/b}, {u}кто хочет с тобой поболтать{/u}."

    show e norm at left1
    with easeinright
    
    show l norm at right1
    with moveinright
    
    l "{cps=10}{font=DejaVuSans.ttf}Дружище, [pname], кого я вижу! {w=1}Сколько лет, сколько зим?{/font}"

    "{cps=10}Троица направилась в коридор."

    scene bg corridor
    with wipeleft

    show l sad at right1
    with dissolve

    l "{cps=10}Жаль, что лето закончилось."

    show e sad at left1
    with dissolve

    e "{cps=10}И не говори."

    e norm "{cps=10}Но мы снова вместе!"

    show e sur
    extend "{cps=10}Лео, ты стал ещё больше?"

    l norm "{cps=10}Может немного."

    show e norm

    "{cps=10}Ребята вышли на улицу."

    scene bg school
    with blinds

    show e sur
    with dissolve

    e "{cps=10}Уже так цветёт!"

    e norm "{cps=10}И благоухает."

    e sad "{cps=10}Не верится, что мы скоро закончим школу..."
    
    scene bg street
    with pushleft

    "{cps=10}Ребята шли в тишине."

    show e norm
    with dissolve

    e "{cps=10}Я так давно тут не была."

    e "{cps=10}Что-то изменилось? {w=1}Или мне кажется?"

    "{cps=10}Девушка резко забыла, о чём говорила."

    play music hap
    
    e '''

    {cps=10}Помните, как мы бегали в тот магазин постоянно?!

    {cps=10}А там Лео поранил коленку и долго плакал, а мы его успокаивали.

    {cps=10}Здесь мы с вами встретились впервые.
    '''

    e sur "{cps=10}Ой, я совсем забыла." 
    
    e "{cps=10}Мы же не отпраздновали твоё возвращение. Куда ты хочешь пойти?"

    menu:
        "Куда ты хочешь пойти?"
        "Пошли в парк.":
            jump park

        "Я хочу домой.":
            $ introvert = True
            jump home

    return

label park:
    scene bg forest
    with fade
    play music st
    
    "{cps=10}Ребята направились в парк и купили мороженное."
    menu:
        "Кому купить мороженное?"
        "Себе":
            $ mon -= 20
            "У вас [mon]"
        "Купить всем":
            $ mon -= 60
            "У вас [mon]"
 
    "{cps=10}После того, как они весело провели вместе время они разошлись."
    
    scene bg room
    with fade
    
    "{cps=10}Спустя некоторое время я проголодался. Что же мне съесть?"

    menu:
        "Что же мне съесть?"

        "Котлеты.":
            "Было вкусно."

        "Рыбу.":
            $ toxic = True
            "Что-то мне плохо."

    jump day2


    return

label ice:
    $sum_money = input

label ice2:




label home:
    scene bg room
    with fade
    play music st

    "{cps=10}Зачем друзья, когда играть в компьютер?"

    "{cps=10}Спустя некоторое время я проголодался. Что же мне съесть?"

    menu:
        "Что же мне съесть?"

        "Котлеты.":
            "Было вкусно."

        "Рыбу.":
            $ toxic = True
            "Что-то странный вкус."

    jump day2
    return

label day2:
    scene bg class
    with fade

    "{cps=10}Я пошёл к ребятам."

    if introvert:
        play music s
        "Друзья болтали."
        show e norm at left1
        show l norm at right1
        "{cps=10}Увидев меня, они переменились в лицах."
        show e sad at left1
        show l sad at right1
        "{cps=10}На их лице уже не было улыбки."
        if toxic:
            "{cps=10}Мне резко поплохело, и я ушёл домой как можно скорее."
            scene bg room
            "{cps=10}Видимо, всё из-за рыбы."
    else:
        "{cps=10}Друзья болтали."
        show e norm at left1
        show l norm at right1
        "{cps=10}Они были рады меня видеть, но мне резко поплохело"
        if toxic:
            "{cps=10}Я пойду домой"
            show e sur
            show l sad
            e "{cps=10}Ты в порядке?"


    return
