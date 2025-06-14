#!/bin/bash
#SBATCH --job-name=run_tst_tests
#SBATCH --output=logs/output_%j.log
#SBATCH --error=logs/error_%j.log
#SBATCH --time=00:10:00
#SBATCH --mem=4G
#SBATCH --cpus-per-task=2
#SBATCH -M genius
#SBATCH -A lp_h_ds_students

# Load Python
module load cluster/genius/batch
module load FFC/2019.1.0.post0-foss-2022a-Python-3.10.4


# Go to project directory
cd ~/concept_of_data_science_project/src

# Confirm location and Python version
echo "Running on $(hostname)"
echo "SLURM_JOB_ID: $SLURM_JOB_ID"
echo "Date: $(date)"
python --version

# Run tests and performance
python -m unittest tst_test.py
python performance.py 