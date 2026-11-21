#!/bin/bash
#SBATCH --job-name=weekly_reports
#SBATCH --cpus-per-task=1
#SBATCH --mem-per-cpu=512M
#SBATCH --time=00:05:00
#SBATCH --output=hpc_output_%j.out

# Load the Python module
module load python

# Create and activate a virtual Python environment
virtualenv --no-download $SLURM_TMPDIR/env
source $SLURM_TMPDIR/env/bin/activate

# Install asteval in the virtual environment
pip install --no-index --upgrade pip
pip install --no-index asteval || pip install asteval

# Run the adapted HPC Python script
python Project-HPC-maly.py
