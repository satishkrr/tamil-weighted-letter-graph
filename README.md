= தமிழ் எழுத்து தொடர் வெப்பப்படம்(?)

முன்னூறாயிரம் சொற்களை கொண்டு, எந்தெந்த எழுத்து எவற்றை தொடர்ந்து வரும் என்று பார்க்கும் முயற்சி.

=== Tamil Weighted Letter Chain Heatmap

This heatmap is produced from over 3 million tamil words collected from news websites. The heatmap is to be read from left to right, i.e the first row of the grid mean, the what tamil letters follow 'ஃ. The rendering of tamil fonts in plotting package is still limited, that is the reason of bizzare text in title as well as the labels. The corpus and the scripts will be made available soon.

== Order of letters.

Here I include the order of the characters in which the plot is meant to be read. This sorting order is based on python sorted() function and the letters are read by open-tamil[1] python projects. Note the consonants e.g 'க்', is at the last of every row. Unicode really messed up tamil character encoding :(

Also note that not all tamil letters are present, because this is collected from a news corpus, we only see the letters which are part of common words.


    ['ஃ', 'அ', 'ஆ', 'இ', 'ஈ', 'உ', 'ஊ', 'எ', 'ஏ', 'ஐ', 'ஒ', 'ஓ', 'ஔ',
    'க', 'கா', 'கி', 'கீ', 'கு', 'கூ', 'கெ', 'கே', 'கை', 'கொ', 'கோ', 'கௌ', 'க்',
    'ங', 'ஙே', 'ங்',
    'ச', 'சா', 'சி', 'சீ', 'சு', 'சூ', 'செ', 'சே', 'சை', 'சொ', 'சோ', 'சௌ', 'ச்',
    'ஜ', 'ஜா', 'ஜி', 'ஜீ', 'ஜு', 'ஜூ', 'ஜெ', 'ஜே', 'ஜை', 'ஜொ', 'ஜோ', 'ஜௌ', 'ஜ்',
    'ஞ', 'ஞா', 'ஞி', 'ஞீ', 'ஞை', 'ஞோ', 'ஞ்',
    'ட', 'டா', 'டி', 'டீ', 'டு', 'டூ', 'டெ', 'டே', 'டை', 'டொ', 'டோ', 'டௌ', 'ட்',
    'ண', 'ணா', 'ணி', 'ணீ', 'ணு', 'ணூ', 'ணெ', 'ணே', 'ணை', 'ணொ', 'ணோ', 'ண்',
    'த', 'தா', 'தி', 'தீ', 'து', 'தூ', 'தெ', 'தே', 'தை', 'தொ', 'தோ', 'தௌ', 'த்',
    'ந', 'நா', 'நி', 'நீ', 'நு', 'நூ', 'நெ', 'நே', 'நை', 'நொ', 'நோ', 'நௌ', 'ந்',
    'ன', 'னா', 'னி', 'னீ', 'னு', 'னூ', 'னெ', 'னே', 'னை', 'னொ', 'னோ', 'னௌ', 'ன்',
    'ப', 'பா', 'பி', 'பீ', 'பு', 'பூ', 'பெ', 'பே', 'பை', 'பொ', 'போ', 'பௌ', 'ப்',
    'ம', 'மா', 'மி', 'மீ', 'மு', 'மூ', 'மெ', 'மே', 'மை', 'மொ', 'மோ', 'மௌ', 'ம்',
    'ய', 'யா', 'யி', 'யீ', 'யு', 'யூ', 'யெ', 'யே', 'யை', 'யொ', 'யோ', 'ய்',
    'ர', 'ரா', 'ரி', 'ரீ', 'ரு', 'ரூ', 'ரெ', 'ரே', 'ரை', 'ரொ', 'ரோ', 'ரௌ', 'ர்',
    'ற', 'றா', 'றி', 'றீ', 'று', 'றூ', 'றெ', 'றே', 'றை', 'றொ', 'றோ', 'ற்',
    'ல', 'லா', 'லி', 'லீ', 'லு', 'லூ', 'லெ', 'லே', 'லை', 'லொ', 'லோ', 'லௌ', 'ல்',
    'ள', 'ளா', 'ளி', 'ளீ', 'ளு', 'ளூ', 'ளெ', 'ளே', 'ளை', 'ளொ', 'ளோ', 'ளௌ', 'ள்',
    'ழ', 'ழா', 'ழி', 'ழீ', 'ழு', 'ழூ', 'ழெ', 'ழே', 'ழை', 'ழொ', 'ழோ', 'ழ்',
    'வ', 'வா', 'வி', 'வீ', 'வு', 'வூ', 'வெ', 'வே', 'வை', 'வொ', 'வோ', 'வௌ', 'வ்',
    'ஷ', 'ஷா', 'ஷி', 'ஷீ', 'ஷு', 'ஷூ', 'ஷெ', 'ஷே', 'ஷை', 'ஷொ', 'ஷோ', 'ஷ்',
    'ஸ', 'ஸா', 'ஸி', 'ஸீ', 'ஸு', 'ஸூ', 'ஸெ', 'ஸே', 'ஸை', 'ஸொ', 'ஸோ', 'ஸௌ', 'ஸ்',
    'ஹ', 'ஹா', 'ஹி', 'ஹீ', 'ஹு', 'ஹூ', 'ஹெ', 'ஹே', 'ஹை', 'ஹொ', 'ஹோ', 'ஹௌ', 'ஹ்']


== Links
[1] (Open-Tamil)[https://github.com/Ezhil-Language-Foundation/open-tamil]
