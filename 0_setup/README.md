* ssh to Comet
* modify `MODULEPATH` in `~/.bashrc`

        export MODULEPATH=/share/apps/compute/modulefiles/applications:$MODULEPATH

* `module avail`
* `module load anaconda`
* check singularity
* `conda create --name py --clone root`
* `source activate py`
* `conda remove conda-env`
* `conda install line_profiler`
