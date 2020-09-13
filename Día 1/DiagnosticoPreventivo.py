from Ayudas import ObtenerNumeroPacientes, PacienteTiene

def Diagnostico(tos, fiebre, dolor_cabeza, dolor_garganta,
                ojos_rojos, malestar_general, dificultad_respirar):
    if (tos or fiebre or dolor_cabeza) and (dolor_garganta or ojos_rojos or malestar_general):
        if dificultad_respirar:
            return 2
        return 1
    return 0


no_pacientes = ObtenerNumeroPacientes()

for patient in range(no_pacientes):
    print(f"Paciente {patient+1}")
    p_nombre = input("Nombre: ")
    print(f"{p_nombre}, responde con un 1 si presentas el síntoma, de lo contrario responde con un 0.\nPresentas")
    p_tos = PacienteTiene("Tos")
    p_fiebre = PacienteTiene("Fiebre")
    p_dolor_cabeza = PacienteTiene("Dolor de cabeza")
    p_dolor_garganta = PacienteTiene("Dolor o ardor de garganta")
    p_ojos_rojos = PacienteTiene("Ojos rojos")
    p_malestar_general = PacienteTiene("Malestar general")
    p_dificultad_respirar = PacienteTiene("Dificultad para respirar")
    p_diagnostico = Diagnostico(p_tos, p_fiebre, p_dolor_cabeza, p_dolor_garganta, p_ojos_rojos,
                                p_malestar_general, p_dificultad_respirar)
    if p_diagnostico == 0:
        print(f"{p_nombre}, es probable que no tengas COVID-19, tus síntomas podrían corresponder a otro padecimiento. Sin embargo, sigue al pendiente de tu estado de salud, y si presentas compliaciones ponte en contacto con el sector salud.")
    elif p_diagnostico == 1:
        print(f"{p_nombre}, es posible que tengas COVID-19. Por favor ponte en contacto con el sector salud para notificar sobre tu caso.")
    else:
        print(f"{p_nombre}, padeces de COVID-19 en un estado grave. Es necesario que te dirigas a una institución de salud de forma inmediata.")
