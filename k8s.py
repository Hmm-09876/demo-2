import docker, subprocess

client = docker.from_env()

image, build_logs = client.images.build(
    path="flask-webapp", 
    tag="flask-webapp:latest"
)

for chunk in build_logs:
    if 'stream' in chunk:
        print(chunk['stream'], end="")

subprocess.run(["minikube", "cache", "add", "flask-webapp:latest"], check=True)

subprocess.run(["kubectl", "apply", "-f", "k8s.yml"], check=True)

print("\nFlask web app deployed to Kubernetes successfully.")