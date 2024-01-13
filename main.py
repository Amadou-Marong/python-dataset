import pandas as pd

# I first  specify the path by storing it in variable
path = ('C:/Users/pc/Downloads/data.csv')

# I now use the pandas library to read from the dataset by passing the path variable in the argument
data = pd.read_csv(path)


# I copy the data to work with and keep the original copy
df = data.copy()

#----------------------- DATA REPRESENTATION -------------------------------------#
# P(S(0) | G(0)) => Meaning the Conditional Probability of death given that the gender is male
# P(S(0) | G(1)) => Meaning the Conditional Probability of death given that the gender is female
# P(S(1) | G(0)) => Meaning the Conditional Probability of alive given that the gender is male
# P(S(1) | G(1)) => Meaning the Conditional Probability of alive given that the gender is female
#
# P(S(0) n G(0)) = > Meaning the probability of death and being male gender
# P(S(0) n G(1)) = > Meaning the probability of death and being female gender
# P(S(1) n G(0)) = > Meaning the probability of alive and being male gender
# P(S(1) n G(1)) = > Meaning the probability of alive and being female gender
#
# P(G(0)) => Probability of being a male gender
# P(G(1)) => Probability of being a female gender


# ---------------------- FORMULARS -------------------------#

# P(S(0) | G(0)) =  P(S(0) n G(0))/ P(G(0))
# P(S(0) | G(1)) =  P(S(0) n G(1))/ P(G(1))
#
# P(S(1) | G(0)) =  P(S(1) n G(0))/ P(G(0))
# P(S(1) | G(1)) =  P(S(1) n G(1))/ P(G(1))


#========================== NOW LETS FIRST FIND P(S(0) | G(0)) ==========================

# Since the 'Sex' Column is given in string value I convert it to numerical data
df['Sex'] = data['Sex'].apply(lambda x: 0 if x == 'male' else 1)

# Number of male gender that died
num_male_and_survived0 = len(df[(df['Sex'] == 0) & (df['Survived'] == 0)])

# Total number of passengers
total_num_passengers = len(df)

# Probability of death and male gender
prob_survived0_and_gender0 = num_male_and_survived0/total_num_passengers

# Number of male passengers
num_male_passengers = len(df[df['Sex'] == 0])

# Probability of male gender
prob_gender0 = num_male_passengers/total_num_passengers

# Conditional probability of death given a male gender
cond_prob_survived0_gender0 = prob_survived0_and_gender0/prob_gender0

print(f'Conditional Probability of P(S(0) | G(0)) : {cond_prob_survived0_gender0}')

#============= NOW LETS FIND THE CONDITIONAL PROBABILITY P(S(0) | G(1)) ==========================

# Number of female gender that died
num_female_and_survived0 = len(df[(df['Sex'] == 1) & (df['Survived'] == 0)])

# Probability of death and female gender
prob_survived0_and_gender1 = num_female_and_survived0/total_num_passengers

# Number of female passengers
num_female_passengers = len(df[df['Sex'] == 1])

# Probability of female gender
prob_gender1 = num_female_passengers/total_num_passengers

# Conditional probability of death and female gender
cond_prob_survived0_gender1 = prob_survived0_and_gender1/prob_gender1

print(f'Conditional Probability of P(S(0) | G(1)) : {cond_prob_survived0_gender1}')

#============= NOW LETS FIND THE CONDITIONAL PROBABILITY P(S(1) | G(0)) ==========================

# Number of male gender alive
num_male_and_survived1 = len(df[(df['Sex'] == 0) & (df['Survived'] == 1)])

# Probability of alive and male gender
prob_survived1_and_gender0 = num_male_and_survived1/total_num_passengers

# Conditional probability of alive given the gender is male
cond_prob_survived1_gender0 = prob_survived1_and_gender0/prob_gender0

print(f'Conditional Probability of P(S(1) | G(0)) : {cond_prob_survived1_gender0}')

#============= NOW LETS FIND THE CONDITIONAL PROBABILITY P(S(1) | G(1)) ==========================

# Number of female gender alive
num_female_and_survived1 = len(df[(df['Sex'] == 1) & (df['Survived'] == 1)])

# Probability of alive and female gender
prob_survived1_and_gender1 = num_female_and_survived1/total_num_passengers

# Conditional probability of alive given the gender is male
cond_prob_survived1_gender1 = prob_survived1_and_gender1/prob_gender1

print(f'Conditional Probability of P(S(1) | G(1)) : {cond_prob_survived1_gender1}')


