start_deployment:
	kubectl create -f ember-app-deployment.yaml
start_service:
	# 创建一个默认的 service ClusterIP 类型供内部访问 绑定的端口和容器暴露端口相同
	kubectl expose deployment ember-app-deployment
get_service:
	kubectl get service ember-app-deployment
get_endpoints:
	kubectl get endpoints ember-app-deployment