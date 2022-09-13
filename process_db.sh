#!/bin/bash 
#SBATCH --job-name=process_db 
#SBATCH --partition=batch 
#SBATCH --constraint=Milan
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=8 
#SBATCH --mem=16GB 
#SBATCH --mail-user=jo10595@uga.edu 
#SBATCH --mail-type=END,FAIL 
#SBATCH --time=72:00:00 

python main.py
