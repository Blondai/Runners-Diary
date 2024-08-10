from date import Date
from energy import Energy
from numerics import Integer, Floating
from run import Run
from duration import Duration
from distance import Distance


def get_example_run() -> Run:
    """
    Create an example Run object populated with predefined data.

    This function initializes and returns a Run object with specific attributes such as date, distance, duration,
    energy, ascent, descent, and other metrics related to a running session.

    Returns:
        Run: A Run object populated with example data.
    """
    date: Date = Date(day=1, month=1, year=1970)
    distance: Distance = Distance(10000)
    duration: Duration = Duration(hours=1, minutes=9, seconds=42)
    energy: Energy = Energy(420)
    ascent: Distance = Distance(13)
    descent: Distance = Distance(15)
    sweat: Integer = Integer(1050)
    avg_heartbeats_per_minute: Integer = Integer(150)
    avg_power: Integer = Integer(300)
    cadence: Integer = Integer(160)
    avg_temperature: Integer = Integer(31)
    aerob: Floating = Floating(2.5)
    anaerob: Floating = Floating(0.0)
    effect: str = 'Basic'
    training: str = 'Basic'
    location: str = 'City'
    notes: str = 'Good Run'
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


def _get_example_date() -> Date:
    """
    Create an example Date object.

    This function returns a Date object initialized with the date January 1, 1970.

    Returns:
        Date: An example Date object.
    """
    date: Date = Date(day=1, month=1, year=1970)
    return date


def _get_example_distance() -> Distance:
    """
    Create an example Distance object.

    This function returns a Distance object initialized with a value of 10,075 meters.

    Returns:
        Distance: An example Distance object.
    """
    distance: Distance = Distance(10075)
    return distance


def _get_example_duration() -> Duration:
    """
    Create an example Duration object.

    This function returns a Duration object initialized with a duration of 1 hour, 9 minutes, and 42 seconds.

    Returns:
        Duration: An example Duration object.
    """
    duration: Duration = Duration(hours=1, minutes=9, seconds=42)
    return duration


def _get_example_energy() -> Energy:
    """
    Create an example Energy object.

    This function returns an Energy object initialized with a value of 420 kilocalories.

    Returns:
        Energy: An example Energy object.
    """
    energy: Energy = Energy(420)
    return energy


def get_example_run_empty() -> Run:
    """
    Create an example Run object with most fields left empty.

    This function initializes and returns a Run object with specific attributes, but most fields are left empty or
    initialized with empty strings. It is useful for testing scenarios where certain data might be missing.

    Returns:
        Run: A Run object with some fields left empty.
    """
    date: Date = Date(day=2, month=1, year=1970)
    distance: Distance = Distance(10000)
    duration: Duration = Duration(hours=1, minutes=9, seconds=42)
    energy: Energy = Energy.from_string('')
    ascent: Distance = Distance.from_string('')
    descent: Distance = Distance.from_string('')
    sweat: Integer = Integer.from_string('')
    avg_heartbeats_per_minute: Integer = Integer.from_string('')
    avg_power: Integer = Integer.from_string('')
    cadence: Integer = Integer.from_string('')
    avg_temperature: Integer = Integer.from_string('')
    aerob: Floating = Floating.from_string('')
    anaerob: Floating = Floating.from_string('')
    effect: str = ''
    training: str = ''
    location: str = ''
    notes: str = ''
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
