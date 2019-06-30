create_secret:
	kubectl create secret generic user --from-file=./username.txt
	kubectl create secret generic pass --from-file=./password.txt
enter_container:
	kubectl exec -it test-projected-volume -- /bin/sh

