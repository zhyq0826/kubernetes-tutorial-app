name = $(name)
build_image:
	docker build -t nginx:k8s .
	docker tag nginx:k8s zhyq0826/nginx:${name}
push_image:
	docker push zhyq0826/nginx:${name}