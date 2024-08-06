import json

from date import Date
from distance import Distance
from energy import Energy
from speed import Speed
from duration import Duration
from utils import _round


class Run:
    # Better with only kwargs?
    def __init__(self,
                 date: Date,
                 distance: Distance,
                 duration: Duration,
                 energy: Energy,
                 ascent: Distance,
                 descent: Distance,
                 sweat: int,
                 avg_heartbeats_per_minute: int,
                 avg_power: int,
                 cadence: int,
                 avg_temperature: int,
                 aerob: float,
                 anaerob: float,
                 effect: str,
                 training: str,
                 location: str,
                 notes: str) -> None:
        self.date: Date = date
        self.distance: Distance = distance
        self.duration: Duration = duration
        self.energy: Energy = energy
        self.ascent: Distance = ascent
        self.descent: Distance = descent
        self.sweat: int = sweat
        self.avg_heartbeats_per_minute: int = avg_heartbeats_per_minute
        self.avg_power: int = avg_power
        self.cadence: int = cadence
        self.avg_steps_per_minutes: int = cadence
        self.avg_temperature: int = avg_temperature
        self.aerob: float = aerob
        self.anaerob: float = anaerob
        self.effect: str = effect
        self.training: str = training
        self.location: str = location
        self.notes: str = notes
        self.speed: Speed = Speed(self.distance, self.duration)
        self.total_steps: int = self.total_steps()

    # TODO: Add dict function to make export an import possible
    def __dict__(self):
        pass

    def speed_kmh(self, number_of_digits: int | None = None) -> float:
        speed_kmh: float = self.speed.to_kmh()
        return _round(speed_kmh, number_of_digits)

    def speed_ms(self, number_of_digits: int | None = None) -> float:
        speed_ms: float = self.speed_ms()
        return _round(speed_ms, number_of_digits)

    def num_of_steps(self, number_of_digits: int | None = None) -> float:
        num_of_steps: float = self.avg_steps_per_minutes * self.duration.to_minutes()
        return _round(num_of_steps, number_of_digits)

    def step_length(self, number_of_digits: int | None = None) -> float:
        num_of_steps: float = self.num_of_steps()
        meters_per_step: float = self.distance.to_meters() / num_of_steps
        return _round(meters_per_step, number_of_digits)

    def num_of_heartbeats(self) -> float:
        num_of_heartbeats: float = self.avg_heartbeats_per_minute * self.duration.to_minutes()
        return _round(num_of_heartbeats)

    def total_steps(self) -> int:
        total_steps: int = int(self.avg_steps_per_minutes * self.duration.to_minutes())
        return total_steps

    # TODO: Not yet working
    def export_to_file(self) -> None:
        raise NotImplementedError("'export_to_file' is not yet implemented.")
        # file_location: str = (f'./LaTeX/'
        #                       f'{self.date.__str__(reversed=True, short=True)} Run/'
        #                       f'{self.date.__str__(reversed=True, short=True)} Run.json')
        # data: str = json.dumps(self.__dict__)
        # with open(file_location, 'w') as file:
        #     file.write(data)


    # TODO: Add import_from_file
    def import_from_file(self, file_name: str) -> None:
        raise NotImplementedError("'import_from_file' is not yet implemented.")


