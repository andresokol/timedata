import typing as tp


class Timedata:
    LIMIT: int = 60

    def __init__(self, hours: int, minutes: int, seconds: int):  # other comment
        if not hours >= 0:
            raise ValueError(f"hours should not less than 0, got {hours}")
        if not 0 <= minutes < self.LIMIT:
            raise ValueError(f"minutes should be between 0 and 59, got {minutes}")
        if not 0 <= seconds < self.LIMIT:
            raise ValueError(f"seconds should be between 0 and 59, got {seconds}")

        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def to_string(self) -> str:
        return f"{self.hours}:{self.minutes:02}:{self.seconds:02}"

    @classmethod
    def from_string(cls, sample) -> "Timedata":
        parts = sample.split(":")
        parts_formatted = [int(part) for part in parts]

        return cls(*parts_formatted)

    def __repr__(self) -> str:
        return f"<Timedata {self.to_string()}>"

    def __str__(self) -> str:
        return self.to_string()

    @classmethod
    def _normalize(
        cls,
        hours: int,
        minutes: int,
        seconds: int,
    ) -> tp.Tuple[int, int, int]:
        if seconds >= cls.LIMIT:
            minutes += seconds // cls.LIMIT
            seconds = seconds % cls.LIMIT
        if minutes >= cls.LIMIT:
            hours += minutes // cls.LIMIT
            minutes = minutes % cls.LIMIT

        return hours, minutes, seconds

    def __add__(self, other) -> "Timedata":
        seconds = self.seconds + other.seconds
        minutes = self.minutes + other.minutes
        hours = self.hours + other.hours

        return self.__class__(*self._normalize(hours, minutes, seconds))

    def _as_tuple(self) -> tp.Tuple[int, int, int]:
        return (self.hours, self.minutes, self.seconds)

    def __as_tuple(self):
        return self._as_tuple()

    def __eq__(self, other) -> bool:
        return self._as_tuple() == other._as_tuple()


class MetricTimedata(Timedata):
    LIMIT = 100


if __name__ == "__main__":
    x = MetricTimedata.from_string("2:30:02")
    y = MetricTimedata.from_string("2:30:00")

    print(x + 10)
