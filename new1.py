#data = [{"a": 1}, {"b": 1}, "str"]
data = []

for item in data:
    assert isinstance(item, dict)