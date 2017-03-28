'''=== RESUM PROVES ICRA-TARIFES-OPTIC A EDAR MANRESA ==='''
import sys
sys.path.insert(0,"./bin") #add bin folder to path
#local imports
import processa as P
processa=P.processa #alias

'''
- Scripts provats: instantani.py, dia.py
- Sempre, error a: P.pregunta(C.creaTramaVar(0b01110011,C.creaASDU183())) #request user data & send password

- RuntimeError: Checksum incorrecte:
    <trama> 19 bytes: 68 0d 0d 68 73 31 08 b7 01 86 c1 08 08 01 01 00 04 34 16 - Checksum incorrecte: 052=/=193
    <trama> 19 bytes: 68 0d 0d 6a 73 01 00 b7 c1 86 11 0c 00 21 00 00 00 34 16 - Checksum incorrecte: 052=/=176
    <trama> 19 bytes: 68 0d 0d 6b 73 01 00 f7 81 46 01 00 00 01 01 08 00 b4 16 - Checksum incorrecte: 180=/=061
    <trama> 19 bytes: 68 0d 0d 68 73 01 00 b7 01 06 91 00 40 21 00 00 00 34 16 - Checksum incorrecte: 052=/=036

- RuntimeError: Tipus de trama desconegut
    <trama> 09 bytes: fd ff ef fc ff bd ff ff df 
    <trama> 08 bytes: ff ff ff ff f7 6d cf ff 
    <trama> 13 bytes: bc cd ff eb 6d 5f e0 df 5f ff a9 31 9f 
    <trama> 19 bytes: 6c 0d 0d 6b 73 21 03 b7 01 46 41 c3 30 21 81 30 0c b4 16 
    <trama> 15 bytes: ef ff 9d f3 ff f7 eb df d5 97 ff f7 f5 ff ff 
    <trama> 19 bytes: 6c 0d 0d 68 73 01 c3 ff 01 07 c0 82 c0 11 82 0c 80 34 16 
    <trama> 17 bytes: bf fe ce 0d 8c fb 6b 5a 73 7b fb 7b eb 3d d1 fb f7 
    <trama> 10 bytes: fe d7 ff ff bf ff fb db ff ff 

ESTRUCTURA TRAMES VARIABLES
1              1      1      1              1         2     var    1          1
+--------------+------+------+--------------+---------+-----+------+----------+--------------+
| Inici (0x68) | Long | Long | Inici (0x68) | Control | A A | ASDU | Checksum | Final (0x16) |
+--------------+------+------+--------------+---------+-----+------+----------+--------------+

68 0d 0d 68 73 01 00 b7 01 06 01 00 00 01 00 00 00 34 16 - Exemple de trama correcta
68 0d 0d 68 73 31 08 b7 01 86 c1 08 08 01 01 00 04 34 16 - Checksum incorrecte: 052=/=193
68 0d 0d 6a 73 01 00 b7 c1 86 11 0c 00 21 00 00 00 34 16 - Checksum incorrecte: 052=/=176
68 0d 0d 6b 73 01 00 f7 81 46 01 00 00 01 01 08 00 b4 16 - Checksum incorrecte: 180=/=061
68 0d 0d 68 73 01 00 b7 01 06 91 00 40 21 00 00 00 34 16 - Checksum incorrecte: 052=/=036

inici:    0x68
longitud: 0x0d = 13 bytes = 3 + 10 bytes (asdu)
control:  0x73 = 115 = 0b01110011 = [res,PRM (peticio),FCB,FCV,FUN=3 (peticio enviament dades usuari)] 
direccio: 1
asdu:
    idt: 0xb7 = 183 (tipus asdu INICIAR SESION Y ENVIAR CLAVE DE ACCESO)
    qev: 0x01 = 1 objecte d'informacio
    cdt: 0x06 = 6 = 0b00000110 T=0 (test), P/N=0 (irrellevant), cause=6 (110) ACTIVATION, 
    dco: 0x01 0x00 0x00 = 1 = direccion de defecto
    contrasenya = 0x1 0x0 0x0 0x0 =  1
checksum: 0x34
fi: 0x16

'''
#processa("\x68\x0d\x0d\x68\x73\x31\x08\xb7\x01\x86\xc1\x08\x08\x01\x01\x00\x04\x34\x16") #-RuntimeError: Checksum incorrecte: 052=/=193
#processa("\x68\x0d\x0d\x68\x73\x01\x00\xb7\x01\x86\xc1\x08\x08\x01\x01\x00\x04\x34\x16") #-RuntimeError: Checksum incorrecte: 052=/=193
processa("\x68\x0d\x0d\x68\x73\x01\x00\xb7\x01\x06\x01\x00\x00\x01\x00\x00\x00\x34\x16")
