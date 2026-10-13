"""
Python Exercises Week 4 (class 3)
========================================================
Exercise 1: Probability Distributions and For-Loops
You are provided with two lists recording the distribution of future stock returns together
with their associate probabilities.
returns = [0.01 , 0.03, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17, 0.19]
probs = [0.05, 0.10, 0.10, 0.10, 0.20, 0.15, 0.10, 0.10, 0.05, 0.05]
(a) Calculate the expected return using a for loop.

(b) Calculate the variance using a for loop.

(c) Make a bar chart which illustrates the probability distribution of returns.
(d) Assume now that returns represent a sample of historical returns (each equally likely).
What would be the sample variance in this case?
(e) [Optional] Sort the list probs so that the highest probabilities appear first. Use only
for-loops (no sort() or max()) and make sure that each probability remains aligned
with its corresponding return.
We will learn next week how these calculations can be done in a simpler way.
========================================================
"""

returns = [0.01 , 0.03, 0.05, 0.07, 0.09, 0.11, 0.13, 0.15, 0.17, 0.19]
probs = [0.05, 0.10, 0.10, 0.10, 0.20, 0.15, 0.10, 0.10, 0.05, 0.05]
expected = 0
σ = 0
for i in range(len(returns)):
    expected+= returns[i] * probs[i]
for i in range(len(returns)):
    σ += probs[i] * (returns[i] - expected)**2
print(f"Expected return, E[R] is equal to {expected:,.2%}; and the  variance (risk,) of this security is {σ:,.2%} squared.")

"can't do c) because haven't learnt matplotlib and other libraries yet; will end the tutorial here"



"""
=======================================================
Exercise 2: Monetary Policy Announcements and ChatGPT
You are given the following data on the prices of two assets (A and B) along with a list of
timestamps hours (we will soon learn how to import data to Python; for now, simply copy
paste the given lists into Python). The data represents intra-daily trading prices around the
monetary policy announcement (monetary tightening) at 14:00. Note the figure below and
use ChatGPT to re-create it on your own as closesly as you can. Do you think the policy
announcement was expected by the market?
========================================================
"""
#(From Claude)
import matplotlib.pyplot as plt

hours = ['09:00','09:10','09:20','09:30','09:40','09:50',
         '10:00','10:10','10:20','10:30','10:40','10:50',
         '11:00','11:10','11:20','11:30','11:40','11:50',
         '12:00','12:10','12:20','12:30','12:40','12:50',
         '13:00','13:10','13:20','13:30','13:40','13:50',
         '14:00','14:10','14:20','14:30','14:40','14:50',
         '15:00','15:10','15:20','15:30','15:40','15:50',
         '16:00','16:10','16:20','16:30','16:40','16:50',
         '17:00','17:10']          # the two extra times

prices_A = [105, 105.2, 105.1, 105.3, 105.2, 105.4, 105.3, 105.2, 105.5, 105.3,
            105.4, 105.6, 105.5, 105.4, 105.6, 105.4, 105.7, 105.5, 105.6, 105.7,
            105.8, 105.6, 105.7, 105.8, 106.0, 105.8, 105.9, 106.1, 106.0, 105.9,
            105.9, 103.0, 102.5, 102.0, 101.5, 101.0, 100.5, 100.2, 100.5, 100.8,
            101.0, 101.5, 101.7, 102.0, 102.5, 103.0, 103.5, 104.0, 104.5, 105.0]

prices_B = [120, 120.2, 120.1, 120.3, 120.2, 120.5, 120.3, 120.4, 120.5, 120.4,
            120.6, 120.7, 120.5, 120.6, 120.8, 120.7, 121.0, 120.8, 121.0, 121.2,
            121.4, 121.2, 121.5, 121.6, 121.8, 121.5, 121.6, 121.9, 121.7, 121.5,
            121.5, 118.5, 117.5, 117.0, 116.5, 115.5, 114.5, 114.0, 114.2, 114.5,
            115.0, 115.5, 116.0, 116.5, 117.0, 117.5, 118.0, 119.0, 119.5, 120.0]

# Safety net: catches a length mismatch with a clear message
assert len(hours) == len(prices_A) == len(prices_B), "lists have different lengths"

fig, ax = plt.subplots(figsize=(11, 6))

ax.plot(hours, prices_A, color='darkred', linestyle='--', linewidth=2, label='Asset A')
ax.plot(hours, prices_B, color='navy', linestyle='-', linewidth=2, label='Asset B')

# Vertical line at the announcement
ax.axvline('14:00', color='gray', linestyle=':', linewidth=2)

# Label box next to the line
ax.text('14:10', 118.5, 'Monetary Tightening Surprise',
        bbox=dict(boxstyle='round', facecolor='white', edgecolor='gray'))

ax.set_title('High-Frequency Asset Prices Reaction to Monetary Policy Announcement',
             fontweight='bold', fontsize=14)
ax.set_xlabel('Time (HH:MM)')
ax.set_ylabel('Price (in USD)')
ax.grid(True, linestyle='--', alpha=0.5)
ax.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

