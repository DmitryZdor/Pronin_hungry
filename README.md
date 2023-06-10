## Голодные игры от Пронина ##

### Часть 1

https://docs.google.com/document/d/1sRngJnE6u0L0422NAmiif63_2tv0haAH/edit?usp=sharing&ouid=106556994657469778825&rtpof=true&sd=true


### Часть 2
#### Чтобы запустить проект нeoбходимо



1. Клонировать репозиторий и перейти в него в командной строке

```
git clone git@github.com:DmitryZdor/Pronin_hungry.git
```
2. Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv     
       или     
python -m venv venv
```
```
source venv/Scripts/activate
           или 
source venv/bin/activate           
```

```
python3 -m pip install --upgrade pip
            или 
python -m pip install --upgrade pip
```
3. Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

4. Находясь в папке проекта, запустить файл main.py

```
python main.py
```