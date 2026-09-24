# LogiSuiteLocal — snapshot de referencia

Este repositorio es el respaldo de referencia del LogiSuite de escritorio y la base visual/funcional para la versión web.

Snapshot utilizado:
- Archivo original: `LogiSuite_María José 12_41am(1).zip`
- SHA-256 del ZIP: `d5527a92e71c4eb5dd636f0bf9e7e587a4cdf9db4bc59ac047639cb462c1ebba`
- Versión de la aplicación: 2.0.0
- Ventana principal: `app/main_window.py`
- Punto de entrada: `main.py`

Orden visual de referencia:
1. General Information
2. Customer Information
5. Carrier Costs & Pricing
   - WWE + Services Management
   - CBCFS + Services Management
   - FedEx + UPS
   - Uber Freight + Local Delivery
   - Plataforma Ganadora
3. Product Information
4. Cubic volume calculator
5. Productos en esta Cotización
6. Barra inferior de acciones

La web debe conservar este orden y comportamiento y adaptarlo a responsive sin convertirlo en un sistema con menú lateral distinto.

Archivos de datos del snapshot:
- databases/products.db
- databases/quotes.db
- databases/rules.db

Los binarios grandes del snapshot original no se sustituyen por versiones parciales. El ZIP adjunto es el snapshot íntegro de referencia.

Este repositorio también sirve para documentar la equivalencia entre el escritorio y LogiSuite Web.
