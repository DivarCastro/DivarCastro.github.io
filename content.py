# -*- coding: utf-8 -*-
"""Contenido del CV en 3 idiomas. Edita aquí y ejecuta: python build_site.py"""

LINKS = dict(
    email="divecast@espol.edu.ec",
    github="https://github.com/DivarCastro",
    linkedin="https://www.linkedin.com/in/divar-castro-rodas-5a568610b/",
    orcid="https://orcid.org/0000-0002-2197-2277",
    rg="https://www.researchgate.net/profile/Divar-Castro-Rodas",
    lattes="http://lattes.cnpq.br/7848794322795201",
)

# Publicaciones (iguales en los 3 idiomas): (año, autores, título, revista, doi)
PUBS = [
 (2026,"Castro-Rodas, D., Pico Molineros, A., Thottolil, R., Bulatov, D., de Paula, E. M. S., & Velastegui-Montoya, A.","Comparison of Supervised Classification Algorithms for Land Use and Land Cover in Guayaquil: An Assessment with Landsat and MapBiomas.","Int. Arch. Photogramm. Remote Sens. Spatial Inf. Sci., XLIX-B3-2026, 565–572.","10.5194/isprs-archives-XLIX-B3-2026-565-2026"),
 (2026,"Castro-Rodas, D., Velastegui-Montoya, A., Guimarães, Y. C., Nascimento, E. S., Pereira, M. D. A., Santos, L. B. L., Alvarez, C., & Sanclemente Ordoñez, E.","Detecting Urban Change with Open-Source GIS Programs: A Case Study in Guayaquil.","ISPRS Ann. Photogramm. Remote Sens. Spatial Inf. Sci., X-3/W4-2025, 49–54.","10.5194/isprs-annals-X-3-W4-2025-49-2026"),
 (2026,"Peña-Villacreses, G., Velastegui-Montoya, A., Castro-Rodas, D., Freire-Granda, D., de Souza, I. N., & Pereira, L. C. C.","GIS Mapping of Allochthonous Marine Litter across the Brazilian Amazon Coast.","ISPRS Ann. Photogramm. Remote Sens. Spatial Inf. Sci., X-3/W4-2025, 279–284.","10.5194/isprs-annals-X-3-W4-2025-279-2026"),
 (2023,"Pineda, F. V. C., Loor, D. S. C., Añez, A. E. P., & Rodas, D. C.","Disruptive Technologies and Businesses: Toward an Accelerated Transformation of Society and the Market.","In Technology, Business, Innovation, and Entrepreneurship in Industry 4.0 (Guarda, Fernandes & Augusto, Eds.). Springer, Cham.","10.1007/978-3-031-17960-0_3"),
 (2022,"Castro Loor, D., Calderón Pineda, F., Castro Rodas, D., & Rodas Idrovo, R.","Posicionamiento de emprendimientos en artesanos, provincia de Santa Elena.","Revista Ciencias Pedagógicas e Innovación, 10(2), 45–50.","10.26423/rcpi.v10i2.580"),
 (2022,"Abad, R., Jaramillo, K. B., Castro, D., Sánchez, J. A., & Rodríguez, J.","Octocoral Distribution Patterns at the Equatorial Front (Tropical Eastern Pacific): Muricea and Leptogorgia.","Oceans, 3, 218–230.","10.3390/oceans3020016"),
 (2021,"Ormaza-González, F. I., Castro-Rodas, D., & Statham, P. J.","COVID-19 Impacts on Beaches and Coastal Water Pollution at Selected Sites in Ecuador, and Management Proposals Post-Pandemic.","Frontiers in Marine Science, 8, 710.","10.3389/fmars.2021.669374"),
]
REFS = [
 ("Jenny Rodríguez, Ph.D.","CENAIM-ESPOL","jenrodri@espol.edu.ec"),
 ("Mercy Borbor Córdova, Ph.D.","FIMCM-ESPOL","meborbor@espol.edu.ec"),
 ("Andrés Velástegui Montoya, Ph.D.","FICT-ESPOL","dvelaste@espol.edu.ec"),
]

L = {}

L["es"] = dict(
 code="es", name="Español", title="Divar Castro Rodas · Teledetección y SIG",
 desc="Candidato doctoral en Ingeniería (Georecursos, ESPOL). SIG, teledetección, LULC y modelamiento urbano y ambiental.",
 role="PhD(c) en Ingeniería (Georecursos) · M.Sc. en SIG · Ingeniero Oceánico Ambiental",
 role_full="PhD(c) en Ingeniería (Georecursos) · M.Sc. en Sistemas de Información Geográfica · Ingeniero Oceánico Ambiental",
 affil="ESPOL, Guayaquil, Ecuador",
 nav=[("experiencia","Experiencia"),("proyectos","Proyectos"),("publicaciones","Publicaciones"),("ponencias","Ponencias"),("educacion","Educación"),("reconocimientos","Reconocimientos")],
 email_lbl="✉️ Correo", pdf_btn="📄 CV (PDF)",
 h=dict(about="Sobre mí",exp="Experiencia profesional",proj="Proyectos",pubs="Publicaciones",talks="Ponencias y eventos",edu="Educación y capacitación",awards="Reconocimientos y becas",
        profile="Perfil profesional",expcv="Experiencia laboral",educv="Formación académica",talkscv="Ponencias y participación en eventos",courses="Cursos y capacitaciones",refs="Referencias",
        contact="Contacto",lang="Idiomas",skills="Habilidades técnicas",soft="Aptitudes",interests="Otros intereses",selcourses="Cursos seleccionados"),
 about=["Candidato Doctoral en Ingeniería con mención en Georecursos (ESPOL). Analista de información oceanográfica y meteorológica con 9 años de experiencia en Sistemas de Información Geográfica y sensores remotos aplicados al monitoreo ambiental y costero. Experiencia en coordinación científica, análisis estadístico, gestión de proyectos de investigación con financiamiento y docencia universitaria. Colaborador activo en proyectos de investigación geoespacial en Ecuador y Brasil."],
 skills=["SIG: QGIS, ArcGIS Pro","Programación: Python, R","Google Earth Engine","PostgreSQL / PostGIS","Sensores remotos y percepción satelital","Piloto de drones (UAV) certificado","Ofimática avanzada"],
 skills_web=["QGIS","ArcGIS Pro","Python","R","Google Earth Engine","PostgreSQL / PostGIS","Sensores remotos","Piloto UAV certificado"],
 soft=["Trabajo en equipo","Capacidad analítica","Comunicación efectiva","Proactividad","Coordinación científica"],
 interests=["Medio ambiente","Limpieza de playas","Visitas técnicas"],
 langs=["Español — Nativo","Inglés — Fluido (B2)","Portugués — Medio"],
 jobs=[
  ("Técnico de Investigación 2","ESPOL","Guayaquil, Ecuador | 2024 – Actualmente",[
    "Elaboración de publicaciones indexadas con temática SIG y percepción remota.",
    "Gestión de propuestas de financiamiento de proyectos de investigación.",
    "Liderazgo en el desarrollo del Geoportal Ecuatoriano de Parámetros Océano-Atmosféricos (GEPOA), para el monitoreo satelital de variables océano-atmosféricas en Áreas Marinas Protegidas.",
    "Colaborador en el proyecto brasileño HIDRA (convocatoria CNPq/MCTI/FNDCT Nº 06/2026, Faixa B), enfocado en eficiencia del uso del agua en ecosistemas (Random Forest, XGBoost, SHAP, Google Earth Engine).",
    "Colaborador en el proyecto STARS (Spatial Tools for Assessing Risks in Sudden Natural Hazards), financiado por Erasmus+ (Capacity Building) y liderado por la Universidad de Lisboa, para el desarrollo de módulos educativos de SIG y BIM en la evaluación de riesgos ante amenazas naturales súbitas (sismos, inundaciones, deslizamientos) en universidades de Ecuador y Colombia.",
    "Participación en proyectos de vinculación con la comunidad."]),
  ("Docente","Tecnológico Universitario Espíritu Santo","Guayaquil, Ecuador | 2022 – Actualmente",[
    "Creación de syllabus y contenido para las asignaturas dictadas.","Planificación académica y seguimiento a estudiantes.","Programación de actividades extracurriculares.","Proyectos de vinculación con la comunidad."]),
  ("Analista de Oceanografía y Meteorología","INOCAR","Guayaquil, Ecuador | 2022 – 2024",[
    "Uso de herramientas SIG y programación para ayudas a la navegación y modelamiento de escenarios de deriva de embarcaciones.","Mantenimiento de la red mareográfica y de boyas del Ecuador.","Alimentación de bases de datos y recopilación de información in situ y satelital.","Participación en cruceros oceanográficos regionales y costeros.","Responsable del catálogo de objetos espaciales de la dirección."]),
  ("Coordinador de Bioensayos & Científico","CENAIM-ESPOL","Santa Elena, Ecuador (Prácticas) | 2017 – 2022",[
    "Análisis estadístico y gestión de información espacial del centro.","Técnico responsable de bioensayos y de la estación oceanográfica/meteorológica.","Seguimiento técnico del Plan Operativo Anual."]),
 ],
 jobs_web=[
  ["Publicaciones indexadas en SIG y percepción remota; gestión de propuestas de financiamiento.","Liderazgo en el desarrollo del Geoportal Ecuatoriano de Parámetros Océano-Atmosféricos (GEPOA).","Colaborador en los proyectos HIDRA (Brasil) y STARS (Erasmus+).","Proyectos de vinculación con la comunidad."],
  ["Creación de syllabus y contenido; planificación académica y seguimiento a estudiantes.","Actividades extracurriculares y proyectos de vinculación."],
  ["SIG y programación para ayudas a la navegación y modelamiento de deriva de embarcaciones.","Mantenimiento de la red mareográfica y de boyas del Ecuador.","Bases de datos, información in situ y satelital; cruceros oceanográficos; catálogo de objetos espaciales."],
  ["Análisis estadístico y gestión de información espacial del centro.","Responsable de bioensayos y de la estación oceanográfica/meteorológica; seguimiento del Plan Operativo Anual."],
 ],
 projects=[
  ("GEPOA","ESPOL · Geoportal","Geoportal Ecuatoriano de Parámetros Océano-Atmosféricos: monitoreo satelital en Áreas Marinas Protegidas.",None),
  ("HIDRA","CNPq/MCTI/FNDCT Nº 06/2026 · Brasil","Eficiencia del uso del agua en ecosistemas con Random Forest, XGBoost, SHAP y Google Earth Engine.",None),
  ("STARS","Erasmus+ · U. de Lisboa","Módulos educativos de SIG y BIM para evaluar riesgos de amenazas naturales súbitas en Ecuador y Colombia.","https://stars-project.eu"),
  ("IPUS (tesis doctoral)","ESPOL · 2024 – presente","Identificación y Predicción del Crecimiento Urbano en Gran Guayaquil.",None),
 ],
 events=[
  ("IGARSS 2026","Conferencista invitado (IEEE). Washington D.C., EE. UU., agosto 2026."),
  ("XXV ISPRS Congress","Conferencista invitado (ISPRS). Toronto, Canadá, julio 2026."),
  ("Latin America GRSS and ISPRS Remote Sensing Conference (LAGIRS)","Tutor y conferencista invitado. Foz de Iguazú, Brasil, noviembre 2025."),
  ("Taller: Descarga y procesamiento de datos satelitales con Python y GEE","Capacitador invitado, FICT-ESPOL. Guayaquil, Ecuador, octubre 2025."),
  ("The 2nd International Electronic Conference on Land","\"A Comparison of Supervised Classification Algorithms in Guayaquil Land Use and Land Cover Data\" — Expositor invitado, MDPI. En línea, Suiza, septiembre 2025."),
  ("AmeriGEO Week 2025","\"Construcción y uso del RuPO Hub para abordar el plástico marino\" — Expositor invitado, Grupo GEO. Bogotá, Colombia, agosto 2025."),
  ("Curso Pre-Antártico","\"Teleconexiones con la Antártida\" — Expositor invitado, INOCAR. Guayaquil, Ecuador, diciembre 2023."),
  ("Curso básico de manejo de SIG en QGIS","Capacitador invitado, UPSE. Santa Elena, Ecuador, diciembre 2023."),
  ("Día Mundial de los Océanos","\"Oceanografía en el Ecuador, ¿Qué estamos haciendo como país?\" — Expositor invitado, ESPOL. Guayaquil, Ecuador, junio 2023."),
  ("Servicios Ecosistémicos","\"Teledetección y Valoración de los Servicios Ecosistémicos\" — Expositor invitado, CODSpace-UAndes. En línea, Colombia, septiembre 2020."),
 ],
 edu=[
  ("Doctorado en Ingeniería, mención Georecursos","ESPOL","2024 – Presente",["Tesis: \"Identificación y Predicción del Crecimiento Urbano en Gran Guayaquil (IPUS)\""]),
  ("Diplomado en IA Aplicada a la Docencia","Universidad de las Américas","2025",[]),
  ("M.Sc. en Sistemas y Ciencias de la Información Geográfica","Universität Salzburg & USFQ","2019 – 2021",[]),
  ("Ingeniero Oceánico Ambiental","ESPOL","2011 – 2015",[]),
 ],
 courses=["Piloto certificado para manejo de drones (40 h) — DGAC","Operación y Manejo de drones (8 h) — ESPOL","Lenguaje de Programación e Inteligencia Artificial (8 h) — ESPOL","Simposio de Oceanografía 2024 (16 h) — ESPOL","Oceanografía de la Región Ecuatorial (20 h) — ESPOL","Análisis y Procesamiento de Información Oceanográfica con Python (40 h) — ESPOL","Diseño e implementación de un modelo numérico de transformación y rebase del oleaje en el litoral ecuatoriano — Modelo SWASH (80 h) — INOCAR","NASA ARSET: Introduction to NASA Earth Observations and Tools for Operational Wildfire Monitoring and Management","NASA ARSET: Monitoring Global Terrestrial Surface Water Height using Remote Sensing","NASA ARSET: Using Google Earth Engine for Land Monitoring Applications","NASA ARSET: Remote Sensing of Coastal Ecosystems","ESRI: 3D Visualization, Animation, Labeling, Manejo de capas, Datos ráster y Coordenadas en ArcGIS Pro"],
 courses_web=["Piloto certificado de drones (40 h) — DGAC","Análisis y procesamiento de información oceanográfica con Python (40 h) — ESPOL","Modelo numérico SWASH de oleaje (80 h) — INOCAR","NASA ARSET: Google Earth Engine para monitoreo terrestre; sensores remotos de ecosistemas costeros; altura de agua superficial; monitoreo de incendios","ESRI: ArcGIS Pro (visualización 3D, ráster, coordenadas)"],
 awards=[("2026","Beca doctoral en Brasil, a partir de agosto."),("2025","Mejor presentación oral — The 2nd International Electronic Conference on Land (MDPI Land, Suiza)."),("2023","Medalla Humboldt-Caldas al mejor trabajo de Biogeografía de Ecuador y Colombia (Academia Colombiana de Ciencias Exactas, Físicas y Naturales, Bogotá)."),("2016–2017","Diploma de honor al mejor graduado de la carrera, período 2016–2017 (ESPOL).")],
 ref_role="Investigadora Docente", ref_role_m="Investigador Docente",
 footer="Guayaquil, Ecuador",
)

L["en"] = dict(
 code="en", name="English", title="Divar Castro Rodas · Remote Sensing & GIS",
 desc="PhD candidate in Engineering (Georesources, ESPOL). GIS, remote sensing, LULC, and urban and environmental modeling.",
 role="PhD(c) in Engineering (Georesources) · M.Sc. in GIS · Environmental Ocean Engineer",
 role_full="PhD(c) in Engineering (Georesources) · M.Sc. in Geographic Information Systems · Environmental Ocean Engineer",
 affil="ESPOL, Guayaquil, Ecuador",
 nav=[("experiencia","Experience"),("proyectos","Projects"),("publicaciones","Publications"),("ponencias","Talks"),("educacion","Education"),("reconocimientos","Awards")],
 email_lbl="✉️ Email", pdf_btn="📄 CV (PDF)",
 h=dict(about="About me",exp="Professional experience",proj="Projects",pubs="Publications",talks="Talks and events",edu="Education and training",awards="Awards and fellowships",
        profile="Professional profile",expcv="Work experience",educv="Education",talkscv="Talks and event participation",courses="Courses and training",refs="References",
        contact="Contact",lang="Languages",skills="Technical skills",soft="Soft skills",interests="Other interests",selcourses="Selected courses"),
 about=["PhD candidate in Engineering, Georesources track (ESPOL). Oceanographic and meteorological information analyst with 9 years of experience in Geographic Information Systems and remote sensing applied to environmental and coastal monitoring. Experience in scientific coordination, statistical analysis, management of funded research projects, and university teaching. Active collaborator in geospatial research projects in Ecuador and Brazil."],
 skills=["GIS: QGIS, ArcGIS Pro","Programming: Python, R","Google Earth Engine","PostgreSQL / PostGIS","Remote sensing and satellite imagery","Certified drone (UAV) pilot","Advanced office software"],
 skills_web=["QGIS","ArcGIS Pro","Python","R","Google Earth Engine","PostgreSQL / PostGIS","Remote sensing","Certified UAV pilot"],
 soft=["Teamwork","Analytical skills","Effective communication","Proactivity","Scientific coordination"],
 interests=["Environment","Beach clean-ups","Technical visits"],
 langs=["Spanish — Native","English — Fluent (B2)","Portuguese — Intermediate"],
 jobs=[
  ("Research Technician 2","ESPOL","Guayaquil, Ecuador | 2024 – Present",[
    "Authoring indexed publications on GIS and remote sensing.",
    "Managing funding proposals for research projects.",
    "Leading the development of the Ecuadorian Geoportal of Ocean-Atmospheric Parameters (GEPOA) for satellite monitoring of ocean-atmospheric variables in Marine Protected Areas.",
    "Collaborator in the Brazilian HIDRA project (call CNPq/MCTI/FNDCT No. 06/2026, Faixa B) on ecosystem water use efficiency (Random Forest, XGBoost, SHAP, Google Earth Engine).",
    "Collaborator in the STARS project (Spatial Tools for Assessing Risks in Sudden Natural Hazards), funded by Erasmus+ (Capacity Building) and led by the University of Lisbon, developing GIS and BIM educational modules for risk assessment of sudden natural hazards (earthquakes, floods, landslides) at universities in Ecuador and Colombia.",
    "Participation in community outreach projects."]),
  ("Lecturer","Tecnológico Universitario Espíritu Santo","Guayaquil, Ecuador | 2022 – Present",[
    "Creating syllabi and content for the courses taught.","Academic planning and student follow-up.","Organizing extracurricular activities.","Community outreach projects."]),
  ("Oceanography and Meteorology Analyst","INOCAR","Guayaquil, Ecuador | 2022 – 2024",[
    "Using GIS tools and programming for navigation aids and vessel drift scenario modeling.","Maintenance of Ecuador's tide gauge and buoy network.","Database updating and collection of in situ and satellite data.","Participation in regional and coastal oceanographic cruises.","In charge of the directorate's spatial object catalog."]),
  ("Bioassay Coordinator & Scientist","CENAIM-ESPOL","Santa Elena, Ecuador (Internship) | 2017 – 2022",[
    "Statistical analysis and management of the center's spatial information.","Technician in charge of bioassays and the oceanographic/meteorological station.","Technical follow-up of the Annual Operating Plan."]),
 ],
 jobs_web=[
  ["Indexed publications on GIS and remote sensing; management of funding proposals.","Leading the development of the Ecuadorian Geoportal of Ocean-Atmospheric Parameters (GEPOA).","Collaborator in the HIDRA (Brazil) and STARS (Erasmus+) projects.","Community outreach projects."],
  ["Syllabus and content creation; academic planning and student follow-up.","Extracurricular activities and outreach projects."],
  ["GIS and programming for navigation aids and vessel drift modeling.","Maintenance of Ecuador's tide gauge and buoy network.","Databases, in situ and satellite data; oceanographic cruises; spatial object catalog."],
  ["Statistical analysis and management of the center's spatial information.","In charge of bioassays and the oceanographic/meteorological station; Annual Operating Plan follow-up."],
 ],
 projects=[
  ("GEPOA","ESPOL · Geoportal","Ecuadorian Geoportal of Ocean-Atmospheric Parameters: satellite monitoring in Marine Protected Areas.",None),
  ("HIDRA","CNPq/MCTI/FNDCT No. 06/2026 · Brazil","Ecosystem water use efficiency with Random Forest, XGBoost, SHAP and Google Earth Engine.",None),
  ("STARS","Erasmus+ · U. of Lisbon","GIS and BIM educational modules to assess risks from sudden natural hazards in Ecuador and Colombia.","https://stars-project.eu"),
  ("IPUS (doctoral thesis)","ESPOL · 2024 – present","Identification and Prediction of Urban Growth in Greater Guayaquil.",None),
 ],
 events=[
  ("IGARSS 2026","Invited speaker (IEEE). Washington, D.C., USA, August 2026."),
  ("XXV ISPRS Congress","Invited speaker (ISPRS). Toronto, Canada, July 2026."),
  ("Latin America GRSS and ISPRS Remote Sensing Conference (LAGIRS)","Tutor and invited speaker. Foz do Iguaçu, Brazil, November 2025."),
  ("Workshop: Downloading and processing satellite data with Python and GEE","Invited trainer, FICT-ESPOL. Guayaquil, Ecuador, October 2025."),
  ("The 2nd International Electronic Conference on Land","\"A Comparison of Supervised Classification Algorithms in Guayaquil Land Use and Land Cover Data\" — Invited speaker, MDPI. Online, Switzerland, September 2025."),
  ("AmeriGEO Week 2025","\"Building and using the RuPO Hub to address marine plastic\" — Invited speaker, GEO. Bogotá, Colombia, August 2025."),
  ("Pre-Antarctic Course","\"Teleconnections with Antarctica\" — Invited speaker, INOCAR. Guayaquil, Ecuador, December 2023."),
  ("Basic GIS course with QGIS","Invited trainer, UPSE. Santa Elena, Ecuador, December 2023."),
  ("World Oceans Day","\"Oceanography in Ecuador: what are we doing as a country?\" — Invited speaker, ESPOL. Guayaquil, Ecuador, June 2023."),
  ("Ecosystem Services","\"Remote Sensing and Valuation of Ecosystem Services\" — Invited speaker, CODSpace-UAndes. Online, Colombia, September 2020."),
 ],
 edu=[
  ("PhD in Engineering, Georesources track","ESPOL","2024 – Present",["Thesis: \"Identification and Prediction of Urban Growth in Greater Guayaquil (IPUS)\""]),
  ("Diploma in AI Applied to Teaching","Universidad de las Américas","2025",[]),
  ("M.Sc. in Geographic Information Systems and Science","Universität Salzburg & USFQ","2019 – 2021",[]),
  ("Environmental Ocean Engineer","ESPOL","2011 – 2015",[]),
 ],
 courses=["Certified drone pilot (40 h) — DGAC","Drone operation and handling (8 h) — ESPOL","Programming Language and Artificial Intelligence (8 h) — ESPOL","Oceanography Symposium 2024 (16 h) — ESPOL","Oceanography of the Equatorial Region (20 h) — ESPOL","Oceanographic Information Analysis and Processing with Python (40 h) — ESPOL","Design and implementation of a numerical model of wave transformation and overtopping on the Ecuadorian coast — SWASH model (80 h) — INOCAR","NASA ARSET: Introduction to NASA Earth Observations and Tools for Operational Wildfire Monitoring and Management","NASA ARSET: Monitoring Global Terrestrial Surface Water Height using Remote Sensing","NASA ARSET: Using Google Earth Engine for Land Monitoring Applications","NASA ARSET: Remote Sensing of Coastal Ecosystems","ESRI: 3D Visualization, Animation, Labeling, Layer Management, Raster Data and Coordinates in ArcGIS Pro"],
 courses_web=["Certified drone pilot (40 h) — DGAC","Oceanographic data analysis and processing with Python (40 h) — ESPOL","SWASH wave numerical model (80 h) — INOCAR","NASA ARSET: Google Earth Engine for land monitoring; remote sensing of coastal ecosystems; terrestrial surface water height; wildfire monitoring","ESRI: ArcGIS Pro (3D visualization, raster data, coordinates)"],
 awards=[("2026","Doctoral fellowship in Brazil, starting August."),("2025","Best oral presentation — The 2nd International Electronic Conference on Land (MDPI Land, Switzerland)."),("2023","Humboldt-Caldas Medal for the best work in Biogeography of Ecuador and Colombia (Colombian Academy of Exact, Physical and Natural Sciences, Bogotá)."),("2016–2017","Honor diploma for the best graduate of the program, 2016–2017 (ESPOL).")],
 ref_role="Research Professor", ref_role_m="Research Professor",
 footer="Guayaquil, Ecuador",
)

L["pt"] = dict(
 code="pt", name="Português", title="Divar Castro Rodas · Sensoriamento Remoto e SIG",
 desc="Doutorando em Engenharia (Georrecursos, ESPOL). SIG, sensoriamento remoto, LULC e modelagem urbana e ambiental.",
 role="Doutorando em Engenharia (Georrecursos) · M.Sc. em SIG · Engenheiro Oceânico Ambiental",
 role_full="Doutorando em Engenharia (Georrecursos) · M.Sc. em Sistemas de Informação Geográfica · Engenheiro Oceânico Ambiental",
 affil="ESPOL, Guayaquil, Equador",
 nav=[("experiencia","Experiência"),("proyectos","Projetos"),("publicaciones","Publicações"),("ponencias","Palestras"),("educacion","Formação"),("reconocimientos","Reconhecimentos")],
 email_lbl="✉️ E-mail", pdf_btn="📄 CV (PDF)",
 h=dict(about="Sobre mim",exp="Experiência profissional",proj="Projetos",pubs="Publicações",talks="Palestras e eventos",edu="Formação e capacitação",awards="Reconhecimentos e bolsas",
        profile="Perfil profissional",expcv="Experiência profissional",educv="Formação acadêmica",talkscv="Palestras e participação em eventos",courses="Cursos e capacitações",refs="Referências",
        contact="Contato",lang="Idiomas",skills="Habilidades técnicas",soft="Competências",interests="Outros interesses",selcourses="Cursos selecionados"),
 about=["Doutorando em Engenharia com menção em Georrecursos (ESPOL). Analista de informação oceanográfica e meteorológica com 9 anos de experiência em Sistemas de Informação Geográfica e sensoriamento remoto aplicados ao monitoramento ambiental e costeiro. Experiência em coordenação científica, análise estatística, gestão de projetos de pesquisa com financiamento e docência universitária. Colaborador ativo em projetos de pesquisa geoespacial no Equador e no Brasil."],
 skills=["SIG: QGIS, ArcGIS Pro","Programação: Python, R","Google Earth Engine","PostgreSQL / PostGIS","Sensoriamento remoto e imagens de satélite","Piloto de drones (UAV) certificado","Informática avançada"],
 skills_web=["QGIS","ArcGIS Pro","Python","R","Google Earth Engine","PostgreSQL / PostGIS","Sensoriamento remoto","Piloto UAV certificado"],
 soft=["Trabalho em equipe","Capacidade analítica","Comunicação eficaz","Proatividade","Coordenação científica"],
 interests=["Meio ambiente","Limpeza de praias","Visitas técnicas"],
 langs=["Espanhol — Nativo","Inglês — Fluente (B2)","Português — Intermediário"],
 jobs=[
  ("Técnico de Pesquisa 2","ESPOL","Guayaquil, Equador | 2024 – Atualmente",[
    "Elaboração de publicações indexadas na temática de SIG e sensoriamento remoto.",
    "Gestão de propostas de financiamento de projetos de pesquisa.",
    "Liderança no desenvolvimento do Geoportal Equatoriano de Parâmetros Oceano-Atmosféricos (GEPOA), para o monitoramento por satélite de variáveis oceano-atmosféricas em Áreas Marinhas Protegidas.",
    "Colaborador no projeto brasileiro HIDRA (chamada CNPq/MCTI/FNDCT Nº 06/2026, Faixa B), voltado à eficiência do uso da água em ecossistemas (Random Forest, XGBoost, SHAP, Google Earth Engine).",
    "Colaborador no projeto STARS (Spatial Tools for Assessing Risks in Sudden Natural Hazards), financiado pelo Erasmus+ (Capacity Building) e liderado pela Universidade de Lisboa, para o desenvolvimento de módulos educacionais de SIG e BIM na avaliação de riscos de ameaças naturais súbitas (sismos, inundações, deslizamentos) em universidades do Equador e da Colômbia.",
    "Participação em projetos de extensão com a comunidade."]),
  ("Docente","Tecnológico Universitario Espíritu Santo","Guayaquil, Equador | 2022 – Atualmente",[
    "Criação de ementas e conteúdo para as disciplinas ministradas.","Planejamento acadêmico e acompanhamento de estudantes.","Programação de atividades extracurriculares.","Projetos de extensão com a comunidade."]),
  ("Analista de Oceanografia e Meteorologia","INOCAR","Guayaquil, Equador | 2022 – 2024",[
    "Uso de ferramentas SIG e programação para auxílios à navegação e modelagem de cenários de deriva de embarcações.","Manutenção da rede maregráfica e de boias do Equador.","Alimentação de bases de dados e coleta de informação in situ e por satélite.","Participação em cruzeiros oceanográficos regionais e costeiros.","Responsável pelo catálogo de objetos espaciais da diretoria."]),
  ("Coordenador de Bioensaios e Cientista","CENAIM-ESPOL","Santa Elena, Equador (Estágio) | 2017 – 2022",[
    "Análise estatística e gestão da informação espacial do centro.","Técnico responsável por bioensaios e pela estação oceanográfica/meteorológica.","Acompanhamento técnico do Plano Operativo Anual."]),
 ],
 jobs_web=[
  ["Publicações indexadas em SIG e sensoriamento remoto; gestão de propostas de financiamento.","Liderança no desenvolvimento do Geoportal Equatoriano de Parâmetros Oceano-Atmosféricos (GEPOA).","Colaborador nos projetos HIDRA (Brasil) e STARS (Erasmus+).","Projetos de extensão com a comunidade."],
  ["Criação de ementas e conteúdo; planejamento acadêmico e acompanhamento de estudantes.","Atividades extracurriculares e projetos de extensão."],
  ["SIG e programação para auxílios à navegação e modelagem de deriva de embarcações.","Manutenção da rede maregráfica e de boias do Equador.","Bases de dados, informação in situ e por satélite; cruzeiros oceanográficos; catálogo de objetos espaciais."],
  ["Análise estatística e gestão da informação espacial do centro.","Responsável por bioensaios e pela estação oceanográfica/meteorológica; acompanhamento do Plano Operativo Anual."],
 ],
 projects=[
  ("GEPOA","ESPOL · Geoportal","Geoportal Equatoriano de Parâmetros Oceano-Atmosféricos: monitoramento por satélite em Áreas Marinhas Protegidas.",None),
  ("HIDRA","CNPq/MCTI/FNDCT Nº 06/2026 · Brasil","Eficiência do uso da água em ecossistemas com Random Forest, XGBoost, SHAP e Google Earth Engine.",None),
  ("STARS","Erasmus+ · U. de Lisboa","Módulos educacionais de SIG e BIM para avaliar riscos de ameaças naturais súbitas no Equador e na Colômbia.","https://stars-project.eu"),
  ("IPUS (tese de doutorado)","ESPOL · 2024 – presente","Identificação e Predição do Crescimento Urbano na Grande Guayaquil.",None),
 ],
 events=[
  ("IGARSS 2026","Palestrante convidado (IEEE). Washington, D.C., EUA, agosto de 2026."),
  ("XXV ISPRS Congress","Palestrante convidado (ISPRS). Toronto, Canadá, julho de 2026."),
  ("Latin America GRSS and ISPRS Remote Sensing Conference (LAGIRS)","Tutor e palestrante convidado. Foz do Iguaçu, Brasil, novembro de 2025."),
  ("Oficina: Download e processamento de dados de satélite com Python e GEE","Instrutor convidado, FICT-ESPOL. Guayaquil, Equador, outubro de 2025."),
  ("The 2nd International Electronic Conference on Land","\"A Comparison of Supervised Classification Algorithms in Guayaquil Land Use and Land Cover Data\" — Palestrante convidado, MDPI. Online, Suíça, setembro de 2025."),
  ("AmeriGEO Week 2025","\"Construção e uso do RuPO Hub para enfrentar o plástico marinho\" — Palestrante convidado, GEO. Bogotá, Colômbia, agosto de 2025."),
  ("Curso Pré-Antártico","\"Teleconexões com a Antártida\" — Palestrante convidado, INOCAR. Guayaquil, Equador, dezembro de 2023."),
  ("Curso básico de SIG com QGIS","Instrutor convidado, UPSE. Santa Elena, Equador, dezembro de 2023."),
  ("Dia Mundial dos Oceanos","\"Oceanografia no Equador: o que estamos fazendo como país?\" — Palestrante convidado, ESPOL. Guayaquil, Equador, junho de 2023."),
  ("Serviços Ecossistêmicos","\"Sensoriamento Remoto e Valoração dos Serviços Ecossistêmicos\" — Palestrante convidado, CODSpace-UAndes. Online, Colômbia, setembro de 2020."),
 ],
 edu=[
  ("Doutorado em Engenharia, menção em Georrecursos","ESPOL","2024 – Presente",["Tese: \"Identificação e Predição do Crescimento Urbano na Grande Guayaquil (IPUS)\""]),
  ("Diploma em IA Aplicada à Docência","Universidad de las Américas","2025",[]),
  ("M.Sc. em Sistemas e Ciências da Informação Geográfica","Universität Salzburg & USFQ","2019 – 2021",[]),
  ("Engenheiro Oceânico Ambiental","ESPOL","2011 – 2015",[]),
 ],
 courses=["Piloto certificado de drones (40 h) — DGAC","Operação e manejo de drones (8 h) — ESPOL","Linguagem de Programação e Inteligência Artificial (8 h) — ESPOL","Simpósio de Oceanografia 2024 (16 h) — ESPOL","Oceanografia da Região Equatorial (20 h) — ESPOL","Análise e Processamento de Informação Oceanográfica com Python (40 h) — ESPOL","Desenho e implementação de um modelo numérico de transformação e galgamento de ondas no litoral equatoriano — Modelo SWASH (80 h) — INOCAR","NASA ARSET: Introduction to NASA Earth Observations and Tools for Operational Wildfire Monitoring and Management","NASA ARSET: Monitoring Global Terrestrial Surface Water Height using Remote Sensing","NASA ARSET: Using Google Earth Engine for Land Monitoring Applications","NASA ARSET: Remote Sensing of Coastal Ecosystems","ESRI: Visualização 3D, Animação, Rotulagem, Gerenciamento de camadas, Dados raster e Coordenadas no ArcGIS Pro"],
 courses_web=["Piloto certificado de drones (40 h) — DGAC","Análise e processamento de informação oceanográfica com Python (40 h) — ESPOL","Modelo numérico de ondas SWASH (80 h) — INOCAR","NASA ARSET: Google Earth Engine para monitoramento terrestre; sensoriamento remoto de ecossistemas costeiros; altura da água superficial; monitoramento de incêndios","ESRI: ArcGIS Pro (visualização 3D, raster, coordenadas)"],
 awards=[("2026","Bolsa de doutorado no Brasil, a partir de agosto."),("2025","Melhor apresentação oral — The 2nd International Electronic Conference on Land (MDPI Land, Suíça)."),("2023","Medalha Humboldt-Caldas ao melhor trabalho de Biogeografia do Equador e da Colômbia (Academia Colombiana de Ciências Exatas, Físicas e Naturais, Bogotá)."),("2016–2017","Diploma de honra ao melhor formando do curso, período 2016–2017 (ESPOL).")],
 ref_role="Pesquisadora Docente", ref_role_m="Pesquisador Docente",
 footer="Guayaquil, Equador",
)

# ---------------------------------------------------------------- POSTS
# Agrega aquí las publicaciones/noticias en las que participas.
# (fecha por idioma, título, resumen por idioma, enlace, fuente)
POSTS = [
 dict(
  date=dict(es="Sep 2025", en="Sep 2025", pt="Set 2025"),
  title=dict(
    es="Investigador de FICT recibe reconocimiento internacional en conferencia organizada por MDPI Land",
    en="FICT researcher receives international recognition at conference organized by MDPI Land",
    pt="Pesquisador da FICT recebe reconhecimento internacional em conferência organizada pela MDPI Land"),
  desc=dict(
    es="Mejor presentación oral en The 2nd International Electronic Conference on Land, con la comparación de algoritmos de clasificación supervisada para LULC en Guayaquil.",
    en="Best Oral Presentation at The 2nd International Electronic Conference on Land, with the comparison of supervised classification algorithms for LULC in Guayaquil.",
    pt="Melhor apresentação oral na The 2nd International Electronic Conference on Land, com a comparação de algoritmos de classificação supervisionada para LULC em Guayaquil."),
  url="https://www.fict.espol.edu.ec/en/news/fict-researcher-receives-international-recognition-conference-organized-mdpi-land",
  source="FICT-ESPOL"),
]
POSTS_H = dict(es="Posts", en="Posts", pt="Posts")
POSTS_MORE = dict(es="Leer publicación →", en="Read post →", pt="Ler publicação →")
