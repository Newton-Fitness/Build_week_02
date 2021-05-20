from kivy.app import App
from kivy.utils import platform
import socket
import pickle
import time
from kivy.clock import Clock


class MyApp(App):
    def on_start(self):
        #self.update_blinker_position()
        if platform == 'android':
            from android.permissions import Permission, request_permissions
            def callback(permission, results):
                if all([res for res in results]):
                    print("Got all permissions")
                    from plyer import gps
                    gps.configure(on_location=self.update_blinker_position)
                    gps.start(minTime=1000, minDistance=0)
                else:
                    print("Did not get all permissions")

            request_permissions([Permission.ACCESS_COARSE_LOCATION,
                                 Permission.ACCESS_FINE_LOCATION], callback)

    def update_blinker_position(self, *args, **kwargs):
        try:
            my_lat = kwargs['lat']
            my_lon = kwargs['lon']
        except Exception:
            my_lat = 9999
            my_lon = 9999
        print("GPS POSITION", my_lat, my_lon)

        HEADERSIZE = 10
        PORT = 5010

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((socket.gethostname(), PORT))

        while True:
            d = {'lat': my_lat, 'lon': my_lon, 'time': time.time()}
            msg = pickle.dumps(d)
            time.sleep(3)
            msg = bytes(f'{len(msg):<{HEADERSIZE}}', 'utf-8') + msg
            s.send(msg)


MyApp().run()