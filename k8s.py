import docker, subprocess, sys, os

IMG_TAG = os.getenv("IMAGE_TAG", "flask-webapp:latest")
DOCKER_PATH = "flask-webapp"
KIND_CLUSTER = os.getenv("KIND_CLUSTER_NAME", "demo-cluster")
K8S_YAML = "k8s.yml"


def build_image(path, tag):
    client = docker.from_env()
    try:
        image, build_logs = client.images.build(path=path, tag=tag)
        for chunk in build_logs:
            if isinstance(chunk, dict) and 'stream' in chunk:
                print(chunk['stream'], end="")
        print(f"\nImage built successfully: {image.tags}")
    except docker.errors.BuildError as e:
        print(f"Error building image: {e}")
        sys.exit(1)


def kind_load(tag, kind_name):
    print(f"Loading image {tag} into kind cluster {kind_name}...")
    try:
        subprocess.run(["kind", "load", "docker-image", tag, "--name", kind_name], check=True)
        print("Image loaded successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error loading image into kind: {e}")
        sys.exit(1)


def kubectl_apply(yaml_file):
    print(f"Applying Kubernetes configuration from {yaml_file}...")
    try:
        subprocess.run(["kubectl", "apply", "-f", yaml_file], check=True)
        print("Kubernetes resources applied successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error applying Kubernetes configuration: {e}")
        sys.exit(1)


if __name__ == "__main__":
    build_image(DOCKER_PATH, IMG_TAG)
    kind_load(IMG_TAG, KIND_CLUSTER)
    kubectl_apply(K8S_YAML)
    print("Deployment completed successfully.")