## Файлы для heroku

Здесь нет файла token.txt - в нем я просто храню токен бота, полученный при регистрации.

Procfile - внутри задаем worker (файл, который будем запускать).  
[Procfile](https://github.com/rogovich/2020_DPO_PythonProg/blob/master/11_Bot/Procfile)

Requirements - перечисляем библиотеки, которые используются в вашем скрипте. Обратите внимание, название некоторых библиотек для установки будет отличаться от того, что пишем в import (например, regex).  
[Requirements.txt](https://github.com/rogovich/2020_DPO_PythonProg/blob/master/11_Bot/requirements.txt)

Runtime - определяем компилятор для нашего скрипта (можно этот файл скопировать отсюда).  
[Runtime.txt](https://github.com/rogovich/2020_DPO_PythonProg/blob/master/11_Bot/runtime.txt)
