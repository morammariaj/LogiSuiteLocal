# main.py
import os
import sys
import traceback
import logging
from pathlib import Path

from PyQt6.QtWidgets import QApplication, QMessageBox
from PyQt6.QtCore import Qt

APP_NAME = "LogiSuite"
APP_VERSION = "2.0.0"

def get_base_dir() -> Path:
    return Path(__file__).resolve().parent

def ensure_required_dirs(base_dir: Path) -> None:
    (base_dir / "databases").mkdir(exist_ok=True)
    (base_dir / "logs").mkdir(exist_ok=True)
    (base_dir / "app").mkdir(exist_ok=True)
    (base_dir / "app" / "dialogs").mkdir(exist_ok=True)
    (base_dir / "app" / "services").mkdir(exist_ok=True)
    (base_dir / "app" / "repositories").mkdir(exist_ok=True)

def configure_logging(base_dir: Path) -> None:
    log_file = base_dir / "logs" / "app.log"
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        handlers=[
            logging.FileHandler(log_file, encoding="utf-8"),
            logging.StreamHandler(sys.stdout),
        ],
    )
    logging.info("==============================================")
    logging.info("Iniciando %s v%s", APP_NAME, APP_VERSION)
    logging.info("Base dir: %s", base_dir)

def excepthook(exc_type, exc_value, exc_tb):
    error_text = "".join(traceback.format_exception(exc_type, exc_value, exc_tb))
    logging.critical("Error no controlado:\n%s", error_text)
    try:
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Icon.Critical)
        msg.setWindowTitle("Error inesperado")
        msg.setText("Ocurrió un error inesperado en la aplicación.")
        msg.setInformativeText(str(exc_value))
        msg.setDetailedText(error_text)
        msg.exec()
    except Exception:
        print(error_text, file=sys.stderr)

def validate_database_files(base_dir: Path) -> list[str]:
    db_dir = base_dir / "databases"
    expected = ["products.db", "quotes.db", "rules.db"]
    return [name for name in expected if not (db_dir / name).exists()]

def create_application() -> QApplication:
    app = QApplication(sys.argv)
    app.setApplicationName(APP_NAME)
    app.setApplicationVersion(APP_VERSION)
    app.setOrganizationName("Flamingo")
    app.setQuitOnLastWindowClosed(True)
    return app

def show_missing_modules_error(import_error: Exception):
    detail = (
        "Faltan módulos del sistema.\n\n"
        "Error detectado:\n"
        f"{import_error}\n\n"
        "Asegúrate de tener los archivos en 'app/dialogs'."
    )
    logging.error(detail)
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Icon.Warning)
    msg.setWindowTitle("Proyecto incompleto")
    msg.setText("El proyecto aún no está completo.")
    msg.setDetailedText(detail)
    msg.exec()

def main() -> int:
    base_dir = get_base_dir()
    ensure_required_dirs(base_dir)
    configure_logging(base_dir)
    sys.excepthook = excepthook
    app = create_application()

    missing_dbs = validate_database_files(base_dir)
    if missing_dbs:
        logging.warning("Faltan bases de datos: %s", ", ".join(missing_dbs))

    try:
        from app.main_window import CotizadorMainWindow
    except Exception as import_error:
        show_missing_modules_error(import_error)
        return 1

    try:
        window = CotizadorMainWindow(base_dir=base_dir)
        window.show()
        logging.info("Ventana principal iniciada correctamente.")
        return app.exec()
    except Exception:
        logging.exception("Fallo al iniciar la ventana principal.")
        raise

if __name__ == "__main__":
    sys.exit(main())
