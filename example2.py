

def check_reactor_temperature(temperature_celsius):       """
    Checks whether temperature is above max_temperature
    and returns a status.
    """
    from reactor import max_temperature
    if temperature_celsius > max_temperature:
        status = 1
    else:
        status = 0
    return status

def test_check_reactor_temperature(monkeypatch):
	monkeypatch.setattr(reactor, "max_temperature", 100)
    assert check_reactor_temperature(99)  == 0
    assert check_reactor_temperature(100) == 0   # boundary cases easily go wrong
    assert check_reactor_temperature(101) == 1