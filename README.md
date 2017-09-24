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
	
Shell:
	python3 manage.py shell		// her kan du gjøre mye rart
```
Endre DB på nettsiden: 127.0.0.1:8000/admin	<br />

## GIT
Git er like kronglete, her er ofte brukte kommandoer.
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
Tekniker: 		Brukernavn: Kim K, 	passord: Kanye	
Tekniker:		Brukernavn: Eminem	passord: RapGod123
Bookingsjef:    	Brukernavn: Jay Z, 	passord: 99problems  	
Booking Ansvarlig :	Brukernavn: Drake, 	passord: Hotline Bling	
```
## Nettsider
Tentativ og UFULLSTENDIG oversikt over nettsider.
```
* Create Booking: to creat booking (added to DB)
* View Dates and Bookings: to view calender view with busy and available dates/scenes and concerts on scenes
* View Bookings: to accept/decline offer (change in DB)
* View Shifts: for technicians to view when they are to work
* Send Tech Needs: for manager to send technical needs
* View Tech Needs: to view tech needs for a band
* View Tech Crew: to view all tech crew for all bookings/concerts on all scenes at all times
* Send Booking Offer: to send a created booking offer to band after(?) accepted
```
