import streamlit as st
import random as rng
import Listor as lis



def getMod(x):
    if x <= 4:
        return "-3"
    elif x <= 6:
        return "-2"
    elif x <= 8:
        return "-1"
    elif x <= 12:
        return "0"
    elif x <= 14:
        return "+1"
    elif x <= 16:
        return "+2"
    else:
        return "+3"


def rollD6s(amount):
    rolls = 0
    results = []
    while(rolls < amount):
        res = rng.randrange(6) + 1
        results.append(res)
        rolls += 1
    results.sort()
    if amount > 3:
        results.pop(0)

    return getMod(sum(results))

def rollStartEquip():
    res = ""
    res += "Du har " + lis.firstRollList[rng.randrange(6)]
    roll1 = rng.randrange(12)
    roll2 = rng.randrange(12)

    
    if roll1 == 4 or roll2 == 1:
        if roll1 == 4:
            res += "den smutsiga pergamentrullen '" + lis.uPerg[rng.randrange(10)] + "'"
        if roll2 == 1:
            res += "samt den rena pergamentrullen '" + lis.cPerg[rng.randrange(10)] + "'"

        res += ". Utöver detta så är du beväpnad med " + lis.weaponList[rng.randrange(6)]
        res += ", och till försvar har du " + lis.armourList[rng.randrange(2)] + "."
    else:
        res += lis.seccondRollList[roll1]
        res += " samt " + lis.thirdRollList[roll2]
        res += ". Utöver detta så är du beväpnad med " + lis.weaponList[rng.randrange(10)]
        res += ", och till försvar har du " + lis.armourList[rng.randrange(4)] + "."
    return res

strength = 0
agility = 0
precence = 0
toughness = 0


col1, col2 = st.columns(2)
with col1:
    st.header('Utrustning')
    with st.container():
        'Du startar med:'
        st.write(rollStartEquip())

with col2:
    selected = st.multiselect('Roll extra dice for:', ['Styrka', 'Smidighet', 'Närvaro', 'Tålighet'], max_selections=2, default=[])
    roll = st.button('Slå!')
    if(roll):
        if 'Styka' in selected:
            strength = rollD6s(4)
            st.write('Styrka: ' + strength)
        else:
            strength = rollD6s(3)
            st.write('Styrka: ' + strength)
        if 'Smidighet' in selected:
            agility = rollD6s(4)
            st.write('Smidighet: ' + agility)
        else:
            agility = rollD6s(3)
            st.write('Smidighet: ' + agility)
        if 'Närvaro' in selected:
            precence = rollD6s(4)
            st.write('Närvaro: ' + precence)
        else:
            precence = rollD6s(3)
            st.write('Närvaro: ' + precence)
        if 'Tålighet' in selected:
            toughness = rollD6s(4)
            st.write('Tålighet: ' + toughness)
        else:
            toughness = rollD6s(3)
            st.write('Tålighet: ' + toughness)

st.write('-------')
if(roll):
    st.write(str((rng.randrange(8) + 1) + int(toughness)) + ' TP, ' + str((rng.randrange(6) + rng.randrange(6) + 2)*10) + ' Silver, ' + str(rng.randrange(4) + 1) + ' dagar värt av mat och vatten.')
st.write('--------')

col3, col4, col5 = st.columns(3)
with col3:
    res1 = str(rng.randrange(6) + 1) + str(rng.randrange(6) + 1)
    st.header(lis.feats.get(res1)[0])
    st.write(lis.feats.get(res1)[1])
with col4:
    st.header('Eller')
with col5:
    res2 = str(rng.randrange(6) + 1) + str(rng.randrange(6) + 1)
    st.header(lis.feats.get(res2)[0])
    st.write(lis.feats.get(res2)[1])

