* ssh to Comet
* modify `MODULEPATH` in `~/.bashrc`

        export MODULEPATH=/share/apps/compute/modulefiles/applications:$MODULEPATH

* `module avail`
* `module load anaconda`
* check singularity, more at <http://singularity.lbl.gov/quickstart>
* `conda create --name py --clone root`
* `source activate py`
* `conda remove conda-env`
* `conda install line_profiler`
