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
`pip install docker flask setuptools wheel`

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
`docker build -t flask-app:latest .`


# Tải và cài act
```
wget -qO act.tar.gz https://github.com/nektos/act/releases/latest/download/act_Linux_x86_64.tar.gz
sudo tar xf act.tar.gz -C /usr/local/bin act
rm -f act.tar.gz
```




















