# MPI Setup
If you are using [Linux OS](https://bitbucket.org/mpi4py/mpi4py/issues/118/cannot-pip-install-mpi4py-with-conda), run this command:
```sh
sudo apt-get install python-mpi4py
```

or if you're using `conda`:
```sh
export CONDA_BUILD_SYSROOT=/
conda create --name mpitest python=3.8 mpich-mpicc
conda activate mpitest
pip install mpi4py
```
If you have Windows or Mac this link can help you [MPI Setup For Windows or Mac](https://nyu-cds.github.io/python-mpi/setup/)

# How to run

Python MPI [Documentation](https://mpi4py.readthedocs.io/en/stable/overview.html)

Use this command to run any `py` file with `N` processes:
```sh
mpiexec -n N python FILE_NAME.py
```

Example:
```sh
mpiexec -n 4 python 01_lab.py
```