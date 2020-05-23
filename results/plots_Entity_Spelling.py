# libraries
import numpy as np
import matplotlib.pyplot as plt

# set width of bar
barWidth = 0.14

# set height of bar
ibm_watson = [0.01,
              0.66667,
              1.00000,
              1.00000,
              0.85714]
luis = [0.01,
        0.01,
        0.01,
        1.00000,
        0.40000]
rasa = [0.46154,
        0.15385,
        0.01,
        0.85714,
        0.01]
wit = [0.86486,
       0.70588,
       0.88889,
       1.00000,
       0.66667]
dialogflow = [0.44444,
              0.62500,
              0.33333,
              1.00000,
              0.80000]

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
plt.xlabel('Groepering per entity per platform',
           fontweight='bold', fontsize=20)
plt.ylabel('F-score', fontweight='bold', fontsize=20)
plt.xticks([r + barWidth*2 for r in range(len(ibm_watson))],
           ["locatie",
            "datum",
            "tijdstip",
            "aantal_personen",
            "onboardService_type"],fontsize=13,rotation=15)

# Create legend & Show graphic
plt.legend()
plt.show()
