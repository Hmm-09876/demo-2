import docker
import sys 

client = docker.from_env()

print("Building the Flask web app Docker image...")
try:
    image, build_logs = client.images.build(path=".", tag="flask-webapp:latest")
    for chunk in build_logs:
        if 'stream' in chunk:
            print(chunk['stream'], end="")
    print(f"\nImage built successfully: {image.tags}")
except docker.errors.BuildError as e:
    print(f"Error building image: {e}")
    sys.exit(1)