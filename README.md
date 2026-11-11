# Ejercicios de práctica – Máster EDEM

Repositorio personal con los **ejercicios, prácticas y apuntes de teoría** de las clases del máster en **EDEM**. Cada carpeta de primer nivel corresponde a una asignatura y recoge lo trabajado en clase: código, ficheros de configuración y notas.

## Contenido

| Carpeta | Asignatura | Qué incluye |
|---------|------------|-------------|
| [DOCKER](DOCKER/) | Docker | Dockerfiles, imágenes, contenedores y Docker Compose |
| [SQL](SQL/) | SQL | Consultas y manipulación de tablas (PostgreSQL) |
| [GIT_ACTIONS](GIT_ACTIONS/) | GitHub Actions | Workflows de CI/CD |
| [API_MANAGEMENT](API_MANAGEMENT/) | API Management | Ejercicios guiados de APIs REST con FastAPI |
| [VIBECODING](VIBECODING/) | Vibe Coding | Proyectos creados con ayuda de IA |

## Detalle por asignatura

### 🐳 Docker
- **DOCKER1** – Primer Dockerfile (`main.py` + comandos básicos) y primeros ejercicios.
- **DOCKER2** – Seis prácticas de Dockerfile (tests con `pytest`, servidor web con `index.html`, contenedor que falla a propósito, etc.) y un fichero de [teoría](DOCKER/DOCKER2/Teoria.txt).
- **DOCKER3** – Docker Compose: servicios definidos en `compose.yaml`, con una práctica que incluye tests.

### 🗄️ SQL
- **SQL1** – `ALTER TABLE`, `SELECT` e `INSERT` sobre una tabla de libros.
- **SQL2** – Creación de tablas con claves primarias y relaciones (`users`, `posts`) e inserción de datos.

### ⚙️ GitHub Actions
Workflows en [`.github/workflows`](GIT_ACTIONS/.github/workflows/), desde un "hello world" con `workflow_dispatch` hasta un entregable que ejecuta un script en Python sobre un fichero `ventas.json`.

### 🔌 API Management
Serie de 18 ejercicios progresivos en [`exercises`](API_MANAGEMENT/docs/superpowers/exercises/): Postman, fundamentos de APIs, FastAPI, CRUD, paginación, MySQL, OpenAPI, autenticación (Basic, API key, JWT, OAuth), roles y permisos, rate limiting, versionado, webhooks con ngrok, MCP y un reto final con Mastodon. Cada ejercicio tiene su propio readme. Más información en el [README del curso](API_MANAGEMENT/docs/superpowers/README.md).

### 🤖 Vibe Coding
- **calculadora-hipoteca** – Calculadora de hipoteca en una sola página HTML.
- **practica1** – En preparación.

## Estructura

```
Ejercicios_de_practica_EDEM/
├── DOCKER/
│   ├── DOCKER1/
│   ├── DOCKER2/        # PRACTICA1 … PRACTICA6 + Teoria.txt
│   └── DOCKER3/        # PRACTICA1 … PRACTICA3 (Compose)
├── SQL/
│   ├── SQL1/
│   └── SQL2/
├── GIT_ACTIONS/
│   └── .github/workflows/
├── API_MANAGEMENT/
│   └── docs/superpowers/exercises/   # 01 … 18
├── VIBECODING/
└── README.md
```

## Cómo usarlo

```bash
git clone https://github.com/jorgeoliverz/Ejercicios_de_practica_EDEM.git
cd Ejercicios_de_practica_EDEM
```

Entra en la carpeta de la asignatura y práctica que quieras. Cada una se ejecuta de forma independiente:

- **Docker:** `docker build -t <nombre> .` y `docker run <nombre>` (o `docker compose up` en las prácticas con `compose.yaml`).
- **SQL:** ejecuta los `.sql` en un cliente de PostgreSQL.
- **API Management:** crea un entorno virtual dentro del ejercicio, instala `requirements.txt` y lanza la app (ver su readme).

## Objetivo

- Llevar un registro ordenado del trabajo de cada asignatura.
- Tener material de consulta y repaso.
- Practicar el control de versiones con Git y GitHub.

## Autor

**Jorge Oliver** – Alumno del máster en EDEM
