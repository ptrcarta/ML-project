# Google Cloud


### Important changes
#### 21.11.2018:
  - Installed with ppip all dependencies (`torch`, `torchvision`, `keras`, `nn-transfer`, `sklearn`, `tensorflow-gpu`, `dill`)
  - Added a new python 2.7 environment (`conda create -n py27 python=2.7 anaconda`)
  - Chaned python 2.7 as default environment, added `source activate py27` to `~/.bash_profile`
  
### Troubleshooting
  - `util.py` not found error is solved by setting `export PYTHONPATH=.` before running the script. Possibly creating `__init__.py` in the `neural-fingerprinting` directory could solve the issue as well, but we don't have permissions to do that. [PG]
