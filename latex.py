import subprocess

from run import Run
from utils import to_string, get_directory, _new_folder


def _get_preamble() -> str:
    """
    Generate the LaTeX preamble for the document.

    Returns:
        str: The LaTeX preamble as a string.
    """
    preamble: str = (r"\documentclass[20pt, a5paper]{article}"
                     "\n"
                     r"\usepackage[utf8]{inputenc}"
                     "\n"
                     r"\usepackage[english]{babel}"
                     "\n"
                     r"\usepackage[T1]{fontenc}"
                     "\n"
                     r"\usepackage[top=15mm, bottom=20mm, left=15mm, right=15mm]{geometry}"
                     "\n"
                     r"\usepackage{siunitx}"
                     "\n"
                     r"\usepackage{tabularx}"
                     "\n"
                     r"\renewcommand{\arraystretch}{2}"

                     "\n\n")
    return preamble


def _get_begin(run: Run) -> str:
    """
    Generate the beginning of the LaTeX document.

    Args:
        run (Run): The run instance.

    Returns:
        str: The beginning part of the LaTeX document as a string.
    """
    begin: str = (r"\begin{document}"
                  "\n"
                  r"\section*{Run of "
                  f"{run.date}"
                  r"}"
                  "\n\n")
    return begin


def _get_table_1(run: Run) -> str:
    """
    Generate the first part of the table for the LaTeX document.

    Args:
        run (Run): The run instance.

    Returns:
        str: The first part of the table of the LaTeX document as a string.
    """
    string_1: str = (r"\begin{center}"
                     "\n"
                     r"\begin{tabularx}{0.5\linewidth}{l l}"
                     "\n"
                     r"Distance & $"
                     f"{to_string(run.distance.to_meters())}"
                     r" \,\unit{\meter}$\\"
                     "\n"
                     r"Duration & $"
                     f"{to_string(run.duration.hours)}"
                     r" \,\unit{\hour}~ "
                     f"{to_string(run.duration.minutes)}"
                     r" \,\unit{\minute}~ "
                     f"{to_string(run.duration.seconds)}"
                     r" \,\unit{\second}$\\"
                     "\n"
                     r"Speed & $"
                     f"{to_string(run.speed().to_kmh())}"
                     r" \,\unit{\kilo\meter\per\hour}$\\"
                     "\n"
                     r"Pace & $"
                     f"{to_string(run.speed().to_pace().__str__(short=True))}"
                     r" \,\unit{\minute\per\kilo\meter}$\\"
                     "\n")
    return string_1


def _get_table_2(run: Run) -> str:
    """
    Generate the second part of the table for the LaTeX document.

    Args:
        run (Run): The run instance.

    Returns:
        str: The second part of the table of the LaTeX document as a string.
    """
    string_2: str = (r"Heartbeat & $"
                     f"{to_string(run.avg_heartbeats_per_minute.integer)}"
                     r" \,\unit{\per\minute}$\\"
                     "\n"
                     r"Cadence & $"
                     f"{to_string(run.cadence.integer)}"
                     r" \,\unit{\per\minute}$\\"
                     "\n"
                     r"Energy & $"
                     f"{to_string(run.energy.kcal)}"
                     r" \,\unit{\kilo cal}$\\"
                     "\n"
                     r"Ascent & $"
                     f"{to_string(run.ascent.to_meters())}"
                     r" \,\unit{\meter}$\\"
                     "\n"
                     r"Descent & $"
                     f"{to_string(run.descent.to_meters())}"
                     r" \,\unit{\meter}$\\"
                     "\n"
                     r"Steps & $"
                     f"{to_string(run.total_steps())}"
                     r"$\\"
                     "\n")
    return string_2


def _get_table_3(run: Run) -> str:
    """
    Generate the third part of the table for the LaTeX document.

    Args:
        run (Run): The run instance.

    Returns:
        str: The third part of the table of the LaTeX document as a string.
    """
    string_3: str = (r"Temperature & $"
                     f"{to_string(run.avg_temperature.integer)}"
                     r" \,\unit{\degreeCelsius}$\\"
                     "\n"
                     r"Sweat & $"
                     f"{to_string(run.sweat.integer)}"
                     r" \,\unit{\milli\liter}$\\"
                     "\n"
                     r"Power & $"
                     f"{to_string(run.avg_power.integer)}"
                     r" \,\unit{\watt}$\\"
                     "\n"
                     r"Training Effect & "
                     f"{to_string(run.effect)}"
                     r"\\"
                     "\n"
                     r"Aerob & $"
                     f"{to_string(run.aerob.floating)}"
                     r"$\\"
                     "\n"
                     r"Anaerob & $"
                     f"{to_string(run.anaerob.floating)}"
                     r"$\\"
                     "\n")
    return string_3


def _get_table_4(run: Run) -> str:
    """
    Generate the fourth part of the table for the LaTeX document.

    Args:
        run (Run): The run instance.

    Returns:
        str: The fourth part of the table of the LaTeX document as a string.
    """
    string_4: str = (r"Training & "
                     f"{to_string(run.training)}"
                     r"\\"
                     "\n"
                     r"Location & "
                     f"{to_string(run.location)}"
                     r"\\"
                     "\n"
                     r"Notes & "
                     f"{to_string(run.notes)}"
                     "\n"
                     r"\end{tabularx}"
                     "\n"
                     r"\end{center}"
                     "\n")
    return string_4


def _get_table(run: Run) -> str:
    """
    Generate the complete table for the LaTeX document.

    Args:
        run (Run): The run instance.

    Returns:
        str: The complete table of the LaTeX document as a string.
    """
    string_1: str = _get_table_1(run)
    string_2: str = _get_table_2(run)
    string_3: str = _get_table_3(run)
    string_4: str = _get_table_4(run)
    string: str = string_1 + string_2 + string_3 + string_4
    return string


def _get_end() -> str:
    """
    Generate the end of the LaTeX document.

    Returns:
        str: The end part of the LaTeX document as a string.
    """
    end: str = (r"\end{document}"
                "\n")
    return end


def _get_text(run: Run) -> str:
    """
    Generate the complete LaTeX document as a string.

    Args:
        run (Run): The run instance.

    Returns:
        str: The complete LaTeX document as a string.
    """
    preamble: str = _get_preamble()
    begin: str = _get_begin(run)
    table: str = _get_table(run)
    end: str = _get_end()
    text: str = preamble + begin + table + end
    return text


def _make_pdf(folder: str, file_location: str) -> None:
    """
    Generate a PDF from the LaTeX file.

    Args:
        folder (str): The output folder.
        file_location (str): The LaTeX file location.
    """
    command = ['pdflatex', '-output-directory', folder, file_location]
    subprocess.run(command)


def safe_to_file(run: Run) -> None:
    """
    Save the run data to a LaTeX file and generate a PDF.

    Args:
        run (Run): The run instance.
    """
    directory: str = get_directory(run)
    file_location: str = directory + f'{run.date.__str__(reversed=True, short=True)} Run.tex'
    _new_folder(directory)
    text: str = _get_text(run)
    with open(file_location, 'w') as file:
        file.write(text)
    _make_pdf(directory, file_location)
