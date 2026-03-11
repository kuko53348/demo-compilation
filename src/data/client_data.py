from models.models_template import LobbyModelCard, QuestionTemplate, ClientProfileTemplate


class QuestionModel:
    questions: list = [
        QuestionTemplate(
            target = "✍ 1. Derechos laborales",
            questions_1 = "✔¿Cuáles son mis derechos laborales si no tengo documentación?",
            questions_2 = "✔¿Cómo puedo denunciar abusos laborales sin temor a represalias?",
            questions_3 = "✔¿Qué protección ofrece la ley contra la discriminación laboral?",
            questions_4 = "✔¿Puedo acceder a seguridad social y salud sin documentación?",
            questions_5 = "✔¿Cómo puedo obtener un contrato de trabajo formal?",
            reference = "https://dt.gob.cl/portal/1628/w3-propertyvalue-161036.html",
        ),
        QuestionTemplate(
            target = "✍ 2. Regularización migratoria",
            questions_1 = "✔¿Cuáles son los pasos para obtener una visa de trabajo en Chile?",
            questions_2 = "✔¿Qué opciones tengo si ingresé al país sin documentos?",
            questions_3 = "✔¿Cómo puedo solicitar la permanencia definitiva?",
            questions_4 = "✔¿Cuáles son los requisitos para cambiar mi estatus migratorio?",
            questions_5 ="✔¿Dónde puedo recibir asesoría legal gratuita sobre migración?",
            reference = "https://extranjeria.gob.cl"
        ),
        QuestionTemplate(
            target = "✍ 3. Protección contra abusos laborales" ,
            questions_1 = "✔¿Qué hacer si mi empleador no me paga el salario acordado?",
            questions_2 = "✔¿Cómo puedo denunciar explotación laboral o condiciones abusivas?",
            questions_3 = "✔¿Qué derechos tengo si sufro acoso o violencia en el trabajo?",
            questions_4 = "✔¿Cuáles son las sanciones para empleadores que contratan inmigrantes sin documentos?",
            questions_5 = "✔¿Cómo puedo acceder a la Inspección del Trabajo para denunciar irregularidades?",
            reference = "https://www.dt.gob.cl/portal/1611/w3-channel.html"
        ),
        QuestionTemplate(
            target = "✍ 4. Acceso a beneficios sociales",
            questions_1 = "✔¿Puedo acceder a atención médica sin un contrato formal?",
            questions_2 = "✔¿Cómo puedo inscribirme en el sistema de pensiones?",
            questions_3 = "✔¿Existen programas de apoyo para inmigrantes en situación vulnerable?",
            questions_4 = "✔¿Qué beneficios laborales pueden solicitar los trabajadores extranjeros?",
            questions_5 = "✔¿Cómo puedo acceder a capacitación laboral para mejorar mis oportunidades?",
            reference = "https://www.minsal.cl/atencion-extranjeros-en-chile/"
        ),
    ]

class ProfileModel:

    experience ="""
Estudios Jurídicos Laboralista
cargo: Abogada
periodo: 2019 - Presente

"""
    ProfileModel: list = [
        ClientProfileTemplate(
            avatar_image="avatar.jpg",
            name="Giselle Hernández Sanabria",
            carrer="Abogada Especialista en Derecho Laboral",
            location="Santiago, Chile",
            contact="linkedin: https://remotojob.com/remoter/giselle-hernandez/\nuniversidad\nUniversidad: Miguel de Cervantes",
            profile="\nAbogada cubana residente en Chile, egresada de derecho, con experiencia en estudios jurídicos laboralistas. Especializada en defensa de trabajadores, negociación colectiva y litigios por precarización laboral.",
            experience=experience,
            education="Universidad Miguel de Cervantes",
            graduation="Egresada en Derecho",
            skills="Litigios laborales\nNegociación colectiva Defensa de derechos fundamentales Interpretación del Código del Trabajo chileno",
            language="Español (Nativo)",
            academic="La precarización laboral y salarial derivada del régimen de subcontratación laboral año: 2021",
            responsability="\nDefensa de trabajadores en procesos judiciales.\nNegociación y asesoramiento en conflictos laborales.\nLitigios sobre precarización y condiciones laborales injustas.\n"
        ),
        ClientProfileTemplate(
            avatar_image="avatar_2.jpg",
            name="Dianelys Mesa Sanabria",
            carrer="Abogada Especialista en Derecho Laboral",
            location="Santiago, Chile",
            contact="linkedin: https://remotojob.com/remoter/giselle-hernandez/\nuniversidad\nUniversidad: Miguel de Cervantes",
            profile="\nAbogada cubana residente en Chile, egresada de derecho, con experiencia en estudios jurídicos laboralistas. Especializada en defensa de trabajadores, negociación colectiva y litigios por precarización laboral.",
            experience=experience,
            education="Universidad Miguel de Cervantes",
            graduation="Egresada en Derecho",
            skills="Litigios laborales\nNegociación colectiva Defensa de derechos fundamentales Interpretación del Código del Trabajo chileno",
            language="Español (Nativo)",
            academic="La precarización laboral y salarial derivada del régimen de subcontratación laboral año: 2021",
            responsability="\nDefensa de trabajadores en procesos judiciales.\nNegociación y asesoramiento en conflictos laborales.\nLitigios sobre precarización y condiciones laborales injustas.\n"
        ),
        ClientProfileTemplate(
            avatar_image="avatar_3.jpg",
            name="Christian javier Quesada Mesa",
            carrer="Abogada Especialista en Derecho Laboral",
            location="Santiago, Chile",
            contact="linkedin: https://remotojob.com/remoter/giselle-hernandez/\nuniversidad\nUniversidad: Miguel de Cervantes",
            profile="\nAbogada cubana residente en Chile, egresada de derecho, con experiencia en estudios jurídicos laboralistas. Especializada en defensa de trabajadores, negociación colectiva y litigios por precarización laboral.",
            experience=experience,
            education="Universidad Miguel de Cervantes",
            graduation="Egresada en Derecho",
            skills="Litigios laborales\nNegociación colectiva Defensa de derechos fundamentales Interpretación del Código del Trabajo chileno",
            language="Español (Nativo)",
            academic="La precarización laboral y salarial derivada del régimen de subcontratación laboral año: 2021",
            responsability="\nDefensa de trabajadores en procesos judiciales.\nNegociación y asesoramiento en conflictos laborales.\nLitigios sobre precarización y condiciones laborales injustas.\n"
        ),
    ]


class LobbyModel:

    """
    📌
    🔹 **Accede a información clara y actualizada sobre leyes y normativas**
    🔹 **Encuentra abogados especializados en La Serena y en todo Chile**
    🔹 **Obtén asesoría personalizada para resolver tus dudas legales**

    💼 **La justicia está a tu alcance. Comienza hoy tu consulta en Legalmente Chile.** 🚀

    """

    lobbyModelCard = LobbyModelCard(
            header='Abogamos Chile!',
            sub_header="📌 Tu portal de información y asesoría jurídica en Chile",
            body_text="🔹 Sabemos que acceder a orientación legal puede ser complicado, por eso\n🔹Legalmente Chile** está aquí para simplificarlo. Desde\n🔹derechos laborales hasta\n🔹contratación de abogados confiables\n🔹Nuestra plataforma te conecta con el conocimiento y los profesionales que necesitas.",
            help_info=" 🔥 Sin mas preambulos se encuentra con los mejores Abogados Laborales de la Serena."
        )