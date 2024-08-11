from date import Date
from distance import Distance
from duration import Duration
from energy import Energy
from numerics import Integer, Floating
from run import Run
from constants import _get_max_tries


def input_run() -> Run:
    date: Date = _input_date()
    distance: Distance = _input_distance()
    duration: Duration = _input_duration()
    energy: Energy = _input_energy()
    ascent: Distance = _input_ascent()
    descent: Distance = _input_descent()
    sweat: Integer = _input_sweat()
    avg_heartbeats_per_minute: Integer = _input_avg_heartbeats_per_minute()
    avg_power: Integer = _input_avg_power()
    cadence: Integer = _input_cadence()
    avg_temperature: Integer = _input_avg_temperature()
    aerob: Floating = _input_aerob()
    anaerob: Floating = _input_anaerob()
    effect: str = _input_effect()
    training: str = _input_training()
    location: str = _input_location()
    notes: str = _input_notes()
    run: Run = Run(date=date,
                   distance=distance,
                   duration=duration,
                   energy=energy,
                   ascent=ascent,
                   descent=descent,
                   sweat=sweat,
                   avg_heartbeats_per_minute=avg_heartbeats_per_minute,
                   avg_power=avg_power,
                   cadence=cadence,
                   avg_temperature=avg_temperature,
                   aerob=aerob,
                   anaerob=anaerob,
                   effect=effect,
                   training=training,
                   location=location,
                   notes=notes)
    return run


def _test_date(string: str) -> bool:
    """
    Validate the format and values of a date string.

    Args:
        string (str): The date string to validate, expected format 'dd.mm.yyyy'.

    Returns:
        bool: True if the string is in the correct format and values are within valid ranges, False otherwise.
    """
    integers: set[str] = set([f'{i}' for i in range(10)])
    lengths: list[int] = [2, 2, 4]
    maxima: list[int] = [31, 12, float('inf')]
    split_string: list[str] = string.split('.')
    for index, string in enumerate(split_string):
        if len(string) != lengths[index]:
            print("String has the wrong format. Use 'dd.mmm.yyyy'.")
            return False
        if int(string) > maxima[index]:
            print(f"Number '{int(string)}' is too big. Needs to be smaller than {maxima[index] + 1}.")
            return False
        for character in string:
            if not character in integers:
                print(f"Part '{character}' of string is not an integer.")
                return False
    return True


def _test_distance(string: str) -> bool:
    """
    Validate that the distance string consists only of digits.

    Args:
        string (str): The distance string to validate.

    Returns:
        bool: True if the string contains only digits, False otherwise.
    """
    integers: set[str] = set([f'{i}' for i in range(10)])
    for character in string:
        if not character in integers:
            print(f"Part '{character}' of string is not an integer.")
            return False
    return True


def _test_duration(string: str) -> bool:
    """
    Validate the format and values of a duration string.

    Args:
        string (str): The duration string to validate, expected format 'hh:mm:ss' or 'mm:ss'.

    Returns:
        bool: True if the string is in the correct format and values are within valid ranges, False otherwise.
    """
    integers: set[str] = set([f'{i}' for i in range(10)])
    lengths: list[int] = [2, 2, 2]
    maxima: list[int] = [float('inf'), 59, 59]
    split_string: list[str] = string.split(':')
    for index, string in enumerate(split_string):
        if len(string) != lengths[index]:
            print("String has the wrong format. Use 'hh:mm:ss' or 'mm:ss'.")
            return False
        if int(string) > maxima[index]:
            print(f"Number '{int(string)}' is too big. Needs to be smaller than {maxima[index] + 1}.")
            return False
        for character in string:
            if not character in integers:
                print(f"Part '{character}' of string is not an integer.")
                return False
    return True


def _test_energy(string: str) -> bool:
    """
    Validate the format and values of a duration string.

    Args:
        string (str): The duration string to validate, expected format 'hh:mm:ss' or 'mm:ss'.

    Returns:
        bool: True if the string is in the correct format and values are within valid ranges, False otherwise.
    """
    integers: set[str] = set([f'{i}' for i in range(10)])
    for character in string:
        if not character in integers:
            print(f"Part '{character}' of string is not an integer.")
            return False
    return True


def _test_int(string: str) -> bool:
    """
    Validate that the integer string consists only of digits.

    Args:
        string (str): The integer string to validate.

    Returns:
        bool: True if the string contains only digits, False otherwise.
    """
    integers: set[str] = set([f'{i}' for i in range(10)])
    for character in string:
        if not character in integers:
            print(f"Part '{character}' of string is not an integer.")
            return False
    return True


def _test_float(string: str) -> bool:
    """
    Validate that the float string consists of digits and optionally a dot.

    Args:
        string (str): The float string to validate.

    Returns:
        bool: True if the string contains only digits and/or a dot, False otherwise.
    """
    floats: set[str] = set([f'{i}' for i in range(10)])
    floats.add('.')
    for character in string:
        if not character in floats:
            print(f"Part '{character}' of string is not an integer or dot.")
            return False
    return True


def _input_date() -> Date:
    """
    Prompt the user to input a date and validate its format.

    Returns:
        Date: A Date object created from the user's input if valid; otherwise, prompts again.

    Raises:
        TimeoutError: If the maximum number of attempts is exceeded.
    """
    for _ in range(_get_max_tries()):
        string: str = input("Date [dd.mm.yyyy]: ")
        if _test_date(string):
            date: Date = Date.from_string(string)
            return date
    raise TimeoutError("To many tries.")


def _input_distance() -> Distance:
    """
    Prompt the user to input a distance and validate its format.

    Returns:
        Distance: A Distance object created from the user's input if valid; otherwise, prompts again.

    Raises:
        TimeoutError: If the maximum number of attempts is exceeded.
    """
    for _ in range(_get_max_tries()):
        string: str = input("Distance [m]: ")
        if string == '':
            print("Distance is a necessary metric.")
            continue
        if _test_distance(string):
            distance: Distance = Distance.from_string(string)
            return distance
    raise TimeoutError("To many tries.")


def _input_duration() -> Duration:
    """
    Prompt the user to input a duration and validate its format.

    Returns:
        Duration: A Duration object created from the user's input if valid; otherwise, prompts again.

    Raises:
        TimeoutError: If the maximum number of attempts is exceeded.
    """
    for _ in range(_get_max_tries()):
        string: str = input("Duration [hh:mm:ss | mm:ss]: ")
        if string == '':
            print("Duration is a necessary metric.")
            continue
        if _test_duration(string):
            duration: Duration = Duration.from_string(string)
            return duration
    raise TimeoutError("To many tries.")


def _input_energy() -> Energy:
    """
    Prompt the user to input energy and validate its format.

    Returns:
        Energy: An Energy object created from the user's input if valid; otherwise, prompts again.

    Raises:
        TimeoutError: If the maximum number of attempts is exceeded.
    """
    for _ in range(_get_max_tries()):
        string: str = input("Energy [kcal]: ")
        if _test_energy(string) or string == '':
            energy: Energy = Energy.from_string(string)
            return energy
    raise TimeoutError("To many tries.")


def _input_ascent() -> Distance:
    """
    Prompt the user to input ascent distance and validate its format.

    Returns:
        Distance: A Distance object created from the user's input if valid; otherwise, prompts again.

    Raises:
        TimeoutError: If the maximum number of attempts is exceeded.
    """
    for _ in range(_get_max_tries()):
        string: str = input("Ascent [m]: ")
        if _test_distance(string) or string == '':
            ascent: Distance = Distance.from_string(string)
            return ascent
    raise TimeoutError("To many tries.")


def _input_descent() -> Distance:
    """
    Prompt the user to input descent distance and validate its format.

    Returns:
        Distance: A Distance object created from the user's input if valid; otherwise, prompts again.

    Raises:
        TimeoutError: If the maximum number of attempts is exceeded.
    """
    for _ in range(_get_max_tries()):
        string: str = input("Descent [m]: ")
        if _test_distance(string) or string == '':
            descent: Distance = Distance.from_string(string)
            return descent
    raise TimeoutError("To many tries.")


def _input_sweat() -> Integer:
    """
    Prompt the user to input the amount of sweat and validate its format.

    Returns:
        Integer: An Integer object created from the user's input if valid; otherwise, prompts again.

    Raises:
        TimeoutError: If the maximum number of attempts is exceeded.
    """
    for _ in range(_get_max_tries()):
        string: str = input("Sweat [mL]: ")
        if _test_int(string) or string == '':
            sweat: Integer = Integer.from_string(string)
            return sweat
    raise TimeoutError("To many tries.")


def _input_avg_heartbeats_per_minute() -> Integer:
    """
    Prompt the user to input the average heartbeats per minute and validate its format.

    Returns:
        Integer: An Integer object created from the user's input if valid; otherwise, prompts again.

    Raises:
        TimeoutError: If the maximum number of attempts is exceeded.
    """
    for _ in range(_get_max_tries()):
        string: str = input("Average Heartbeats per Minute [bpm]: ")
        if _test_int(string) or string == '':
            avg_heartbeats_per_minute: Integer = Integer.from_string(string)
            return avg_heartbeats_per_minute
    raise TimeoutError("To many tries.")


def _input_avg_power() -> Integer:
    """
    Prompt the user to input the average power and validate its format.

    Returns:
        Integer: An Integer object created from the user's input if valid; otherwise, prompts again.

    Raises:
        TimeoutError: If the maximum number of attempts is exceeded.
    """
    for _ in range(_get_max_tries()):
        string: str = input("Average Power [W]: ")
        if _test_int(string) or string == '':
            avg_power: Integer = Integer.from_string(string)
            return avg_power
    raise TimeoutError("To many tries.")


def _input_cadence() -> Integer:
    """
    Prompt the user to input the cadence and validate its format.

    Returns:
        Integer: An Integer object created from the user's input if valid; otherwise, prompts again.

    Raises:
        TimeoutError: If the maximum number of attempts is exceeded.
    """
    for _ in range(_get_max_tries()):
        string: str = input("Cadence [steps / min]: ")
        if _test_int(string) or string == '':
            cadence: Integer = Integer.from_string(string)
            return cadence
    raise TimeoutError("To many tries.")


def _input_avg_temperature() -> Integer:
    """
    Prompt the user to input the average temperature and validate its format.

    Returns:
        Integer: An Integer object created from the user's input if valid; otherwise, prompts again.

    Raises:
        TimeoutError: If the maximum number of attempts is exceeded.
    """
    for _ in range(_get_max_tries()):
        string: str = input("Average Temperature [°C]: ")
        if _test_int(string) or string == '':
            avg_temperature: Integer = Integer.from_string(string)
            return avg_temperature
    raise TimeoutError("To many tries.")


def _input_aerob() -> Floating:
    """
    Prompt the user to input the aerob value and validate its format.

    Returns:
        Floating: A Floating object created from the user's input if valid; otherwise, prompts again.

    Raises:
        TimeoutError: If the maximum number of attempts is exceeded.
    """
    for _ in range(_get_max_tries()):
        string: str = input("Aerob: ")
        if _test_float(string) or string == '':
            aerob: Floating = Floating.from_string(string)
            return aerob
    raise TimeoutError("To many tries.")


def _input_anaerob() -> Floating:
    """
    Prompt the user to input the anaerob value and validate its format.

    Returns:
        Floating: A Floating object created from the user's input if valid; otherwise, prompts again.

    Raises:
        TimeoutError: If the maximum number of attempts is exceeded.
    """
    for _ in range(_get_max_tries()):
        string: str = input("Anaerob: ")
        if _test_float(string) or string == '':
            anaerob: Floating = Floating.from_string(string)
            return anaerob
    raise TimeoutError("To many tries.")


def _input_effect() -> str:
    """
    Prompt the user to input the effect and return the value.

    Returns:
        str: The effect string provided by the user.
    """
    string: str = input("Effect: ")
    return string


def _input_training() -> str:
    """
    Prompt the user to input the training type and return the value.

    Returns:
        str: The training string provided by the user.
    """
    string: str = input("Training: ")
    return string


def _input_location() -> str:
    """
    Prompt the user to input the location and return the value.

    Returns:
        str: The location string provided by the user.
    """
    string: str = input("Location: ")
    return string


def _input_notes() -> str:
    """
    Prompt the user to input notes and return the value.

    Returns:
        str: The notes string provided by the user.
    """
    string: str = input("Notes: ")
    return string
