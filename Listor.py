uPerg = [
    "Portarna söderut står vidöppna i din hand",
    "Ingenting är enkelt",
    "Te-le-kin-esis",
    "Lucy-fires levitation",
    "Luften är svår att andas",
    "Krafter från violetta skyar en regntung natt",
    "Utnyttja odöda",
    "Det som inte syns skadar desto mer",
    "Trött kropp, tungt ögonlock",
    "Död"
]

cPerg = [
    "Helande beröringar från kryptorna i djupet",
    "Förbarmande över värdelös själ",
    "Döda viskningar",
    "Himmelsänd hinna",
    "Ingen måste dö",
    "Dialog med kreatur",
    "Varde ljus... eller mörker",
    "Finner det som illa vill",
    "Hårda ord från en annan dimension",
    "När ord är lag"
]

light = [
    "Päls",
    "Gambeson",
    "Läderskydd",
    "Tjocka kläder",
    "Lätt Hjälm"
]

med = [
    "Fjällpansar",
    "Ringbrynja",
    "Hjälm och harnesk"
]

heavy = [
    "Plåtrustning",
    "Lamellpansar"
]

feats = {
    '11' : ['Assassin’s Deathblow', 'A firm grip. A sharp knife. That’s all it takes for someone to disappear into the alleys of Galgenbeck. You’ve become adept at it over the years. \n \n • Succeeding a DR12 Strength test allows you to grapple an unaware foe and automatically crit with a one handed bladed weapon.'],
    '12' : ['Battle-hardened Deathspeaker', 'You were called to battle, not for your prowess with blade and shield. Not for your speed and might. But because the words you spoke brought death to your enemies. \n \n • You may cast Powers while wearing medium armor. You may take this feat a second time to also include heavy armor.'],
    '13' : ['Beastly Scholar', 'You study the beasts of the land. Gutting them and spilling viscera to uncover secrets of the world. \n \n • You may scry and see the future with an animal’s innards. Gain an omen for every 10 hp the beast had, but never more than your maximum omens. Usable once per animal kind. \n \n • The beasts’ innards may also provide enlightening information.'],
    '14' : ['Bloodied knuckles', 'Years of bare knuckle fighting have turned your hands into deadly bludgeons. They are heavy with scars from the guilty and innocent. \n \n • Your unarmed attacks deal d6 damage and ignore light armour. You may take this feat a second time to increase this to d8 damage and medium armour. You may take this feat a third time to increase this to d10 damage and have them ignore all armour. \n \n • Fumbling an unarmed attack means you break a hand dealing the damage to yourself. You must seek out a specialist help to set your bones.'],
    '15' : ['Blood Pact', 'It’s a cruel world to be all alone in. But you’ve found a way to avoid this fate. \n \n • Form a blood pact with a willing participant. You can communicate by thought no matter the distance, this never goes away. Whatever one experiences, so does the other. This includes injury and death.'],
    '16' : ['Bloodthirsty Rage', 'The rush of combat is addictive. You’re always chasing that high. It’s kill or be killed. You can’t stop to ask questions. \n \n • When landing an attack that kills a creature you must move and attack another (this may include allies), adding d6 damage for every creature slain. Your onslaught stops when you fail to kill and you fall to the ground exhausted, losing your next turn.'],
    '21' : ['Bone Crafter', 'You don’t believe in letting things go to waste. Including the corpses of the fallen. \n \n • You can craft equipment of strangely high quality using a number of humanoid corpses. \n > A d6 weapon, 1 corpse worth of bones. \n > A shield, 5 corpses worth of bones. \n > Light armor, 10 corpses worth.'],
    '22' : ['Butcher', 'You’ve hacked livestock and poultry into small pieces before. You know what makes them work and how they are made. Humans aren’t that different. \n \n • On a DR12 Agility test, any ally that dies near you instead becomes broken as you attempt rapid life saving surgery. Should the person still die you may make d4 rations out of the corpse.'],
    '23' : ['Calm Killer', 'The knife or arrow that is most careful is the deadliest. You have a sharp eye for gaps and kinks in armour. \n \n • Once per turn when making a ranged or melee attack, you may reroll the damage dealt and keep the higher result.'],
    '24' : ['Cats Eyes', 'You looked up at the birds for a sign. Scattered bones, spilled entrails. For naught. But one day you saw your fate in the eyes of a cat lurking in the shadows. \n \n • Perfect vision in darkness, but the light of the sun burns your eyes. −2DR presence when in darkness, +2DR when in daylight. \n \n • Staring into the eyes of a wild beast let’s you feel whatever it is feeling.'],
    '25' : ['Dual Wielder', 'You’re no trained soldier. But you think two weapons should help you kill twice as fast. It hasn’t failed you yet. \n \n • You suffer no penalty when attacking with two weapons, you roll both damage dice and combine the results.'],
    '26' : ['Fateful Visions', 'The fates steer your journey across the dying world. One can only hope they guide you to redemption and not destruction. \n \n • Consume an omen and spend a few moments in quiet meditation. Ask the Game Master a question pertaining to the current situation. \n \n • You will be granted a bizarre vision that provides enlightening information. GM rolls a d4 in secret, on a 1 the vision is deceptive.'],
    '31' : ['Iron Stomach', 'When crops fail, and livestock births inedible abominations. One learns to not be picky when it comes to food. \n \n • You may consume rotting, putrid flesh with a DR6 Toughness test. Others witnessing this may find it disgusting. Outcasts roll morale.'],
    '32' : ['First Strike', 'You believe that the Shimmering Fields are for those who leap into battle, those who are first to reap glory. \n \n • Whether your side passes or fails the initiative roll, you may always act first if your action involves inflicting harm.'],
    '33' : ['Gutsy Strike', 'You once saw a man decapitate a horse with a giant sword. It was less a sword and more a large slab of iron. You can’t help but think of the beast’s vacant eyes whenever you swing your own sword. \n \n • When wielding zweihand weapons, you may swing with +2 to your DR. If the attack lands you add d6 to your damage. Missing allows your opponent to strike with an attack that you can defend against at +2DR'],
    '34' : ['Harbinger of Misery', 'You feel a dark blessing course though your veins. You have dedicated yourself to the black disk which will block out the sun. \n \n • Gain 4 Maximum omens instead of 2. As long as you live the GM rolls two misery dice every day.'],
    '35' : ['Herbalist Healer', 'You’ve spent what seemed like an eternity under the haze filled apprenticeship of a herbalist master. You left with a new outlook on life, and a few extra skills. \n \n • Once per day you may scrounge to find the necessary herbs and flora to create an infection curing elixir that also heals d4 hp. \n \n • DR12 Presence to attempt this treatment, failing instead creates a toxin dealing D4 damage.'],
    '36' : ['Horrific Growth', 'Maybe it was something you ate, or a Power had grown malevolent. Whatever it is you can’t get rid of it. \n \n • You violently grow an extra arm and hand. It functions just like your other arms and can grip things just fine. Other people see it as a sign of evil.'],
    '41' : ['Hyper Awareness', 'You are paranoid. Seeing danger in every shadow. Everything wants to kill you. You are jittery with bird-like movements. \n \n • You can never be the victim of a surprise attack. Additionally your side takes the initiative on a 3+.'],
    '42' : ['Immortal Memory', 'You are haunted by the memories of those that have fallen. Even if their spirits have moved on, and the bodies are dust, their memories linger for eternity. \n \n • Whenever encountering a place of great suffering. You may relive the tragedy through a memory that lingers. \n \n • There is a 1/20 chance that things become all too real. You suffer the same fate in reality. This might cause creatures and Powers to reappear.'],
    '43' : ['Inspired Storyteller', 'Your tales bring joy and smiles to everyone around you, even in the bleakest of times. All of it lies of course, but who cares? \n \n • DR9 Presence test whenever resting to weave a compelling tale. increase the DR+1 for every additional audience member. Success allows everyone to gain an omen. You cannot exceed your maximum number of omens.'],
    '44' : ['Leech', 'An acquired taste. Or perhaps a disease. Maybe a curse. An eternal thirst. \n \n • Blood heals and sustains you. A pint of blood heals you for D4 hp. You may still eat regular food, but you suffer the effects of starvation after one day.'],
    '45' : ['Likeable', 'There’s something about your smile. The way you compose yourself. The way you speak. You’re best described as approachable. It’s weird. \n \n • Whenever a reaction roll is made, roll 3d6 and keep the highest two dice.'],
    '46' : ['Living Armor', 'You’ve survived war. You’ve survived because of cold steel that has been scarred so that you may live. It’s become a part of you and you’ve learned to carry its burden. \n \n • Remove the Agility penalty for the armor you are currently wearing. This does not affect your defence rolls. \n \n • You may not remove your armor without painfully dying. This also happens if it breaks. Repairing it is possible, but very painful.'],
    '51' : ['Lucky', 'Fate? Sounds ominous. You prefer luck. Good things always seem to happen to you. This has lulled you into a false sense of security. How long will this last? \n \n • You do not have any omens. And no omens can be spent to influence your roll. Instead you always roll 2d20 for your tests and pick the highest result. \n \n • However, you still fumble if either of them come up as 1. Your luck has to run out eventually.'],
    '52' : ['Mortal Draw', 'Your blade hungers. Blood is the only thing that can sate it. Once drawn it demands it, and will punish you for failing. \n \n • Your first attack in combat always deals max damage assuming the attack hits. If you miss, your opponent may attack you. This can be defended against at +2DR'],
    '53' : ['Negotiator', 'You abhor conflict. A pacifist by nature, sometimes it’s best to try de-escalate the situation. Some call you a coward. \n \n • Roll a Presence test, DR6+ opponents highest morale. Success means the fighting stops. For now.'],
    '54' : ['Outback Survivalist', 'Time spent in the harsh wilderness has taught you how to thrive. Small comforts can be made even in this bleak world. \n \n • DR9 Presence test to create a comfortable campsite. DR+1 for every additional person it shelters. When resting at this camp everyone recovers 2d6 hp instead of d6'],
    '55' : ['Party Chef', 'You’ve mastered the art of cooking slop. Able to turn the most horrid of food somewhat palatable. \n \n • DR9 Presence to cook a meal when resting. DR+1 for any additional servings. On success you may stretch a single ration to feed the entire party, failing means the ration is spoiled.'],
    '56' : ['Piper', 'You may speak with rats, whistling allows you to attract d4 number of them. They might not have reliable information but are always happy to converse with you.'],
    '61' : ['Power Word', 'The powers that be whisper dark secrets in your ears wherever you walk. Their incessant chittering never gives you peace. \n \n • You innately know one random sacred or unclean Power. Additionally once you have read a scroll you may carve its esoteric glyphs into your flesh and no longer need the scroll itself to cast it. \n \n • Every night there is 1/20 chance that you accidentally cast a Power in your sleep. This Power also has a 1 in 6 chance of fumbling.'],
    '62' : ['Predatory Sense', 'Somewhere along your bloodline wickedness was introduced. It’s influence is thin within your blood but ever present. \n \n • You have a keen sense of smell when it comes to humans. You can sniff individuals out from a room away, identify someone, and even track them easily with a DR12 Presence test.'],
    '63' : ['Reckless Attacker', 'Overzealous, constantly making bad calls, an extremely poor sense of judgement. But you’ve lived this long so you must be doing something right. \n \n •You may attack the same target twice on your turn. Missing the second attack allows your opponent to land an attack that you can defend against at +2DR.'],
    '64' : ['Shield Breaker', 'You know that the moment an opponent is at their most vulnerable is right after they’ve attacked. \n \n • Whenever you use your shield to block all incoming damage, you may attempt a counter attack with +3 damage.'],
    '65' : ['Skinner', 'Your skin crawls and itches constantly. Constantly scabbing and foul. The skin of others brings you momentary solace. \n \n • You may wear the skin of a creature you recently killed to disguise yourself. You look, sound and even smell like them. \n \n • The skin decays after d4 hours and you revert back to your normal, wretched form.'],
    '66' : ['Vile Blood', 'Something about your blood is wrong. It’s more akin to the putrid ichor of a corpse. \n \n • Whenever a creature attacks you with a biting attack and hurts you it is poisoned. It suffers d4 damage for d6 rounds. \n \n • Additionally should you suffer an infection roll a d2. On a 2 you do not have infection.'],
}

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