# Tests for safe threading

Finding that Python Version 3.10 behaves different in threading version 3.9 and before. Running on Windows 10.

Python 3.8

```
> py -3.8 basic_thread_tests.py
Interpreter switch interval: 0.005
Python Version: 3.8.2
Issue found: 17503455 but expected 100000000
Issue found: 17150604 but expected 100000000
Issue found: 23602452 but expected 100000000
```

Python 3.10

```
> py -3.10 basic_thread_tests.py
Interpreter switch interval: 0.005
Python Version: 3.10.5
```

## Resources

https://www.educative.io/courses/python-concurrency-for-senior-engineering-interviews/xlm6QznGGNE
https://www.youtube.com/watch?v=s5PCh_FaMfM
