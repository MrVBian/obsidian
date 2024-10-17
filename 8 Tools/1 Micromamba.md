
# 1 安装

https://mamba.readthedocs.io/en/latest/installation/micromamba-installation.html

```shell
# Linux Intel (x86_64):
curl -Ls https://micro.mamba.pm/api/micromamba/linux-64/latest | tar -xvj bin/micromamba
# Linux ARM64:
curl -Ls https://micro.mamba.pm/api/micromamba/linux-aarch64/latest | tar -xvj bin/micromamba
# Linux Power:
curl -Ls https://micro.mamba.pm/api/micromamba/linux-ppc64le/latest | tar -xvj bin/micromamba
# macOS Intel (x86_64):
curl -Ls https://micro.mamba.pm/api/micromamba/osx-64/latest | tar -xvj bin/micromamba
# macOS Silicon/M1 (ARM64):
curl -Ls https://micro.mamba.pm/api/micromamba/osx-arm64/latest | tar -xvj bin/micromamba
```
If you want to persist these changes, you can automatically write them to your `.bashrc` (or `.zshrc`) by running `./micromamba shell init ...`. This also allows you to choose a custom MAMBA_ROOT_ENVIRONMENT, which is where the packages and repodata cache will live.

```shell
# Linux/bash:
./bin/micromamba shell init -s bash -p ~/micromamba  # this writes to your .bashrc file
# sourcing the bashrc file incorporates the changes into the running session.
# better yet, restart your terminal!
source ~/.bashrc

# macOS/zsh:
./micromamba shell init -s zsh -p ~/micromamba
source ~/.zshrc
```

# 2 使用


```shell
micromamba create -n myenv python=3.9            # 创建环境

micromamba activate myenv                        # 激活环境
micromamba activate /path/to/env

micromamba install package_A package_B=version   # micromamba 或者 pip安装包

micromamba search package_A                      # 查找包
micromamba update package_A                      # update更新包
micromamba remove package_A                      # remove移除包

micromamba list                                  # 查看安装包
micromamba create -f env.yml                     # 包含所需的环境名称和要使用的通道

conda list --explicit --md5                      # 显式_环境锁定文件
micromamba create -n xtensor -f explicit_env.txt # 安装这样的文件

micromamba deactivate
```