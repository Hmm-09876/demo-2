[![CI/CD](https://github.com/Hmm-09876/demo-2/actions/workflows/demo-2/k8s-ci-cd.yml/badge.svg)](https://github.com/Hmm-09876/demo-2/actions)
# Mục tiêu demo-2

1. Hiểu rõ hơn về CI/CD

2. Phát triển REST API với Flask

3. Thử nghiệm CI/CD cục bộ với Act

4. Triển khai hạ tầng IaC

5. Quản lý monorepo
***
## Những gì cần cài ban đầu

# Cài Wrangler CLI
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
\. "$HOME/.nvm/nvm.sh"
nvm install 24
npm install -g wrangler
```

# Khởi tạo project và deploy
```
wrangler init
wrangler deploy
```

## -> URL demo
`https://steep-fog-d998.demo2-test.workers.dev/`

# Cài các dependencies
```
pip install docker flask pytest app
```

# Cài Minikube
```
curl -Lo minikube https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64 \
  && chmod +x minikube
sudo install minikube /usr/local/bin/
```

# Thêm user vào nhóm Docker
```
sudo usermod -aG docker $USER
newgrp docker
```

# Khởi động Minikube
```
minikube start --driver=docker
```

# Cài và setup Kind
```
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.29.0/kind-linux-amd64
chmod +x kind
mv ./kind /usr/local/bin/
kind create cluster --name kind
kind load docker-image my-backend:latest
```
# Cài và setup Helm
```
snap install helm --clasic
helm create helm-chart
helm upgrade --install demo ./helm-chart -f helm-chart/values.yaml
```

# Cài kubectl và kiểm tra node
```
sudo snap install kubectl --classic
kubectl get nodes
```

# Chuyển Docker client sang Minikube
```
eval $(minikube docker-env)
```

# Build Docker image cho Flask
```
docker build -t flask-app:latest .
```

# Tải và cài act
```
wget -qO act.tar.gz https://github.com/nektos/act/releases/latest/download/act_Linux_x86_64.tar.gz
sudo tar xf act.tar.gz -C /usr/local/bin act
rm -f act.tar.gz
```

***
## Chạy thử và test nhanh cho client
# Clone repo về
```
git clone https://github.com/Hmm-09876/demo-2.git
cd demo-2/
```

# Xây dựng Docker image cho backend
```
sudo usermod -aG docker $USER
newgrp docker
docker build -t my-backend:latest . 
```

# Tải và nạp image vào Kind
```
[ $(uname -m) = x86_64 ] && curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.29.0/kind-linux-amd64
chmod +x kind
mv ./kind /usr/local/bin/
kind create cluster --name kind
kind load docker-image my-backend:latest
```

# Triển khai ứng dụng qua Helm
```
snap install helm --clasic
helm create helm-chart
helm upgrade --install demo ./helm-chart -f helm-chart/values.yaml
```

# Kiểm tra trạng thái của Pod
```
kubectl get pods
```



















