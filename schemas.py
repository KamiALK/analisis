from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

# class UserData(BaseModel):
    
#     username: str
#     nombre: str
#     apellido: str
#     celular: int
#     edad: int
#     cedula: int
#     genero:str
#     email: str
#     passwd: str
    
# class UserID(UserData):
#     ID: int |None=None


# class JugadoresBase(UserID):
#     pass



class EvaluacionesBase(BaseModel):
    
    arbitro_id: int
    evaluador_id: int
    partido_id: int
    estado_fisico: int
    observacionesEF: Optional[str] = None
    desplazamiento: int
    observacionesD: Optional[str] = None
    lectura_de_juego: int
    observacionesL: Optional[str] = None
    control_de_juego: int
    observacionesCDJ: Optional[str] = None
    nivelDificultadTorneo: int
    DificultadEtapaTorneo: int
    temperaturaEquipos: int
    situacionesRealesA: int
    faltasNaturalezaA: int
    faltasTacticasA: int
    situacionesRealesI: int
    faltasNaturalezaI: int
    faltasTacticasI: int

class Evaluaciones(EvaluacionesBase):
    ID: int








# class EquipoSchema(BaseModel):
#     ID: Optional[int]
#     nombre: str
#     lider_id: Optional[List[int]] = None
#     jugadores_id: Optional[List[int]] = None

# class partido_arbitro_scheme(BaseModel):
#     partido_id: int 
#     arbitro_1_id: Optional[int] = None
#     arbitro_2_id: Optional[int] = None
#     arbitro_3_id: Optional[int] = None
#     arbitro_4_id: Optional[int] = None
    
#     class Config:
#         from_attributes = True    

# class arbitro_asignacion_scheme(BaseModel):
#     partido_id: int 
#     arbitro_1_id: Optional[int] = None
#     arbitro_2_id: Optional[int] = None
#     arbitro_3_id: Optional[int] = None
#     arbitro_4_id: Optional[int] = None
#     evaluacion_id: Optional[int] = None 

#     class Config:
#         from_attributes = True

    



# class CampeonatoSchema(BaseModel):
#     ID: int
#     nombre: str
#     equipos: List[EquipoSchema] = []
#     partidos: List[PartidoBase] = []

#     class Config:
#         from_attributes = True
