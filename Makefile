.PHONY: all clean

all : csma

csma:
	pyinstaller --onefile ./src/csma.py
	cp ./dist/csma ./csma

clean :
	rm -r ./dist
	rm -r ./build
	rm -r ./src/__pycache__
	rm ./*.spec
	rm ./csma
