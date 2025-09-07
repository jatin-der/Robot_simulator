import requests
import time
import math

BASE = "http://127.0.0.1:5000"

def move(turn, distance):
    r = requests.post(f"{BASE}/move_rel",
                      json={"turn": turn, "distance": distance})
    return r.json()

def capture():
    r = requests.get(f"{BASE}/capture")
    return r.json()

def distance(a, b):
    return math.hypot(a["x"] - b["x"], a["y"] - b["y"])

def main():
    goal = {"x": 50, "y": 50}
    print("🚀 Starting autonomous navigation...")

    for step in range(100):
        state = capture()
        robot = state["robot"]

        dx = goal["x"] - robot["x"]
        dy = goal["y"] - robot["y"]
        dist = math.hypot(dx, dy)

        if dist < 20:
            print("🎯 Goal reached!")
            break

        step_x = 2 if dx > 0 else -2
        step_y = 2 if dy > 0 else -2
        move(step_x, step_y)

        print(f"Step {step}: Robot at {robot}, moving toward {goal}")
        time.sleep(0.1)

if __name__ == "__main__":
    main()
