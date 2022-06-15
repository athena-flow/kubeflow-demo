```shell
sudo docker build -t yiluxiangbei/mnist:v0.0.1 .
sudo docker push yiluxiangbei/mnist:v0.0.1

dsl-compile --py mnist_op.py --output mnist_op.py.zip

https://v0-5.kubeflow.org/docs/pipelines/sdk/dsl-overview/
https://v0-5.kubeflow.org/docs/pipelines/sdk/install-sdk/
```
