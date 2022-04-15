import time


def retry_if_failed(func):
    """retry function if failed"""
    retry_number = 3
    delay = 0

    def retry():
        """retry function if failed"""
        counter = 0

        while counter < retry_number:     
            try:
                return func()
            except Exception as excp:
                counter += 1
                print(excp)

                if counter >= retry_number:
                    raise excp

                time.sleep(delay)

    return retry
