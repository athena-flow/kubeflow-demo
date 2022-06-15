#!/usr/bin/env python3
# mnist_op.py

import kfp
from kfp import dsl

def train_mnist_op():
  return dsl.ContainerOp(name='mnist', image='yiluxiangbei/mnist:v0.0.1')

@dsl.pipeline(
    name='mnist train',
    description='test'
)
def pipeline():
  op = train_mnist_op()

if __name__ == '__main__':
  kfp.compiler.Compiler().compile(pipeline, __file__ + '.zip')
