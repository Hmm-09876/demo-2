[![CI/CD](https://github.com/Hmm-09876/demo-2/actions/workflows/k8s-ci-cd.yml/badge.svg)](https://github.com/Hmm-09876/demo-2/actions)
## Một project nhỏ để luyện tập cách build, test và deploy một ứng dụng đơn giản. Không phải project kiểu production, mà là nơi mình thử nghiệm workflow thực tế, từ code, test cho tới deploy.

# Mục tiêu demo-2
- Chạy app local từ đầu đến cuối
- Viết test đơn giản và kiểm tra kết quả
- Debug và tìm nguyên nhân lỗi
- Build Docker image và chạy container
- Deploy app lên Kubernetes local
- Làm quen với GitHub Actions, hiểu flow CI/CD cơ bản

## Mình dùng gì cho project
- Python / Flask cho phần app chính
- pytest để viết và chạy test
- Docker để build và chạy container
- Kubernetes, Kind và Helm để thử deploy local
- GitHub Actions cho phần CI/CD
- Cloudflare Workers cho một demo API nhỏ (Kết quả demo: https://steep-fog-d998.demo2-test.workers.dev/)

***
# Nguồn tham khảo
Flask: https://flask.palletsprojects.com/en/stable/quickstart/

Docker: https://docs.docker.com/engine/install/ubuntu/

Kubernetes: https://kubernetes.io/docs/tasks/

Helm: https://helm.sh/docs/intro/quickstart/

GitHub Actions: https://docs.github.com/en/actions/get-started/quickstart



