from date import Date
from energy import Energy
from run import Run
from duration import Duration
from distance import Distance


def get_example_run() -> Run:
    date: Date = Date(day=1, month=1, year=1970)
    distance: Distance = Distance(10000)
    duration: Duration = Duration(hours=1, minutes=9, seconds=42)
    energy: Energy = Energy(420)
    ascent: Distance = Distance(13)
    descent: Distance = Distance(15)
    sweat: int = 1050
    avg_heartbeats_per_minute: int = 150
    avg_power: int = 300
    cadence: int = 160
    avg_temperature: int = 31
    aerob: float = 2.5
    anaerob: float = 0.0
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


def get_example_date() -> Date:
    date: Date = Date(day=1, month=1, year=1970)
    return date


def get_example_distance() -> Distance:
    distance: Distance = Distance(10075)
    return distance


def get_example_duration() -> Duration:
    duration: Duration = Duration(hours=1, minutes=9, seconds=42)
    return duration


def get_example_energy() -> Energy:
    energy: Energy = Energy(420)
    return energy
