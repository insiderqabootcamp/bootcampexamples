import pytest

from base.database_controller import DataBaseController


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    if result.when == 'call' or (result.when == 'setup' and result.failed):
        case_name = result.nodeid
        path = result.fspath
        if result.failed:
            stack_trace = result. + "\n" + result.
        else:
            stack_trace = result.capstdout
        status = result.outcome
        duration = result.duration
