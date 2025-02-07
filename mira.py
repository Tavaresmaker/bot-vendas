import time
import pyautogui

def ajustar_sensibilidade():
    print("Ajustando sensibilidade do Free Fire...")
    # Simula um toque na tela para ativar a mira
    pyautogui.click(x=500, y=1200)  # Ajuste as coordenadas conforme o seu celular
    time.sleep(0.1)
    pyautogui.dragTo(500, 800, duration=0.2)  # Arrasto leve para cima

if __name__ == "__main__":
    print("Auxílio de mira ativado!")
    while True:
        ajustar_sensibilidade()
        time.sleep(0.5)  # Ajuste o tempo entre os toques
