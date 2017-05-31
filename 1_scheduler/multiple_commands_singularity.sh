#!/bin/bash

source deactivate
module load singularity

IMAGE=/oasis/scratch/comet/zonca/temp_project/Ubuntu.img

singularity exec $IMAGE bash multiple_commands.sh
