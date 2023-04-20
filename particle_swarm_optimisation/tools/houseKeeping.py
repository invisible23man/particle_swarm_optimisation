import os
import glob
import datetime

def cleanup_logs_and_figures(logDir = './logs', figDir = './figures'):
    # get current date and time
    now = datetime.datetime.now()

    # define timestamp format
    timestamp_format = now.strftime("pso_%Y-%m-%d")

    # get all log files for the day
    log_files = glob.glob(os.path.join(logDir,f"{timestamp_format}*.log"))
    # get all figure files for the day
    fig_files = glob.glob(os.path.join(figDir,f"{timestamp_format}*.png"))

    for file in [log_files, fig_files]:
        remove_file(file) 

def remove_file(files):
    # sort files by timestamp
    files.sort()
    
    # keep only the last file
    if len(files) > 1:
        files_to_delete = files[:-1]
        for file in files_to_delete:
            os.remove(file)

if __name__ == '__main__':
    print("Cleaning up...")
    cleanup_logs_and_figures()
