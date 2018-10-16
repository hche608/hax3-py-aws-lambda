###############################################
#
#
#
#
###############################################


AMZ_LINUX_VERSION:=latest
current_dir := $(shell pwd)
container_dir := /opt/app

all: archive

clean:
	sudo rm -rf env
	sudo rm -rf build/lambda.zip

archive: clean
	docker run --rm -ti \
		-v $(current_dir)\:$(container_dir) \
		amazonlinux\:$(AMZ_LINUX_VERSION) \
		/bin/bash -c "cd $(container_dir) && ./build_lambda.sh"