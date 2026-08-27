# Input Shaper notes - Test 20230430

## Y Axis

__GCode:__ `TEST_RESONANCES AXIS=X`
__Analysis:__ `~/klipper/scripts/calibrate_shaper.py /tmp/resonances_x_*.csv -o /tmp/shaper_calibrate_x.png`
```
Fitted shaper 'zv' frequency = 50.6 Hz (vibrations = 14.3%, smoothing ~= 0.066)
To avoid too much smoothing with 'zv', suggested max_accel <= 10000 mm/sec^2
Fitted shaper 'mzv' frequency = 48.0 Hz (vibrations = 0.2%, smoothing ~= 0.088)
To avoid too much smoothing with 'mzv', suggested max_accel <= 6800 mm/sec^2
Fitted shaper 'ei' frequency = 59.8 Hz (vibrations = 1.0%, smoothing ~= 0.090)
To avoid too much smoothing with 'ei', suggested max_accel <= 6700 mm/sec^2
Fitted shaper '2hump_ei' frequency = 73.0 Hz (vibrations = 0.0%, smoothing ~= 0.101)
To avoid too much smoothing with '2hump_ei', suggested max_accel <= 5900 mm/sec^2
Fitted shaper '3hump_ei' frequency = 88.8 Hz (vibrations = 0.0%, smoothing ~= 0.104)
To avoid too much smoothing with '3hump_ei', suggested max_accel <= 5800 mm/sec^2
Recommended shaper is mzv @ 48.0 Hz
```

## Y Axis

__GCode:__ `TEST_RESONANCES AXIS=Y`
__Analysis:__ `~/klipper/scripts/calibrate_shaper.py /tmp/resonances_y_*.csv -o /tmp/shaper_calibrate_y.png`
```
Fitted shaper 'zv' frequency = 62.2 Hz (vibrations = 17.8%, smoothing ~= 0.046)
To avoid too much smoothing with 'zv', suggested max_accel <= 15100 mm/sec^2
Fitted shaper 'mzv' frequency = 38.8 Hz (vibrations = 4.5%, smoothing ~= 0.135)
To avoid too much smoothing with 'mzv', suggested max_accel <= 4400 mm/sec^2
Fitted shaper 'ei' frequency = 55.4 Hz (vibrations = 4.3%, smoothing ~= 0.105)
To avoid too much smoothing with 'ei', suggested max_accel <= 5700 mm/sec^2
Fitted shaper '2hump_ei' frequency = 48.8 Hz (vibrations = 1.9%, smoothing ~= 0.227)
To avoid too much smoothing with '2hump_ei', suggested max_accel <= 2600 mm/sec^2
Fitted shaper '3hump_ei' frequency = 48.4 Hz (vibrations = 0.5%, smoothing ~= 0.350)
To avoid too much smoothing with '3hump_ei', suggested max_accel <= 1600 mm/sec^2
Recommended shaper is ei @ 55.4 Hz
```
