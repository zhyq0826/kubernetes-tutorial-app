start_pod1:
	kubectl create -f ember-app-pod.yaml
start_pod2:
	kubectl create -f ember-app-pod2.yaml
start_service:
	kubectl create -f ember-app-service.yaml
get_pod:
	kubectl get pods -l app=ember-app
get_service:
	kubectl get service ember-app-service
get_endpoints:
	kubectl get endpoints ember-app-service
describe_service:
	kubectl describe service ember-app-service
delete_service:
	kubectl delete services ember-app-service
delete_pods:
	kubectl delete pods ember-app ember-app2