import streamlit as st
import google.generativeai as genai

# Configura la API key (puedes guardarla en un secreto de Streamlit Cloud)
genai.configure(api_key=st.secrets["GOOGLE_API_KEY"])

# Define el modelo que usarás (el que ya te funcionó)
model = genai.GenerativeModel('gemini-1.5-flash-latest')

# --- Interfaz de la aplicación ---
st.title("Experto en Principios y Organizacion del Escultismo de Venezuela")
st.write("Hazme una pregunta sobre los Principios y la Organización de la Asociación de Scouts de Venezuela.")

# Define el prompt
# Aquí es donde le das toda la información.
prompt = f"""
Eres un experto en la historia y organización de la Asociación de Scouts de Venezuela. Tu tarea es responder a las preguntas de los usuarios basándote únicamente en el siguiente texto de referencia. No inventes información. Si la respuesta no está en el texto, di "No tengo la información para responder esa pregunta".

---
[

PRINCIPIOS Y ORGANIZACIÓN DE LA ASOCIACIÓN DE SCOUTS DE VENEZUELA

CAPÍTULO I INSTITUCIONALIDAD
Artículo 1. La Institución se denomina ASOCIACIÓN DE SCOUTS DE VENEZUELA. Es una asociación civil sin fines de lucro, con personería jurídica propia, conforme al Acta Constitutiva de fecha 15 de febrero de 1937, inscrita en la Oficina Subalterna del Primer Circuito de Registro del Departamento Libertador del Distrito Federal, bajo el N° 71, Tomo 2, Protocolo Primero, ahora Registro Inmobiliario del Primer Circuito del Municipio Libertador del Distrito Capital. Sus estatutos son los aprobados por la Asamblea Nacional Scout y los Reglamentos promulgados por el Consejo Nacional Scout. Su representación legal recae en el Consejo Nacional Scout, quien a través del Director Ejecutivo Nacional llevará a cabo las actuaciones que correspondan en las instancias gubernamentales, públicas, privadas y judiciales.
Artículo 2. Su duración será de cien (100) años, contados a partir de la fecha de registro de estos estatutos por ante la Oficina de Registro Respectiva. Dicho plazo podrá ser prorrogado por periodos iguales, mayores o menores, según lo disponga la Asamblea Nacional Scout.
Artículo 3. La Asociación de Scouts de Venezuela, antes “Federación de Boys Scouts (Exploradores) de Venezuela” como heredera de la Tropa San Sebastián, fundada en Maracaibo el 27 de mayo de 1913 por Ramón Ocando Pérez, es la única organización en el país, reconocida y aprobada por la Conferencia Scout Mundial como miembro de la Organización Mundial del Movimiento Scout.
Artículo 4. El nombre Asociación de Scouts de Venezuela y su emblema están registrados como denominación comercial en el Registro de la Propiedad Industrial del antes Ministerio de Fomento, bajo el N° 10832-D, en el Libro 5°, Tomo XXVII-F-147, en fecha 1 de octubre de 1973.
Se cuenta con un logo definido como un elemento gráfico que consiste en la desconceptualización de la Flor de Lis Mundial Scout, de manera abstracta e inorgánica, conformada por tres elementos separados uno del otro, de colores amarillo, azul y rojo. Al lado derecho del elemento gráfico se leen las palabras SCOUTS y VENEZUELA, colocadas la primera sobre la segunda, utilizando letras curvas, en color negro. El cual se encuentra registrado como denominación comercial en el Servicio Autónomo de la Propiedad Industrial (SAPI) del Ministerio de Producción y Comercio según solicitud registrada bajo el N° 04-012537.
Se utiliza adicionalmente como emblema la Flor de Lis con los colores nacionales en sus tres pétalos, conteniendo en los pétalos laterales dos estrellas de 5 puntas, y debajo de ella la leyenda “Siempre Listo”.
La Asociación de Scouts de Venezuela reconoce como Marca Scout Mundial, el elemento gráfico propio

de la Organización Mundial del Movimiento Scout, protegido internacionalmente, bajo las premisas que
Principios y Organización de la Asociación de Scouts de Venezuela

esta considera para su diseño y como marca a utilizar en el país reconoce dicho elemento gráfico con la inclusión de la palabra VENEZUELA.
Artículo 5. El domicilio legal de la Asociación de Scouts de Venezuela y sede de su Consejo Nacional Scout, es el Edificio Askain, piso 1, oficina 1-l. Chacaito. Urbanización El Rosal en la ciudad de Caracas, capital de la República Bolivariana de Venezuela, pudiendo celebrar actos y establecer oficinas temporales o permanentes en cualquier lugar del territorio nacional. El alcance de la organización es todo el territorio de la República Bolivariana de Venezuela.
Artículo 6. La Asociación de Scouts de Venezuela, es una organización apolítica, voluntaria, formada por niñas, niños, adolescentes, jóvenes y adultos de cualquier género, origen, raza y credo, inspirados en los ideales del Movimiento Scout Mundial fundado por Lord Baden Powell de Gilwell.
La Misión del Movimiento Scout, es contribuir a la educación de las niñas, niños, adolescentes y jóvenes, mediante un sistema de valores basado en la Promesa y Ley Scout, ayudar a la construcción de un mundo mejor donde la gente esté realizada como individuo y juegue un papel constructivo en la sociedad.
Esto se logra:

•    Involucrándolos a lo largo de sus años de formación en un proceso educativo no formal;

•	Empleando un método específico que convierte a cada individuo en el principal agente de su desarrollo como persona independiente, colaboradora, responsable y comprometida;
•	Ayudándolos a establecer un sistema de valores basado en principios espirituales, sociales y personales como se expresa en la Promesa y Ley.
Artículo 7. Los Propósitos u objeto de la Asociación son:

a)  Contribuir a la educación de niñas, niños, adolescentes y jóvenes mediante un sistema de autoeducación progresiva basado en un sistema de valores y sustentado en  un Proyecto Educativo que es revisado y actualizado de manera periódica;
b)  Coadyuvar a los padres, representantes, educadores y a la comunidad, en la gestión formativa de niñas, niños, adolescentes y jóvenes de uno u otro sexo, a su cuidado;
c)  Contribuir al mejoramiento de la sociedad en la que actúa, aportando individuos líderes capaces de vivir dentro de ella y orientarla;
d)  Captar adultos de buena voluntad para que, a través de un proceso de  formación,  promuevan el    Método   Scout   a   cuantas   niñas,   niños,   adolescentes   y   jóvenes   quieran   recibirlo voluntariamente;
e)  Impartir  educación  no formal mediante el  Método  Scout,  como  sistema  de  autoeducación progresiva según:
•   Una Promesa y una Ley basada en valores;

•   Aprendizaje por la acción;

Principios y Organización de la Asociación de Scouts de Venezuela

•   Participación en pequeños grupos;

•   Apoyo de adulto facilitador y motivante;

•   Programas progresivos y estimulantes;

•   Marcos simbólicos;

•   Vida al aire libre;

•   Involucramiento Comunitario.

f)   Velar por la preservación de la pureza de los Principios y el Método del Escultismo;

g)  Diseñar, implantar, evaluar acciones y programas orientados a la prevención integral en materia de drogas y comportamientos adictivos mediante el desarrollo del programa de jóvenes;
h)  Representar a la Organización Mundial del Movimiento Scout en el país.

Artículo 8. La norma de vida de los miembros de la Asociación de Scouts de Venezuela está basada en la Promesa y Ley Scout, aplicadas en cada nivel de la estructura y en principio por lo contemplado en el ordenamiento jurídico nacional.
PRINCIPIOS

El Movimiento Scout está fundado sobre los siguientes principios:

Deber para con Dios: La adhesión a los principios espirituales, la fidelidad a la religión que los expresa, y la aceptación de los deberes que de ellos emanan.
Deber para con los demás: La lealtad para con su país dentro de la perspectiva de la paz, de la comprensión y la cooperación en el plano local, nacional e internacional. La participación en el desarrollo de la sociedad dentro del respeto a la dignidad del hombre y a la integridad de la naturaleza.
Deber para consigo mismo: La responsabilidad de su propio desarrollo. ADHESIÓN A UNA PROMESA Y UNA LEY
Todos los miembros del Movimiento Scout deben adhesión a una Promesa y una Ley que refleje, el deber para con Dios, el deber para con los demás, y el deber hacia consigo mismo, inspirados en la Promesa y la Ley concebidas por el Fundador del Movimiento Scout, en los siguientes términos:
La Promesa Scout: Por mi honor y con la ayuda de Dios me obligo a servir lo mejor que pueda a mi iglesia y a mi patria, a ayudar a mi prójimo en cualquier circunstancia, y a cumplir la Ley Scout.
La Ley Scout

1.  El scout cifra su honor en merecer confianza.

2.  El scout es leal.

3.  El scout servicial.

4.  El scout es amigo de todos y hermano de cualquier otro scout.

5.  El Scout es cortés.

6.  El Scout ve en la naturaleza la obra de Dios, la cuida y la protege.

7.  El Scout obedece a conciencia, es trabajador y perseverante.
Principios y Organización de la Asociación de Scouts de Venezuela

8.  El Scout sonríe y canta en sus dificultades.

9.  El Scout es ahorrativo, cuida y respeta el bien ajeno.

10. El Scout es puro de pensamiento, palabra y obra.

Artículo 9. A salvo del Peligro: la Asociación de Scouts de Venezuela promueve que existan políticas y procedimientos para garantizar un entorno seguro para niños, jóvenes y adultos.
Artículo 10. El patrimonio de la Asociación de Scouts de Venezuela está conformado por: Los aportes de sus asociados y por los bienes que formen parte de su inventario inicial. A él, se sumarán los que adquiera en lo sucesivo por cualesquier títulos y los recursos que obtenga de manera lícita por:
a)   Contribuciones de empresas o entidades para el cumplimiento del objeto de la Asociación;

b)   Contribuciones otorgadas por entes oficiales, sean municipales, estadales o nacionales;

c)   Donaciones, herencias, legados o subvenciones;

d)   Rentas e intereses que provengan de sus bienes actuales y/o futuros;

e)	Aportes específicos recibidos de terceros, con arreglo a las disposiciones legales aplicables, armónicos con las actividades y fines de la Asociación;
f)    Contribuciones recibidas de instituciones o personas residentes en el extranjero;

g)	Derechos por el uso de la marca scout; Derechos de autor que  eventualmente pudieran corresponder por obras a cuya edición contribuya.
h)   Los Bienes pertenecientes a Grupos, Distritos o Regiones Scouts que cesen en sus funciones;

i)	El buen nombre e imagen de la Asociación de Scouts de Venezuela adquirido por la tradición de ser la Institución Juvenil más antigua de Venezuela y todos sus miembros obligados a preservar este bien intangible;
j)    Todos los documentos, manuales, programas y proyectos realizados por los Miembros de la

Asociación Scout de Venezuela;

k)	Las asignaciones correspondientes a Proyectos de Financiamiento con instituciones públicas, privadas, nacionales o extranjeras.
Parágrafo Primero: En ningún caso las ganancias, beneficios de cualquier naturaleza o parte alguna del patrimonio de la Asociación de Scouts de Venezuela puede ser distribuida a sus fundadores, asociados o miembros y no se realizará pago alguno a título de reparto de utilidades o de patrimonio. Parágrafo Segundo: El patrimonio de la Asociación de Scouts de Venezuela, en caso de liquidación de esta, será traspasado a una o varias asociaciones civiles sin fines de lucro, cuyos objetivos y propósitos giren en torno al desarrollo educativo de la juventud venezolana y sean coincidentes con los Principios Fundamentales del Movimiento Scout.
Artículo 11. La Asociación de Scouts de Venezuela tiene el derecho exclusivo de usar el nombre, los emblemas, distintivos, insignias, condecoraciones, uniformes, método, programas, lemas, términos y literatura propios del Movimiento Scout Mundial en el territorio nacional. Por lo tanto, sus miembros son Principios y Organización de la Asociación de Scouts de Venezuela

los únicos autorizados para practicar el Escultismo ideado por Lord Baden Powell de Gilwell, y para adquirir, usar y portar dentro y fuera del territorio de la República, los uniformes, insignias, distintivos, emblemas y cualquier otra identificación que les sean propias.
Artículo 12. La Asociación de Scouts de Venezuela, manifiesta su aceptación a las disposiciones establecidas en la Constitución de la Organización Mundial del Movimiento Scout, así como su apoyo a la política general de la Organización comprometiéndose a adecuar sus ordenamientos ante cualquier modificación que así lo amerite.
Artículo 13. La disolución o cierre de la Asociación de Scouts de Venezuela será decidida por la Asamblea Nacional Scout y deberá contar con al menos el 75% de los delegados de la Asamblea Nacional Scout.
Artículo 14. La Oficina Scout Nacional (OSN), es el centro de operaciones y de servicio de la Asociación. A través de ella operan el Consejo Nacional Scout, la Dirección Ejecutiva Nacional y las áreas de gestión bajo su responsabilidad, las Comisiones Nacionales, y otros órganos de carácter nacional. Asimismo, allí reposan todos los documentos de la Institución, libros contables, soportes, libros, registros diversos, entre otros. La OSN estará bajo la inmediata responsabilidad del Director Ejecutivo Nacional.
Parágrafo único: El Consejo Nacional Scout, de acuerdo con propuesta del Director Ejecutivo Nacional, podrá establecer oficinas de la OSN en cualquier lugar del territorio nacional. De igual manera, en aras de un mejor funcionamiento podrá descentralizar las tareas propias de sus áreas de gestión en dichas oficinas de la OSN o en las Regiones Scouts.
Artículo 15. Los Principios y Organización tienen como ámbito de aplicación todas las estructuras e instancias de la Asociación de Scouts de Venezuela. Sus disposiciones son de obligatorio cumplimiento por todos los miembros e instancias de la institución y su incumplimiento deriva en la aplicación de las sanciones y medidas establecidas en el reglamento correspondiente.

CAPÍTULO II MIEMBROS
Artículo 16. Los miembros de la Asociación de Scouts de Venezuela son:

a)  Miembros Activos Jóvenes:

•   Las niñas, niños, adolescentes y jóvenes, de uno u otro sexo, que  pertenezcan a

          Unidades o Grupos Scouts registrados en la Asociación de Scouts de Venezuela. b)  Miembros Activos Adultos:
•   Los adultos registrados en Unidades o Grupos de la Asociación de Scouts de Venezuela;

•	Las personas nombradas o elegidas para cargos nacionales, regionales o distritales debidamente registrados en la Asociación de Scouts de Venezuela;
•   Los  adultos  colaboradores  de  los  Grupos  Scouts  en  la  Asociación  de  Scouts  de


Principios y Organización de la Asociación de Scouts de Venezuela

Venezuela;

•	Los miembros de los organismos o grupos ciudadanos patrocinantes de Grupos Scout registrados en la Asociación de Scouts de Venezuela;
•	Todos aquellos a quienes el Consejo Nacional Scout, por iniciativa propia o en consulta con los Consejos Regionales, designen para prestar su colaboración en tareas específicas.
c)  Miembros honorarios:

•	La persona propuesta por el Consejo Nacional Scout, por la Asamblea Nacional Scout, por los Distritos y Grupos Scouts, así como aquella persona que por iniciativa propia lo solicite. Todo lo anterior en atención a servicios prestados a la comunidad en beneficio del bien común o a la Asociación de Scouts de Venezuela en cualquier instancia dentro del marco de los establecido en nuestra Promesa y Ley Scout, así como en los procesos de formación que se persiguen con las niñas, niños, adolescentes y jóvenes en general. En todos los casos el Consejo Nacional Scout decidirá la aceptación con base a la acreditación del proponente.
Artículo 17. Los miembros adultos activos de la Asociación, a excepción de los honorarios, deberán procurar el nivel mínimo de formación correspondiente a la instancia en la que desarrolla su rol, en concordancia con la Política Nacional del área de Adultos.
Artículo 18. Sólo podrán ser seleccionados para desempeñar cargos institucionales de Dirección, aquellos adultos registrados en la Asociación de Scouts de Venezuela, que hayan obtenido el nivel mínimo de formación necesario para ejercer el cargo para el cual se concursa. En caso de no pertenecer a la Asociación de Scouts de Venezuela o poseer la formación mínima requerida, el candidato debe comprometerse a regularizar ambos procesos en un plazo no mayor de un (1) año.
Artículo 19. El Consejo Nacional Scout (CNS) de la Asociación de Scouts de Venezuela, podrá nombrar un Presidente honorario a los efectos de promover la imagen y misión del Movimiento Scout o desarrollar alguna representación particular, cuyas funciones específicas serán definidas por el CNS, sin menoscabo de las funciones y atribuciones del Presidente del CNS.
Artículo 20. La condición de miembro de la Asociación de Scouts de Venezuela se demuestra por medio del sistema de registro institucional de la Asociación de Scouts de Venezuela.
Artículo 21. La condición de miembro de la Asociación de Scouts de Venezuela se pierde por:

a)       No renovar su inscripción anual obligatoria en el sistema de registro institucional  de la

Asociación de Scouts de Venezuela;

b)	Cuando a pesar de haber cumplido con lo establecido en el aparte “a” de este Artículo se haya evidenciado inconsistencia en la naturaleza de los datos de registro proporcionados, ya sea para la inscripción o renovación de esta en el sistema de registro institucional de la Asociación Principios y Organización de la Asociación de Scouts de Venezuela

de Scouts de Venezuela;

c)       Renuncia escrita a la condición de miembro de la Asociación de Scouts de Venezuela;

d)	Decisión firme de cualquiera de las instancias de la estructura Scout que ejerzan funciones de convivencia o por sentencia definitivamente firme en cualquier instancia o materia judicial. La pérdida de condición de miembro bajo este literal es de carácter permanente;
e)       Al cesar en las funciones que lo cualificaban para ser miembro honorario;

f)	Por falta de probidad y/o atentar contra los intereses y el patrimonio de la asociación, respetando siempre el derecho a la defensa y al debido proceso.
Parágrafo Primero: Todo lo anterior deberá llevarse a cabo siempre y en todo momento dentro del marco  de  nuestra  Ley  y  Promesa  Scout,  en consonancia  con  los  Principios  y  Organización, reglamentos, documentos y políticas de la Asociación de Scouts de Venezuela y las leyes de la República Bolivariana de Venezuela, respetando todas las garantías constitucionales.
Parágrafo Segundo: La Asociación de Scouts de Venezuela y, por ende, ninguna instancia de esta puede pasar por encima de las decisiones de ningún tribunal de la República Bolivariana de Venezuela ni permitir procesos que contravengan las leyes y decisiones de los tribunales del país.
Artículo  22.  La  condición  de  miembro  de  la  Asociación  de  Scouts  de  Venezuela  se  suspende temporalmente por:
a)	Haber evidenciado falsedad en la naturaleza de los datos de registro proporcionados, ya sea para la inscripción o renovación de esta en el sistema de registro institucional de la Asociación de Scouts de Venezuela;
b)	Estar incurso al menos en calidad de imputado en un proceso judicial en materia penal, o de investigado en proceso por violación de disposiciones establecidas en la Ley Orgánica de Protección del Niño, Niña y Adolescente, ante los organismos de la República Bolivariana de Venezuela;
c)     Por decisión firme de una instancia de convivencia, en función de la aplicación de una sanción. d)     Renuncia al cargo para el cual fue designado o electo, quedando sin ningún otro bajo el cual
cumpla un rol dentro de la estructura.

Parágrafo Primero: La condición de miembro se restablece al momento de la corrección de los datos en el literal “a” del presente Artículo y que dicha corrección sea avalada por el área responsable de Registro Scout Nacional; al igual que para el caso del literal “d”, donde la restitución de la membresía se llevará a efecto al momento en se cuente con un nuevo cargo dentro de la institución. En el caso del literal “b” se restituye la condición de miembro al finalizar la investigación y que la persona involucrada demuestre ante el Consejo del nivel correspondiente su absolución por escrito emanada del ente correspondiente.
Parágrafo Segundo: En el caso del literal “b”, en procura de salvaguardar el interés superior del

Principios y Organización de la Asociación de Scouts de Venezuela

niño y la reputación de la Institución, todo miembro activo de la Asociación de Scouts de Venezuela que se encuentre inmerso en una averiguación de tipo penal o de Protección de Niños, Niñas y Adolescentes, será retirado de sus actividades scouts, reincorporándose con todos sus derechos y obligaciones tan pronto demuestre por escrito ante el Consejo respectivo la resolución del caso a su favor.
Artículo 23. El período de vigencia del Registro Institucional tendrá una duración de un año, pudiendo realizar el mismo en cualquier época del año desde el 01 de enero al 31 de diciembre de cada año, teniendo que realizar su renovación antes de la fecha tope de caducidad de este.

CAPÍTULO III ASAMBLEA NACIONAL SCOUT
Artículo 24. La Asamblea Nacional Scout es el máximo organismo deliberativo y de elección de la

Asociación de Scouts de Venezuela y se reunirá en sesiones ordinarias una vez al año. La Asamblea Nacional Scout estará integrada por:
1.  Delegados con derecho a voz y voto:

a.  Los miembros electos del Consejo Nacional Scout electos por una Asamblea Nacional

Scout;

b.  Dos (02) miembros delegados del Comité Consultivo;

c.   Los Comisionados de Distritos Oficiales;

d.  Los Jefes o Sub-Jefes de todos los Grupos Scouts registrados en la Asociación de Scouts de Venezuela, que cuenten con todas las unidades registradas en al menos 25% de la membresía ideal;
e.  Un delegado adicional electo por cada Distrito Scout Oficial y registrado en la Asociación de Scouts de Venezuela en alguno de los grupos que conforman el Distrito, siempre que este cuente con al menos doscientos cincuenta (250) miembros activos jóvenes registrados en la Asociación de Scouts de Venezuela .
2.  Observadores con derecho a voz:

a.  Los Comisionados de Distrito designados;

b.  El Director Ejecutivo Nacional;

c.   El Comisionado Internacional;

d.  Los Coordinadores Nacionales de la Red de Jóvenes;

e.  El Contralor Nacional;

f.   El Consultor Jurídico;

g.  Los Directores Nacionales;

h.  Los Cooperadores Nacionales;

i.    Los Comisionados Regionales;
Principios y Organización de la Asociación de Scouts de Venezuela

j.    Los Asistentes y Cooperadores Regionales;

k.   Los Adultos de la Institución debidamente registrados y acreditados por una Asamblea

Distrital;

l.    Personas, instituciones o comisiones invitadas por el Consejo Nacional Scout.

Parágrafo Único: Jefes o Subjefes de Grupos Scouts y los Comisionados de Distritos tienen derecho a voto, siempre que hayan entregado al Director Ejecutivo Nacional el Informe Anual de Gestión y el Informe Financiero del Grupo Scout, correspondiente al año precedente, dentro del lapso establecido para ello.
Artículo 25. El quórum de la Asamblea Nacional Scout lo constituye:

a)  Los miembros del Consejo Nacional Scout que estén presentes, y

b)  La mitad más uno de los representantes señalados en los incisos 1.c, 1.d y 1.e del Artículo anterior, tomados en conjunto.
Parágrafo Único: Si el día y hora de la instalación, se determina que no existe quórum, se llamará a una nueva sesión para dentro de las dos horas siguientes y en esta ocasión la Asamblea Nacional Scout sesionará con los delegados presentes. La Asamblea Nacional Scout así constituida podrá deliberar y tomar decisiones sobre los puntos contenidos en la agenda, con excepción de aquellos relacionados con propuestas para la modificación de los Principios y Organización.
Artículo 26. Son funciones y atribuciones de la Asamblea Nacional Scout:

a)   Trazar las políticas y directrices de la Asociación de Scouts de Venezuela;

b)	Modificar los Principios y Organización en sus partes Primera y Segunda, de conformidad con las disposiciones contenidas en el Artículo 94 de los Principios y Organización de la Asociación de Scouts de Venezuela;
c)	Elegir a los miembros del Consejo Nacional Scout por períodos de tres (3) años. Ningún miembro electo permanecerá en funciones por más de seis (6) años consecutivos, retirándose un tercio de ellos en cada Asamblea Nacional Scout ordinaria. En caso de ausencias absolutas, la siguiente Asamblea Nacional Scout ordinaria o extraordinaria elegirá a los miembros para completar el período. Este período no se contará como parte del período máximo estatutario de seis (6) años; la Asamblea Nacional Scout determina la calificación de ausencia absoluta;
d)   Aprobar o improbar la Gestión de las áreas estratégicas presentadas por el Consejo Nacional

Scout;

e)   Aprobar o improbar los Estados Financieros auditados de la Asociación de Scouts de Venezuela;

f)    Las que tenga a bien atribuirse a sí misma, respetando las normativas vigentes.

Parágrafo Único: En caso de ser improbada una Gestión, el Director de Área

correspondiente pondrá su cargo a la orden, pudiendo ser ratificado o removido por el Director

Ejecutivo Nacional.

Principios y Organización de la Asociación de Scouts de Venezuela

Artículo 27. La Asamblea Nacional Scout se reunirá de manera presencial, virtual o mixta en sesiones ordinarias en el primer trimestre de cada año. La convocatoria será realizada por el Consejo Nacional Scout el cual fijará fecha, lugar y modalidad con un mínimo de sesenta (60) días calendario de anticipación
Artículo 28. Para el nombramiento de delegados y observadores a la Asamblea Nacional Scout Ordinaria se tomará como base el Registro Nacional de los Grupos al  31 de diciembre del año precedente.
Artículo 29. La Asamblea Nacional Scout se reúne en sesiones extraordinarias cuando sea convocada por:
a)     El Consejo Nacional Scout, o

b)     La mitad más uno de los Consejos de Distritos oficiales, debiendo presentar la solicitud ante el

Consejo Nacional Scout a los efectos respectivos.

La convocatoria se hará con un mínimo de cuarenta y cinco (45) días calendario de anticipación, informando a los participantes los motivos de la convocatoria, así como la fecha, hora y modalidad de su realización. Para las Asambleas Nacionales Scout Extraordinarias se tomará como base el corte acumulado del Registro Nacional de los Grupos Scouts en la Asociación de Scouts de Venezuela , noventa (90) días calendario antes de la celebración de esta.

CAPÍTULO IV CONSEJO NACIONAL SCOUT
Artículo 30. El Consejo Nacional Scout es el máximo organismo directivo de la Asociación de Scouts de Venezuela. Está integrado por:
a)     Nueve (9) miembros electos por la Asamblea Nacional Scout, conforme se determina en el

Artículo 24 literal “c”, con derecho a voz y voto;

b)	Dos (2) miembros jóvenes electos por el Foro Nacional de Participación Juvenil o evento similar, para ser los Coordinadores Nacionales de la Red de Jóvenes, conforme se determina en los Estatutos Generales de la Red de Jóvenes de la Asociación de Scouts de Venezuela, con derecho a voz y voto;
c)     El Director Ejecutivo Nacional, designado por el Consejo Nacional Scout, con derecho a voz;

   d)     El Comisionado Internacional, designado por el Consejo Nacional Scout, con derecho a voz. Los miembros del Consejo Nacional Scout electos tanto por la Asamblea Nacional Scout como por el Foro Nacional de Participación Juvenil se incorporarán al finalizar los eventos en donde fueron electos. La vacante, absoluta o temporal, de un miembro electo del Consejo Nacional Scout señalado en el literal “a” solo podrá ser cubierta por el voto que emita la próxima Asamblea Nacional Scout. Para el caso de los miembros indicados en el literal “b”, los mismos serán reemplazados según lo establecido en los
estatutos generales de la Red de Jóvenes de la Asociación de Scouts de Venezuela (para el caso de los
Principios y Organización de la Asociación de Scouts de Venezuela

coordinadores nacionales).

Paragrafo primero: En cuanto a la ausencia temporal de algún miembro del Consejo Nacional Scout se determinará con base a por lo menos dos (2) inasistencias consecutivas a las sesiones del Consejo Nacional Scout sin causa justificada.
Parágrafo segundo: En caso de que las vacantes de los miembros electos indicados en el literal “a” sean más de la mitad más uno, se convocará a una Asamblea Nacional Scout Extraordinaria. La mitad más uno señalada en este Parágrafo se calculará en función del número total de miembros electos activos indicados en el literal “a” que forman la instancia. Si el número total es par, la mitad más uno de los miembros se calculará de manera directa; para el caso de un número total impar de miembros, se calculará la mitad más uno de estos, considerando como base del cálculo el número par inmediatamente anterior al total de miembros electos activos indicados en el literal “a”.
Parágrafo tercero: El Consejo Nacional Scout podrá invitar a sus sesiones a quien considere necesario, con el propósito de coadyuvar a su labor, cuya participación tendrá derecho a voz.
Artículo 31. El quórum de las reuniones del Consejo Nacional Scout lo constituye la mitad más uno de los miembros electos activos indicados en el literal “a” del artículo 30. La mitad más uno para el establecimiento del quórum del Consejo Nacional Scout se calculará en función del número total de los miembros electos activos indicados en el literal “a” que forman la instancia. Si el número total es par, la mitad más uno de los miembros se calculará de manera directa; para el caso de un número total impar de miembros, se calculará la mitad más uno de estos, considerando como base del cálculo el número par inmediatamente anterior al total de miembros electos activos indicados en el literal “a”.
Parágrafo Primero: Las decisiones del Consejo Nacional Scout se tomarán por mayoría simple de los votos emitidos por los miembros electos activos indicados en los literales “a” y “b”, salvo aquellas establecidas en los Principios y Organización que indiquen lo contrario.
Parágrafo Segundo: En caso de que un miembro electo del Consejo Nacional Scout, pierda la condición de miembro de la Asociación de Scouts de Venezuela de manera definitiva o temporal, el total a considerar será el de los miembros electos y activos dentro de la Asociación de Scouts de Venezuela hasta tanto se subsane la vacante.
Artículo 32. El Consejo Nacional Scout se reúne en forma física en cualquier parte del territorio nacional o  en  modalidad virtual, cuantas  veces sea convocado  por  el Presidente  o  por  delegación  en  el Vicepresidente, o a solicitud de la mitad más uno de los miembros electos activos del CNS indicados en el literal “a” del artículo 30; para que la reunión sea válida debe cumplirse con el quórum establecido en el Artículo 31.
Artículo 33. Son funciones y atribuciones del Consejo Nacional Scout:

a)    Ejecutar  los  mandatos  y  resoluciones  de  la  Asamblea  Nacional  Scout  y  velar  por  su

Principios y Organización de la Asociación de Scouts de Venezuela

cumplimiento;

b)    Evaluar las recomendaciones que efectúe la Asamblea Nacional Scout;

c)	Designar por y entre los miembros electos por una Asamblea Nacional Scout, al Presidente-Jefe Scout Nacional y Vicepresidente, al Tesorero y al Sub-Tesorero de su seno. El Vicepresidente y el Sub-Tesorero llenarán las ausencias temporales o absolutas del Presidente-Jefe Scout y del Tesorero respectivamente;
d)    Nombrar y reemplazar al Director Ejecutivo Nacional; e)    Nombrar y reemplazar al Comisionado Internacional; f)     Nombrar y reemplazar al Contralor Nacional;
g)	Definir e implementar los Objetivos, Metas, Programas y Plan Nacional de Desarrollo que deben presentarse anualmente a la Asamblea Nacional Scout, con los  ajustes  derivados de su aplicación, año tras año;
h)	Crear organismos nacionales de asesoría y operación, establecer sus características y formas de procedimiento en el Reglamento Nacional de Funcionamiento, y designar a sus integrantes;
i)	Crear Regiones y Distritos Scout y delimitarles su jurisdicción; así como cualquier modificación que se pudiera presentar a posterior;
j)	Velar por el proceso de Registro de las Unidades y Grupos Scout y por el cumplimiento de las condiciones establecidas. Autorizar registros de grupos scouts y unidades complementarias, así como suspender o cancelar los mismos por incumplimientos de los Principios, Propósitos de la institución o contravenir las condiciones establecidas para el Registro Institucional;
k)    Presentar a la Asamblea Nacional Scout candidatos para el Consejo Nacional Scout:

l)	Presentar ante la Asamblea Nacional Scout a los miembros del comité de escrutinios para su validación;
m)   Dictar  e  interpretar  los  reglamentos  operativos  de  la  tercera  parte  de  los  Principios  y

Organización;

n)    Aceptar la renuncia de sus miembros;

o)	Otorgar a cualquiera de  los miembros del Consejo  Nacional Scout, poderes  generales y especiales, judiciales o extrajudiciales, con las facultades que le son propias al Consejo Nacional Scout;
p)	Fijar la política general que habrá de seguir la Asociación de Scouts de Venezuela en cuanto a la disposición o administración de sus bienes y velar por su cumplimiento;
q)	Resolver sobre la compra y venta de inmuebles, y en general, sobre las inversiones de carácter permanente;
r)	Ejecutar de manera directa o por medio de la designación que este considere, cualquier acto de disposición y administración que considere conveniente, a nombre de la Asociación de
Principios y Organización de la Asociación de Scouts de Venezuela

Scouts de Venezuela;

s)	Delegar, si así lo considera conveniente, en el Director Ejecutivo Nacional el ejercicio de las facultades de disposición y administración que estime apropiadas;
t)	Corresponden al Consejo Nacional Scout, los más amplios poderes de disposición y administración;
u)    Las demás que le atribuya los Principios y Organización.

Artículo 34. El Presidente del Consejo Nacional Scout – Jefe Scout Nacional de la Asociación de Scouts de Venezuela, tendrá las siguientes funciones y atribuciones:
a)   Presidir la Asamblea Nacional Scout ordinaria y extraordinaria;

b)   Convocar y presidir las sesiones del Consejo Nacional Scout;

c)   Refrendar con su firma los acuerdos, decisiones y proposiciones del Consejo Nacional Scout;

d)   Ejercer las demás atribuciones que le correspondan según los Principios y Organización y el

Reglamento Nacional de Funcionamiento.

Artículo 35. Las atribuciones de cada uno de los miembros del Consejo Nacional Scout son determinadas en el Reglamento Nacional de Funcionamiento.
Artículo 36. El Director Ejecutivo Nacional es la autoridad ejecutiva nacional sobre los asuntos diarios de la Asociación de Scouts de Venezuela y goza de autonomía operativa y funcional. Del ejercicio de sus funciones rinde cuentas al Consejo Nacional Scout.
Artículo 37. El cargo de Director Ejecutivo Nacional puede ser desempeñado por un profesional remunerado o no, debidamente calificado.
Artículo 38. Son funciones y atribuciones del Director Ejecutivo Nacional:

a)     Llevar la gestión diaria de la Asociación de Scouts de Venezuela;

b)	Ejercer las facultades de administración y disposición que el Consejo Nacional Scout le delegue;
c)	Ejercer la representación legal de la Asociación de Scouts de Venezuela ante las autoridades civiles, militares, judiciales, así como ante instituciones públicas y privadas.
d)	Otorgar Poderes de representación para velar por los intereses de toda índole de la Asociación de Scouts de Venezuela a quien así considere necesario.
e)	Abrir y cerrar cuentas bancarias, cuentas corrientes y de ahorro, efectuar depósitos a plazos o hacer las colocaciones que mejor beneficien los intereses de la Asociación de Scouts de Venezuela. La movilización de las cuentas bancarias y los actos de disposición de los bienes en efectivo los hace con la supervisión del Tesorero Nacional o Sub-Tesorero o a quien el Consejo Nacional Scout autorice para tal atribución;
f)	Junto con el Tesorero Nacional o Sub-Tesorero o a quien el Consejo Nacional Scout autorice para  la atribución,  puede ejecutar cualquier  otra operación  de naturaleza  financiera  que Principios y Organización de la Asociación de Scouts de Venezuela

demande sus funciones, a excepción del otorgamiento de fianzas o aceptación de obligaciones que comprometan el patrimonio de la Asociación de Scouts de Venezuela, que impliquen la venta o enajenación de los bienes muebles e inmuebles de la Asociación de Scouts de Venezuela;
g)	Mantener  informado  al  Tesorero  Nacional  de  forma  mensual  sobre  los  movimientos administrativos y financieros de la Asociación de Scouts de Venezuela;
h)	Designar a los Directores Nacionales a cargo de las áreas estratégicas de la Asociación de Scouts de Venezuela, así como a sus Cooperadores, voluntarios remunerados o no, debidamente calificados, quienes le estarán subordinados en sus funciones;
i)	Designar al Consultor Jurídico de la Asociación de Scouts de Venezuela, quien le estará subordinado en sus funciones, con aprobación previa del Consejo Nacional Scout;
j)	Designar a los Comisionados Regionales, quienes le estarán subordinados en el ejercicio de sus funciones;
k)	Dirigir la planificación, programación, ejecución y evaluación de los diferentes procesos que inicie la Institución, siguiendo las pautas que establezca la Asamblea Nacional Scout y el Consejo Nacional Scout, dando cuenta a este último;
l)      Recibir o autorizar la recepción de aportes, donativos o patrocinios para la Asociación de

Scouts de Venezuela;

m)	Dirigir al Equipo Operativo Nacional en la definición, programación y evaluación de estrategias de funcionamiento de la Institución;
n)     Promover y autorizar el desarrollo de actividades de autogestión;

o)     Las demás que le señale el Consejo Nacional Scout.

Artículo 39. El cargo de Contralor Nacional será ejercido por un profesional debidamente calificado, remunerado o no, cuya función fundamental está circunscrita al manejo eficiente y efectivo de los recursos inmuebles, muebles y monetarios de la Institución. Su función está enmarcada en el control de uso de los recursos recibidos por la Institución por parte de las diferentes instancias organizativas de la misma y su utilización de acuerdo con las pautas establecidas en la Política de Administración y Finanzas, y en el Manual de Procedimientos Administrativos establecido en consecuencia.
Su dependencia funcional es del Consejo Nacional Scout, el cual lo nombra. Esta persona debe ser mayor de edad, y con profesión y experiencia apropiada para el desempeño de este cargo. Sus funciones están descritas en el Reglamento Nacional de Funcionamiento. Podrá ejercer sus funciones en todo el país, para lo cual podrá nombrar Contralores Regionales de acuerdo con las pautas del Reglamento Nacional de Funcionamiento y sometidos a los procedimientos correspondientes a la materia.
Artículo 40. El cargo de Consultor Jurídico será ejercido por un profesional debidamente calificado y colegiado, remunerado o no, cuya función está relacionada con la representación ante el Estado y los Principios y Organización de la Asociación de Scouts de Venezuela

particulares de la Institución, cuando así lo faculte de manera expresa y directa el Consejo Nacional Scout por medio de acta suscrita por el mismo; velando por los intereses mismos de la Institución, y el cumplimiento de las normas jurídicas establecidas en el Estado de Derecho Venezolano por todos los miembros de la Institución. Su funcionamiento está enmarcado en las pautas indicadas en el Reglamento Nacional de Funcionamiento.
Esta persona debe ser mayor de edad y con profesión de Abogado. Su dependencia funcional es ante el Director Ejecutivo Nacional, el cual lo nombra, con aprobación previa del Consejo Nacional Scout. Pudiendo éste proponer al DEN personas en Distritos y Regiones Scouts para conformar Asesores Legales, a fin de apoyar la labor.
Artículo 41. El Comisionado Internacional tendrá la responsabilidad de representación de la Asociación de Scouts de Venezuela en el exterior ante la OMMS y las OSN que la integran, relativa en todos los asuntos que atañe a la Institución, sus actividades y membresía.
El cargo de Comisionado Internacional, será ejercido por una persona debidamente calificada, remunerado o no, conocedor de las Políticas Mundiales, Regionales y Nacionales de la Asociación de Scouts de Venezuela, cuya función fundamental es la administración eficiente y efectiva de las relaciones entre nuestra Institución y las demás que conforman la OMMS, así como otras asociaciones e instituciones que redunden en beneficios de la formación de jóvenes en todo el mundo.
Su dependencia funcional es ante el Consejo Nacional Scout, el cual lo nombra y lo remueve. De su gestión informará al Consejo Nacional Scout. Esta persona debe ser mayor de edad, preferiblemente profesional y con experiencia apropiada para el desempeño de este cargo.

CAPÍTULO V COMITÉ CONSULTIVO
Artículo 42. El Comité Consultivo está integrado por los Ex-Presidentes y Ex-Vicepresidentes de la Asociación de Scouts de Venezuela. Con excepción de aquellos que hayan sido sujetos a las condiciones establecidas en los literales “c” y “d” del artículo 21 de los Principios y Organización de la Asociación de Scouts de Venezuela.
Artículo 43. El Comité Consultivo elige de su seno a dos (2) delegados registrados que lo representarán, con derecho a voz y voto, en las Asambleas Nacionales Scout Ordinarias y Extraordinarias. Todos los integrantes del Comité Consultivo deberán renovar ante la Oficina Scout Nacional su membresía a fin de poder participar en todos estos procesos.
Artículo 44. El Comité Consultivo se reúne de manera presencial o virtual cada vez que sea convocado por el Consejo Nacional Scout, con la finalidad de someter a su criterio las materias que este último considere conveniente.
Los  dictámenes  del  Comité  Consultivo  sobre  las  materias  sometidas  a  su  consulta  deben  ser

presentados por escrito y estimados por el consultante como una opinión a considerar, haciendo
Principios y Organización de la Asociación de Scouts de Venezuela

referencia a ellos en las actas del organismo. Dichos dictámenes no son vinculantes.

CAPÍTULO VI LA CONVIVENCIA
Artículo 45. La convivencia se fundamentará en los compromisos y prácticas responsables de los miembros de la comunidad scout, propiciando actuaciones coherentes con los Principios Scouts. La convivencia, procurará no solo la interrelación activa y positiva entre los miembros de la Asociación, sino también para con las comunidades, orientada esta relación a promover y concretar una cultura de paz, basada en el compartir y desarrollar la vivencia de valores ciudadanos y democráticos.
Artículo 46. El apego a la disciplina, la moral y el cumplimiento de las directrices y reglamentos por parte de los miembros de la Asociación de Scouts de Venezuela son consideradas, revisadas, atendidas, calificadas, sancionadas y apeladas de conformidad con las disposiciones del Reglamento Scout respectivo, el cual estará orientado en principios educativos y en el interés de garantizar el debido proceso, la inmediatez, la imparcialidad y la celeridad en la búsqueda siempre de la justicia y la preservación del buen nombre e imagen de la Asociación de Scouts de Venezuela y la de sus miembros. Artículo 47. Las instancias responsables de promover y garantizar la convivencia en la Institución, así como la aplicación del Reglamento respectivo, son los Consejos de Grupo, los Consejos de Distrito, Consejos Regionales y el Consejo Nacional Scout, en atención al concepto de ámbito de acción y conforme se establezca en el reglamento correspondiente.
Artículo 48. Las faltas son vistas y sancionadas observando el concepto de territorialidad; cuando la persona a quien se le revise una falta cambie de grupo, Distrito o Región, donde se cometió la misma, el caso será revisado por la instancia superior de las dos instancias (anterior y la actual) en las cuales se ha encontrado la persona reclamada desde el momento en que ocurrieron los hechos y el momento en que se revisan los mismos. De esta acción, la instancia anterior deberá notificar de inmediato a la instancia superior y a la Dirección Ejecutiva Nacional, a los efectos de su control, seguimiento y aseguramiento del debido proceso y de la defensa.
Artículo 49. Los organismos encargados de la administración de la convivencia, si así lo requieren, pueden formar Comisiones Accidentales o Ad Hoc.
Artículo 50. Cualquier persona, actuando como cualquiera de las partes, tiene el derecho de aplicar recursos jerárquicos ante las decisiones, para lo cual podrá recurrir a los mecanismos contemplados en el Reglamento Scout correspondiente, todo ello garantizando el debido proceso.
Parágrafo Único: La Asociación de Scouts de Venezuela no puede pasar por encima de las decisiones de ningún tribunal ni permitir procesos que contravengan las leyes y decisiones de los tribunales de la república
Artículo 51. Cualquier persona debe responder por las acciones que haya cometido en contra del buen

nombre e imagen de la Asociación de Scouts de Venezuela o la de alguno de sus miembros, sea dicha
Principios y Organización de la Asociación de Scouts de Venezuela

persona o no miembro de la institución. Los diferentes niveles de la estructura desarrollarán las acciones que correspondan ante las instancias correspondientes para llevar lo anterior a efecto.

CAPÍTULO VII REGIÓN SCOUT
Artículo 52. El Consejo Nacional Scout establece espacios territoriales que pueden corresponder a los límites político-territoriales de un Estado, denominándose Regiones Scouts; sin embargo, se pueden hacer otros agrupamientos geográficos que contribuyan a la unidad de acción de los Grupos Scouts o unidades en esa jurisdicción y de los Distritos Scouts que la integren. Las Regiones Scouts deben ser conformadas por al menos 2 Distritos Scouts.
Parágrafo único: El Consejo Nacional Scout podrá definir zonas de atención territorial a fin de maximizar la capacidad de soporte y atención, para las cuales la Dirección Ejecutiva Nacional podrá designar el apoyo que esta considere necesario para la ejecución de dicha atención.
Artículo 53. Cada Región Scout está bajo la responsabilidad de un Consejo Regional, presidido por un Comisionado Regional, de rango nacional, voluntario o remunerado, designado y removido por el Director Ejecutivo Nacional.
Parágrafo Único: Para la designación del Comisionado Regional, el Director Ejecutivo Nacional elegirá, de un mínimo de tres (03) y un máximo de cinco (05) candidatos, propuestos por el Consejo Regional correspondiente. El Consejo Regional velará por que cada uno de los candidatos cumpla con los perfiles establecidos por la Dirección Nacional de Adultos, para la ejecución del cargo.
Artículo 54. El Consejo Regional fija su sede, atendiendo a la conveniencia de una mejor comunicación con los Distritos Scout de la jurisdicción.
Artículo 55. El Consejo Regional es el organismo que atiende y coadyuva a los Grupos y Distritos Scouts en la aplicación del Programa Scout, lineamientos y directrices emanados de la Dirección Ejecutiva Nacional, conforme al Plan Nacional de Desarrollo de la Asociación de Scouts de Venezuela; está integrado por:
a)   El Comisionado Regional, designado por el Director Ejecutivo Nacional, con voz y voto;

b)   Los Comisionados de Distrito, electos y designados; con voz y voto;

c)   Los dos (02) miembros de los órganos de representación juvenil, con voz y voto.

d)	Los Asistentes del Comisionado Regional, a razón de uno por cada área de gestión nacional, y los cooperadores regionales que sean necesarios para el cumplimiento de la gestión y el apoyo a los Distritos, con derecho a voz;
e)	El Director Ejecutivo Nacional, cuando tenga a bien participar, lo presidirá y asumirá el voto en sustitución del Comisionado Regional.
Artículo 56. El quórum del Consejo Regional lo constituye:

a)   La mitad más uno de los Comisionados de Distrito electos y designados.
Principios y Organización de la Asociación de Scouts de Venezuela

Para la constitución del quórum debe estar presente el Comisionado Regional o el Director Ejecutivo Nacional o el asistente designado por ellos para que haga sus veces. El quórum de las reuniones del Consejo Regional lo constituye la mitad más uno de sus miembros. Para todos los casos, la mitad más uno se calculará en función del número total de miembros que forman la instancia, constituyéndose la mayoría simple. Si el número total es par, la mitad más uno de los miembros se calculará de manera directa; para el caso de un número total impar de miembros, se calculará la mitad más uno de estos, considerando como base del cálculo el número par inmediatamente anterior al total de miembros. Artículo 57. El Comisionado Regional es un elemento promotor y facilitador, de apoyo y seguimiento, para el trabajo de organización de los Distritos Scout en la visión de apoyo, en la delimitación de su jurisdicción. De su acción reporta al Director Ejecutivo Nacional.
Artículo 58. El Consejo Regional se reúne de manera presencial o virtual por lo menos una vez cada dos  (2) meses,  convocado por  el Comisionado Regional o  quien  haga  sus  veces, o  en reunión extraordinaria a solicitud de la mitad más uno de sus miembros, considerando la mayoría simple indicada en el Artículo 55. Toda decisión debe ser tomada por la mitad más uno, y deben ser asentadas en el acta correspondiente.
Artículo 59. Son funciones y atribuciones del Consejo Regional:

a)  Desarrollar y organizar los Distritos Scouts con las comunidades de su jurisdicción;

b)  Asegurar la ejecución adecuada de los mandatos y resoluciones del Consejo Nacional Scout y la Asamblea Nacional Scout, a través de la Dirección Ejecutiva Nacional;
c)  Revisar, evaluar y aplicar los correctivos correspondientes al Plan anual de la Región, así como enviar semestralmente los informes de gestión de cada área al Director Ejecutivo Nacional;
d)  Enviar mensualmente a la Dirección Ejecutiva Nacional de acuerdo con los procedimientos administrativos, los recaudos necesarios para la emisión de los estados financieros de la Región;
e)  Establecer el Programa Anual de Actividades de la Región, en concordancia con los Propósitos, Metas y Plan Nacional de Desarrollo de la Asociación, sin dejar de prestar atención a los planes o requerimientos propios de los Distritos Scouts y el Ciclo Institucional de Programa de Jóvenes;
f)	Coadyuvar con el registro anual de las Unidades y Grupos Scout y de sus integrantes de acuerdo con las pautas del Registro Institucional;
g)  Coadyuvar en la formulación y evaluación de Proyectos de auto-gestión de los Distritos Scouts; h)  Evaluar la propuesta de proyectos que sugieran la captación de fondos en los Distritos Scouts de su jurisdicción, así como asegurar la debida notificación a la Dirección Ejecutiva Nacional,
para su autorización, en especial, aquellos proyectos que sugieran el uso de la Marca Scout;

i)	Supervisar a través de su asistente regional respectivo o a quien este designe, la captación de fondos de los Distritos Scouts, así como el uso correcto de la Marca Scout;
j)   Presentar  ante  la  Dirección  Ejecutiva  Nacional  su  informe  de  gestión  anual  y  su  plan  y

Principios y Organización de la Asociación de Scouts de Venezuela

presupuesto del siguiente año, de acuerdo con el reglamento de funcionamiento de la Región;

k)  Proponer ante el Director Ejecutivo Nacional un mínimo de tres (03) y un máximo de cinco (05) candidatos a elegir, para la designación del cargo de Comisionado Regional. El Consejo Regional velará por que cada uno de los candidatos cumpla con los perfiles establecidos por la Dirección Nacional de Adultos, para la ejecución del cargo;
l)	Velar por que se mantenga el buen nombre e imagen de la Asociación de Scouts de Venezuela adquirido por la tradición de ser la Institución Juvenil más antigua de Venezuela y todos sus miembros como bien intangible;
m) Las demás que le señale el Reglamento Nacional de Funcionamiento, el Reglamento Nacional de la Región, o que le atribuya los presentes Principios y Organización.
Artículo 60. El Comisionado Regional, voluntario remunerado o no, designado por el Director Ejecutivo Nacional, con base a lo establecido en el Artículo 53, es la primera autoridad ejecutiva a cargo de los asuntos diarios de la Región y la representa ante las autoridades civiles o militares de su Jurisdicción, y en el desempeño de su cargo recibe y pone en práctica las instrucciones que le trasmita el Director Ejecutivo Nacional.
Artículo 61. El Comisionado Regional responde a los lineamientos nacionales en cuanto a metas y objetivos, asegura la debida aplicación del Programa de Jóvenes en su jurisdicción, por lo tanto, no puede ocupar otra posición de línea mientras ejerza su cargo.
Artículo 62. El Comisionado Regional es un elemento promotor y facilitador, de apoyo y seguimiento, para el trabajo de organización de los Distritos Scout en la visión de apoyo en el desarrollo y ejecución de los programas nacionales que deben desarrollar los Distritos y sus grupos scout donde se delimita su jurisdicción. De su gestión y acciones reporta a la Dirección Nacional Ejecutiva como brazo extensor del mismo, llevando a la estructura directrices y lineamientos de organización, formación y de programa para la debida aplicación del programa de jóvenes.
Sus funciones y atribuciones son:

a)     Dar apoyo a los Comisionados de Distrito para el mejor desempeño de sus funciones;

b)	Promover la organización de nuevos Grupos Scouts y Distritos en la zona geográfica designada, juntamente con las comunidades;
c)	Promover la captación y la formación de Adultos Scouts, detectando necesidades a nivel regional y organizar de común acuerdo con los Comisionados de Distrito los cursos que estén previstos en el Esquema de Formación vigente;
d)	Formar el Equipo Regional con: Asistentes, tantos como áreas de gestión nacional existan; Cooperadores Regionales a cargo de tareas específicas; miembros de las distintas Comisiones necesarias para el cumplimiento de la gestión y el debido apoyo a los Distritos;
e)     Convocar, presidir y conducir el Consejo Regional con los Comisionados de Distrito y el

Principios y Organización de la Asociación de Scouts de Venezuela

Equipo Regional;

f)      Mantener frecuente comunicación con el resto del Nivel Nacional;

g)	Responder y coordinar el envío oportuno de los informes financieros y de gestión de cada área a la Dirección Ejecutiva Nacional;
h)	Coordinar los eventos regionales para jóvenes, de común acuerdo con los Comisionados de Distrito, y de conformidad con las necesidades y características de la Región;
i)	Otorgar y Recomendar el otorgamiento de condecoraciones, distinciones y reconocimientos a quienes las merezcan;
j)	Cumplir con los Objetivos de Aprendizaje del Esquema de Formación vigente que ha fijado la Asociación de Scouts de Venezuela y verificar su cumplimiento mínimo para los cargos que así lo requieran en su Región;
k)     Promover el cumplimiento de las metas nacionales a niveles de Grupo, Distrito y Región;

l)	Participar con su equipo regional en los seminarios de formación y actualización de las distintas áreas estratégicas;
m)	Coadyuvar a los Distritos Scouts en la realización de los eventos regionales para los jóvenes, de conformidad con las necesidades y características de la Región;
n)	Crear organismos regionales de asesoría y operación, establecer sus características y formas de procedimiento y designar a sus integrantes;
o)	Atender los Grupos Scouts y unidades complementarias que se encuentren en zonas en expansión conforme a lo indicado en el artículo 54 sobre los espacios territoriales. Los representantes de dichos Grupos y unidades podrán ser invitados al Consejo Regional con derecho a Voz.
p)	Velar por que se mantenga el buen nombre e imagen de la Asociación de Scouts de Venezuela adquirido por la tradición de ser la Institución Juvenil más antigua de Venezuela y todos sus miembros como bien intangible;
       q)     Los demás que le señale el Consejo Nacional Scout y estos Principios y Organización. Artículo 63. Las funciones y atribuciones individuales de los demás miembros del Consejo Regional son determinadas por el Reglamento de Funcionamiento de la Región.

CAPÍTULO VIII DISTRITO SCOUT
Artículo 64. Toda Región está dividida en Distritos Scouts. Cada Distrito está formado por un número no menor de tres (3) y no mayor de nueve (9) Grupos Scouts registrados en la Asociación de Scouts de Venezuela; los Grupos de un Distrito deben encontrarse próximos geográficamente para hacer posible una mejor comunicación, supervisión y asesoramiento.
Parágrafo Único: Un Distrito pierde su condición de Distrito Oficial por la renuncia de su Comisionado
Principios y Organización de la Asociación de Scouts de Venezuela

de Distrito Electo o cuando el número de grupos registrados sea inferior a tres (3), en consecuencia, el Comisionado de Distrito pierde su condición de Comisionado de Distrito Electo y cesa en sus funciones. Cuando esto suceda el Comisionado Regional correspondiente designará en un lapso no mayor a treinta (30) días calendario un Comisionado de Distrito Interino, con las responsabilidades, funciones y atribuciones descritas en los Principios y Organización y demás Reglamentos. Cuando el Distrito pueda reportar de nuevo tres grupos registrados, recuperará su condición de Distrito Oficial. El Comisionado de Distrito Interino, deberá llamar en un lapso no mayor a quince (15) días calendario a Asamblea Distrital para elegir a un Comisionado de Distrito.
Artículo 65. El Distrito está integrado por:

a)   La Asamblea Distrital;

b)   El Consejo Distrital;

c)   El Comisionado de Distrito, sus Asistentes y Cooperadores;

d)   Los Grupos Scouts.

e)   Unidades complementarias.

Artículo 66. La Asamblea Distrital está integrada por:

a)     El Comisionado de Distrito, quien la convoca y preside, con derecho a voz y voto;

b)	Los delegados de los Grupos Scouts registrados en la Asociación de Scouts de Venezuela , con derecho a voz y voto;
c)     Los Asistentes y Cooperadores Distritales, con derecho a voz;

a)       Otros miembros activos adultos de los Grupos o unidades complementarias del respectivo

Distrito, con derecho a voz.

Cada Grupo Scout estará representado, con derecho a voz y voto por:

a)     Un(a) Jefe o un(a) Subjefe de Grupo;

b)	Un Adulto de Unidad (por rama), siempre que ella cuente, como mínimo, con el 50% de la membresía ideal que establece el Reglamento del Grupo Scout;
c)     Un Padre o Representante integrante del Consejo de Grupo;

d)     El Representante de la Institución Patrocinadora, miembro del Consejo de Grupo. e)     Un joven adulto electo por los jóvenes de cada Grupo.
Artículo 67. Son funciones y atribuciones de la Asamblea de Distrito:

a)      Servir de foro para establecer criterios de unidad y acción entre el Comisionado de Distrito, los

     Asistentes, los Cooperadores, los Jefes de Grupo y Unidades, y los organismos comunitarios; b)      Establecer los planes para el fortalecimiento, la formación, la identificación de los recursos humanos y materiales del Distrito, canalizando las necesidades y aspiraciones de los Grupos
Scouts y de los miembros de base hacia instancias superiores;

c)      Elegir al Comisionado de Distrito, para un período de un (1) año, pudiendo reelegirlo por un

Principios y Organización de la Asociación de Scouts de Venezuela

período en dos ocasiones consecutivas, para un máximo de tres (3) años consecutivos en el cargo. El Comisionado electo o reelecto tomará posesión del cargo al finalizar la Asamblea Distrital donde lo eligieron;
d)	Elegir al Delegado adicional del Distrito ante la Asamblea Nacional Scout, de entre los miembros activos adultos de los Grupos Scouts registrados;
e)      Presentar a la Asamblea Nacional Scout candidatos para cargos electivos nacionales;

f)       Las demás que le señale los Principios y Organización.

Parágrafo Único: El Comisionado de Distrito electo que cese en sus funciones no podrá ocupar por un (1) año el mismo cargo en otro Distrito.
Artículo 68. La Asamblea Distrital se reúne por lo menos una (1) vez al año, o cuando sea convocada por el Comisionado de Distrito o el Consejo Distrital.
El quórum de la Asamblea Distrital lo constituye:

a)     El Comisionado de Distrito;

     b)     La mitad más uno de los delegados de los Grupos Scout registrados en su jurisdicción. El Comisionado de Distrito, o quien haga sus veces, preside sus deliberaciones.
Parágrafo Primero: El Consejo Nacional Scout puede convocar a la Asamblea Distrital y será el Director Ejecutivo Nacional, o quien haga sus veces, quien presida sus deliberaciones. Parágrafo Segundo:  La  Asamblea  Distrital podrá  realizarse  de manera  presencial o  bajo metodologías virtuales y/o a distancia.
Artículo 69. La Asamblea Distrital se rige por un Reglamento Interno y de Debates, igual y de uso obligatorio en todos los Distritos.
Artículo 70. El Comisionado de Distrito ocupa un puesto clave en la estructura institucional. Es un elemento promotor, facilitador y motivador de las Unidades y Grupos Scouts, con responsabilidad directa en la aplicación del Programa de Jóvenes en su jurisdicción. El Comisionado de Distrito no podrá desempeñar otro cargo dentro de la Asociación mientras ejerza su cargo y debe velar por el Propósito y la Misión del Movimiento Scout.
Artículo 71. Son funciones y atribuciones del Comisionado de Distrito:

a)  Establecer una relación estrecha con las Unidades y Grupos Scouts de su jurisdicción, y servir de canal de comunicación entre los Grupos Scout y la Asamblea Distrital, y entre ésta y el Nivel Regional;
b)  Designar y remover, a los Asistentes de las Áreas Estratégicas y los Cooperadores necesarios para garantizar el correcto apoyo a las Unidades y Grupos Scouts;
c)  Garantizar que en su jurisdicción se establezca, aplique y actualice el Plan de Distrito para que se alcancen las metas nacionales fijadas en la Asamblea Nacional Scout;
d)  Identificar las oportunidades que puedan surgir en las Áreas Estratégicas y las comunidades de

Principios y Organización de la Asociación de Scouts de Venezuela

su jurisdicción, detectados por él o por el Consejo Distrital y que puedan influir en las Unidades y Grupos Scouts puestos a su cuidado;
e)  Dedicar especial atención al cumplimiento de la cantidad mínima de miembros establecidos por el Nivel Nacional, para las Unidades co-educativas de su jurisdicción;
f)	Vigilar el correcto funcionamiento de las unidades complementarias y los Consejos de Grupo y las buenas relaciones con las Instituciones Patrocinadoras y su comunidad respectivamente;
g)  Supervisar  la  correcta  Aplicación  del  Método  Scout  y  de  las  Normas  establecidas  en  el

Reglamento de Seguridad en actividades Scouts;

h)  Garantizar que las Unidades y Grupos Scouts y miembros individuales de su jurisdicción cumplan con el Registro anual;
i)   Convocar y presidir reuniones ordinarias y extraordinarias de la Asamblea Distrital;

j)	Entregar  los  informes  que  el  Comisionado  Regional  le  solicite  sobre  el  funcionamiento  y aplicación del Programa de Jóvenes en los Grupos Scouts bajo su supervisión;
k)  Asistir a la reunión de la Asamblea Nacional Scout;

l)   Asistir a los Consejos Regionales;

m) Prestar la Asesoría Integral Personalizada al Consejo de Grupo que representen oportunidades de mejoras en su funcionamiento. Puede designar a otro miembro del equipo distrital para que ejerza esta función, manteniendo informado de su actuación al Consejo Distrital y Regional correspondientes;
n)  Firmar, previa autorización del Director Ejecutivo Nacional y en representación de la Asociación de Scouts de Venezuela, los convenios de cooperación interinstitucionales que se gestionen para beneficio de las Unidades y Grupos Scouts de su jurisdicción;
o)  Es  responsable  de coordinar  el envío  oportuno  al  Comisionado  Regional  de  los  informes financieros y de gestión de cada área, con sus recaudos y soportes;
p)  Velar por que se mantenga el buen nombre e imagen de la Asociación de Scouts de Venezuela adquirido por la tradición de ser la Institución Juvenil más antigua de Venezuela y todos sus miembros como bien intangible;
q)  Las demás que le asigne el Director Ejecutivo Nacional directamente o por intermedio del

Comisionado Regional, la Asamblea Distrital o el Consejo Distrital.

Artículo 72. El Consejo Distrital es la instancia natural y permanente que apoya y supervisa el funcionamiento de las Unidades y Grupos Scout del Distrito; se reúne de manera presencial o virtual por lo menos una vez cada dos (2) meses, convocado por el Comisionado de Distrito o la mitad más uno de los Jefes de Grupos.
El quórum del Consejo Distrital lo constituye:

a)   El Comisionado de Distrito;

Principios y Organización de la Asociación de Scouts de Venezuela

b)   La mitad más uno de los Jefes o Sub Jefes de Grupo registrados en la Asociación de Scouts de

Venezuela a la fecha;

c)   Al menos uno de los dos jóvenes electos como representación juvenil.

El Comisionado de Distrito, o quien haga sus veces, preside sus deliberaciones, salvo los casos de existencia de conflictos de interés previamente declarados.
Parágrafo Primero: Para efectos del quórum del Consejo Distrital, se tomará en cuenta el corte de membresía del último dia del mes anterior.
Parágrafo Segundo: Para todos los casos, la mitad más uno se calculará en función del número total de miembros que forman la instancia. Si el número total es par, la mitad más uno de los miembros se calculará de manera directa; para el caso de un número total de miembros impar, se calculará la mitad más uno de estos, considerando como base del cálculo el número par inmediatamente anterior al total de miembros.
Artículo 73. El Consejo Distrital está integrado por:

a)   El Comisionado de Distrito, quien lo convoca y preside, con voz y voto

b)   Los Jefes o Subjefes de Grupo, con voz y voto por Grupo Scout registrado;

c)   Los dos (02) miembros de los órganos representación juvenil, con voz y voto. d)   Los Asistentes y Cooperadores Distritales, con derecho a voz;
e)   El Comisionado Regional cuando tenga a bien participar, con derecho a voz.

Artículo 74. Son Funciones y atribuciones del Consejo Distrital:

a)      Servir de vínculo entre el Comisionado de Distrito, sus Asistentes, los Jefes y Subjefes de

Grupo de su jurisdicción, y los organismos del Nivel Regional;

b)	Coordinar los planes de mejoramiento, formación y progreso de las Unidades y Grupos Scouts, canalizar las necesidades y aspiraciones de los miembros de base hacia las instancias superiores;
c)      Recomendar a la Asamblea Distrital candidatos para el cargo de Comisionado de Distrito;

d)      Supervisar  el  cumplimiento  de  las  normas mínimas  de  membresía  establecidas  a  Nivel

Nacional para cada Rama y Unidad en los Grupos Scouts de Distrito;

e)      Conocer, calificar, decidir e imponer sanciones conforme al procedimiento establecido en el

Reglamento Scout correspondiente;

f)       Convocar a reuniones de la Asamblea Distrital;

g)      Hacer seguimiento a la asistencia directa (Asesoría Integral Personalizada) realizada por el

Comisionado de Distrito a los Consejos de Grupo que presenten fallas en su funcionamiento;

h)	Presentar ante la Asamblea Distrital y ante el Consejo Regional su informe de gestión anual y su plan y presupuesto del siguiente año, de acuerdo con el reglamento de funcionamiento de
Distrito;

Principios y Organización de la Asociación de Scouts de Venezuela

i)	Revisar y recomendar los reconocimientos conforme con el Reglamento de Condecoraciones y Distinciones;
j)       Mediar, conocer, calificar, decidir conforme al procedimiento establecido en el Reglamento

Scout correspondiente;

k)      Las demás que le asigne el Comisionado Regional o la Asamblea Distrital.

CAPÍTULO IX UNIDAD Y GRUPO SCOUT
Artículo 75. La unidad o el Grupo Scout, es el escenario de la Asociación de Scouts de Venezuela, en el que se imparte el programa de jóvenes de manera progresiva a través de las unidades a niñas, niños, adolescentes y jóvenes. Los esfuerzos de todos los organismos Distritales, Regionales y Nacionales deben promover la permanencia, desarrollo y expansión de las Unidades y los Grupos Scouts en el territorio nacional.
Artículo 76. El Grupo Scout es el escenario donde concurren dos (2) o más unidades, en distintas fases del desarrollo evolutivo, para contar con la oportunidad de desarrollar un proceso de progresión personal, considerando las características que determinen los programas de cada Rama.
      Parágrafo  único:  Podrán  conformarse  a  su  vez  Unidades  Scouts  Complementarias,  no pertenecientes  a  un  Grupo  Scout,  que  podrán  implementar  el  Proyecto  Educativo  de  la Asociación de Scouts de Venezuela en los espacios y escenarios en que estas se desenvuelvan. Artículo 77. El Consejo de Grupo solicitará el registro del Grupo Scout ante la Oficina Scout Nacional, a través del canal que esta defina, previa inspección y recomendación del Comisionado de Distrito
respectivo. De no contar con la instancia, será el DEN quien instruirá el mecanismo de validación. Parágrafo Único: El registro de los Grupos Scouts es obligatorio, a los efectos de su representación en el seno de la Asamblea de Distrito y/o Nacional, así como su participación en los eventos definidos en los Ciclos Institucionales de Programa y actividades de formación.
Artículo 78. La estructura operativa del Grupo Scout es la siguiente:

a)  El Consejo de Grupo;

b)  Las Unidades.

Artículo  79.  El  Consejo  de  Grupo  es  el  máximo  organismo  de  coordinación del  Grupo,  bajo  el acompañamiento del Jefe de Grupo, priorizando su rol de garante del Método Scout, así como la permanencia y crecimiento del Grupo. Se reúne de manera presencial o virtual por lo menos una vez cada dos (2) meses, convocado por el Jefe de Grupo o Sub Jefe de Grupo en ausencia del primero, o en reunión extraordinaria a solicitud de la mitad más uno de sus miembros.
Artículo 80.  El Consejo de Grupo está integrado por:

a)     Un(a) Jefe y un(a) Subjefe de Grupo, ambos con derecho a voz y voto;

b)     Los Adultos de las Unidades, todos con derecho a voz y voto;
Principios y Organización de la Asociación de Scouts de Venezuela

c)     Un (1) Representante de la Institución Patrocinadora, con derecho a voz y voto;

d)	Un Padre o Representante por cada Unidad del Grupo, con derecho a voz y voto, dentro de los cuales serán designados por el Consejo de Grupo el Tesorero y Secretario. Estos Padres o Representantes serán designados en Asambleas de Padres o Representantes, general o por rama;
e)     Dos (02) miembros jóvenes con voz y voto.

f)      El Comisionado de Distrito cuando tenga a bien asistir, con derecho a voz.

Artículo 81. El quórum del Consejo de Grupo lo constituye:

a)   El Jefe o Sub jefe de Grupo;

b)   La mitad de los Adultos de las unidades registradas;

c)   Al menos uno de los dos jóvenes electos como representación juvenil

d)   La mitad de la representación de los Padres o Representantes de las Unidades registradas. Parágrafo Único: El quorum será la mitad de los miembros antes descritos, siempre que dicho número sea par, y en caso de ser impar, será la mitad del número par, inmediatamente anterior a la cifra impar del total. Determinando de esta forma la mayoría de sus integrantes en las reuniones.
Artículo 82. Son funciones y atribuciones del Consejo de Grupo:

a)	Promover la participación entre la Institución Patrocinadora, los Padres o Representantes, y los Adultos scouts del Grupo;
b)	Captar, seleccionar, renovar, reubicar y retirar a los adultos designados para la conducción del Grupo o Unidad, a ser ratificados por la Asociación de acuerdo con lo establecido en la Política Nacional de Adultos;
c)	Proveer los recursos necesarios para la operación exitosa del Método Scout en todas las Unidades del Grupo, de acuerdo con los Principios, Objetivos y Políticas establecidas por la Asociación;
d)	Coordinar y ejecutar los planes de captación y formación de los adultos voluntarios de manera de asegurar su continuidad con calidad en la labor;
e)	Asegurar los recursos materiales y financieros necesarios para el desarrollo del Método Scout, tales como: lugar de reunión, equipos y transporte, campamentos y otros eventos, instructores, sinodales;
f)	Comprometer y lograr la participación de todas las Unidades del Grupo en las actividades y eventos que se organicen a Nivel Nacional, Regional o Distrital;
g)	Asegurar la permanencia operativa de las Unidades, detectando y tomando las acciones necesarias para aumentar la persistencia de sus miembros;
h)        Responder por la aplicación del Método Scout en las unidades del grupo;

i)         Velar que cada miembro del grupo efectúe o renueve oportunamente su registro institucional;

Principios y Organización de la Asociación de Scouts de Venezuela

j)	Designar a los Adultos del grupo, por un periodo de un (1) año, asegurándose de la firma del acuerdo mutuo en base a las Metas Nacionales. Pudiendo reelegir al Jefe de Grupo por un (1) período en 2 ocasiones, para un máximo de 3 años en el cargo;
k)	Designar a la institución patrocinadora cuyo representante formará parte del Consejo de Grupo por un periodo de un (1) año, y validar que dicho representante firme su acuerdo mutuo en base a las Metas Nacionales del Plan Nacional de Desarrollo.
l)	Mantener informado al Comisionado de Distrito de las necesidades y aspiraciones del Grupo, y aceptar las que él haga o trasmita a nombre del Comisionado Regional;
m)	Conocer, calificar y sancionar las faltas cometidas por miembros del Grupo, conforme a las disposiciones del Reglamento Scout correspondiente;
n)        Designar los representantes del Grupo Scout ante la Asamblea Distrital;

o)	Verificar   permanentemente   el  cumplimiento  de   las   metas   mínimas   de   membresía establecidas a Nivel Nacional para cada Rama;
p)	Otorgar y Recomendar el otorgamiento condecoraciones y distinciones para los miembros del Grupo que se hagan merecedores de ellas, de conformidad con lo dispuesto en el Reglamento de Condecoraciones y Distinciones;
q)	Velar por que se mantenga el buen nombre e imagen de la Asociación de Scouts de Venezuela adquirido por la tradición de ser la Institución Juvenil más antigua de Venezuela y todos sus miembros como bien intangible;
r)	Presentar ante la Asamblea de Grupo y ante la Asamblea Distrital, su informe de gestión anual y su plan y presupuesto del siguiente año, de acuerdo con el Reglamento de Funcionamiento de Grupos;
s)        Las demás que le sean asignadas por los Principios y Organización.

Artículo 83. Son funciones y atribuciones del Jefe de Grupo:

a)	Supervisar  la correcta aplicación  del Método Scout  en  las  Unidades  contribuyendo  en  la coordinación de las actividades;
b)   Velar porque las actividades se realicen en función del cumplimiento de la Promesa y Ley Scout;

c)   Convocar y presidir las reuniones del Consejo de Grupo;

d)   Responder por la aplicación y cumplimiento de las Metas Nacionales en su Grupo Scout;

e)	Participar,  personalmente  y  con  su  Grupo,  en  los  programas  y  actividades  Nacionales, Regionales y Distritales;
f)    Responsabilizarse por la formación adecuada de los Adultos del Grupo;

g)   Visitar por separado a las Unidades del Grupo, al menos una vez al mes;
h)	Informar al Consejo de Grupo de las actividades y programas de los niñas, niños, adolescentes y jóvenes a su cuidado;

Principios y Organización de la Asociación de Scouts de Venezuela

i)	Velar por que se mantenga el buen nombre e imagen de la Asociación de Scouts de Venezuela adquirido por la tradición de ser la Institución Juvenil más antigua de Venezuela y todos sus miembros como bien intangible;
j)	Asistir a las reuniones de la Asamblea Distrital y del Consejo Distrital cada vez que se le convoque;
k)	Consignar los informes de gestión anual y el administrativo ante el Consejo Distrital o en su defecto ante el Director Ejecutivo Nacional;
l)	Representar al Grupo Scout en la Asamblea Nacional Scout, pudiendo en caso de que lo amerite, delegar su representación en el subjefe de grupo;
m)  Las demás que le señale los Principios y Organización, el Comisionado de Distrito o que le correspondan por la naturaleza de sus funciones.
Artículo 84. Funciones y atribuciones del Subjefe de Grupo:

a)     Colaborar con el Jefe de Grupo en la supervisión de la correcta aplicación del Método Scout;

b)     Ejercer adecuada supervisión sobre todos los aspectos que tengan que ver con el Plan de

Grupo;

c)     Vigilar el oportuno registro anual del Grupo y de todos sus integrantes;

d)     Substituir al Jefe de Grupo en caso de ausencia temporal o absoluta hasta que el Consejo de

Grupo designe a un nuevo Jefe de Grupo;

e)	Desarrollar el área de Adultos en el Movimiento Scout, dentro del Grupo para el logro de las Metas Nacionales en esta área, apoyándose en el Asistente Distrital de Adultos en el Movimiento Scout
f)      Las demás que asigne el Consejo de Grupo o el Jefe de Grupo.

Parágrafo único: La ausencia temporal o absoluta del Jefe de Grupo es declarada por el Consejo de Grupo.
Artículo 85. La Unidad Scout es el espacio que promueve la aplicación del Método Scout, en concordancia con las características, necesidades y aspiraciones de los miembros activos jóvenes y de la comunidad donde residen, representando el pequeño grupo la célula fundamental sobre la cual giran los procesos educativos.
Artículo 86. La Institución Patrocinadora es la empresa, Institución educativa, u otro organismo público o privado que patrocina el funcionamiento de un Grupo Scout, cuyo objetivo no colida con los principios del Movimiento Scout.
Artículo 87. Son funciones y atribuciones de la Institución Patrocinadora:

a)   Participar en los Consejos de Grupo; con derecho a voz y voto;

b)   Facilitar los medios necesarios para el buen funcionamiento del Grupo;

c)   Promocionar la participación de adultos para ser seleccionados como Adultos del Grupo;

Principios y Organización de la Asociación de Scouts de Venezuela

d)   Nombrar el Representante de la Institución ante el Consejo de Grupo y la Asamblea Distrital;

e)	Velar porque el Grupo cumpla con el Registro Anual ante la Asociación de Scouts de Venezuela, ratificando en el mismo su Compromiso de Patrocinio;
f)    Promover la realización de la Asamblea Anual de Padres y Representantes;

g)   Colaborar en la programación de actividades del Grupo;

h)   Las demás que le señale el P.O.R.

CAPÍTULO X ELECCIONES NACIONALES
Artículo 88. Los procesos de elección de autoridades del Nivel Nacional durante la Asamblea Nacional Scout son coordinados por el comité de escrutinios, comisión creada para tal fin, el cual tendrá las siguientes funciones:
a)  Verificar el quórum antes del proceso de votación.

b)  Coordinar los mecanismos utilizados durante los procesos de votaciones desde la instalación hasta la clausura de la Asamblea Nacional Scout. Dichos mecanismos deben ser establecidos con antelación a la instalación de la Asamblea Nacional Scout, de acuerdo con las metodologías a utilizar durante la reunión.
c)  Validar el número de votos registrados y permitidos.

d)  Organizar el proceso de votación, organizar durante la Asamblea a los delegados y observadores con derecho a intervenir, hacer el escrutinio de los votos emitidos, y validar que el proceso se realice conforme a lo dispuesto en el Reglamento Interior y de Debates de la Asamblea Nacional Scout;
e)  Proclamar a las autoridades electas;

Artículo 89. El Consejo Nacional Scout, previo a la instalación de la Asamblea Nacional Scout, propondrá los integrantes al Comité de Escrutinios. El Comité de Escrutinios estará formado por cinco (5) miembros, quienes deben estar presentes durante el desarrollo de la Asamblea Nacional Scout. De igual modo el Consejo Nacional Scout designará tres suplentes para el Comité de Escrutinios de entre las personas que se hayan registrado en la Asamblea.
Parágrafo Primero: El Comité de Escrutinios podrá estar conformado con miembros de la institución que se hayan registrado o no como participantes en la Asamblea Nacional Scout. Parágrafo Segundo: El Consejo Nacional Scout recomendará, a la Asamblea Nacional Scout, las cinco (5) personas que conformarán el Comité de Escrutinios. En caso de que la propuesta no sea aprobada por la Asamblea, los delegados y observadores podrán proponer alternativas de personas para ser sometidas a votación, durante la Sesión de Apertura de la Asamblea Nacional Scout.
Parágrafo Tercero: Los candidatos a cargos electivos nacionales no podrán ser miembros del
Principios y Organización de la Asociación de Scouts de Venezuela

Comité de Escrutinios.

Artículo 90. El proceso de elecciones de autoridades del nivel nacional inicia al momento en que las instancias facultadas para respaldar las postulaciones oficialicen sus propuestas dentro de las actas correspondientes. La Dirección Ejecutiva Nacional debe:
a)	Recibir las postulaciones de candidatos a ocupar cargos nacionales electivos y presentarlos a consideración de la Asamblea Nacional Scout. El proceso para seguir será el siguiente:
-	Validar el plazo para la presentación de candidaturas, que no será menor a sesenta (60) días calendario antes de la fecha de celebración de la Asamblea Nacional Scout en que serán electos, a fin de poder comunicar, antes de los treinta (30) días calendario de la celebración de dicha Asamblea Nacional Scout, la lista de los candidatos aceptados y el resumen de sus currículos, los cuales serán publicados a través de los medios electrónicos con que cuente la Institución con el fin de dar la mayor difusión a la Institución;
-	Verificar que las postulaciones incluyan el Curriculum Vitae de los candidatos y una Carta de Aceptación de la postulación;
-	Verificar los recaudos recibidos y, basados en esa verificación, aceptar o rechazar la candidatura.
b)       Presentar ante el Comité de escrutinios el proceso desarrollado en el literal “a” para su

validación.

Parágrafo Primero: Los miembros electos en cargos de Elección Nacional se incorporarán a sus cargos al finalizar la Asamblea Nacional Scout en la que son electos.
Parágrafo Segundo: No se aceptará como candidato, a ocupar cargos electivos a ninguna persona que tenga abierto un proceso de convivencia o tenga pendiente el cumplimiento de una sanción, contemplando tanto las situaciones y procesos internas como externas.
Artículo 91. Se deben promover mecanismos que procuren la participación de todos los delegados y observadores. Se podrán utilizar mecanismos tecnológicos que garanticen la practicidad, transparencia y rapidez de los procesos de este tipo, a fin de garantizar el adecuado desarrollo de la Asamblea Nacional Scout y conforme a la agenda que se haya establecido.
CAPÍTULO XI MODIFICACIONES AL P.O.R.
Artículo 92. Los Principios y Organización podrán ser modificados por la Asamblea Nacional Scout en sus partes I y II, Principios y Organización, por iniciativa del Consejo Nacional Scout o del setenta y cinco (75) por ciento de los Distritos Oficiales.
El proyecto de reforma y su exposición de motivos será presentado a consideración de los miembros de la Asociación con, por lo menos, noventa (90) días calendario de anticipación a la celebración de la Asamblea Nacional Scout donde será discutido.
Principios y Organización de la Asociación de Scouts de Venezuela

Artículo 93. La Parte III, Reglamentos, será promulgada, modificada e interpretada por el Consejo Nacional Scout. Para su validez, los Reglamentos o sus modificaciones deben ser aprobados por las dos terceras partes de los miembros activos del Consejo Nacional Scout. Los Reglamentos entrarán en vigor quince (15) días calendario después de su aprobación.
Parágrafo Único: De no aprobarse un Reglamento sometido a consideración en una reunión del Consejo Nacional Scout, en la próxima reunión del Consejo Nacional Scout debe presentarse de nuevo a consideración; en caso de no ser aprobado por la mayoría calificada (dos terceras partes), se someterá a votación nuevamente de manera inmediata en la próxima reunión del Consejo Nacional Scout y podrá ser aprobado por la mayoría simple de sus miembros; quienes voten en contra o salven su voto deben soportar por escrito la motivación correspondiente.
Artículo 94. Las modificaciones de los Principios y Organización de la Asociación de Scouts de Venezuela serán decididas por la Asamblea Nacional Scout y deberá contar con la aprobación de al menos las dos terceras partes de los votos de la Asamblea Nacional Scout.

CAPÍTULO XII DISPOSICIONES TRANSITORIAS Y FINALES
Artículo 95. Los presentes Principios y Organización fueron aprobados por la Asamblea Nacional Scout el día 30 de marzo de 2025 y entrará en vigor en el mismo momento de su aprobación, salvo las excepciones expuestas en las presentes disposiciones transitorias y finales.
Artículo 96. Con la eliminación de la Corte de Honor, los miembros electos para periodos mayores a un año cesan en sus funciones con la aprobación de estos Principios y Organización.
Artículo 97. Los Ex-Presidentes de la Corte de Honor, miembros del Comité Consultivo, se mantendrán

en sus funciones, aun con la eliminación de esa instancia.

























Principios y Organización de la Asociación de Scouts de Venezuela




]
---

Pregunta del usuario:
{st.text_input("¿Qué quieres saber?")}
"""

# Campo de texto para que el usuario pegue el artículo
user_question = st.text_input("Hazme una pregunta:", key="question_input")

# Botón para activar el bot
if st.button("Obtener respuesta"):
    if user_question:
        # Envía el prompt y la pregunta del usuario al modelo
        with st.spinner("Buscando respuesta..."):
            response = model.generate_content(prompt + user_question)
            
        # Muestra el resultado
        st.subheader("Respuesta:")
        st.success(response.text)
    else:
        st.error("Por favor, escribe una pregunta.")