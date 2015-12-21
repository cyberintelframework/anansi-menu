DOCKER_REPO=gijzelaerr/cif-menu

.PHONY: build clean

all: run

build:
	docker build --pull -t ${DOCKER_REPO} .

run: build
	docker run -ti -e URL,USERNAME, PASSWORD ${DOCKER_REPO}

clean:
	docker rmi ${DOCKER_REPO}
