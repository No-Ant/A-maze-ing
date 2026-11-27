from typing import NotRequired, TypedDict, Any, cast


class ConfigError(Exception):
    def __init__(self, message: str = "Config error!") -> None:
        super().__init__(message)


class Config(TypedDict):
    WIDTH: int
    HEIGHT: int
    ENTRY: tuple[int, int]
    EXIT: tuple[int, int]
    OUTPUT_FILE: str
    PERFECT: bool
    SEED: NotRequired[int]


def get_values(path: str) -> dict[str, Any]:

    values: dict = {}
    key_value: list = []
    try:
        with open(path, "r") as file:
            for line in file:
                line = line.rstrip("\r\n")
                key_value = line.split("=", 1)
                if not key_value[0].strip() or key_value[0].strip()[0] == "#":
                    continue
                if len(key_value) != 2:
                    raise ConfigError(
                        "The configuration file must contain "
                        "one KEY=VALUE pair per line!"
                    )
                if (
                    key_value[0] != key_value[0].strip()
                    or key_value[1] != key_value[1].strip()
                ):
                    raise ConfigError(
                        "Only empty lines or comments can "
                        "contain white spaces!"
                    )
                if key_value[0] == "OUTPUT_FILE":
                    if not key_value[1]:
                        raise ConfigError("OUTPUT_FILE must have a value!")
                if key_value[0] == "PERFECT":
                    if key_value[1].strip() == "True":
                        values[key_value[0]] = True
                        continue
                    elif key_value[1].strip() == "False":
                        values[key_value[0]] = False
                        continue
                    else:
                        raise ConfigError("PERFECT must be True or False!")
                if key_value[0] == "ENTRY" or key_value[0] == "EXIT":
                    coordinates: list = key_value[1].strip().split(",")
                    if len(coordinates) != 2:
                        raise ConfigError(
                            "Invalid coordinates: "
                            "both must follow the format x,y!"
                        )
                    for i in range(0, 2):
                        try:
                            coordinates[i] = int(coordinates[i])
                        except ValueError:
                            raise ConfigError(
                                "Invalid coordinates: both must be an int!"
                            ) from None
                    values[key_value[0]] = tuple(coordinates)
                    continue
                if key_value[0] == "WIDTH" or key_value[0] == "HEIGHT":
                    try:
                        values[key_value[0]] = int(key_value[1])
                    except ValueError:
                        raise ConfigError(
                            "Invalid dimensions: both must be an int!"
                        ) from None
                    continue
                if key_value[0] == "SEED":
                    try:
                        values[key_value[0]] = int(key_value[1])
                    except ValueError:
                        raise ConfigError(
                            "Invalid seed: must be an int!"
                        ) from None
                    continue
                values[key_value[0]] = key_value[1].strip()
        return values
    except (OSError, UnicodeDecodeError) as e:
        raise ConfigError(f"Error opening config file: {e}") from e


def validate_values(values: dict[str, Any]) -> Config:
    valid_parameters: list = [
        "WIDTH",
        "HEIGHT",
        "ENTRY",
        "EXIT",
        "OUTPUT_FILE",
        "PERFECT",
        "SEED"
    ]
    mandatory = [
        "WIDTH",
        "HEIGHT",
        "ENTRY",
        "EXIT",
        "OUTPUT_FILE",
        "PERFECT"
    ]
    for key in values:
        if key not in valid_parameters:
            raise ConfigError("Invalid key!")
    for key in mandatory:
        if key not in values:
            raise ConfigError(f"Missing key! Must have at least: {mandatory}")
    height = values["HEIGHT"]
    width = values["WIDTH"]
    entry_coord = values["ENTRY"]
    exit_coord = values["EXIT"]
    if height < 3 or width < 3:
        raise ConfigError("Maze must be at least a 3x3!")
    if exit_coord == entry_coord:
        raise ConfigError("Entry and exit must be different!")
    if entry_coord[0] not in range(0, width):
        raise ConfigError("Entry is out of bounds!")
    if exit_coord[0] not in range(0, width):
        raise ConfigError("Exit is out of bounds!")
    if entry_coord[1] not in range(0, height):
        raise ConfigError("Entry is out of bounds!")
    if exit_coord[1] not in range(0, height):
        raise ConfigError("Exit is out of bounds!")
    return cast(Config, values)


if __name__ == "__main__":
    test = get_values("config.txt")
    print(test)
    validate_values(test)
