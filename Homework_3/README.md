# **Modules and virtual environments** :wrench:
## Homework3

Programmer Mikhail published comprehensive study focused on **python modules** and **virtual environments**. In *Supplementary* he attached a link 
to the repository on *Github* with [his code](https://github.com/krglkvrmn/Virtual_environment_research). Unfortunately, the utility **ultraviolence.py** was not adapted 
for widespread usage. Here some guidelines with **requirements.txt** for proper launch of Mikhail's script on **Ubuntu 22.04.1 LTS** with **Python v3.11.0a7**. 

### System
Launch of utility **ultraviolence.py** was tested on **Ubuntu 22.04.1 LTS** (codename: jammy) with **Python version 3.11.0a7**.

### Files
In this directory there are *four files*: [README.md](./README.md), [pandas_fix.sh](./pandas_fix.sh), [requirements.txt](./requirements.txt), and [ultraviolence.py](./ultraviolence.py).
- **README.md**: guidlines for *ultraviolence.py* proper launch
- **pandas_fix.sh**: bash script for modifying **pandas module** *frame.py* script
- **requirements.txt**: .txt file with the dependencies for *ultraviolence.py*
- **ultraviolence.py**: Mikhal's .py utility

### Launch
**I. Python 3.11 installation**\
For *ultraviolence.py* launch you need **Python version 3.11**. 
Here guidelines for **Python version 3.11.0a7** installation on **Ubuntu 22.04.1 LTS** 
based on [recommendations](https://www.linuxcapable.com/how-to-install-python-3-11-on-ubuntu-22-04-lts/#Install_Python_311_-_PPA_Method).
- create your Python project working directory

`mkdir /home/ultraviolent_project/` *(as an example)*
- navigate to your working directory

`cd /home/ultraviolent_project/`
- use the `wget` command to download the [Python 3.11 archive](https://www.python.org/ftp/python/3.11.0/Python-3.11.0a7.tar.xz)

`wget https://www.python.org/ftp/python/3.11.0/Python-3.11.0a7.tar.xz`
- extract the Python archive using `tar` command

`tar -xf Python-3.11.0a7.tar.xz`
- optionally, move Python-3.11.0a7 to a proper destination, such as the `/opt/` directory

`sudo mv Python-3.11.0a7 /opt/`
- install the dependencies required to install Python 3.11.0a7

`sudo apt install build-essential zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev libssl-dev libsqlite3-dev libreadline-dev libffi-dev curl libbz2-dev pkg-config make -y`
- navigate to the directory Python-3.11.0a7

`cd /opt/Python-3.11.0a7/`
- run the `./configure` command

`./configure --enable-optimizations --enable-shared`
- compile the built and configured environment with the `make` command

`make -j {number of cpu}`
- once you have finished building, install Python binaries

`sudo make altinstall`\
*Note, it is advised to use the `make altinstall` command NOT to overwrite the default Python 3 binary system.*
- after the installation, you need to configure the dynamic linker run-time bindings with the `ldconfig` command

`sudo ldconfig /opt/Python-3.11.0a7`
- confirm that *Python 3.11* is installed and the build version by running the following command

`python3.11 --version` (*output should be: Python 3.11.0a7*)

**II. Virtual environment creation**\
After **Python 3.11** installation, create **virtual environment**, which independent of the system installed Python and its modules.
- navigate to your working directory

`cd /home/ultraviolent_project/`
- create *Python 3.11* **ultraviolent** virtual environment using `venv` command

`python3.11 -m venv ultraviolent`
- activate **ultraviolent** venv using `source` command

`source ultraviolent/bin/activate`
- check python version in **ultraviolent**

`python --version` (*output should be: Python 3.11.0a7*)

**III. Utility launch**\
Now you need to install specified packages listed in **requirements.txt**. 
In **ultraviolence.py**, lane 37 type `set` was used to index pandas `DataFrame`, which caused syntax error. 
So, to tackle this you need to modify *frame.py* for *pandas package* located in `./ultraviolent/lib/python3.11/site-packages/pandas/core/frame.py`. 
Bash script **pandas_fix.sh** is used to comment lines where index type is checked.  
- install the specified packages using the configuration file [requirements.txt](./requirements.txt)

`python -m pip install -r requirements.txt`
- run bash script [pandas_fix.sh](./pandas_fix.sh) to modify *frame.py* for *pandas package*

`bash pandas_fix.sh`
- launch [ultraviolence.py](./ultraviolence.py)

`python ultraviolence.py`

Enjoy Mikhail's script!
