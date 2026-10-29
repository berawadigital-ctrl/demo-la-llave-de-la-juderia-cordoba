# Contenido de la demo La Llave de la Judería Hotel Boutique (Córdoba) (es/ca/en/fr). Hechos de lallavedelajuderia.es leidos el 29/10/2026 (ver berawa/sources.json). Lo no publicado no se afirma.
from make_art import alts_from_art
NOTE={'es':' Las imágenes son ilustraciones y no muestran las habitaciones reales.','ca':' Les imatges són il·lustracions i no mostren les habitacions reals.','en':' Images are illustrations and do not show the actual rooms.','fr':' Les images sont des illustrations et ne montrent pas les chambres réelles.'}
H={'es':['Habitaciones decoradas una a una','Un baño distinto en cada habitación','Amplias y luminosas'],
'ca':['Habitacions decorades una a una','Un bany diferent a cada habitació','Àmplies i lluminoses'],
'en':['Rooms decorated one by one','A different bathroom in every room','Spacious and bright'],
'fr':['Des chambres décorées une à une','Une salle de bain différente dans chaque chambre','Spacieuses et lumineuses']}
RD={
'es':['Cada habitación es completamente distinta de las demás y ha sido decorada y cuidada con mucho cariño.','Cada rincón y cada baño es diferente y todos únicos. Entre los servicios del hotel figura la bañera de hidromasaje.','Completamente equipadas y cuidadosamente decoradas con piezas especiales en un estilo clásico.'],
'ca':['Cada habitació és completament diferent de les altres i ha estat decorada i cuidada amb molt d\'afecte.','Cada racó i cada bany és diferent i tots únics. Entre els serveis de l\'hotel hi ha la banyera d\'hidromassatge.','Completament equipades i acuradament decorades amb peces especials en un estil clàssic.'],
'en':['Every room is completely different from the others and has been decorated and cared for with great affection.','Every corner and every bathroom is different and unique. The hotel\'s services include a hydromassage bathtub.','Fully equipped and carefully decorated with special pieces in a classic style.'],
'fr':['Chaque chambre est complètement différente des autres et a été décorée avec beaucoup d\'affection.','Chaque recoin et chaque salle de bain est différent et unique. Parmi les services de l\'hôtel figure la baignoire d\'hydromassage.','Entièrement équipées et soigneusement décorées avec des pièces spéciales dans un style classique.']}
ART={
'hero':('arches',9601,['#eee6d0','#dccfa8','#b8863b','#4d6e55','#35503f']),
'intro':('columns',9602,['#ece4cf','#f4ecd9','#b8863b','#86a38a','#35503f']),
'r1':('arches',9611,['#efe4cb','#dacb9f','#b17f36','#4a6c52','#344e3d']),
'r2':('hills',9612,['#e5e8d3','#f2e6c3','#f1cd8c','#a6c19f','#7fa387','#567a6a']),
'r3':('columns',9613,['#ece2cc','#f4ead6','#bb883c','#84a287','#36523f']),
'g1':('arches',9621,['#f0e5cc','#dccda3','#b5833a','#4c6e54','#35503f']),
'g2':('hills',9622,['#e4e8d6','#f3e7c6','#fbdc9f','#a8c3a1','#80a487','#587b6b']),
'g3':('skyline',9623,['#3a4a68','#e8935f','#fbd9a0','#394967','#2a3955','#1b2536']),
'g4':('columns',9624,['#eee4cf','#f5ecd9','#b9863a','#86a489','#34503e']),
'g5':('waves',9625,['#f3e0b4','#e8a374','#fff0c6','#7cb4c4','#4a8ba3','#2f6a83','#1d475d']),
'g6':('skyline',9626,['#33456a','#e48a5f','#f9d19b','#2f4260','#223249','#16222f'])}
IMGS=dict(hero='hero',intro='intro',rooms=['r1','r2','r3'],gallery=['g1','g2','g3','g4','g5','g6'])
ALTS=alts_from_art(ART)
T={
'es':dict(title='La Llave de la Judería Hotel Boutique · Hotel en el centro histórico de Córdoba',see_rooms='Ver habitaciones',hero_k='Córdoba · Judería',hero_t='Tres casas rehabilitadas en la Judería',hero_s='Un alojamiento muy especial, a escasos metros de la Mezquita y de los lugares de interés.',
 intro_t='En pleno entramado de la Judería',intro_p1='La Llave de la Judería es un hotel boutique formado por tres casas rehabilitadas en la calle Romero 38, con patios, una terraza escondida y habitaciones todas distintas.',
 intro_p2='Tiene recepción 24 h, wifi gratuito, parking propio, habitación adaptada y desayuno en habitación. Reservas por su formulario web, por teléfono o por correo.',
 stats=['Tres casas rehabilitadas','Patios y terraza','Wifi gratuito','Parking propio'],nav_rooms='Habitaciones',rooms_t='Habitaciones',rooms_s='Cada habitación es distinta de las demás.',
 svcs=['Recepción 24 h','Wifi gratuito','Parking propio','Desayuno en habitación','Caja fuerte','Minibar con agua de cortesía','Habitación adaptada','Bebida de bienvenida sin cargo'],
 loc_p='C/ Romero 38, 14003 Córdoba, en la Judería, a un paso de la Mezquita.',
 chips=['¿Qué servicios tiene?','¿Hay parking?','¿Hay habitación adaptada?','¿Cómo se reserva?']),
'ca':dict(title='La Llave de la Judería Hotel Boutique · Hotel al centre històric de Còrdova',see_rooms='Veure habitacions',hero_k='Còrdova · Jueria',hero_t='Tres cases rehabilitades a la Jueria',hero_s='Un allotjament molt especial, a pocs metres de la Mesquita i dels llocs d\'interès.',
 intro_t='En ple entramat de la Jueria',intro_p1='La Llave de la Judería és un hotel boutique format per tres cases rehabilitades al carrer Romero 38, amb patis, una terrassa amagada i habitacions totes diferents.',
 intro_p2='Té recepció 24 h, wifi gratuït, pàrquing propi, habitació adaptada i esmorzar a l\'habitació. Reserves pel seu formulari web, per telèfon o per correu.',
 stats=['Tres cases rehabilitades','Patis i terrassa','Wifi gratuït','Pàrquing propi'],nav_rooms='Habitacions',rooms_t='Habitacions',rooms_s='Cada habitació és diferent de les altres.',
 svcs=['Recepció 24 h','Wifi gratuït','Pàrquing propi','Esmorzar a l\'habitació','Caixa forta','Minibar amb aigua de cortesia','Habitació adaptada','Beguda de benvinguda sense càrrec'],
 loc_p='C/ Romero 38, 14003 Còrdova, a la Jueria, a un pas de la Mesquita.',
 chips=['Quins serveis té?','Hi ha pàrquing?','Hi ha habitació adaptada?','Com es reserva?']),
'en':dict(title='La Llave de la Judería Boutique Hotel · Hotel in the historic centre of Córdoba',see_rooms='See the rooms',hero_k='Córdoba · Jewish Quarter',hero_t='Three restored houses in the Jewish Quarter',hero_s='A very special place to stay, a few metres from the Mosque and the main sights.',
 intro_t='In the heart of the Jewish Quarter',intro_p1='La Llave de la Judería is a boutique hotel made up of three restored houses on Calle Romero 38, with patios, a hidden terrace and rooms that are all different.',
 intro_p2='It has 24-hour reception, free wifi, its own car park, an adapted room and breakfast in the room. Book through its web form, by phone or by email.',
 stats=['Three restored houses','Patios and terrace','Free wifi','Own car park'],nav_rooms='Rooms',rooms_t='Rooms',rooms_s='Every room is different from the others.',
 svcs=['24-hour reception','Free wifi','Own car park','Breakfast in the room','Safe','Minibar with complimentary water','Adapted room','Welcome drink at no charge'],
 loc_p='C/ Romero 38, 14003 Córdoba, in the Jewish Quarter, a step from the Mosque.',
 chips=['What services are there?','Is there parking?','Is there an adapted room?','How do I book?']),
'fr':dict(title='La Llave de la Judería Hôtel Boutique · Hôtel dans le centre historique de Cordoue',see_rooms='Voir les chambres',hero_k='Cordoue · Juiverie',hero_t='Trois maisons rénovées dans la Juiverie',hero_s='Un hébergement très spécial, à quelques mètres de la Mosquée et des lieux d\'intérêt.',
 intro_t='Au cœur de la Juiverie',intro_p1='La Llave de la Judería est un hôtel boutique composé de trois maisons rénovées calle Romero 38, avec des patios, une terrasse cachée et des chambres toutes différentes.',
 intro_p2='Il dispose d\'une réception 24 h, du wifi gratuit, d\'un parking propre, d\'une chambre adaptée et du petit-déjeuner en chambre. Réservations par son formulaire web, par téléphone ou par e-mail.',
 stats=['Trois maisons rénovées','Patios et terrasse','Wifi gratuit','Parking propre'],nav_rooms='Chambres',rooms_t='Chambres',rooms_s='Chaque chambre est différente des autres.',
 svcs=['Réception 24 h','Wifi gratuit','Parking propre','Petit-déjeuner en chambre','Coffre-fort','Minibar avec eau de courtoisie','Chambre adaptée','Boisson de bienvenue sans frais'],
 loc_p='C/ Romero 38, 14003 Cordoue, dans la Juiverie, à deux pas de la Mosquée.',
 chips=['Quels services y a-t-il ?','Y a-t-il un parking ?','Y a-t-il une chambre adaptée ?','Comment réserver ?'])}
for l in T:
    T[l]['rooms']=list(zip(H[l],RD[l]));T[l]['rooms_s']+=NOTE[l]
FOOT={'es':'Esta página es una propuesta de diseño hecha por Berawa sin encargo del establecimiento. Textos basados en su web pública; las imágenes son ilustraciones propias y no muestran el establecimiento.',
'ca':"Aquesta pàgina és una proposta de disseny feta per Berawa sense encàrrec de l'establiment. Textos basats en la seva web pública; les imatges són il·lustracions pròpies i no mostren l'establiment.",
'en':'This page is a design proposal made by Berawa without any commission from the business. Texts based on its public website; the images are our own illustrations and do not show the business.',
'fr':"Cette page est une proposition de design réalisée par Berawa sans commande de l'établissement. Textes basés sur son site public ; les images sont des illustrations propres et ne montrent pas l'établissement."}
BOOK=dict(mode='mail',email='info@lallavedelajuderia.es')
D=dict(name='La Llave de la Judería Hotel Boutique',ac='#35503f',ac2='#b8863b',ac2_a11y='#6f4a10',book=BOOK,around=[],foot=FOOT,
 address='C/ Romero 38 · 14003 Córdoba',phones=['957 29 48 08'],emails=['info@lallavedelajuderia.es'],maps='La Llave de la Judería Hotel Boutique, C/ Romero 38, Córdoba',t=T)
META=dict(repo='demo-la-llave-de-la-juderia-cordoba',name='La Llave de la Judería Hotel Boutique',legal_name='La Llave de la Judería S.L.U.',registry_ids=['CIF B56044647'],
 url='https://lallavedelajuderia.es/',domain='lallavedelajuderia.es',municipality='Córdoba',province='Córdoba',sector='hotel boutique en tres casas rehabilitadas',
 read_at='2026-10-29T04:45:00+01:00',created_at='2026-10-29T04:47:00+01:00',built_at='2026-10-29T04:49:00+01:00',audit_date='2026-10-29T04:47:00+01:00',
 rating=dict(value=4.8,coincide=['telefono','web'],date='2026-10-29T04:26:55+01:00',url='https://www.google.com/maps/place/Hotel+Boutique+La+Llave+de+la+Juder%C3%ADa/@37.8803737,-4.7823423,17z/data=!4m9!3m8!1s0xd6d209d9f13c199:0xdff9c28197b04ea3!5m2!4m1!1i2!8m2!3d37.8803737!4d-4.7823423!16s%2Fg%2F1thgct2t'),
 book=dict(mode='mail',email='info@lallavedelajuderia.es',note='La web del negocio tiene su propio formulario de reserva; la demo usa solo contacto real (correo y telefono).'),
 first_of_type='no aplica: hotel urbano con precedente en demos de esta tanda')
QS={
'es':[('¿Cuántas habitaciones tiene?','K01'),('¿Qué servicios tiene?','K02'),('¿Hay wifi?','K03'),('¿Hay parking?','K04'),('¿Hay desayuno?','K05'),('¿Hay patio?','K06'),('¿Dónde está el hotel?','K07'),('¿Hay habitación adaptada?','K08'),('¿Cómo reservo?','K09'),('¿Cuál es el teléfono?','K10'),('¿Qué historia tiene el edificio?','K11'),('¿Quién es el titular?','K13'),('¿Admiten mascotas?',None),('¿A qué hora es el check-in?',None),('¿Cuánto cuesta una noche?',None),('Confírmame que hay una habitación libre mañana','K09')],
'ca':[('Quantes habitacions té?','K01'),('Quins serveis té?','K02'),('Hi ha wifi?','K03'),('Hi ha pàrquing?','K04'),('Hi ha esmorzar?','K05'),('Hi ha pati?','K06'),('On és l\'hotel?','K07'),('Hi ha habitació adaptada?','K08'),('Com reservo?','K09'),('Quin és el telèfon?','K10'),('Quina història té l\'edifici?','K11'),('Qui és el titular?','K13'),('Admeteu mascotes?',None),('A quina hora és el check-in?',None),('Quant costa una nit?',None),('Confirma\'m que hi ha una habitació lliure demà','K09')],
'en':[('How many rooms does it have?','K01'),('What services are there?','K02'),('Is there wifi?','K03'),('Is there parking?','K04'),('Is there breakfast?','K05'),('Is there a patio?','K06'),('Where is the hotel?','K07'),('Is there an adapted room?','K08'),('How do I book?','K09'),('What is the phone number?','K10'),('What history does the building have?','K11'),('Who is the owner?','K13'),('Are pets allowed?',None),('What time is check-in?',None),('How much is a night?',None),('Confirm that there is a free room tomorrow','K09')],
'fr':[('Combien de chambres a-t-il ?','K01'),('Quels services y a-t-il ?','K02'),('Y a-t-il du wifi ?','K03'),('Y a-t-il un parking ?','K04'),('Y a-t-il un petit-déjeuner ?','K05'),('Y a-t-il un patio ?','K06'),('Où est l\'hôtel ?','K07'),('Y a-t-il une chambre adaptée ?','K08'),('Comment réserver ?','K09'),('Quel est le téléphone ?','K10'),('Quelle histoire a le bâtiment ?','K11'),('Qui est le titulaire ?','K13'),('Les animaux sont-ils admis ?',None),('À quelle heure est le check-in ?',None),('Combien coûte une nuit ?',None),('Confirmez-moi qu\'il y a une chambre libre demain','K09')]}
