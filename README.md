# Void Protocol v1.0

Un frenético juego arcade de defensa y estrategia con estética neon cyberpunk. Protege tu núcleo de infinitas oleadas de enemigos gestionando hábilmente tus recursos y posicionando defensas automatizadas.

## Características Principales
- **Estética Neon/Cyberpunk**: Efectos visuales de alto contraste, brillos dinámicos y "juice" intensivo mediante sacudidas, partículas y explosiones.
- **Acción Táctica**: Coloca Orbes (15 Rc) y Gravitones (60 Rc) para ralentizar y diezmar a enjambres enemigos de distintas clases (Básicos, Elites, Rápidos, Drones Curanderos).
- **Sobrevive a las Oleadas**: La dificultad escala por minutos y enemigos derrotados. Cuidado con los Drones Némesis (Jefes) cada 200 bajas.
- **Micro-Decisiones de Ritmo**: Los Orbes tienen vida limitada (10 segundos). Usa sabiamente la energía y recupera ventaja táctica con Habilidades Activas:
  - **[1] Sobrecarga**. Aumenta la velocidad de ataque y reduce cooldowns pasivos (amarillo).
  - **[2] Reparación**. Restaura una vida del Núcleo en situaciones críticas (rojo).

## Controles
- **Ratón (Movimiento/Apuntar)**
- **CLIC IZQUIERDO**: Construye un Orbe de Energía (15 Rc)
- **CTRL + CLIC IZQUIERDO**: Construye un Gravitón ralentizador (60 Rc)
- **Tecla [1]**: Activa la habilidad Sobrecarga cuando parpadea en Amarillo brillante.
- **Tecla [2]**: Activa la habilidad de Reparación del núcleo cuando parpadea en Rojo intenso.
- **Tecla [E]**: Alterna la Interfaz de Habilidades para mayor inmersión y concentración.
- **Tecla [ESPACIO] / [ESC]**: Abre el menú principal / Pausa técnica (Ajustes de Sonido, UI, Vibración).

## Juega Directamente
La mejor opción siempre será probarlo jugando:
🔗 **[Play Void Protocol]()**

## Despliegue (Deploy) - GitHub Pages
Este proyecto está hecho en Javascript puro sobre un Canvas HTML5 y empaquetado en un único archivo `index.html` sin dependencias externas de librerías, listo para despliegues instantáneos o para empaquetarlo con Electron / Capacitor.

Para publicar:
1. Crea un repositorio nuevo en GitHub (público o privado si pagas la subscripción de Git Pages).
2. Sube los archivos base (`index.html` como raíz) vía git o interfaz web.
3. Ve a `Settings > Pages` en el repositorio, selecciona la rama `main` y marca guardar.
4. En pocos minutos tu juego estará visible para todo el mundo.
