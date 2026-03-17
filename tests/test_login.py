import time
import os
from dotenv import load_dotenv
load_dotenv()

BASE_URL = os.getenv("BASE_URL")

if not BASE_URL:
    raise Exception("A variável de ambiente BASE_URL não está definida.")

# ==============================
# HELPERS
# ==============================

def wait_flutter(page):
    page.wait_for_load_state("domcontentloaded")
    page.wait_for_timeout(5000)  # tempo seguro pro Flutter renderizar


def ensure_dirs():
    os.makedirs("artifacts/screenshots", exist_ok=True)
    os.makedirs("artifacts/logs", exist_ok=True)
    os.makedirs("artifacts/traces", exist_ok=True)


def log(message):
    with open("artifacts/logs/test_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{time.ctime()} - {message}\n")


def click_relative_to_center(page, offset_x, offset_y):
    viewport = page.viewport_size

    if viewport is None:
        raise Exception("Viewport não disponível")

    x = viewport["width"] / 2 + offset_x
    y = viewport["height"] / 2 + offset_y

    # DEBUG VISUAL (pode comentar depois)
    page.mouse.move(x, y)
    page.wait_for_timeout(300)

    page.mouse.click(x, y)
    page.wait_for_timeout(300)


def type_text(page, text):
    page.keyboard.press("Control+A")
    page.keyboard.press("Backspace")
    page.keyboard.type(text, delay=50)


# ==============================
# TESTE PRINCIPAL
# ==============================

def test_login_completo(page, context):
    ensure_dirs()

    context.tracing.start(screenshots=True, snapshots=True, sources=True)

    log("Iniciando teste de login")

    page.goto(BASE_URL)
    wait_flutter(page)

    log("Página carregada")

    # ==========================
    # AJUSTE DE OFFSETS (baseado no layout atual)
    # ==========================
    OFFSET_WHATSAPP = 60
    OFFSET_SENHA = 140
    OFFSET_ENTRAR = 220

    # ==========================
    # WHATSAPP
    # ==========================
    click_relative_to_center(page, 0, OFFSET_WHATSAPP)
    type_text(page, "47988888888")
    log("WhatsApp preenchido")

    # ==========================
    # SENHA
    # ==========================
    click_relative_to_center(page, 0, OFFSET_SENHA)
    type_text(page, "123456")
    log("Senha preenchida")

    # ==========================
    # BOTÃO ENTRAR
    # ==========================
    click_relative_to_center(page, 0, OFFSET_ENTRAR)
    log("Botão Entrar clicado")

    page.wait_for_timeout(5000)

    # ==========================
    # VALIDAÇÃO
    # ==========================
    if "login" in page.url.lower():
        log("Falha no login")
        raise Exception("Login não realizado")

    log("Login realizado com sucesso")

    # ==========================
    # SCREENSHOT
    # ==========================
    timestamp = int(time.time())
    screenshot_path = f"artifacts/screenshots/login_{timestamp}.png"
    page.screenshot(path=screenshot_path)

    log(f"Screenshot salvo em {screenshot_path}")

    # ==========================
    # TRACE
    # ==========================
    trace_path = f"artifacts/traces/trace_{timestamp}.zip"
    context.tracing.stop(path=trace_path)

    log(f"Trace salvo em {trace_path}")

    # ==========================
    # VIDEO
    # ==========================
    if page.video:
        try:
            video_path = page.video.path()
            log(f"Vídeo salvo em {video_path}")
        except:
            log("Vídeo não disponível")

    log("Teste finalizado com sucesso\n")