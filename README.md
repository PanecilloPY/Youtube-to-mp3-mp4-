
# YouTube Downloader

Una aplicación simple para descargar videos de YouTube en formato MP4 o MP3. Desarrollada con Flask, yt-dlp y Tailwind CSS.

## Requisitos Previos

Antes de comenzar, asegúrate de tener instalado lo siguiente:

- **Python 3.8 o superior**
- **pip** (gestor de paquetes de Python)
- **Git** (opcional, para clonar el repositorio)

## Instalación

Sigue estos pasos para instalar y ejecutar la aplicación en tu máquina local.

### 1. Clonar el Repositorio

Primero, clona el repositorio en tu máquina local:

```bash
git clone https://github.com/tu-usuario/yt-downloader.git
cd yt-downloader
```

### 2. Crear un Entorno Virtual

Es recomendable crear un entorno virtual para aislar las dependencias del proyecto:

```bash
python -m venv .venv
```

#### Activar el Entorno Virtual

- **Windows**:
  ```bash
  .venv\Scripts\activate
  ```
  
- **macOS/Linux**:
  ```bash
  source .venv/bin/activate
  ```

### 3. Instalar Dependencias

Instala las dependencias necesarias usando `pip`:

```bash
pip install -r requirements.txt
```

### 4. Instalar FFmpeg

Si deseas descargar videos en formato MP4, necesitarás **FFmpeg** para combinar los streams de video y audio. Sigue las instrucciones para tu sistema operativo:

- **Windows**: Descarga FFmpeg desde [https://ffmpeg.org/download.html](https://ffmpeg.org/download.html) y agrega la carpeta `bin` al PATH.
- **macOS**: Usa Homebrew para instalar FFmpeg:
  ```bash
  brew install ffmpeg
  ```
- **Linux (Ubuntu/Debian)**:
  ```bash
  sudo apt update
  sudo apt install ffmpeg
  ```

### 5. Ejecutar la Aplicación

Una vez que todo esté configurado, ejecuta la aplicación:

```bash
python app.py
```

La aplicación estará disponible en `http://localhost:5000`.

## Uso

1. Abre tu navegador y ve a `http://localhost:5000`.
2. Ingresa la URL del video de YouTube que deseas descargar.
3. Selecciona el formato de descarga (MP4 o MP3).
4. Haz clic en "Descargar".
5. El video se descargará y se guardará en tu carpeta de descargas.

## Estructura del Proyecto

```
yt-downloader/
├── app.py                # Backend en Flask
├── requirements.txt      # Dependencias de Python
├── static/               # Archivos estáticos (CSS, JS)
│   └── styles.css        # Estilos personalizados
├── templates/            # Plantillas HTML
│   └── index.html        # Página principal
└── README.md             # Documentación
```

## Contribuciones

Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una nueva rama (`git checkout -b feature/nueva-funcionalidad`).
3. Realiza tus cambios y haz commit (`git commit -m 'Añadir nueva funcionalidad'`).
4. Haz push a la rama (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

## Licencia

Este proyecto está bajo la licencia MIT. Consulta el archivo [LICENSE](LICENSE) para más detalles.

---

¡Gracias por usar YouTube Downloader! 🚀
