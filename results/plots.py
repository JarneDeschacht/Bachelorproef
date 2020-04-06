# libraries
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.14

# set height of bar
ibm_watson = [0.88235,
              0.35294,
              0.42857,
              0.96774,
              0.57143,
              0.81481,
              0.87500,
              0.78571,
              0.53846,
              0.93750]
luis = [0.96552,
        0.38710,
        0.62500,
        0.90909,
        0.51613,
        0.62069,
        0.82759,
        0.59259,
        0.61538,
        0.90909]

# TODO
rasa = [0.88235,
        0.35294,
        0.42857,
        0.96774,
        0.57143,
        0.81481,
        0.87500,
        0.78571,
        0.53846,
        0.93750]
wit = [0.88235,
       0.35294,
       0.42857,
       0.96774,
       0.57143,
       0.81481,
       0.87500,
       0.78571,
       0.53846,
       0.93750]
dialogflow = [0.88235,
              0.35294,
              0.42857,
              0.96774,
              0.57143,
              0.81481,
              0.87500,
              0.78571,
              0.53846,
              0.93750]

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
plt.xlabel('groepering per intent per platform', fontweight='bold', fontsize=20)
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
