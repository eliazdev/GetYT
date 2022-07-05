ui: src/ui/main.ui
	@echo Compiling UI file...
	pyuic5 -o src/ui/ui.py src/ui/main.ui
	@echo Done!
src: src/main.py
	@echo Compiling source code...
	pyinstaller -F --noconsole --onefile src/main.py
	@echo Done!