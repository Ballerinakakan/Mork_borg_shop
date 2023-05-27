import streamlit as st
import random as rng
import Listor as lis

firstRollList = [
    "",
    "",
    "en ryggsäck, rymmer 7 normalstora föremål och ",
    "en säck, rymmer 10 normalstora föremål och ",
    "en liten vagn, eller valfritt föremål ovan och ",
    "en åsna, inte så dumt, eller valfritt föremål ovan och "
]

seccondRollList = [
    "10 meter rep",
    "facklor (Närvaro + 4 stycken)",
    "en oljelampa (med olja för Närvaro + 6 timmar)",
    "en magnesiumremsa",
    "en slumpad smutsig pergamentrulle",
    "en vass nål",
    "en förbandslåda (Närvaro + 4 användningar, stoppar blörningar/infektioner och läker t6 TP)",
    "en metallfil + dyrkar",
    "en saxfälla (Närvaro mot SG14 för att upptäcka, t8 skada)",
    "en bomb (försluten vätska som kastas, t10 skada)",
    "en flaska rött gift, " + str(rng.randrange(4) + 1) + " doser (Tålighet mot SG12 eller t10 skada)",
    "ett krucifix i silver"
]

thirdRollList = [
    "ett livselixir, " + str(rng.randrange(4) + 1) + " doser (läker t6 TP och häver infektion)",
    "en slumpad ren pergamentrulle",
    "en loppäten hund (" + str(rng.randrange(6) + 3) + " TP, bett t4, lyder bara dig)",
    str(rng.randrange(4) + 1) + " apor som ignorerar men älskar dig (" + str(rng.randrange(4) + 3) + " TP, slag/bett t4)",
    "en dyrbar parfym värd 25s",
    "en verktygslåda (10 spikar, tång, hammare, liten såg och en borr)",
    "5 meter tung kätting",
    "en änterhake",
    "en sköld (-1 TP skada alternativt ignorera all skada och förstör skölden)",
    "ett bräckjärn (t4 skada om det används som vapen)",
    "ister (kan funka som 5 måltider)",
    "ett tält"
]

weaponList = [
    "ett lårben, t4 skada",
    "en stav, t4 skada",
    "ett kortsvärd, t4 skada",
    "en kniv, t4 skada",
    "en hjälmkrossare, t6 skada",
    "ett svärd, t6 skada",
    "en pilbåge, t6 skada, med Närvaro + 10 pilar",
    "en stridsgissel, t8 skada",
    "en armborst, t8 skada, med Närvaro + 10 skäftor",
    "EINEN ZWEIHÄNDER, T10 SKADA"
]

armourList = [
    "ett rejält övermod då du inte använder någon rustning",
    "lätt rustning, -t2 skada, nivå 1",
    "medeltung rustning, -t4 skada, nivå 2",
    "tung rustning, -t6 skada, nivå 3"
]

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
    res += "Du har " + firstRollList[rng.randrange(6)]
    roll1 = rng.randrange(12)
    roll2 = rng.randrange(12)

    
    if roll1 == 4 or roll2 == 1:
        if roll1 == 4:
            res += "den smutsiga pergamentrullen '" + lis.uPerg[rng.randrange(10)] + "'"
        if roll2 == 1:
            res += "samt den rena pergamentrullen '" + lis.cPerg[rng.randrange(10)] + "'"

        res += ". Utöver detta så är du beväpnad med " + weaponList[rng.randrange(6)]
        res += ", och till försvar har du " + armourList[rng.randrange(2)] + "."
    else:
        res += seccondRollList[roll1]
        res += " samt " + thirdRollList[roll2]
        res += ". Utöver detta så är du beväpnad med " + weaponList[rng.randrange(10)]
        res += ", och till försvar har du " + armourList[rng.randrange(4)] + "."
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

