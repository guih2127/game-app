from game.models import *
from datetime import datetime

def apagar_dados():
	Game.objects.all().delete()
	Developer.objects.all().delete()
	Genre.objects.all().delete()
	Platform.objects.all().delete()
	Mode.objects.all().delete()
	Friends.objects.all().delete()
	UserRequests.objects.all().delete()
	User.objects.all().delete()
	UserGamesInformation.objects.all().delete()

def create_platforms():
	Platform.objects.bulk_create(
		[Platform(name="Playstation 4"),
		Platform(name="Xbox One"),
		Platform(name="Playstation 3"),
		Platform(name="Xbox 360"),
		Platform(name="PC")]
	)

def create_genres():
	Genre.objects.bulk_create(
		[Genre(name="RPG"),
		Genre(name="Action"),
		Genre(name="Puzzle"),
		Genre(name="Fantasy"),
		Genre(name="Japanese"),
		Genre(name="Fighting"),
		Genre(name="Indie"),
		Genre(name="Racing"),
		Genre(name="Soccer"),
		Genre(name="Sports"),
		Genre(name="MMORPG"),
		Genre(name="Rhythm"),
		Genre(name="Survival"),
		Genre(name="Stealth"),
		Genre(name="Shooter"),
		Genre(name="FPS"),
		Genre(name="Platform"),
		Genre(name="Simulation"),
		]
	)

def create_modes():
	Mode.objects.bulk_create(
		[Mode(name="Online"),
		Mode(name="Offline")
		]
	)

def create_developers():
	Developer.objects.bulk_create(
		[Developer(name="From Software", website="www.fromsoftware.com"),
		Developer(name="Eletronic Arts", website="www.ea.com"),
		Developer(name="Atlus", website="www.atlus.com"),
		Developer(name="Naughty Dog", website="www.naughtydog.com"),
		Developer(name="2K Games", website="www.2kgames.com"),
		Developer(name="Activision", website="www.activision.com"),
		Developer(name="Bamdai Namco", website="www.bamdai.com"),
		Developer(name="Bioware", website="www.bioware.com"),
		Developer(name="Blizzard", website="www.blizzard.com"),
		Developer(name="Microsoft Studios", website="www.microsoft.com"),
		Developer(name="Konami", website="www.konami.com"),
		Developer(name="Sega", website="www.sega.com"),
		Developer(name="Capcom", website="www.capcom.com"),
		Developer(name="Niantic", website="www.niantic.com"),
		]
	)

def create_games():
	persona5 = Game.objects.create(name="Persona 5", release_date=datetime(2016, 9, 16), developer=Developer.objects.get(name="Atlus"),metacritic=92,text='''Persona 5 é um jogo eletrônico de RPG desenvolvido pela Atlus. O jogo é cronologicamente a sexta edição da série Persona, que faz parte principalmente da franquia Megami Tensei.''')
	persona5.genre.add(Genre.objects.get(name="RPG")),
	persona5.genre.add(Genre.objects.get(name="Simulation")),
	persona5.platforms.add(Platform.objects.get(name="Playstation 4")),
	persona5.platforms.add(Platform.objects.get(name="Playstation 3")),
	persona5.modes.add(Mode.objects.get(name="Offline")),

	forzahorizon4 = Game.objects.create(name="Forza Horizon 4", release_date=datetime(2018, 10, 2), developer=Developer.objects.get(name="Microsoft Studios"),metacritic=92,text='''Forza Horizon 4 é um jogo de corrida em mundo aberto desenvolvido pela Playground Games em colaboração com a Turn 10 e publicado pela Microsoft Studios. É o quarto da franquia Forza Horizon e o décimo primeiro da edição Forza, tem data de lançamento para 02 de outubro de 2018 exclusivamente para Xbox One e Windows 10.''')
	forzahorizon4.genre.add(Genre.objects.get(name="Racing")),
	forzahorizon4.genre.add(Genre.objects.get(name="Sports")),
	forzahorizon4.platforms.add(Platform.objects.get(name="Xbox One")),
	forzahorizon4.platforms.add(Platform.objects.get(name="Xbox 360")),
	forzahorizon4.modes.add(Mode.objects.get(name="Offline")),
	forzahorizon4.modes.add(Mode.objects.get(name="Online")),

def create_users():
	User.objects.create_user(username="guih21", email="guih21@hotmail.com", password="123456", first_name="Guilherme", last_name="Araujo"),
	User.objects.create_user(username="lucas89", email="lucas89@gmail.com", password="123456", first_name="Lucas", last_name="Manini"),
	User.objects.create_user(username="matheusramos8", email="matheusramos871@gmail.com", password="123456", first_name="Matheus", last_name="Ramos"),

def create_reviews():
	Review.objects.create(game=Game.objects.get(name="Persona 5"), author=User.objects.get(username="guih21"), text="Ótimo jogo! Me diverti muito jogando ele.", note=9)

apagar_dados()
create_users()
create_developers()
create_platforms()
create_genres()
create_modes()
create_games()
create_reviews()