# Input Shaper notes - Test 20230302

## Y Axis

__GCode:__ `TEST_RESONANCES AXIS=X`
__Analysis:__ `~/klipper/scripts/calibrate_shaper.py /tmp/resonances_x_*.csv -o /tmp/shaper_calibrate_x.png`
```
Fitted shaper 'zv' frequency = 52.4 Hz (vibrations = 8.5%, smoothing ~= 0.062)
To avoid too much smoothing with 'zv', suggested max_accel <= 10700 mm/sec^2
Fitted shaper 'mzv' frequency = 51.6 Hz (vibrations = 0.1%, smoothing ~= 0.076)
To avoid too much smoothing with 'mzv', suggested max_accel <= 7800 mm/sec^2
Fitted shaper 'ei' frequency = 62.2 Hz (vibrations = 0.0%, smoothing ~= 0.083)
To avoid too much smoothing with 'ei', suggested max_accel <= 7200 mm/sec^2
Fitted shaper '2hump_ei' frequency = 78.8 Hz (vibrations = 0.0%, smoothing ~= 0.087)
To avoid too much smoothing with '2hump_ei', suggested max_accel <= 6900 mm/sec^2
Fitted shaper '3hump_ei' frequency = 96.0 Hz (vibrations = 0.0%, smoothing ~= 0.089)
To avoid too much smoothing with '3hump_ei', suggested max_accel <= 6700 mm/sec^2
Recommended shaper is mzv @ 51.6 Hz
```

## Y Axis

__GCode:__ `TEST_RESONANCES AXIS=Y`
__Analysis:__ `~/klipper/scripts/calibrate_shaper.py /tmp/resonances_y_*.csv -o /tmp/shaper_calibrate_y.png`
```
Fitted shaper 'zv' frequency = 38.0 Hz (vibrations = 6.7%, smoothing ~= 0.110)
To avoid too much smoothing with 'zv', suggested max_accel <= 5600 mm/sec^2
Fitted shaper 'mzv' frequency = 36.4 Hz (vibrations = 0.3%, smoothing ~= 0.154)
To avoid too much smoothing with 'mzv', suggested max_accel <= 3900 mm/sec^2
Fitted shaper 'ei' frequency = 43.4 Hz (vibrations = 0.0%, smoothing ~= 0.171)
To avoid too much smoothing with 'ei', suggested max_accel <= 3500 mm/sec^2
Fitted shaper '2hump_ei' frequency = 55.2 Hz (vibrations = 0.0%, smoothing ~= 0.177)
To avoid too much smoothing with '2hump_ei', suggested max_accel <= 3400 mm/sec^2
Fitted shaper '3hump_ei' frequency = 67.2 Hz (vibrations = 0.0%, smoothing ~= 0.181)
To avoid too much smoothing with '3hump_ei', suggested max_accel <= 3300 mm/sec^2
Recommended shaper is mzv @ 36.4 Hz
```
