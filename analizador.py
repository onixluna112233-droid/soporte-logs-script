# Script de automatización para monitoreo de registros de soporte
# Autora: Karla Nolasco

import datetime

def analizar_logs():
    # Simulamos registros que vienen de un servidor de aplicaciones
    registros = [
        "2026-10-13 08:00:01 INFO Sistema iniciado correctamente",
        "2026-10-13 08:05:22 WARNING Uso de memoria RAM al 82%",
        "2026-10-13 08:12:10 ERROR Timeout en conexion con API de pagos",
        "2026-10-13 08:15:00 INFO Transaccion procesada exitosamente",
        "2026-10-13 08:20:45 ERROR Respuesta HTTP 500 en servidor web"
    ]

    print("=== REPORTE DE ANOMALIAS DE SOPORTE ===")
    print(f"Fecha de analisis: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")

    alertas = 0
    for linea in registros:
        if "ERROR" in linea or "WARNING" in linea:
            alertas += 1
            print(f"[ALERTA DETECTADA] -> {linea}")

    print(f"\nTotal de eventos criticos encontrados: {alertas}")

if __name__ == "__main__":
    analizar_logs()