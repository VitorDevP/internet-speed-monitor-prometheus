from exporter import AppMetrics
from internet_proof import InternetProfilling

if __name__ == "__main__":
    print("Starting internet speed monitor exporter")

    profilling = InternetProfilling()
    
    exporter = AppMetrics(profilling)

    exporter.start()
