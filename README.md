## get_substring.py
### `get_2ch_substring(in_str: str)`
#### Finds the longest substring consisting of no more than two different characters.
## tests.py
#### Test cases to check the algorithm correctness and empirical confirmation of the O(N) complexity
```
N:    1024 chars | PROBES:  2560 | T(avg):      933838 ns | T/N:      912 ns/char
N:    2048 chars | PROBES:  1280 | T(avg):     1806641 ns | T/N:      882 ns/char
N:    4096 chars | PROBES:   640 | T(avg):     3662109 ns | T/N:      894 ns/char
N:    8192 chars | PROBES:   320 | T(avg):     7617188 ns | T/N:      930 ns/char
N:   16384 chars | PROBES:   160 | T(avg):    14843750 ns | T/N:      906 ns/char
N:   32768 chars | PROBES:    80 | T(avg):    29296875 ns | T/N:      894 ns/char
N:   65536 chars | PROBES:    40 | T(avg):    67187500 ns | T/N:     1025 ns/char
N:  131072 chars | PROBES:    20 | T(avg):   121875000 ns | T/N:      930 ns/char
N:  262144 chars | PROBES:    10 | T(avg):   254687500 ns | T/N:      972 ns/char

T/N(avg): 927ns/char | T/N(dev):  43ns/char ~4.6%
```