import typing as tp


class Timedata:
    def __init__(self, hours: int, minutes: int, seconds: int):
        if not hours >= 0:
            raise ValueError(f"hours should not less than 0, got {hours}")
        if not 0 <= minutes < 60:
            raise ValueError(f"minutes should be between 0 and 59, got {minutes}")
        if not 0 <= seconds < 60:
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

        return cls(*parts_formatted)  # 🤔🤔🤔

    def __repr__(self) -> str:
        return f"<Timedata {self.to_string()}>"

    def __str__(self) -> str:
        return self.to_string()

    @staticmethod
    def _normalize(
        hours: int,
        minutes: int,
        seconds: int,
    ) -> tp.Tuple[int, int, int]:
        if seconds >= 60:
            minutes += seconds // 60
            seconds = seconds % 60
        if minutes >= 60:
            hours += minutes // 60
            minutes = minutes % 60

        return hours, minutes, seconds

    def __add__(self, other) -> "Timedata":
        seconds = self.seconds + other.seconds
        minutes = self.minutes + other.minutes
        hours = self.hours + other.hours

        return Timedata(*self._normalize(hours, minutes, seconds))

    def to_tuple(self) -> tp.Tuple[int, int, int]:
        return (self.hours, self.minutes, self.seconds)

    def __eq__(self, other) -> bool:
        return self.to_tuple() == other.to_tuple()


if __name__ == "__main__":
    x = Timedata.from_string("2:30:02")
    y = Timedata.from_string("2:30:00")

    print(x + y)
