# 一、使用virtualenv

## 1. 使用pip

```shell
python3 -m pip3 install --upgrade pip
sudo apt install python3-pip
pip install virtualenv
```

## 2. 创建运行环境

```shell
virtualenv [虚拟环境名称] 
virtualenv venv

#如果不想使用系统的包,加上–no-site-packeages参数
virtualenv  --no-site-packages 创建路径名
```

## 3. 激活环境

linux:

```shell
cd venv
source ./bin/activate
```

Windows 10:

```shell
cd venv
.\Scripts\activate.bat
```

## 4. 退出环境

linux:

`deactivate`

Windows 10:

`.\Scripts\deactivate.bat`

## 5. 删除环境

没有使用virtualenvwrapper前，可以直接删除venv文件夹来删除环境

## 6. 使用环境

进入环境后，一切操作和正常使用python一样 安装包使用`pip install 包`

## 7. 实用技巧

记录安装的第三方模块
```shell
pip freeze > requirements.txt
```
安装txt文件里所记录的所有第三方模块
```shell
pip install -r requirements.txt
```

# 二、conda

## 1. 管理conda自身

```shell
# 查看conda版本
conda --version

# 设置镜像
#设置清华镜像
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/free/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/pkgs/main/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/conda-forge/
conda config --add channels https://mirrors.tuna.tsinghua.edu.cn/anaconda/cloud/bioconda/
#设置bioconda
conda config --add channels bioconda
conda config --add channels conda-forge
#设置搜索时显示通道地址
conda config --set show_channel_urls yes

# 更新conda
conda update conda
```
## 2. 管理环境
### 2.1 创建虚拟环境

```shell
conda create -n env_name python=3.8

# 创建虚拟环境的同时安装必要的包
conda create -n env_name numpy matplotlib python=3.8
```
## 2.2 查看有哪些虚拟环境

```shell
conda env list
conda info -e
conda info --envs
```
## 2.3 激活虚拟环境

```shell
conda activate env_name
```
 在4.6版本以前需要使用如下命令：


> [!warning] 在4.6版本以前需要使用如下命令
> Linux:  source activate your_env_name
> Windows: activate your_env_name

## 2.4 退出虚拟环境

```shell
conda activate
conda deactivate
```

## 2.5 删除虚拟环境

```shell
# 执行以下命令可以将该指定虚拟环境及其中所安装的包都删除
conda remove --name env_name --all

# 如果只删除虚拟环境中的某个或者某些包
conda remove --name env_name  package_name
```

## 2.6 导入导出环境

```shell
#获得环境中的所有配置
conda env export --name myenv > myenv.yml
#重新还原环境
conda env create -f  myenv.yml
```
# 三、包(Package)的管理

## 3.1 查询包的安装情况


https://blog.csdn.net/chenxy_bwave/article/details/119996001