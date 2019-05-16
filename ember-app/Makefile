name=k8s-ember-app
build_image:
	docker build -t nginx:${name} .
	docker tag nginx:${name} zhyq0826/nginx:${name}
push_image:
	docker push zhyq0826/nginx:${name}