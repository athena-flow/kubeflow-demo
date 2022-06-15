```shell
sudo docker build -t yiluxiangbei/mnist:v0.0.1 .
sudo docker push yiluxiangbei/mnist:v0.0.1

dsl-compile --py mnist_op.py --output mnist_op.py.zip

https://v0-5.kubeflow.org/docs/pipelines/sdk/dsl-overview/
https://v0-5.kubeflow.org/docs/pipelines/sdk/install-sdk/

apt-get update; apt-get install -y wget bzip2
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```
