# Git_test_project

## Для запуска на Linux.

1. Установить `Python` последней версии:

	```
	sudo apt-get update
	sudo apt-get upgrade
	sudo apt-get install python3.8
	```

2. Устаноить `pip`:

	```
	python3 -m pip install pip
	```

3. Добавить виртуалтное окружение:

	```
	sudo apt-get install -y python3.8-venv
 
	cd ./Downloads/final_test_task-master
	python3 -m venv selenium
	```

4. Активировать виртуальное окружение:

	```bash
	source venv/bin/activate
	```

5. Установить в виртуальное окружение необходимые пакеты.

	```
	pip install -r requirements.txt
	```
	
6. Запустить тест следующей командой:

	```
	pytest
	```

7. Для деактивации виртуального окружения воспользуйтесь командой:

	```
	deactivate
	```
