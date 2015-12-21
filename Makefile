DOCKER_REPO=gijzelaerr/cif-menu

.PHONY: build clean

all: run

build:
	docker build --pull -t ${DOCKER_REPO} .

run: build
	docker run -ti \
		-e SENSOR_URL=${SENSOR_URL} \
		-e SENSOR_USERNAME=${SENSOR_USERNAME} \
		-e SENSOR_PASSWORD=${SENSOR_PASSWORD} \
		-e SENSOR_NAME=${SENSOR_NAME} \
		${DOCKER_REPO}

clean:
	docker rmi ${DOCKER_REPO}
