from pynput import mouse
import threading
import time

class MouseTracker:
    def __init__(self):
        self.position = (0, 0)
        self.lock = threading.Lock()
        self.interval = 0.1  # Intervalo em segundos

    def on_move(self, x, y):
        with self.lock:
            self.position = (x, y)

    def on_click(self, x, y, button, pressed):
        if pressed:
            print(f"Mouse clicked at ({x}, {y}) with {button}")

    def on_scroll(self, x, y, dx, dy):
        print(f"Mouse scrolled at ({x}, {y}) with delta ({dx}, {dy})")

    def process(self):
        last_position = (0, 0)
        while True:
            with self.lock:
                if self.position != last_position:
                    last_position = self.position
                    print(f"Mouse moved to ({self.position[0]}, {self.position[1]})")
            time.sleep(self.interval)

# Cria uma instância do rastreador do mouse
tracker = MouseTracker()

# Inicia o rastreamento em uma thread separada
tracker_thread = threading.Thread(target=tracker.process)
tracker_thread.daemon = True
tracker_thread.start()

# Começa a escutar os eventos do mouse
with mouse.Listener(on_move=tracker.on_move, on_click=tracker.on_click, on_scroll=tracker.on_scroll) as listener:
    listener.join()


