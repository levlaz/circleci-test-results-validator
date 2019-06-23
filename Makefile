build:
	docker build . -t levlaz/circleci-tr-validator

shell:
	docker run -it \
	-v ${PWD}:/usr/src/app \
	-e CIRCLE_TOKEN=${CIRCLE_TOKEN} \
	levlaz/circleci-tr-validator sh