# maccas

How to build package and push to Pypy.

### Development
Install in dev mode
```
pip install -e .
```

## To get help 
Understad different default params
```
maccas_train --help
```
## To run different model
Say, huggingface instead of default from configs.
```maccas_train model=hf```


## Use CIFAR10 dataset and timm pretrained models

Reference repo https://github.com/ashleve/lightning-hydra-template

- Add cifa10_datamodule.py in maccas/data folder with class of data module.
- Add cifar10.yaml in configs/data folder to instantiate the data model for training with previous step class references
- Add timm_module.py in maccas/models
- Add timm.yaml to configs folder with previous 1 step references

- Add eval.py to maccas folder similar to train.py
- Add eval.yaml to configs folder ( user must provide checkpoint path )

maccas_train data=cifar10 model=timm

maccas_eval --help

pip install timm==0.9.2