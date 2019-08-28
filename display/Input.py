import json
import keyboard


class InputData:
    def __init__(self):
        self.keypress = ""

    def update(self, topic, payload):
        try:
            topic = topic.split("/")
            if topic[1] != "input":
                return

            input_data = json.loads(payload)
            self.keypress = input_data["input"]
            keyboard.press_and_release(self.keypress)

        except Exception as e:
            print("Something happened", e)
