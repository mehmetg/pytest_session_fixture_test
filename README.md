`py.test -s test\` produces the output below. Showing that the session_fixture gets executed 3 times.

```
============================= test session starts ==============================
platform darwin -- Python 2.7.12, pytest-2.9.2, py-1.4.31, pluggy-0.3.1
rootdir: /Users/mehmetgerceker/workspace/pytest_session_fixture_test/test, inifile: 
collected 3 items 

test/module1/test_module1.py session setup
testing module1
.
test/module2/test_module2.py session setup
testing module2
.
test/module3/test_module3.py session setup
testing module3
.session teardown
session teardown
session teardown


=========================== 3 passed in 0.02 seconds ===========================
```