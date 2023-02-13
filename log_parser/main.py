import tailer
import logging
import json
import re

logging.basicConfig(level=logging.INFO)
log = logging.getLogger(__name__)

def parse_log_to_json(log_line: str):
    log_pattern = re.compile(r"^(\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}.\d{3}(?:Z|[+-]\d{2}:\d{2}))\s*(\w+)\s*(\d*)\s*---\s*\[\s*([a-zA-Z0-9\._-]+)?\]\s*([^\s]+)\s*:\s*([^\n]+)$")
    match = log_pattern.match(log_line)
    if match:
        timestamp = match.group(1)
        log_level = match.group(2)
        process_id = match.group(3)
        thread_name = match.group(4)
        logger_name = match.group(5)
        message = match.group(6)
        log_json = {"timestamp": timestamp, "logLevel": log_level, "processId": process_id, "thread": thread_name, "loggerName": logger_name, "message": message}
        log.info(f'Successfully converted log to json: {log_json}')
        return log_json
    else:
        log.error('Failed to parse log')
        return None

if __name__ == '__main__':
    logfile_in = 'logs/app.log'
    jsonfile_out = 'logs/app.json'
    with open(logfile_in, 'r') as logfile:
        for line in tailer.follow(logfile):
            with open(jsonfile_out, 'a') as jsonfile:
                json_line = parse_log_to_json(line)
                if json_line is not None:
                    jsonfile.write(json.dumps(parse_log_to_json(line))+'\n')
