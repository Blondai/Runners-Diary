from input_run import input_run
from latex import safe_to_file
from run import Run

run: Run = input_run()
print("\nSaving run to json file.")
run.export_to_file()
print("\nExporting run to pdf file.")
safe_to_file(run)
