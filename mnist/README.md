```shell
sudo docker build -t yiluxiangbei/mnist:v0.0.1 .
sudo docker push yiluxiangbei/mnist:v0.0.1

sudo yum install jq
latest_version=$(curl --silent https://api.github.com/repos/kubeflow/pipelines/releases/latest | jq -r .tag_name)
sudo pip3 install https://storage.googleapis.com/ml-pipeline/release/${latest_version}/kfp.tar.gz --upgrade

which dsl-compile
dsl-compile --py mnist_op.py --output mnist_op.py.zip

https://v0-5.kubeflow.org/docs/pipelines/sdk/dsl-overview/
https://v0-5.kubeflow.org/docs/pipelines/sdk/install-sdk/

apt-get update; apt-get install -y wget bzip2
wget https://repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh

bash Miniconda3-latest-MacOSX-x86_64.sh
export PATH=<YOUR_MINICONDA_PATH>/bin:$PATH
conda create --name mlpipeline python=3.7
source activate mlpipeline

latest_version=$(curl --silent https://api.github.com/repos/kubeflow/pipelines/releases/latest | jq -r .tag_name)
pip install https://storage.googleapis.com/ml-pipeline/release/${latest_version}/kfp.tar.gz --upgrade
which dsl-compile
/<PATH_TO_YOUR_USER_BIN>/miniconda3/envs/mlpipeline/bin/dsl-compile
```
