# Para esse código funcionar instale as bibliotecas com o comando:
# -> pip install scikit-fuzzy <-
# -> pip install numpy <-
# -> pip install scipy <-

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl
from re import X


def fuzzy_potassio(input_value_potassio, input_value_ctc):
    x_potassio = np.arange(0, 271, 0.01)
    x_ctc = np.arange(0, 31, 0.01)

    potassio_ctc_1 = ctrl.Antecedent(x_potassio, 'Potassio1')
    potassio_ctc_2 = ctrl.Antecedent(x_potassio, 'Potassio2')
    potassio_ctc_3 = ctrl.Antecedent(x_potassio, 'Potassio3')
    potassio_ctc_4 = ctrl.Antecedent(x_potassio, 'Potassio4')
    ctc = ctrl.Antecedent(x_ctc, 'CTC')

    classe_potassio = ctrl.Consequent(np.arange(1, 6, 1), 'Classe Potassio')
    # ativa as funções baseando-se no valor da classe da argila
    potassio_ctc_1['muito baixo'] = fuzz.zmf(x_potassio, 14.4, 20)
    potassio_ctc_1['baixo'] = fuzz.trapmf(x_potassio, [16.8, 23.1, 36, 48])
    potassio_ctc_1['medio'] = fuzz.trapmf(x_potassio, [32.8, 45.1, 54, 72])
    potassio_ctc_1['alto'] = fuzz.trapmf(x_potassio, [48.8, 67.1, 108, 144])
    potassio_ctc_1['muito alto'] = fuzz.smf(x_potassio, 96, 132)

    potassio_ctc_2['muito baixo'] = fuzz.zmf(x_potassio, 21.6, 30)
    potassio_ctc_2['baixo'] = fuzz.trapmf(x_potassio, [24.8, 34.1, 54, 72])
    potassio_ctc_2['medio'] = fuzz.trapmf(x_potassio, [48.8, 67.1, 81, 108])
    potassio_ctc_2['alto'] = fuzz.trapmf(x_potassio, [72.8, 100.1, 162, 216])
    potassio_ctc_2['muito alto'] = fuzz.smf(x_potassio, 144, 198)

    potassio_ctc_3['muito baixo'] = fuzz.zmf(x_potassio, 28.8, 40)
    potassio_ctc_3['baixo'] = fuzz.trapmf(x_potassio, [32.8, 45.1, 72, 96])
    potassio_ctc_3['medio'] = fuzz.trapmf(x_potassio, [64.8, 89.1, 108, 144])
    potassio_ctc_3['alto'] = fuzz.trapmf(x_potassio, [96.8, 133.1, 216, 288])
    potassio_ctc_3['muito alto'] = fuzz.smf(x_potassio, 192, 264)

    potassio_ctc_4['muito baixo'] = fuzz.zmf(x_potassio, 32.4, 45)
    potassio_ctc_4['baixo'] = fuzz.trapmf(x_potassio, [36.8, 50.6, 81, 108])
    potassio_ctc_4['medio'] = fuzz.trapmf(
        x_potassio, [72.8, 100.1, 121.5, 162])
    potassio_ctc_4['alto'] = fuzz.trapmf(x_potassio, [108.8, 149.6, 243, 324])
    potassio_ctc_4['muito alto'] = fuzz.smf(x_potassio, 216, 297)

    ctc['1'] = fuzz.zmf(x_ctc, 6.75, 9)
    ctc['2'] = fuzz.trapmf(x_ctc, [6.08, 8.36, 13.5, 18])
    ctc['3'] = fuzz.trapmf(x_ctc, [12.08, 16.61, 27, 36])
    ctc['4'] = fuzz.smf(x_ctc, 24, 33)

    classe_potassio['muito baixo'] = fuzz.trimf(
        classe_potassio.universe, [1, 1, 1])
    classe_potassio['baixo'] = fuzz.trimf(classe_potassio.universe, [2, 2, 2])
    classe_potassio['medio'] = fuzz.trimf(classe_potassio.universe, [3, 3, 3])
    classe_potassio['alto'] = fuzz.trimf(classe_potassio.universe, [4, 4, 4])
    classe_potassio['muito alto'] = fuzz.trimf(
        classe_potassio.universe, [5, 5, 5])

    rule1 = ctrl.Rule(ctc['1'] & potassio_ctc_1['muito baixo'],
                      classe_potassio['muito baixo'])
    rule2 = ctrl.Rule(ctc['1'] & potassio_ctc_1['baixo'],
                      classe_potassio['baixo'])
    rule3 = ctrl.Rule(ctc['1'] & potassio_ctc_1['medio'],
                      classe_potassio['medio'])
    rule4 = ctrl.Rule(ctc['1'] & potassio_ctc_1['alto'],
                      classe_potassio['alto'])
    rule5 = ctrl.Rule(ctc['1'] & potassio_ctc_1['muito alto'],
                      classe_potassio['muito alto'])

    rule6 = ctrl.Rule(ctc['2'] & potassio_ctc_2['muito baixo'],
                      classe_potassio['muito baixo'])
    rule7 = ctrl.Rule(ctc['2'] & potassio_ctc_2['baixo'],
                      classe_potassio['baixo'])
    rule8 = ctrl.Rule(ctc['2'] & potassio_ctc_2['medio'],
                      classe_potassio['medio'])
    rule9 = ctrl.Rule(ctc['2'] & potassio_ctc_2['alto'],
                      classe_potassio['alto'])
    rule10 = ctrl.Rule(
        ctc['2'] & potassio_ctc_2['muito alto'], classe_potassio['muito alto'])

    rule11 = ctrl.Rule(
        ctc['3'] & potassio_ctc_3['muito baixo'], classe_potassio['muito baixo'])
    rule12 = ctrl.Rule(ctc['3'] & potassio_ctc_3['baixo'],
                       classe_potassio['baixo'])
    rule13 = ctrl.Rule(ctc['3'] & potassio_ctc_3['medio'],
                       classe_potassio['medio'])
    rule14 = ctrl.Rule(ctc['3'] & potassio_ctc_3['alto'],
                       classe_potassio['alto'])
    rule15 = ctrl.Rule(
        ctc['3'] & potassio_ctc_3['muito alto'], classe_potassio['muito alto'])

    rule16 = ctrl.Rule(
        ctc['4'] & potassio_ctc_4['muito baixo'], classe_potassio['muito baixo'])
    rule17 = ctrl.Rule(ctc['4'] & potassio_ctc_4['baixo'],
                       classe_potassio['baixo'])
    rule18 = ctrl.Rule(ctc['4'] & potassio_ctc_4['medio'],
                       classe_potassio['medio'])
    rule19 = ctrl.Rule(ctc['4'] & potassio_ctc_4['alto'],
                       classe_potassio['alto'])
    rule20 = ctrl.Rule(
        ctc['4'] & potassio_ctc_4['muito alto'], classe_potassio['muito alto'])

    SE_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
                                 rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20])
    SE = ctrl.ControlSystemSimulation(SE_ctrl)

    SE.input['Potassio1'] = input_value_potassio
    SE.input['Potassio2'] = input_value_potassio
    SE.input['Potassio3'] = input_value_potassio
    SE.input['Potassio4'] = input_value_potassio

    SE.input['CTC'] = input_value_ctc
    SE.compute()
    output_value = SE.output['Classe Potassio']

    pertinencia_mb = [fuzz.interp_membership(x_potassio, potassio_ctc_1['muito baixo'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['1'].mf, input_value_ctc),
                      fuzz.interp_membership(
                          x_potassio, potassio_ctc_2['muito baixo'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['2'].mf, input_value_ctc),
                      fuzz.interp_membership(
                          x_potassio, potassio_ctc_3['muito baixo'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['3'].mf, input_value_ctc),
                      fuzz.interp_membership(x_potassio, potassio_ctc_4['muito baixo'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['4'].mf, input_value_ctc)]

    pertinencia_ba = [fuzz.interp_membership(x_potassio, potassio_ctc_1['baixo'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['1'].mf, input_value_ctc),
                      fuzz.interp_membership(
                          x_potassio, potassio_ctc_2['baixo'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['2'].mf, input_value_ctc),
                      fuzz.interp_membership(
                          x_potassio, potassio_ctc_3['baixo'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['3'].mf, input_value_ctc),
                      fuzz.interp_membership(x_potassio, potassio_ctc_4['baixo'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['4'].mf, input_value_ctc)]

    pertinencia_me = [fuzz.interp_membership(x_potassio, potassio_ctc_1['medio'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['1'].mf, input_value_ctc),
                      fuzz.interp_membership(
                          x_potassio, potassio_ctc_2['medio'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['2'].mf, input_value_ctc),
                      fuzz.interp_membership(
                          x_potassio, potassio_ctc_3['medio'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['3'].mf, input_value_ctc),
                      fuzz.interp_membership(x_potassio, potassio_ctc_4['medio'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['4'].mf, input_value_ctc)]

    pertinencia_al = [fuzz.interp_membership(x_potassio, potassio_ctc_1['alto'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['1'].mf, input_value_ctc),
                      fuzz.interp_membership(
                          x_potassio, potassio_ctc_2['alto'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['2'].mf, input_value_ctc),
                      fuzz.interp_membership(
                          x_potassio, potassio_ctc_3['alto'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['3'].mf, input_value_ctc),
                      fuzz.interp_membership(x_potassio, potassio_ctc_4['alto'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['4'].mf, input_value_ctc)]

    pertinencia_ma = [fuzz.interp_membership(x_potassio, potassio_ctc_1['muito alto'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['1'].mf, input_value_ctc),
                      fuzz.interp_membership(
                          x_potassio, potassio_ctc_2['muito alto'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['2'].mf, input_value_ctc),
                      fuzz.interp_membership(
                          x_potassio, potassio_ctc_3['muito alto'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['3'].mf, input_value_ctc),
                      fuzz.interp_membership(x_potassio, potassio_ctc_4['muito alto'].mf, input_value_potassio)*fuzz.interp_membership(x_ctc, ctc['4'].mf, input_value_ctc)]

    max_pertinencia = []

    max_pertinencia.append(max(pertinencia_mb))

    max_pertinencia.append(max(pertinencia_ba))

    max_pertinencia.append(max(pertinencia_me))

    max_pertinencia.append(max(pertinencia_al))

    max_pertinencia.append(max(pertinencia_ma))

    # Calculando a dose de potássio
    # <Classe:valor>
    dose_por_classe = [150, 90, 60, 30, 0]
    soma = 0

    for i in range(len(dose_por_classe)):
        soma += max_pertinencia[i] * dose_por_classe[i]

    soma_pesos = sum(max_pertinencia)

    dose_potassio_hectare = round(soma/soma_pesos, 2)

    return dose_potassio_hectare


def fuzzy_fosforo(input_value_fosforo, input_value_argila):
    x_fosforo = np.arange(0, 61, 0.01)
    prct_argila = np.arange(0, 101, 0.01)

    fosforo_argila_1 = ctrl.Antecedent(x_fosforo, 'Fosforo1')
    fosforo_argila_2 = ctrl.Antecedent(x_fosforo, 'Fosforo2')
    fosforo_argila_3 = ctrl.Antecedent(x_fosforo, 'Fosforo3')
    fosforo_argila_4 = ctrl.Antecedent(x_fosforo, 'Fosforo4')
    argila = ctrl.Antecedent(prct_argila, 'Argila')

    classe_fosforo = ctrl.Consequent(np.arange(1, 6, 1), 'Classe Fosforo')

    fosforo_argila_1['muito baixo'] = fuzz.zmf(x_fosforo, 2.7, 3.6)
    fosforo_argila_1['baixo'] = fuzz.trapmf(x_fosforo, [2.48, 3.41, 5.4, 7.2])
    fosforo_argila_1['medio'] = fuzz.trapmf(x_fosforo, [4.88, 6.71, 8.1, 10.8])
    fosforo_argila_1['alto'] = fuzz.trapmf(x_fosforo, [7.28, 10.1, 16.2, 21.6])
    fosforo_argila_1['muito alto'] = fuzz.smf(x_fosforo, 14.4, 19.8)

    fosforo_argila_2['muito baixo'] = fuzz.zmf(x_fosforo, 3.6, 4.8)
    fosforo_argila_2['baixo'] = fuzz.trapmf(x_fosforo, [3.28, 4.51, 6.4, 9.6])
    fosforo_argila_2['medio'] = fuzz.trapmf(
        x_fosforo, [7.48, 8.91, 10.8, 14.4])
    fosforo_argila_2['alto'] = fuzz.trapmf(
        x_fosforo, [9.68, 13.31, 21.6, 28.8])
    fosforo_argila_2['muito alto'] = fuzz.smf(x_fosforo, 19.2, 26.4)

    fosforo_argila_3['muito baixo'] = fuzz.zmf(x_fosforo, 5.4, 7.2)
    fosforo_argila_3['baixo'] = fuzz.trapmf(
        x_fosforo, [4.88, 6.71, 10.8, 14.4])
    fosforo_argila_3['medio'] = fuzz.trapmf(
        x_fosforo, [9.68, 13.31, 16.2, 21.6])
    fosforo_argila_3['alto'] = fuzz.trapmf(
        x_fosforo, [14.48, 19.81, 32.4, 43.2])
    fosforo_argila_3['muito alto'] = fuzz.smf(x_fosforo, 28.8, 39.6)

    fosforo_argila_4['muito baixo'] = fuzz.zmf(x_fosforo, 9, 12)
    fosforo_argila_4['baixo'] = fuzz.trapmf(x_fosforo, [8.08, 11.11, 18, 24])
    fosforo_argila_4['medio'] = fuzz.trapmf(x_fosforo, [16.08, 22.11, 27, 36])
    fosforo_argila_4['alto'] = fuzz.trapmf(x_fosforo, [24.08, 33.11, 54, 72])
    fosforo_argila_4['muito alto'] = fuzz.smf(x_fosforo, 48, 66)

    argila['4'] = fuzz.zmf(prct_argila, 14.4, 20)
    argila['3'] = fuzz.trapmf(prct_argila, [16.8, 23.1, 36, 48])
    argila['2'] = fuzz.trapmf(prct_argila, [32.8, 45.1, 54, 72])
    argila['1'] = fuzz.smf(prct_argila, 52.8, 60)

    classe_fosforo['muito baixo'] = fuzz.trimf(
        classe_fosforo.universe, [1, 1, 1])
    classe_fosforo['baixo'] = fuzz.trimf(classe_fosforo.universe, [2, 2, 2])
    classe_fosforo['medio'] = fuzz.trimf(classe_fosforo.universe, [3, 3, 3])
    classe_fosforo['alto'] = fuzz.trimf(classe_fosforo.universe, [4, 4, 4])
    classe_fosforo['muito alto'] = fuzz.trimf(
        classe_fosforo.universe, [5, 5, 5])

    rule1 = ctrl.Rule(
        argila['4'] & fosforo_argila_1['muito baixo'], classe_fosforo['muito baixo'])
    rule2 = ctrl.Rule(
        argila['4'] & fosforo_argila_1['baixo'], classe_fosforo['baixo'])
    rule3 = ctrl.Rule(
        argila['4'] & fosforo_argila_1['medio'], classe_fosforo['medio'])
    rule4 = ctrl.Rule(
        argila['4'] & fosforo_argila_1['alto'], classe_fosforo['alto'])
    rule5 = ctrl.Rule(
        argila['4'] & fosforo_argila_1['muito alto'], classe_fosforo['muito alto'])

    rule6 = ctrl.Rule(
        argila['3'] & fosforo_argila_2['muito baixo'], classe_fosforo['muito baixo'])
    rule7 = ctrl.Rule(
        argila['3'] & fosforo_argila_2['baixo'], classe_fosforo['baixo'])
    rule8 = ctrl.Rule(
        argila['3'] & fosforo_argila_2['medio'], classe_fosforo['medio'])
    rule9 = ctrl.Rule(
        argila['3'] & fosforo_argila_2['alto'], classe_fosforo['alto'])
    rule10 = ctrl.Rule(
        argila['3'] & fosforo_argila_2['muito alto'], classe_fosforo['muito alto'])

    rule11 = ctrl.Rule(
        argila['2'] & fosforo_argila_3['muito baixo'], classe_fosforo['muito baixo'])
    rule12 = ctrl.Rule(
        argila['2'] & fosforo_argila_3['baixo'], classe_fosforo['baixo'])
    rule13 = ctrl.Rule(
        argila['2'] & fosforo_argila_3['medio'], classe_fosforo['medio'])
    rule14 = ctrl.Rule(
        argila['2'] & fosforo_argila_3['alto'], classe_fosforo['alto'])
    rule15 = ctrl.Rule(
        argila['2'] & fosforo_argila_3['muito alto'], classe_fosforo['muito alto'])

    rule16 = ctrl.Rule(
        argila['1'] & fosforo_argila_4['muito baixo'], classe_fosforo['muito baixo'])
    rule17 = ctrl.Rule(
        argila['1'] & fosforo_argila_4['baixo'], classe_fosforo['baixo'])
    rule18 = ctrl.Rule(
        argila['1'] & fosforo_argila_4['medio'], classe_fosforo['medio'])
    rule19 = ctrl.Rule(
        argila['1'] & fosforo_argila_4['alto'], classe_fosforo['alto'])
    rule20 = ctrl.Rule(
        argila['1'] & fosforo_argila_4['muito alto'], classe_fosforo['muito alto'])

    SE_ctrl = ctrl.ControlSystem([rule1, rule2, rule3, rule4, rule5, rule6, rule7, rule8, rule9,
                                 rule10, rule11, rule12, rule13, rule14, rule15, rule16, rule17, rule18, rule19, rule20])
    SE = ctrl.ControlSystemSimulation(SE_ctrl)

    SE.input['Fosforo1'] = input_value_fosforo
    SE.input['Fosforo2'] = input_value_fosforo
    SE.input['Fosforo3'] = input_value_fosforo
    SE.input['Fosforo4'] = input_value_fosforo

    SE.input['Argila'] = input_value_argila
    SE.compute()
    output_value = SE.output['Classe Fosforo']

    pertinencia_mb = [fuzz.interp_membership(x_fosforo, fosforo_argila_1['muito baixo'].mf, input_value_fosforo)*fuzz.interp_membership(prct_argila, argila['4'].mf, input_value_argila),
                      fuzz.interp_membership(x_fosforo, fosforo_argila_2['muito baixo'].mf, input_value_fosforo)*fuzz.interp_membership(
                          prct_argila, argila['3'].mf, input_value_argila),
                      fuzz.interp_membership(x_fosforo, fosforo_argila_3['muito baixo'].mf, input_value_fosforo)*fuzz.interp_membership(
                          prct_argila, argila['2'].mf, input_value_argila),
                      fuzz.interp_membership(x_fosforo, fosforo_argila_4['muito baixo'].mf, input_value_fosforo)*fuzz.interp_membership(prct_argila, argila['1'].mf, input_value_argila)]

    pertinencia_ba = [fuzz.interp_membership(x_fosforo, fosforo_argila_1['baixo'].mf, input_value_fosforo)*fuzz.interp_membership(prct_argila, argila['4'].mf, input_value_argila),
                      fuzz.interp_membership(x_fosforo, fosforo_argila_2['baixo'].mf, input_value_fosforo)*fuzz.interp_membership(
                          prct_argila, argila['3'].mf, input_value_argila),
                      fuzz.interp_membership(x_fosforo, fosforo_argila_3['baixo'].mf, input_value_fosforo)*fuzz.interp_membership(
                          prct_argila, argila['2'].mf, input_value_argila),
                      fuzz.interp_membership(x_fosforo, fosforo_argila_4['baixo'].mf, input_value_fosforo)*fuzz.interp_membership(prct_argila, argila['1'].mf, input_value_argila)]

    pertinencia_me = [fuzz.interp_membership(x_fosforo, fosforo_argila_1['medio'].mf, input_value_fosforo)*fuzz.interp_membership(prct_argila, argila['4'].mf, input_value_argila),
                      fuzz.interp_membership(x_fosforo, fosforo_argila_2['medio'].mf, input_value_fosforo)*fuzz.interp_membership(
                          prct_argila, argila['3'].mf, input_value_argila),
                      fuzz.interp_membership(x_fosforo, fosforo_argila_3['medio'].mf, input_value_fosforo)*fuzz.interp_membership(
                          prct_argila, argila['2'].mf, input_value_argila),
                      fuzz.interp_membership(x_fosforo, fosforo_argila_4['medio'].mf, input_value_fosforo)*fuzz.interp_membership(prct_argila, argila['1'].mf, input_value_argila)]

    pertinencia_al = [fuzz.interp_membership(x_fosforo, fosforo_argila_1['alto'].mf, input_value_fosforo)*fuzz.interp_membership(prct_argila, argila['4'].mf, input_value_argila),
                      fuzz.interp_membership(x_fosforo, fosforo_argila_2['alto'].mf, input_value_fosforo)*fuzz.interp_membership(
                          prct_argila, argila['3'].mf, input_value_argila),
                      fuzz.interp_membership(x_fosforo, fosforo_argila_3['alto'].mf, input_value_fosforo)*fuzz.interp_membership(
                          prct_argila, argila['2'].mf, input_value_argila),
                      fuzz.interp_membership(x_fosforo, fosforo_argila_4['alto'].mf, input_value_fosforo)*fuzz.interp_membership(prct_argila, argila['1'].mf, input_value_argila)]

    pertinencia_ma = [fuzz.interp_membership(x_fosforo, fosforo_argila_1['muito alto'].mf, input_value_fosforo)*fuzz.interp_membership(prct_argila, argila['4'].mf, input_value_argila),
                      fuzz.interp_membership(x_fosforo, fosforo_argila_2['muito alto'].mf, input_value_fosforo)*fuzz.interp_membership(
                          prct_argila, argila['3'].mf, input_value_argila),
                      fuzz.interp_membership(x_fosforo, fosforo_argila_3['muito alto'].mf, input_value_fosforo)*fuzz.interp_membership(
                          prct_argila, argila['2'].mf, input_value_argila),
                      fuzz.interp_membership(x_fosforo, fosforo_argila_4['muito alto'].mf, input_value_fosforo)*fuzz.interp_membership(prct_argila, argila['1'].mf, input_value_argila)]

    max_pertinencia = []

    max_pertinencia.append(max(pertinencia_mb))

    max_pertinencia.append(max(pertinencia_ba))

    max_pertinencia.append(max(pertinencia_me))

    max_pertinencia.append(max(pertinencia_al))

    max_pertinencia.append(max(pertinencia_ma))

    dose_por_classe = [250, 170, 130, 90, 0]
    soma = 0

    for i in range(len(dose_por_classe)):
        soma += max_pertinencia[i] * dose_por_classe[i]

    soma_pesos = sum(max_pertinencia)

    if soma_pesos != 0:
        dose_fosforo_hectare = soma/soma_pesos
    else:
        dose_fosforo_hectare = 0

    return round(dose_fosforo_hectare, 2)
