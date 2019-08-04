Python
import sys

from globalLog import ta_log

if __name__ == '__main__':
    ta_log.info("start")
    try:
        print(1 / 0)
    except Exception:
        ta_log.error("error:")
        ta_log.exception(sys.exc_info())
    ta_log.debug("end")
