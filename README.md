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


## Use CIFAR10 dataset

- Add cifa10_datamodule.py in maccas/data folder with class of data module.
- Add cifar10.yaml in configs/data folder to instantiate the data model for training