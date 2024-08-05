from date import Date
from distance import Distance
from energy import Energy
from time import Time
from utils import _round


class Run:
    def __init__(self) -> None:
        self.date: Date = None
        self.distance: Distance = None  # In metres
        self.duration: Time = None  # hh:mm:ss
        self.energy: Energy = None
        self.ascent: Distance = None
        self.descent: Distance = None
        self.sweat: int = None
        self.avg_heartbeats_per_minute: int = None
        self.avg_power: int = None
        self.avg_steps_per_minutes: int = None
        self.avg_temperature: int = None
        self.effect: str = None  # Pace, Basic,...
        self.location: str = None
        self.Notes: str = None

    def speed_kmh(self, number_of_digits: int | None = None) -> float:
        speed_kmh: float = self.distance.to_kilometer() / self.duration.to_hours()
        return _round(speed_kmh, number_of_digits)

    def speed_ms(self, number_of_digits: int | None = None) -> float:
        speed_ms: float = self.distance.to_meter() / self.duration.to_seconds()
        return _round(speed_ms, number_of_digits)

    def num_of_steps(self, number_of_digits: int | None = None) -> float:
        num_of_steps: float = self.avg_steps_per_minutes * self.duration.to_minutes()
        return _round(num_of_steps, number_of_digits)

    def step_length(self, number_of_digits: int | None = None) -> float:
        num_of_steps: float = self.num_of_steps()
        meters_per_step: float = self.distance.to_meter() / num_of_steps
        return _round(meters_per_step, number_of_digits)

    def num_of_heartbeats(self) -> float:
        num_of_heartbeats: float = self.avg_heartbeats_per_minute * self.duration.to_minutes()
        return _round(num_of_heartbeats)


