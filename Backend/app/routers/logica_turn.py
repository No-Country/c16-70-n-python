from ..models.models import Generador_turn, db
from datetime import datetime, timedelta


def crear_config_turno(dia, hora_inicio, hora_fin, duracion_turno):
    try:
        if dia == 'Lunes':
            dia_n = 1
        elif dia == 'Martes':
            dia_n = 2
        elif dia == 'Miercoles':
            dia_n = 3
        elif dia == 'Jueves':
            dia_n = 4
        elif dia == 'Viernes':
            dia_n = 5
        elif dia == 'Sabado':
            dia_n = 6
        elif dia == 'Domingo':
            dia_n = 7

        nuevo_generador = Generador_turn(
            gnt_int_dia=dia_n,
            gnt_time_horainicio=hora_inicio,
            gnt_str_horafin=hora_fin,
            gnt_str_duracionturn=duracion_turno
        )
        db.session.add(nuevo_generador)
        db.session.commit()
        return True, "Generador de turnos creado exitosamente"
    except Exception as e:
        return False, f"Error al crear el generador de turnos: {str(e)}"
    
def habilitar_turnos(fecha):
    fecha_objeto = datetime.strptime(fecha, '%Y-%m-%d')
    # Obtiene el nombre del día de la semana
    numerodia = fecha_objeto.weekday() + 1

    configuracion_dias = Generador_turn.query.filter_by(gdt_int_dia=numerodia).first()
    
    inicio = configuracion_dias.gnt_time_horainicio
    fin = configuracion_dias.gnt_str_horafin
    duracion = configuracion_dias.gnt_str_duracionturn

    hora_inicio_turnos = inicio
    
    lista_turnos = []
    #a modo de prueba lo hago en una lista
    while hora_inicio_turnos < fin:
        hora_fin_turno = hora_inicio_turnos + timedelta(minutes=duracion)
        lista_turnos.append((hora_inicio_turno.strftime('%H:%M'), hora_fin_turno.strftime('%H:%M')))
        hora_inicio_turno = hora_fin_turno

    for turno in lista_turnos:
        print(f"Turno: {turno[0]} - {turno[1]}")


    


