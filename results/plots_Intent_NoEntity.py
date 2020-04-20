# libraries
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.14

# set height of bar
ibm_watson = [0.68966,
              0.40000,
              0.44444,
              0.96774,
              0.57143,
              0.81481,
              0.87500,
              0.78571,
              0.53846,
              0.93750]
luis = [0.69565,
        0.38710,
        0.62500,
        0.90909,
        0.51613,
        0.62069,
        0.82759,
        0.59259,
        0.61538,
        0.90909]
rasa = [0.92857,
        0.35714,
        0.40000,
        0.88235,
        0.48000,
        0.73333,
        0.83333,
        0.80000,
        0.52174,
        0.83333]
wit = [0.50000,
       0.43750,
       0.38462,
       1.00000,
       0.59259,
       0.82759,
       0.89655,
       0.76923,
       0.61538,
       1.00000]
dialogflow = [0.47619,
              0.29630,
              0.45714,
              0.83333,
              0.50000,
              0.74286,
              0.84211,
              0.70588,
              0.61538,
              0.86667]

# Set position of bar on X axis
r1 = np.arange(len(ibm_watson))
r2 = [x + barWidth for x in r1]
r3 = [x + barWidth for x in r2]
r4 = [x + barWidth for x in r3]
r5 = [x + barWidth for x in r4]

# Make the plot
plt.bar(r1, ibm_watson, color='#0f63fe', width=barWidth,
        edgecolor='white', label='IBM Watson')
plt.bar(r2, luis, color='#009480', width=barWidth,
        edgecolor='white', label='LUIS')
plt.bar(r3, rasa, color='#5b17ee', width=barWidth,
        edgecolor='white', label='RASA NLU')
plt.bar(r4, wit, color='#bcd5ee', width=barWidth,
        edgecolor='white', label='Wit.ai')
plt.bar(r5, dialogflow, color='#ef6c00', width=barWidth,
        edgecolor='white', label='Dialogflow')

# Add xticks on the middle of the group bars
plt.xlabel('Groepering per intent per platform',
           fontweight='bold', fontsize=20)
plt.ylabel('F-score', fontweight='bold', fontsize=20)
plt.xticks([r + barWidth*2 for r in range(len(ibm_watson))],
           ["greetings",
            "geefBestemmingen",
            "geefReisTijden",
            "boekBusreis",
            "geefActueleInfo",
            "wijzigBusreis",
            "annuleerBusreis",
            "geefOnboardServices",
            "meldKlachten",
            "huurBusMetChauffeur"])

# Create legend & Show graphic
plt.legend()
plt.show()
