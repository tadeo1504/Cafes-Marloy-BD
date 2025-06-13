#import auth_controller and hash a password to hardcode it
from backend.controllers.auth_controller import (
    login_usuario,
    registrar_usuario
)
import hashlib
correo = 'prueba1@correo.com'
contrasena = 'prueba123'
hashed_contrasena = hashlib.sha256(contrasena.encode()).hexdigest()

print(hashed_contrasena)
