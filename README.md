# Secure System Hardening Script

## Descripción

Este repositorio contiene un script en Python diseñado para automatizar la configuración de seguridad en sistemas Linux. El objetivo es aplicar medidas de **endurecimiento** (hardening) que minimizan riesgos y refuerzan la protección del sistema frente a amenazas comunes.

## Características Principales

- **Política de Contraseñas Seguras**
  - Establece la expiración de contraseñas a 90 días.
  - Configura el algoritmo de hashing **SHA-512** para el almacenamiento seguro de contraseñas.
  - Requiere contraseñas de al menos 8 caracteres y limita las repeticiones consecutivas.

- **Monitoreo y Auditoría**
  - Habilita el registro de contraseñas en los logs de auditoría.
  - Configura un banner de advertencia en el mensaje de inicio de sesión (MOTD).

- **Permisos y Accesos**
  - Establece permisos por defecto a `700` para archivos del usuario y `755` para otros.
  - Bloquea el acceso SSH directo para el usuario root.
  - Habilita el modo estricto y configura el nivel de registro (LogLevel) de SSH a `INFO`.

- **Protección de Red**
  - Activa y configura el firewall para bloquear todo el tráfico entrante y permitir el tráfico saliente.
  - Aplica reglas para rechazar conexiones desde rangos de IPs privadas y multicast.

- **Protección del Sistema**
  - Deshabilita SElinux para evitar conflictos de configuración.
  - Instala y configura ClamAV para la detección y eliminación de malware.
  - Activa protecciones contra ataques TCP SYN, suplantación de IP y solicitudes ICMP maliciosas.

## Instalación y Uso

1. Clona el repositorio:
   ```bash
   git clone https://github.com/tu_usuario/secure-hardening-script.git
