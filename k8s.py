import docker, subprocess, sys, os, yaml

IMAGE_NAME = os.getenv("IMAGE_NAME", "flask-webapp")
IMG_TAG = os.getenv("IMAGE_TAG", "latest")
DOCKER_PATH = "flask-webapp"
KIND_CLUSTER = os.getenv("KIND_CLUSTER_NAME", "demo-cluster")
K8S_DIR = "k8s"

FULL_TAG = f"{IMAGE_NAME}:{IMG_TAG}"


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


def write_kustomization(path, name, tag):
    file_path = os.path.join(path, "kustomization.yml")
    if os.path.exists(file_path):
        with open(file_path, "r") as f:
            data = yaml.safe_load(f) or {}
    else:
        data = {}
    updated = False
    for img in data.get("images", []):
        if img.get("name") == name:
            img["newTag"] = tag
            updated = True
            break
    if not updated:
        data.setdefault("images", []).append({"name": name, "newTag": tag})
    with open(file_path, "w") as f:
        yaml.safe_dump(data, f)
    print(f"Updated {name} to tag {tag}")
 

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
        subprocess.run(["kubectl", "apply", "-k", yaml_file], check=True)
        print("Kubernetes resources applied successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error applying Kubernetes configuration: {e}")
        sys.exit(1)


if __name__ == "__main__":
    build_image(DOCKER_PATH, FULL_TAG)
    write_kustomization(K8S_DIR, IMAGE_NAME, IMG_TAG)
    kind_load(FULL_TAG, KIND_CLUSTER)
    kubectl_apply(K8S_DIR)
    print("Deployment completed successfully.")