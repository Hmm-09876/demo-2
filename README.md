[![CI/CD](https://github.com/Hmm-09876/demo-2/actions/workflows/k8s-ci-cd.yml/badge.svg)](https://github.com/Hmm-09876/demo-2/actions)
# Mục tiêu demo-2

1. Hiểu và thực hành CI/CD (GitHub Actions + Act)

2. Cung cấp hai API:
   - Backend: REST API với Flask + basic test.
   - Serverless: Todo API bằng TypeScript cho Cloudflare Workers.

3. Triển khai ứng dụng lên KinD bằng Helm và cấu hình HPA.

4. Hiểu rõ hơn về Kubernetes manifest.

***
# Những gì cần cài ban đầu

## Cài Wrangler CLI
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.3/install.sh | bash
\. "$HOME/.nvm/nvm.sh"
nvm install 24
npm install -g wrangler
```

## Khởi tạo project và deploy
```
wrangler init
wrangler deploy
```

# -> URL demo-api
https://steep-fog-d998.demo2-test.workers.dev/


## Cài các dependencies
```
pip install docker flask pytest app
```

## Cài kubectl
https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/

## Cài kind
https://kind.sigs.k8s.io/docs/user/quick-start/
	
## Cài helm
https://helm.sh/docs/intro/install/

## Cài docker
https://docs.docker.com/engine/install/ubuntu/

## Tải Metrics Server manifest:
```
wget https://github.com/kubernetes-sigs/metrics-server/releases/latest/download/components.yaml
```

## Tải và cài act
```
wget -qO act.tar.gz https://github.com/nektos/act/releases/latest/download/act_Linux_x86_64.tar.gz
sudo tar xf act.tar.gz -C /usr/local/bin act
rm -f act.tar.gz
```

***
# Chạy thử và test nhanh cho client
## Clone repo về
```
git clone https://github.com/Hmm-09876/demo-2.git
cd demo-2/
```

## Create kind cluster
```
kind create cluster --name demo-cluster
```

## Build, load image và apply k8s.yml manifest
```
python k8s.py
```

## Apply metrics-server manifest
```
kubectl apply -f components.yaml
```

## Deploy Helm chart
```
helm upgrade --install demo-backend ./helm-chart -n demo --create-namespace
```

## Check pods & HPA
```
kubectl get pods -n demo
kubectl get hpa -n demo
kubectl top pods -n demo
```

## Cleanup
```
kubectl delete ns demo
kind delete cluster --name demo-cluster
```


















