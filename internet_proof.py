import speedtest

from retry import retry_if_failed

st = speedtest.Speedtest()

class InternetProfilling:
    """Internet profilling class"""

    def run(self):
        """execute a internet speed profilling"""
        speed_test = test_internet()
        internet_info = get_internet_info()

        return {**speed_test, **internet_info}

@retry_if_failed
def test_ping():
    """test ping"""
    st.get_best_server()

    return st.results.ping

@retry_if_failed
def test_download():
    """test download speed"""
    return st.download() / 1000

@retry_if_failed
def test_upload():
    """test upload speed"""
    return st.upload() / 1000

@retry_if_failed
def get_near_server():
    """get near server"""
    return st.get_closest_servers()

def test_internet():
    """test download & upload speed, ping """
    try:
        ping = test_ping()
        download_speed = test_download()
        upload_speed = test_upload()
    except:
        print("some metrics could not be loaded")
    finally:
        return {
            "ping": ping,
            "download": download_speed,
            "upload": upload_speed
        }

def get_internet_info():
    """get internet info, near server and ISP"""
    nearst_servers = get_near_server()
    isp = st.config["client"]

    return {
        "nearsted_servers": nearst_servers,
        "isp": isp
    }
