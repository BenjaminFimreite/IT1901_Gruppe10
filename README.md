# IT1901_Gruppe10

Hei alle sammen :-) 

## LES MEG!
Det er litt kronglete å jobbe med django, så her er en liter recap.
```
KJØRE Django Server:	
	python3 manage.py runserver	// Siden nåes via 127.0.0.1:8000 	
	
NY App:	
	python3 manage.py startapp ‘appnavn’
	
Migrate modeller inn i database (SQLite):
	python3 manage.py makemigrations
	python3 manage.py migrate
***merge
	python3 manage.pu makemigrations --merge
	
Shell:
	python3 manage.py shell		// her kan du gjøre mye rart
	
Legge til permission på bruker i 'shell':
// Forutsetter at det finnes en klasse i roles.py med permission du ønsker å legge til...
	from django.contrib.auth.models import User
	from rolepermissions.roles import AbstractUserRole
	user = User.objects.get(id=1)   // hent ønsket user
	assign_role(user, 'doctor')     // doctor er rollen
	
```
Endre DB på nettsiden: 127.0.0.1:8000/admin	<br />

## GIT
Git kommandoer:
```
// Først... la oss gjøre våre egne, lokale endringer klare... vi sier at git skal vite om disse
git add .	
git commit -m «melding»	

// Så kan vi sette sammen vår kode med den som ligger på remote repo (github.com)
git pull	
// Fiks eventuelle konflikter NÅ, FØR PUSH!!!
// Etter at alt er fiksa kan vi dele våre endringer med resten av gruppa ved å pushe
git push	

// Om det blir problemer med merging kan du kjøre dette (da resettes alt du har lokalt til det som ligger på git, så alle endringer du har gjort siden forrige pull forsvinner):
git fetch --all 
git reset --hard origin/master 

git status	// Viser status om filer, tracked, untracker, nye og endrede filer er røde	
git branch	// Viser alle branches, og den du er i nå
git branch minNyeBranch		// Lager en ny branch med navnet 'minNyeBranch'
git checkout branchName		// Flytter det til 'branchName'
```
## Roller i DB
```
Superuser:		Brukernavn: admin, 	passord: qwerty123	
Arrangør:       	Brukernavn: Rihanna, 	passord: Umbrella  	
Tekniker: 		Brukernavn: KimK, 	passord: Kanye	
Tekniker:		Brukernavn: Eminem	passord: RapGod123
Bookingsjef:    	Brukernavn: JayZ, 	passord: 99problems  	
Booking Ansvarlig :	Brukernavn: Drake, 	passord: Hotline Bling	
Manager:		Brukernavn: Man,	passord: qwerty123
PR Ansvarlig		Brukernavn: Nas		passord: qwerty123
Servering Ansvarlig:	Brukernavn: DinerDash	passord: qwerty123
```
## Nettsider
Fullstendig oversikt over nettsider.
```
* Create Booking: to creat booking (added to DB)
* Manage shifts/My shifts: view all registered shifts or view shifts you are registered at
* Bookings: view all bookings and click button to view more information (including pr information) about the specific booking
* Overview: full overview of coming concerts, archive, archive by genre, and scene overview
* Pending Bookings: to accept/decline booking offer
* Bands: view all registered bands and click button to view more information about the spcific band
* Send technical requirements: for manager to send technical requirements
* Manager register songs: to register new songs
```
