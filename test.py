from example import get_example_run_empty, get_example_run
from latex import safe_to_file
from run import Run

run: Run = get_example_run_empty()
run.export_to_file()

run: Run = Run.import_from_file(r'.\LaTeX\70.01.02 Run\70.01.02 Run.json')
safe_to_file(run)

run: Run = get_example_run()
run.export_to_file()

run: Run = Run.import_from_file(r'./LaTeX/70.01.01 Run/70.01.01 Run.json')
safe_to_file(run)
