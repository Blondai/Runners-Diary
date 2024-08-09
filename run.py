import json
from typing import Any

from date import Date
from distance import Distance
from energy import Energy
from speed import Speed
from duration import Duration
from utils import _round, get_directory, file_exists


class Run:
    """
    Represents a recorded run with various attributes including date, distance, duration, and more.

    Attributes:
        date (Date): The date of the run.
        distance (Distance): The distance covered in the run.
        duration (Duration): The duration of the run.
        energy (Energy): The energy expended during the run.
        ascent (Distance): The total ascent during the run.
        descent (Distance): The total descent during the run.
        sweat (int): The amount of sweat produced during the run (in milliliters).
        avg_heartbeats_per_minute (int): The average heartbeats per minute during the run.
        avg_power (int): The average power output during the run (in watts).
        cadence (int): The cadence during the run (steps per minute).
        avg_temperature (int): The average temperature during the run (in degrees Celsius).
        aerob (float): The aerobic effect of the run.
        anaerob (float): The anaerobic effect of the run.
        effect (str): The training effect of the run.
        training (str): The type of training during the run.
        location (str): The location where the run took place.
        notes (str): Additional notes about the run.
    """

    # Konvert to all kwargs?
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
        """
                Initialize a Run instance with the specified attributes.

                Args:
                    date (Date): The date of the run.
                    distance (Distance): The distance covered in the run.
                    duration (Duration): The duration of the run.
                    energy (Energy): The energy expended during the run.
                    ascent (Distance): The total ascent during the run.
                    descent (Distance): The total descent during the run.
                    sweat (int): The amount of sweat produced during the run (in milliliters).
                    avg_heartbeats_per_minute (int): The average heartbeats per minute during the run.
                    avg_power (int): The average power output during the run (in watts).
                    cadence (int): The cadence during the run (steps per minute).
                    avg_temperature (int): The average temperature during the run (in degrees Celsius).
                    aerob (float): The aerobic effect of the run.
                    anaerob (float): The anaerobic effect of the run.
                    effect (str): The training effect of the run.
                    training (str): The type of training during the run.
                    location (str): The location where the run took place.
                    notes (str): Additional notes about the run.
                """
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
        self.avg_temperature: int = avg_temperature
        self.aerob: float = aerob
        self.anaerob: float = anaerob
        self.effect: str = effect
        self.training: str = training
        self.location: str = location
        self.notes: str = notes

    def __dict__(self):
        """
        Convert the Run instance to a dictionary representation.

        Returns:
            dict[str, Any]: A dictionary with the Run attributes as key-value pairs.
        """
        dictionary: dict[str, Any] = {'date': self.date.__str__(),
                                      'distance': self.distance.__str__(),
                                      'duration': self.duration.__str__(),
                                      'energy': self.energy.__str__(),
                                      'ascent': self.ascent.__str__(),
                                      'descent': self.descent.__str__(),
                                      'sweat': str(self.sweat),
                                      'avg_heartbeats_per_minute': str(self.avg_heartbeats_per_minute),
                                      'avg_power': str(self.avg_power),
                                      'cadence': str(self.cadence),
                                      'avg_temperature': str(self.avg_temperature),
                                      'aerob': str(self.aerob),
                                      'anaerob': str(self.anaerob),
                                      'effect': str(self.effect),
                                      'training': str(self.training),
                                      'location': str(self.location),
                                      'notes': str(self.notes)}
        return dictionary

    def speed(self) -> Speed:
        """
        Calculate the Speed of the run.

        Returns:
            Speed: An instance of the Speed class representing the run's speed.
        """
        speed: Speed = Speed(self.distance, self.duration)
        return speed

    def num_of_steps(self, number_of_digits: int | None = None) -> float:
        """
        Calculate the number of steps taken during the run and round it to the specified number of digits.

        Args:
            number_of_digits (int | None): The number of decimal places to round to. If None, no rounding.

        Returns:
            float: The number of steps taken, rounded to the specified number of digits.
        """
        num_of_steps: float = self.cadence * self.duration.to_minutes()
        return _round(num_of_steps, number_of_digits)

    def step_length(self, number_of_digits: int | None = None) -> float:
        """
        Calculate the length of each step in meters and round it to the specified number of digits.

        Args:
            number_of_digits (int | None): The number of decimal places to round to. If None, no rounding.

        Returns:
            float: The length of each step in meters, rounded to the specified number of digits.
        """
        num_of_steps: float = self.num_of_steps()
        meters_per_step: float = self.distance.to_meters() / num_of_steps
        return _round(meters_per_step, number_of_digits)

    def num_of_heartbeats(self) -> float:
        """
        Calculate the total number of heartbeats during the run.

        Returns:
            float: The total number of heartbeats.
        """
        num_of_heartbeats: float = self.avg_heartbeats_per_minute * self.duration.to_minutes()
        return _round(num_of_heartbeats)

    def total_steps(self) -> int:
        """
        Calculate the total number of steps taken during the run.

        Returns:
            int: The total number of steps taken.
        """
        total_steps: int = int(self.cadence * self.duration.to_minutes())
        return total_steps

    def export_to_file(self) -> None:
        """
        Export the Run instance data to a JSON file.
        """
        directory: str = get_directory(self)
        file_location: str = directory + f'{self.date.__str__(reversed=True, short=True)} Run.json'
        file_exists(file_location)
        data: str = json.dumps(self.__dict__())
        with open(file_location, 'w') as file:
            file.write(data)

    @staticmethod
    def import_from_file(file_name: str) -> 'Run':
        """
        Import a Run instance from a JSON file.

        Args:
            file_name (str): The name of the JSON file to read data from.

        Returns:
            Run: A Run instance created from the data in the JSON file.
        """
        with open(file_name, 'r') as file:
            data = json.load(file)
        date: Date = Date.from_string(data['date'])
        distance: Distance = Distance.from_string(data['distance'])
        duration: Duration = Duration.from_string(data['duration'])
        energy: Energy = Energy.from_string(data['energy'])
        ascent: Distance = Distance.from_string(data['ascent'])
        descent: Distance = Distance.from_string(data['descent'])
        sweat: int = int(data['sweat'])
        avg_heartbeats_per_minute: int = int(data['avg_heartbeats_per_minute'])
        avg_power: int = int(data['avg_power'])
        cadence: int = int(data['cadence'])
        avg_temperature: int = int(data['avg_temperature'])
        aerob: float = float(data['aerob'])
        anaerob: float = float(data['anaerob'])
        effect: str = data['effect']
        training: str = data['training']
        location: str = data['location']
        notes: str = data['notes']
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
