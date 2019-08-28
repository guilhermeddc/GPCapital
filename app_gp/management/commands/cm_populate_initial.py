from django.core.management.base import BaseCommand
from app_gp.models import *


class Command(BaseCommand):

    def handle(self, *args, **options):

        ChoicesCustomerService.objects.all().delete()
        ChoicesEthnicity.objects.all().delete()
        ChoicesEyeColor.objects.all().delete()
        ChoicesGenre.objects.all().delete()
        ChoicesHairColor.objects.all().delete()
        ChoicesLanguage.objects.all().delete()
        ChoicesPaymentAccepted.objects.all().delete()
        ChoicesPlace.objects.all().delete()
        ChoicesQuestion.objects.all().delete()
        ChoicesServicesOffered.objects.all().delete()

        customer_service = ["Casais", "Mulheres", "Homens", "Deficiente física"]
        for obj in customer_service:
            ChoicesCustomerService.objects.create(customer_service=obj)

        ethnicity = ["Branco", "Mestiço", "Mulato", "Negro", "Oriental", "Pardo"]
        for obj in ethnicity:
            ChoicesEthnicity.objects.create(ethnicity=obj)

        eye_color = ["Azuis", "Castanhos", "Verdes", "Outras cores"]
        for obj in eye_color:
            ChoicesEyeColor.objects.create(eye_color=obj)

        # eye_color = ["Azuis", "Castanhos", "Verdes", "Outras cores"]
        # for obj in eye_color:
        #     ChoicesGenre.objects.create(eye_color=obj)

        hair_color = ["Loiros", "Ruivos", "Castanhos", "Pretos", "Grisalhos", "Outras cores"]
        for obj in hair_color:
            ChoicesHairColor.objects.create(hair_color=obj)

        choices_languages = ["Português", "Inglês", "Espanhol", "Alemão"]
        for obj in choices_languages:
            ChoicesLanguage.objects.create(language=obj)

        choices_payment_accepted = ["Cartão de crédito", "Cartão de débito", "Dinheiro"]
        for obj in choices_payment_accepted:
            ChoicesPaymentAccepted.objects.create(payment=obj)

        choices_place = ["Local próprio", "Hotéis / Motéis / Domicílio", "Eventos", "Viagens"]
        for obj in choices_place:
            ChoicesPlace.objects.create(place=obj)

        choices_question = [
            "Como você gosta que seus clientes lhe tratem?",
            "Como você se excita mais?",
            "Como você se veste para receber seus clientes?",
            "E a bebida que mais gosta qual seria?",
            "É mais caseira ou de balada?",
            "Em qual momento do dia você se sente sexy?",
            "Gosta de animais? Tem algum bichinho?",
            "Gosta de atender mulheres?",
            "Gosta de ver filmes pornôs?",
            "Goza mais fácil na penetração ou com sexo oral?",
            "Já teve experiências com pessoas do mesmo sexo?",
            "O que um homem deve fazer pra chamar sua atenção?",
            "O que um homem deve fazer pra te encher de tesão?",
            "O que você acha que os homens não sabem sobre as mulheres e deveriam saber?",
            "O que você ama comer mas tem que maneirar pra não engordar?",
            "O que você faz para se manter assim bonita?",
            "O que você gosta de fazer nas horas livres?",
            "O que você gosta de fazer pra dar prazer a um homem?",
            "O que você mais ama no mundo?",
            "O que você usa para dormir?",
            "Prefere cinema ou teatro?",
            "Prefere dias quentes pra usar decote e mostrar as pernas ou o frio pra se sentir elegante?",
            "Quais são seus principais charmes de conquista? Suas armas de sedução?",
            "Qual a cor de lingerie você acha que fica perfeita em você?",
            "Qual a fantasia sexual que gostaria de realizar?",
            "Qual a maior loucura sexual que você já fez?",
            "Qual a parte do seu corpo te dá maior prazer quando tocam?",
            "Qual a parte do seu corpo você mais gosta?",
            "Qual a pior cantada você já recebeu?",
            "Qual a principal qualidade que um homem deve ter?",
            "Qual culinária você prefere para um jantar romântico?",
            "Qual elogio você mais recebe?",
            "Qual fantasia sexual realizou que foi inesquecível?",
            "Qual foi a maior proposta indecente que você já recebeu?",
            "Qual o perfume você usa como arma de sedução?",
            "Qual parte do seu corpo você acha mais sensual?",
            "Qual posição mais gosta de fazer sexo?",
            "Qual posição você mais gosta na cama?",
            "Qual principal elogio você gosta de receber?",
            "Qual seu prato preferido?",
            "Qual sua bebida preferida?",
            "Qual sua posição sexual preferida?",
            "Qual tipo de homem mexe com você?",
            "Quando você está carente o que você faz?",
            "Quantos orgasmos que você já teve em uma relação?",
            "Que tipo de balada você curte?",
            "Que tipo de cantada funciona com você?",
            "Que tipo de música você gosta de ouvir?",
            "Se eu fosse te levar pra jantar, qual restaurante você ia preferir?",
            "Se eu te desse uma passagem pra você viajar pra qualquer lugar do mundo, que lugar escolheria?",
            "Tem algum presente que você gosta de ganhar?",
            "Tem alguma fantasia não realizada?",
            "Um assunto que você acha chato?",
            "Um lugar hoje para descansar?",
            "Uma assunto que você não gosta?",
            "Você acha que vale tudo entre quatro paredes?",
            "Você curtiu a experiência?",
            "Você é mais de dar prazer ou de receber?",
            "Você é mais do tipo assanhada ou tímida?",
            "Você gosta de fazer sexo ouvindo música?",
            "Você já se apaixonou por algum cliente?",
            "Você já transou com dois homens ao mesmo tempo?",
            "Você já transou em locais públicos?",
            "Você parte pra cima quando quer conquistar alguém ou fica na sua?",
            "Você pratica algum esporte?",
            "Você prefere viajar pra praia ou pro campo?"
        ]
        for obj in choices_question:
            ChoicesQuestion.objects.create(question=obj)

        choices_services_offered = [
            "Acompanhante",
            "Ativa",
            "BDSM",
            "Beijo grego",
            "Beijo na boca",
            "Brinquedos eróticos",
            "Banho juntos",
            "Chuva dourada",
            "Chuva negra",
            "Dominação",
            "Deixa fotografar",
            "Dupla penetração",
            "Fetiche",
            "Gozo facial",
            "Inversão de papéis",
            "Masturbação",
            "Massagem prostática",
            "Massagem tântrica",
            "Massagem erótica",
            "Massagem tailandesa",
            "Massagem espanhola",
            "Massagem nuru",
            "Massagem relaxante",
            "Massagem com óleo e mãos",
            "Massagem com os pés",
            "Namoradinha",
            "Passiva",
            "Podolatria",
            "Seios naturais",
            "Striptease",
            "Swingers",
            "Sexo anal",
            "Sexo grupal",
            "Sexo oral",
            "Sexo vaginal"
        ]
        for obj in choices_services_offered:
            ChoicesPlace.objects.create(services=obj)

        self.stdout.write(self.style.SUCCESS('INSERTED!'))
