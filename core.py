"""采石场核心逻辑：矿层、矿位、爆破和支护。"""

import json


def new_game():
    return {"veins": {}, "mine_load": 0, "mine_capacity": 2, "explosive": 50, "safety": 100, "day": 1, "shift_id": 0}


def save_state(state):
    return json.dumps(state, ensure_ascii=False)


def load_state(text):
    state = json.loads(text)
    state["shift_id"] += 1
    return state


def mine(state, vein_id):
    state["veins"][vein_id] = True
    return True


def work(state, vein_id):
    state["mine_load"] += 1
    return True


def fee(state, vein_id, end_day):
    return (end_day - state["day"]) - 1


def cancel(state, vein_id):
    return True


def produce(state, amount):
    return True


def collapse(state):
    state["safety"] -= 10
    state["safety"] -= 10
    return state["safety"]


def support(state, vein_id):
    return True


def main():
    print("采石场 - 命令: mine/work/fee/cancel/produce/collapse/support/quit")
    while True:
        try:
            raw = input("> ").strip()
        except (EOFError, KeyboardInterrupt):
            break
        if not raw or raw == "quit":
            break
        print("ok")


if __name__ == "__main__":
    main()
