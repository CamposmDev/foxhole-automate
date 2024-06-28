PROG_NAME=foxhole-auto
BUILD_VERSION=1.0.0
ENTRY_POINT=src/main.py
ZIP_FILE=dist/$(PROG_NAME)_$(BUILD_VERSION)_windows.zip
TAR_FILE=dist/$(PROG_NAME)_$(BUILD_VERSION)_linux.tar.gz

OSFLAG 				:=
ifeq ($(OS),Windows_NT)
	OSFLAG += -D WIN32
	ifeq ($(PROCESSOR_ARCHITECTURE),AMD64)
		OSFLAG += -D AMD64
	endif
	ifeq ($(PROCESSOR_ARCHITECTURE),x86)
		OSFLAG += -D IA32
	endif
else
	UNAME_S := $(shell uname -s)
	ifeq ($(UNAME_S),Linux)
		OSFLAG += -D LINUX
	endif
	ifeq ($(UNAME_S),Darwin)
		OSFLAG += -D OSX
	endif
		UNAME_P := $(shell uname -p)
	ifeq ($(UNAME_P),x86_64)
		OSFLAG += -D AMD64
	endif
		ifneq ($(filter %86,$(UNAME_P)),)
	OSFLAG += -D IA32
		endif
	ifneq ($(filter arm%,$(UNAME_P)),)
		OSFLAG += -D ARM
	endif
endif

all: clean
	@echo $(OSFLAG)

build-linux:
	pyinstaller --onefile --name=$(PROG_NAME) $(ENTRY_POINT)
	tar -czf $(TAR_FILE) -C dist $(PROG_NAME)

build-win:
	pyinstaller --noconsole --onedir --name=$(PROG_NAME) $(ENTRY_POINT)
	robocopy "assets" "dist\foxhole-auto\src" foxhole.ico || exit 0
	powershell.exe Compress-Archive -Path dist/$(PROG_NAME) -DestinationPath $(ZIP_FILE)

clean:
	rm -rf build dist
	rm ${PROG_NAME}.spec

.PHONY: all build-linux build-win clean