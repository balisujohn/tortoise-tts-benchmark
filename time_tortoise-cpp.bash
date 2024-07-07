#!/bin/bash

# Number of times to run the command
n=10

# Command to run (replace with your own command)
command_to_run="./tortoise --voice '../models/mol.bin' --message 'based... dr. freeman?'"

# CSV file to save results
csv_file="time_results.csv"

# Header for CSV file
echo "Run,Real_time,User_time,System_time" > "$csv_file"

# Loop to run the command n times
for (( i=1; i<=$n; i++ ))
do
    # Run the command and capture time output
    TIMEFORMAT='%R,%U,%S'
    real_user_sys=$( { time (eval "$command_to_run" >/dev/null 2>&1); } 2>&1 )
    #real_user_sys=$( { time ./tortoise --voice "../models/mol.bin" --message "based... dr. freeman?" 2>&1; } 2>&1 )
    # Extract real, user, and system times
    real_time=$(echo $real_user_sys | cut -d',' -f1)
    user_time=$(echo $real_user_sys | cut -d',' -f2)
    sys_time=$(echo $real_user_sys | cut -d',' -f3)
    # Append results to CSV file
    echo "$i,$real_time,$user_time,$sys_time" >> "$csv_file"
done