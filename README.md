# python_playground

## Description
In this I am going to start some python projects with the goal of working on some smaller AI works.

Thanks given to **ChatGPT** and **Artificial Intelligence for Developers (in easysteps)*** book see [https://www.ineasysteps.com] or visit local library.

So more to come.

# Preparing

## Install Python :white_check_mark:
[Python Install](https://www.python.org/downloads)

Be sure to check the **Add python.exe to the PATH** box. Then choose **Custom Installation.** Then **Next**. And another **Next** to **Finish**.

## Installing PIP :white_check_mark:
<!-- CTRL+E to get the special single quote -->
`python -m ensurepip --upgrade`
or
`python.exe -m pip install --upgrade pip`

## Installing pygame :white_check_mark:
Pygame allows for graphics to be created.
`pip install pygame`

## Other Installs (will add later on if necessary) :white_large_square:
To allow for speeding up the neural networks training process.

### Install WSL2 :white_check_mark:
https://learn.microsoft.com/en-us/windows/wsl/install

> [!IMPORTANT]
> **To launch Ubuntu enter `wsl.exe -d Ubuntu`.**

Regular Update and upgrade packages required. So make the following a habit:
`sudo apt update && sudo apt upgrade`
https://learn.microsoft.com/en-us/windows/wsl/setup/environment

Using **Windows Terminal** you can enter `Ctrl+Shift+P` to get the **Command Palette**.
https://learn.microsoft.com/en-us/windows/terminal/install#invoke-the-command-palette

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

**Linux and Bash**
https://learn.microsoft.com/en-us/windows/wsl/tutorials/linux

> [!CAUTION]
> Tensor Flow requires Python 3.8, 3.9, 3.10, 3.11. Which means Python 3.12+ is not yet supported. Version of Python as of this writing is 3.13.3.
> Using WSL2 you can install Python 3.11 and pip (using `pyenv`).

### Install pyenv with Python version 3.11.9
1. From CMD prompt enter in `wsl.exe -d Ubuntu`.
2. Enter `sudo apt update`.
3. Enter ```sudo apt install -y build-essential libssl-dev zlib1g-dev \
    libbz2-dev libreadline-dev libsqlite3-dev curl \
    llvm libncursesw5-dev xz-utils tk-dev libxml2-dev \
    libxmlsec1-dev libffi-dev liblzma-dev git```
4. Enter `curl https://pyenv.run | bash`
5. Then Enter in the following:
   ```
   # Add pyenv to shell
   echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
   echo 'command -v pyenv >/dev/null || export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
   echo 'eval "$(pyenv init -)"' >> ~/.bashrc
   exec "$SHELL"
   ```
6. Enter `pyenv install 3.11.9`.
7. Enter `pyenv global 3.11.9`.


## Install CuDNN and CUDA toolkit** :white_large_square:
https://docs.nvidia.com/deeplearning/cudnn/installation/linux.html


## Install Tensor Flow :white_large_square:
Need Microsoft Visual C++ Redistributable for Visual Studio 2015, 2017, 2019, and 2022.
https://learn.microsof.com/en-US/cpp/windows/latest-supported-vc-redist?view=msvc-170

`pip install tensorflow`

`pip install tensorflow_datasets`

`pip install matplotlib`

> [!WARNING]
> If above doesn't work then you should follow steps [Install pyenv with Python version 3.11.9](#Install-pyenv-with-Python-version-3.11.9).
> Used **ChatGPT** to assist in resolution.


