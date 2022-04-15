import time

from prometheus_client import Gauge, Info, start_http_server


class AppMetrics:
    """
    Representation of Prometheus metrics and loop to fetch and transform
    application metrics into Prometheus metrics.
    """

    def __init__(self, profilling, port = 9000, polling_interval_seconds=5):
        self.profilling = profilling
        self.polling_interval_seconds = polling_interval_seconds
        self.port = port

        # Prometheus metrics to collect
        self.current_requests = Gauge("download", "Download Speed")
        self.pending_requests = Gauge("upload", "Upload Speed")
        self.ping = Gauge("ping", "Ping")
        self.isp = Info("isp", "ISP")

    def run_metrics_loop(self):
        """Metrics fetching loop"""

        while True:
            self.fetch()
            time.sleep(self.polling_interval_seconds)

    def fetch(self):
        """
        Get metrics from application and refresh Prometheus metrics with
        new values.
        """
        results = self.profilling.run()

        # Update Prometheus metrics with application metrics
        self.current_requests.set(results['download'])
        self.pending_requests.set(results['upload'])
        self.ping.set(results['ping'])
        self.isp.info({"ISP": results['isp']['isp']})
    
    def start(self):
        """
            start prometheus exporter
        """

        print("Starting exporter server on port {}".format(self.port))

        start_http_server(self.port)
        
        print("server running")
        self.run_metrics_loop()
