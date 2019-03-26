from game.models import *

def erase_data():
	Game.objects.all().delete()
	Developer.objects.all().delete()
	Genre.objects.all().delete()
	Platform.objects.all().delete()
	Mode.objects.all().delete()
	Friends.objects.all().delete()
	UserRequests.objects.all().delete()
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

