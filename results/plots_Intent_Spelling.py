# libraries
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.14

# set height of bar
ibm_watson = [0.28571,
              0.40000,
              0.57143,
              0.88889,
              0.75000,
              0.66667,
              1.00000,
              1.00000,
              0.50000,
              1.00000]
luis = [0.66667,
        0.40000,
        0.75000,
        0.66667,
        0.50000,
        0.75000,
        0.00000,
        0.00000,
        0.50000,
        0.50000]
rasa = [0.66667,
        0.00000,
        0.44444,
        0.80000,
        0.80000,
        0.85714,
        0.80000,
        0.63158,
        0.33333,
        0.66667]
wit = [0.00000,
       0.00000,
       0.25000,
       0.75000,
       0.57143,
       0.66667,
       0.85714,
       1.00000,
       0.00000,
       1.00000]
dialogflow = [0.50000,
              0.40000,
              0.00000,
              0.80000,
              0.40000,
              0.57143,
              0.00000,
              0.85714,
              0.00000,
              1.00000]

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
