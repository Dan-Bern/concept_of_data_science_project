#!/bin/bash -l
#SBATCH --job-name=run_performance
#SBATCH --output=logs/performance_%j.out
#SBATCH --error=logs/performance_%j.err
#SBATCH --time=00:10:00
#SBATCH --mem=4G
#SBATCH --cpus-per-task=2
#SBATCH --account=lp_h_ds_students
#SBATCH --cluster=genius

# Load necessary modules
module purge
module load cluster/genius/batch
module load Python/3.12.3-GCCcore-13.3.0

# Activate your virtual environment
source ~/venvs/cds_proj_env/bin/activate

# Go to the directory with performance.py
cd ~/concept_of_data_science_project/src

which python
python --version
pip list | grep BTrees

# Run the script
python3 performance.py