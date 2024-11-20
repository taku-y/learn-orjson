import numpy as np
from typing import List
from dataclasses import dataclass, field
import orjson
from dacite import from_dict


@dataclass
class Data:
    name: str
    x: List[np.ndarray] = field(default_factory=list)

# Custom deserialization function to handle NumPy arrays
def from_dict_with_numpy(data_class, data):
    if 'x' in data:
        data['x'] = [np.array(e["data"]) for e in data["x"]]
    return from_dict(data_class=data_class, data=data)

def main():
    with open(
        "data.json", "rb"
    ) as file:  # Use "rb" to read in binary mode for `orjson`
        json_data = orjson.loads(file.read())
        data = from_dict_with_numpy(data_class=Data, data=json_data)
    print(data)

if __name__ == "__main__":
    main()
