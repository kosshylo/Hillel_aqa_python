import  pytest
from lesson_11.homework_11.LogEventFunc import log_event, read_last_log_line,parsed_logLevel_from_logging_line,parsed_status_from_logging_line,parsed_username_from_logging_line

class TestLoginFunc:


    def test1_log_level_is_info_for_success_status(self):
        log_event("Kostia", "success")
        last_line = read_last_log_line()
        level = parsed_logLevel_from_logging_line(last_line)
        assert level == "INFO", f"Expected INFO log level, but got: {level}"


    def test2_log_level_is_warning_for_expired_status(self):
        log_event("Oleksiy", "expired")
        last_line = read_last_log_line()
        level = parsed_logLevel_from_logging_line(last_line)
        assert level == "WARNING", f"Expected WARNING log level, but got: {level}"

    def test3_log_level_is_error_for_failed_status(self):
        log_event("Sasha", "failed")
        last_line = read_last_log_line()
        level = parsed_logLevel_from_logging_line(last_line)
        assert level == "ERROR", f"Expected ERROR log level, but got: {level}"

    def test4_got_proper_status(self):
        log_event("Oleksiy", "expired")
        last_line = read_last_log_line()
        parsed_status = parsed_status_from_logging_line(last_line)
        assert parsed_status == "expired", f'Got status: "{parsed_status}". Expected: "expired" status'


    def test5_got_proper_name(self):
        log_event("Sasha", "failed")
        parsed_username: str = parsed_username_from_logging_line(read_last_log_line())
        assert parsed_username == "Sasha", f'Got username: "{parsed_username}". Expected: "Sasha"'
    def setup_class(self):
        print("precondition setup")





