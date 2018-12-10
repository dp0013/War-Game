# -*- coding: utf-8 -*-
"""
Created on Sun Oct 14 04:14:09 2018

@author: D. Plyler
"""
import random
import time
#import emoji

secbreak = str('-' * 50)  #create global variable for 'section breaks'
#print(secbreak)

class War:  #Establish the War class with supporting attributes
    
    #generate random action variables
    def random_letter():
        rand_actions = ['a', 'b', 'c']
        return random.choice(rand_actions)
    #generate random numbers between 1 and 3 for random numerical options
    def random_number():
        for x in range(1):
            return random.randint(1,3)
    #generate random reply variables for input errors
    def random_error():
        rand_err = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
        return random.choice(rand_err)
    #generate random country
    def random_country():
        rand_country = ['Germany', 'Britain', 'France']
        return random.choice(rand_country)

    #first menu            
    def play():
        play = input("Would you like to play a game?  Please answer 'Y' or 'N':  ")
        if play.lower() == 'y':  #player has balls
            print()
            print("Great!  For this game, responses for choosing your path are done by entering one of the single-letter options provided in brackets [].")
            print()
            print("The year is 1989.  The United Soviet Socialist Republics (USSR) is in a state of disarray as it has been losing its grip on several socialist countries that have become vulnerable to, or completely fallen under pressure of, capitalist-driven revolts and revolutions.  In an unprecedented and even more unexpected move, the USSR just launched a missile toward Malmstrom AFB, Montana.")
            print()
            War.first_move()
        elif play.lower() == 'n':  #player is a wuss
            print()
            print("Laaammmeee....let's talk again when you are more exciting.")
            print(secbreak)
        else:  #player is an idiot
            for i in range(0,3):
                time.sleep(1.5)
                print("Buehler...?")
                print()
                i+=1
            time.sleep(1.5)    
            print("WAKE UP!")
            print(secbreak)
            War.play()
            
            
    def first_move():
        firstMove = input("How should we respond?  Our current available options are to either launch a missile [L] or try to contact USSR leadership (Mikhail Gorbachev) directly [C].  Choose one quickly:  ")
        if firstMove.lower() == 'l':  #player launches
                print()
                print(secbreak)
                print("Launching a missile...you're a brave soul.")
                print()
                War.missile1()
        elif firstMove.lower() == 'c':  #player chooses to communicate
            print()
            print(secbreak)
            print("Calling Gorbachev now...let's hope he's home!")
            print()
            War.communicate()
        else:  #erroneous input:
            print()
            War.errors()
            print(secbreak)
            War.first_move()
            
        
    def missile1():
        target1 = input("Should we target a populated [P] or rural [R] area?  Choose:  ")        
        if target1.lower() == 'p':
            print()
            print(secbreak)
            print("It's been an hour since we launched a missile at a heavily populated area.  Reports are coming in of heavy casualties; thousands have been instantly vaporized, from what we can tell.  No word on Gorbachev or other leadership.")
            print()
            War.second_move()
        elif target1.lower() == 'r':
            print()
            print(secbreak)
            print("It's been an hour since we launched a missile at a rural area. Reports are coming in of very limited casualties, but strong rhetoric from Soviet leadership.")
            print()
            War.second_move()
        else:  #erroneous input
            print()
            War.errors()
            print(secbreak)
            War.missile1()
            
           
    def second_move():
        secondMove = input("I'm afraid our options at this point are limited.  We can either call an ally [A] for assistance or try to call the USSR leadership [C].  We could also task some reconnaissance assets in an effort to gain more intelligence regarding our adversary's current status and intentions [R].  How should we proceed?  ")
        if secondMove.lower() == 'a':  #call ally
             print()
             print(secbreak)
             print("There's no shame in calling a friend for help.....is there?")
             c = War.random_country()
             c.rstrip()
             print()
             print("You roll the dice and decide to contact", c, ", who have proven themselves to be reliable allies in the past. ")
             print()
             War.ally(c)
        elif secondMove.lower() == 'c':  #communicate with USSR
            print()
            print(secbreak)
            print("""You task your communications officer to make the call on a red line to the Kremlin.  As you privately debate whether you hope he actually survived your retaliatory attacks, your comms officer shouts out, "Calling Gorbachev." """)
            print()
            War.communicate()
        elif secondMove.lower() == 'r':  #leverage reconnaissance assets
            print()
            print(secbreak)
            print("After quickly debating the utility of trying to contact the Kremlin directly versus reaching out to allies for assistance in what might appear to some as an act of desperation, you opt to task reconnaissance planes and available spy satellites instead in an effort to gain more information.  After several days of mixed reporting, various intelligence reports have begun to trickle in. ")
            print()
            War.recon()
        else:  #erroneous input
            print()
            War.errors()
            print(secbreak)
            War.second_move()
           
            
    def recon():
        x = War.random_letter()        
        if x == str('a'):  #contact USSR
            print("Our latest intelligence indicates Soviet forces have been severely crippled.  At this point, the most advisable option is to contact USSR leadership directly.")
            print()
            War.communicate()
        elif x == str('b'):  #strike again
             #  NEED TO CHANGE THIS PART OF THE STORY TO MATCH THE LAUNCH THREAT.  DIPLOMACY IS NOT GOOD IF USSR PREPPING FOR ANOTHER LAUNCH.
             print("Satellite imagery indicates Soviet forces have barely been affected.  They are preparing for another launch.")
             print()
             print(""" "Damn it!  We need to end this quickly!  Get me Gorbachev on the line NOW!"  Your operator fumbles for the numbers, but connects you quicker than he ever has before to any number ever in the history of ever.""")
             print()
             War.communicate()
        elif x == str('c'):  #sabotage
            print("Our imagery indicates few Soviet resources remain mobilized and operative.  We should be able to sabotage all remaining imminent threats to buy time.")
            print()
            War.sabotage()
        
        
    #  NEED TO UPDATE THIS SECTION AND EVEYTHING ELSE AFTER IT    
    def sabotage():
        sabotage = input("Deciding to take advantage of our adversary's vulnerable state, we may send in saboteurs to ensure any imminent threat capabilities are taken offline.  Should we send in an available SEAL Team [S] or rely on CIA assets [C] across Europe?  ")
        if sabotage.lower() == 's':  #send SEAL Team
             print()
             print(secbreak)
             print("Opting for a more surgical approach, you task Naval Special Warfare Group (NSWG) 2 to deploy the appropriate resources in an effort to identify and sabotage all imminent threat capabilities within reach.  ")
             print()
             War.seals()
        elif sabotage.lower() == 'c':  #task CIA assets
            print()
            print(secbreak)
            print(""" "Get me the CIA Chief.  We need a covert hand in this ASAP." """)
            print()
            War.cia()
        else:  #erroneous input
            print()
            War.errors()
            print(secbreak)
            War.sabotage()      

           
    def diplomacy():
        print("Given the current situation and recent developments, diplomacy may be the best option at this time.  However, the recent attacks have made traditional diplomatic overtures less than palpable to the American people; this will require less transparent and perhaps unorthodox methods.")
        print()
        print("We could solicit an ally for assistance as a proxy [A] or we could send a trusted, unofficial representative with good relations to speak on our behalf [U].  Your Chief of Staff, who normally never chimes in, offers a third, less desirable option: conduct a secret, in-person visit with Gorbachev himself in a neutral country [I].")
        diplomacy = input("Whichever path we take, it will require the most careful of planning, the highest level of confidentiality, and the most delicate of handling.  Which option would you prefer: solicit an ally [A], communicate via an unofficial representative [U], or arrange to meet Gorby in-person [I]?  ")
        if diplomacy.lower() == 'a':  #solicit ally
             c = War.random_country()
             c.rstrip()
             print()
             print("You roll the dice and decide to contact", c, ", who have proven themselves to be reliable allies in the past.  ")
             return c
             print()
#             print(secbreak)
             War.ally(c)
        elif diplomacy.lower() == 'u':  #send unofficial rep
            print()
            print("Your Chief of Staff contacts Donald Trump, who alleges to have great relations with several senior Soviet officials through first- and second-hand affiliations, both private and professional.  One of these contacts, only identified as 'Sergei,' offers to relay any important communiques to the Foreign Minister.")
            print()
            print(secbreak)
            War.rep()
        elif diplomacy.lower() == 'i':  #leverage reconnaissance assets
            print()
            print("Within two days, you are en route to Switzerland to meet with Gorbachev, his Ministers of Defense and Foreign Affairs. ")
            print(secbreak)
            War.meeting()
        else:  #erroneous input
            print()
            War.errors()
            print(secbreak)
            War.diplomacy() 
            

    def communicate():
        x = War.random_letter()        
        if x == 'a':  #Gorbachev answers
            print("""After ringing for what seems like hours, the ring tones finally stop.  You hear a static-riddled click, followed by a familiar voice.  "Dobroye den, my friend!  I see we have problem.  BIG problem."  Suspecting he's been drinking -- understandable, given the current situation -- you recollect your thoughts and respond deliberately and confidently: "Da." """)  
            print()
            print("Invoking the 'pregnant pause' tactic, you refuse to say anything further and allow him to fill in the empty, awkward silence in a desperate effort to gain more insight into his intentions.  After about 5 very awkward, long, silent seconds, Gorbachev indicates he is willing to come to the table and allow you to present your case as to why you launched a missile at his country.  Stunned, you realize either Gorby has lost his mind or lost control of his country; neither is a good situation.")  
            comm = input("Do you accept [A] or reject [R] his offer?  ")
            print()
            if comm.lower() == 'a':
                print("You tell your Chief of Staff to prepare your chopper for a trip to Air Force One.  You're going to Switzerland to meet with Gorby.")
                print()
                print(secbreak)
                War.meeting()
                print()
            elif comm.lower() == 'r':
                print("You tell Gorbachev what is basically the political equivalent of 'shove it' and warn him that there will be another 'gift' inbound.  He shouts something in Russian which you are sure is anything but an offer to surrender or otherwise accept responsibility right before the line cuts out.  THIS.  IS.  WAR!")
                print()
                print(secbreak)
                War.missile1()
            else:
                War.errors()
                print(secbreak)
                War.communicate()
        elif x == 'b':  #Sergei answers
            print(""" "Hello Comrade President.  President Gorbachev is...unavailable at the moment.  However, I am authorized to speak on his behalf.  I am called Sergei.  Let's meet in person and discuss this....unfortunate turn of events."  You are confused and concerned at once; but you must respond decisively...and quickly.""")
            comm = input("Do you accept [A] or reject [R] his offer?  ")
            print()
            if comm.lower() == 'a':
                print("You tell your Chief of Staff to prepare your chopper for a trip to Air Force One.  You're going to Switzerland to meet with Gorby.")
                print()
                print(secbreak)
                War.meeting()  
            print()
            if comm.lower() == 'r':
                print("You tell Gorbachev what is basically the political equivalent of 'shove it' and warn him that there will be another 'gift' inbound.  He shouts something in Russian which you are sure is anything but an offer to surrender or otherwise accept responsibility right before the line cuts out.  This is war.")
                print()
                print(secbreak)
                War.missile1()            
        else:  #no one answers
            print("After a full minute of ringing, no one answers your call.  But there may be another option to reach out to your new 'frenemy' via an intermediary....")
            c = War.random_country()
            print()
            print("You roll the dice and decide to contact", c, ", who have proven themselves to be reliable allies in the past.  ")
            print()
            print(secbreak)
            War.ally(c)
   
    
    def ally(c):  #call ally
        if c == 'Germany':  #call Germany
            print(""" "Guten tag, meine freund! Was ist los mit die welt heute??"  (German leadership has never been very shy about getting to the point, which you usually appreciate.)  You inform your German counterpart that your launch was a retaliatory attack for the USSR's initial launch at Malmstrom AFB, MT, at which point you are interrupted.  "Don't vorry, my friend!  Vee vill assist in any vay possible." """)
            print()
            print("Germany states they will contact the Kremlin and intervene on your behalf, assuring you that they will not leave USSR any doubt regarding their solidarity with the American people on this issue.  After hours of waiting for Germany to call you back, you get the call for which you've been anxiously waiting.")
            print()
            print(""" "Guten abend, meine freund!  Vell, vee spoke viss zee Kremlin and zay say dis is all just big misunderstanding, ya?  Zay say dat one of der officers tried to make a coup and launch missile to start velt var tree."  You conceal your true thoughts regarding this shocking news as you reply, "We are happy to hear this was an anomaly and trust that the situation is under control at this time."  "Vell, der ist one problem ztill; zey fear zat admitting ziss problem vill embolden any potential revolutionary factions to act against der gowernment.  Zo, you zee, zay vant dat zee US claim rezponzibility, ya?" """)
            print()            
        elif c == 'France':  #call France
            print(""" "Bon jour! C'est va?  We suspect not very good, from zee smell of things."  Wishing you had studied more French instead of French exchange students in school, you inform your German counterpart that your launch was a retaliatory attack for the USSR's initial launch at Malmstrom AFB, MT.  "Well this is unfortunate for you.  However, we are in a very precarious position."  (You decide not to make any jokes at this comment as it wouldn't be prudent, nor would it likely be understood by the French.""")   
            print()
            print(""" "As you know, we have negotiated many beneficial energy and trade deals with Gorbachev over the last six months.  Unfortunately, we cannot afford to intervene at this time.  Le sigh.  We are willing to sell you some of our best wines and cheese to assist with your current situation, if desired."  Keenly aware that your calls are all recorded as part of the official historical record, you reserve some very 'choice' words for any future in-person meetings with French leadership....if you survive this.""")
            print()          
            print(""" "Well sacre bleu and SCREW YOU, TOO, France!"  Probably not the most diplomatic response before you slam the phone down, but at this point, you really don't care.  "Call Britain or Germany; France is dead to me!"  Your operator dials another number....""")
            print()
            print(secbreak)
            c = War.random_country()
            if c == 'France':
                print(""" After a few seconds, you hear a voice.  "Oh I see you have come to your zenses, mais oui!"  "What the...?!?  GOD DAMN IT!  I dont' want to speak with France again...EVER!  Get me someone else!  ANYONE ELSE!"  You slam the phone down and give your operator a look of heavy disapproval.""")
                print()
                print(""" "Sorry!" answers yoru operator while dialing a number feverishly.  "Okay, I have another one on the line!" """)
                j = ['Germany','Britain']
                c = random.choice(j)
                print(secbreak)
                War.ally(c)
            else:
                print(secbreak)
                War.ally(c)
                
        elif c == 'Britain':  #call Britain
            print(""" "Good day, 'governor!  What in the bloody hell is going on over there?  I say, old chap, we allow you colonies to rule on your own and the whole bloody world goes to..."  You cut off your English counterpart as time is precious and, quite frankly, the accent is just a little condescending at this point.""")
            print()
            print("""In the interest of time, you decide not to remind them of America's assistance during those little 'blips' in history known better as 'World War I' and 'World War II' and inform your less than cheery counterpart that your launch was a retaliatory attack for the USSR's initial launch.  "Ah.  I see.  Well, we will see what we can do.  I shall contact the Kremlin and ring you within minutes."  Although relieved at the offer to intervene, you decide not to hold your breath.""")
            print()
            print("""After what seems like an eternity, the phone rings.  "Allo, old chap!  We have good news and bad news; which would you like first?"  Having had your fill of bad news, you opt for the good first.  "Well, it seems one of our Soviet 'comrades' attempted to start a coup with a rogue missile attack."  You conceal your true thoughts regarding this shocking news as you reply, "We are happy to hear this was an anomaly and trust that the situation is under control at this time."  "Agreed, but the less palpable news is that there may be more subversive elements in the ranks.  Admitting the Kremlin's momentary loss of control might embolden any potential revolutionary factions, resulting in further rogue actions.  They would prefer if the US takes the fall for this one, in order to prevent more potential chaos within the Soviet ranks, you see." """)
            print()
            print(secbreak)                      
        print(""" "Well this is a kick in the n**s," you think to yourself, but you quickly remind yourself it could have been much worse as no populated areas were targeted in your country.  Still, the story that America launched a first strike would be hard to sell to the American people and other nations in general.  Further, even if the story was believable, the potential fallout (pun intended) of such an aggressive and unprovoked attack would be a public relations nightmare.""")
        print()
        print("""You realize there are only 3 viable options:  lie to the American public in the interest of helping prevent a potentially even worse crisis in the USSR [L]; reject the USSR proposition by telling the truth [T], detailing the events to the public as they really happened while risking all-out revolution in the USSR and extended global nuclear war; or decide based on a time-trusted method for settling major disputes going back hundreds of years: the game of rock, paper, scissors [R]. """)
        #select an option:
        ally = input("Which will it be?  Lie to the American public [L], tell the truth [T], or play rock, paper, scissors [R]?  ")
        print()
        if ally.lower() == 'l':  #lie to the world, but help USSR save face
            print(secbreak)
            print("You decide that lying to the American public and the world about the details of the event is more palatable as the alternative would surely result in more attacks carried out by an emboldened Soviet insurgency.  You immediately hold an impromptu press conference in the interest of saving time and potentially getting ahead of any further attacks; however, as you start to speak, your SecDef whispers in your ear.  You cancel the press conference and swiftly leave the room.  The reporters, though confused and left without any information, begin to report on what just happened, if nothing else.")
            print()
            print(secbreak)
            War.end_planeCrash()
        elif ally.lower() == 't':  #tell truth but risk global nuclear war
            print()
            print("You opt to tell the truth and go it alone as Moscow is obviously not willing to cooperate.  As you gather your staff to prepare for the press conference, your SecDef whispers in your ear.  You hear the first few words, but then everything is a blur as your head starts to spin....")
            print()
            print(secbreak)
            War.end_planeCrash()
        elif ally.lower() == 'r':  #rock, paper, scissors!
            print()
            print(secbreak)
            War.rps()
        else:
            print()
            War.errors()
            print(secbreak)
            War.ally(c)         
        
    def rps():  #rock, paper, scissors
        print("You board Air Force One en route to what the world thinks is a peace summit and truce agreement with Mikhail Gorbachev and the USSR in Geneva, Switzerland.  After a fairly quick and relaxing flight, you land in Switzerland.  The Secret Service quickly ferries you away to the site of the summit, where the Russians are already waiting in a private, secured conference room.  The USSS and Russian security services secure the room after you enter, requesting only the presence of Gorbachev and his closest advisers along with yours.")
        print()
        print(""" "Well, Mikhail, it has been too long.  I hate that we must meet under these circumstances."  "Da, I agree.  You must understand we have some corrupt dogs in ranks; although few, they have strong bite.  As Russian say, 'they baby bears...but they still bears.'"  You both chuckle at this, although the underlying and potentially devastating implications are well understood by both sides.  You wonder to yourself if the success of capitalism, having inspired a select few within the Soviet ranks to take drastic, revolutionary measures, may ironically be to blame for eventually starting World War III.  But you make neither mention of this nor ask Gorbachev's opinion as both are moot at this stage.  "So, Gorby, do we settle this the way we make all our major decisions, as agreed?" """) 
        print()
        print(""" "Da!  This how I chose my wife, and has never failed me in all major decision regarding all Communist Party General and Secretary selection.  Look at Nicolae Ceausescu!  Romania is stellar example of peaceful Soviet Republic!"  Deciding it would be best to not go into lengthy discourse on the CIA's recent reports you've read on Romania suffering from serious revolts and uprisings among the populace and laborers, you extend your closed fist instead.  Gorbachev fist-bumps you with his, then you both start to count to three while shaking fists up and down on each count....""")
        print()
        print(secbreak)
        War.USA()
    
    def USA():
        #rock =1, paper =2, scissors =3
        USA = input("Which will you choose: Rock ([R], Paper [P], or Scissors [S]?  ")
        print()
        if USA.lower() == 'r':
            USA = 1
        elif USA.lower() == 'p':
            USA = 2
        elif USA.lower() == 's':
            USA = 3
        else:
            War.errors()
            print(secbreak)
            War.USA()            
        War.random_number()  
        USSR = War.random_number()  #randomly assign USSR rock, paper, or scissors        
        # Russia wins
        if USA == 2 and USSR == 3 or USA == 1 and USSR == 2 or USA == 3 and USSR == 1:
            if USSR == 1:
                USSR = 'Rock'
                print("Well look at that.  USSR chose Rock!")
            if USSR == 2:
                USSR = 'Paper'
                print("Well look at that.  USSR chose Paper!")
            if USSR == 3:
                USSR = 'Scissors'
                print("Well look at that.  USSR chose Scissors!")
            
            if USA == 1:
                USA = 'Rock'
            if USA == 2:
                USA = 'Paper'
            if USA == 3:
                USA = 'Scissors'
            print()
            print(""" "DAAA!!!  My """, USSR, "beat", USA.rstrip(), """!  Spasiba, comrade!  I know this not easy, but Soviet Union thank you for assistance!"  Your public relations chief, who is present, nearly faints just imagining the coming storm surely to result from having to explain this nuclear disaster as the result of American aggression.  "No problem, Gorby.  Just remember this when and if the time comes for the Great Bear to help the Eagle."  You give your last goodbyes and gather your team of advisers to head back to Air Force One.  The coming days will be long and difficult, but things could be worse.  You could be Gorbachev.""")
            print()
            War.exit_lose()        
        # USA wins
        elif USA == 3 and USSR == 2 or USA == 1 and USSR == 3 or USA == 2 and USSR == 1:
            if USSR == 1:
                USSR = 'Rock'
                print("Well look at that.  USSR chose Rock!")
            if USSR == 2:
                USSR = 'Paper'
                print("Well look at that.  USSR chose Paper!")
            if USSR == 3:
                USSR = 'Scissors'
                print("Well look at that.  USSR chose Scissors!")
            
            if USA == 1:
                USA = 'Rock'
            if USA == 2:
                USA = 'Paper'
            if USA == 3:
                USA = 'Scissors'
            print()
            print(""" You jump up and down like a little kid while others look on with a mixture of disgust and disbelief.  "YES!!!  In your FACE, Gorby! """, USA, "beats", USSR.rstrip(), """!  Spasiba, comrade!"  Gorbachev looks visibly defeated.  The grim reality that he will need to admit his government has lost some control over members of its own military forces with access to the most destructive weapons ever to exist on planet Earth immediately sets in.  "This not good for us.  We will honor agreement, but not good.  Dasvedanya, comrade President; until next time."  He turns to his team and says, "let's go" as they all scurry out to meet with the press and explain the situation to an eager world.""")
            print()
            print("Boarding Air Force One, you are relieved that you will not have to lie to the public, but still anxious over the subversive elements still unaccounted for within the Soviet ranks.  How will they receive this news?  Will the Soviet public interpret Gorbachev's inability to prevent rogue nuclear strikes as a loss of confidence in him?  In the entire system??  What will their next actions be?  These thoughts disturb you to the point of inducing a headache, so you lie down to get some much needed -- and much deserved! -- rest.")
            print()
            War.exit_win()        
        else:  # it's a draw
            print(""" "Damn it!  A tie.  The suspense is killing me.  Let's go again...." """)
            print()
            print(secbreak)
            War.USA()
            

    def rep():
        print(""" "Well SOMEone has to talk to the Kremlin, but it obviously can't be me right now.  Call Donald!"  Within minutes, Donald Trump is on the phone from his golf resort in Mar-a-Lago, Florida.  "Hey there!  Good to hear from you!  How can I serve my country today?"  "Donald, I'll cut straight to it: the nation needs your help.  Do you know anyone in senior levels of Soviet leadership?"  "Of course!  I know all the bigliest SOviets, and let me tell ya, they're good people.  Great people.  I'll call you back as soon as I finish this round of golf.  I'm having the best game, the most beautiful game!" """)
        print()
        print("""After 12 hours, the call you've been waiting anxiously finally comes.  "Donald, tell em some good news!"  "Well, I had the best game of golf.  As you know, I'm the best player out there.  Others are good, but I'm good more often.  Anyway, I spoke with Ivanka and she contacted an uncle of hers.  Gorbachev would like to meet you in person in Geneva, Switzerland, if that's okay with you.  As compensation for my help, I only ask..."  CLICK.  You're sure Donald wouldn't have asked anything unreasonable, but you'll deal with it later.""")
        print()
        print("You tell your Chief of Staff to prepare your chopper for a trip to Air Force One.  You're going to Switzerland to meet with Gorby.")
        print()
        print(secbreak)
        War.meeting()
        
    
    def meeting():
        print("As you deplane, you are greeted by Swiss leadership in accordance with typical cordiality and protocol; however, none of this assuages your apprehension about meeting with Gorbachev.  His intentions are still unclear, and his accusation of having made the first strike is preposterous.  Thus, this meeting is imperative because as long as he's talking, he's NOT launching nuclear missiles at your people.  Right?")
        print()
        print(""" Arriving at the palace where the meeting is held, you are quickly ushered behind closed doors where you see Gorbachev sipping on water....which might be vodka and not water.  "Dobroye den, my friend!  Would you like..."  Gorbachev begins with pleasantries, but you go straight to business.  "Let's dispense with pleasantries; we both know why we're here: to figure out how our countries will prevent World War III."  His expression turns from a wide smile to a stern grimace.  "Da...you are right.  It seems we have problem." """)
        print()
        print(""" "BIG problem, HUGE problem, freaking hundreds of people already vaporized problem, Gorby!"  Gorbachev has a habit of minimizing things, like the time when the Soyuz almost collided with the Apollo shuttle, or the time when KGB accidentally poisoned your dog, but you refuse to allow him to minimize this one.  "OK, OK!  We have certain angry people on our side.  We hunt these dogs down now, but our missile was not intentional.  We hope you can forgive."  The presence of ideological defectors within Soviet ranks comes as no surprise; the fact that they have the placement and access to launch nuclear weapons is a whole other story.""")
        print()
        print("The way you see it, there are only three viable options at this point:  1) The USSR and the USA can issue a joint public statement denouncing the USSR's first strike, blaming it on a technical glitch, while we help hunt down those responsible; 2) demand a public apology from the USSR and expose the existence of revolutionary forces among their ranks in an effort to further weaken communism ideology; or 3) give the secret order to your Secret Service agents to kill Gorbachev and his security detail.")
        print()
        print(secbreak)
        meeting = input("Which option do you offer Gorbachev: issue a joint public statement denouncing the USSR first strike as a technical glitch [J], demand a public apology from the USSR [D], or kill Gorbachev [K]?  ")
        if meeting.lower() == 'j':
            print()
            print(""" "The way I see it, Gorby, the USSR needs to issue a joint public statement denouncing your first strike as the result of a technical glitch.  We will help you track down those truly responsible for this dastardly deed, but the USA will NOT take the fallout for this one."  "Fallout...I see what you did there.  USA always funny, even in face of danger.  USSR not so funny.  This last time we see each other, comrade President.  Dasvedanya!"  Gorbachev and his staff abruptly leave not only the palace, but the country.  This did not go the way you planned.""")
            print()
            c = War.random_country()
            print(""" "CRAP!  Get me""", c,""" "on the phone now!  This is going to require a heavier hand than I anticipated." """)
            print(secbreak)
            War.ally(c)
        elif meeting.lower() == 'd':
            print()
            print(secbreak)
            print(""" "The way I see it, Gorby, the USA deserves a public apology from you.  The world also needs to know the truth as to how this happened."  Gorby does not look happy; his entire head turns so dark red that his well-known birthmark is almost invisible compared to his new color.  "THAT IS NOT ACCEPTABLE!  Soviet Union will collapse if world knows truth!"  (The irony of this statement is not lost on you, given that everyone in the Western world already knew this.)  What you were not prepared for, however, was the sound of AK-47s.  Gorbachev had apparently given a signal to his guards, who immediately opened fire and killed all of your Secret Service agents.  The last thing you hear is Gorby laughing as you are struck on the back of the head by the end of a rifle.""")
            print()
            War.end_captive()          
        elif meeting.lower() == 'k':
            print()
            print(""" "The way I see it, Gorby, the USSR has already fallen.  The loss of control of your nuclear capability is but a mere symptom for a larger, advanced disease.  Communism had a good run, but it's clearly proven to be a failure."  "What do you mean?  Soviet Union is strong!  Look at Romania; their people love Nicolae!"  (Little does Gorby know that Nicolae Ceausescu would be hunted down by his own people and executed alongside his wife after a kangaroo court trial for numerous crimes against humanity under the Soviet flag in only weeks from now).""")
            print() 
            print(""" "That may be, Gorby, but the world will love this even more", you manage to utter as you give your Secret Service agents the signal to attack.  They swiftly dispatch with Gorbachev's guards, who had been smoking and joking among themselves nearly the entire time.  Gorbachev is stunned and visibly shaken as your agents pull him from under the heavy, solid oak conference table consuming 60% of the room.""")
            print()
            print(""" "NYET! NYET!  Please, I beg you!  USA good people; we do what you wish!"  You try to ignore the overwhelming stench of fresh urine, likely coming from only one living person in that room.  "Sorry, Gorby.  It's been a good run, but the world deserves better.  Dasvedanya....bitch."  The Secret Service Agents open fire, laying waste to not only Gorbachev, but likely decades of vicious communist rule.""")
            print()
            print("""You pat yourself on the back aboard Air Force One, imagining the ticker-tape parade awaiting you upon your return to the USA.  Your pleasant daydreams are interrupted as your press officer asks you to turn on the television.  "Which channel?" you ask, assuming that they are drawing your attention to the great news that has already begun to spread around the globe.  "Any channel."  As you watch the reporter for a few seconds, your giddy daydreams vanish and are replaced quickly with dread, anger, and fear rolled up into one.  The news has spread around the globe....the news that the USA has committed a war crime by assassinating one of the 'greatest leaders of all time.'  Every human rights organization and developed nation leader is calling for your head on a platter, even your 'closest allies.' """)
            print()
            print("You hear commotion in the cabin outside your door, but after a few seconds, your own Secret Service agents bust into your cabin.  As you start to get up and demand to know what is going on, one of the agents manages to hit you in the back of the head with the butt of his gun.  Your world goes black as all sound fades to nothing." )
            print()
            War.end_hanging()         
        #erroneous input:    
        else:
            print()
            War.errors()
            print(secbreak)
            War.meeting()
        

    def seals():
        print("Naval Special Warfare Group (NSWG) 2 receives orders at 0400 hrs (EST).  They quickly deploy and within 12 hours have penetrated deep into Western Russia. Three NSW units have been tasked to target RT-2PM - SS-25 SICKLE and R-36M / SS-18 SATAN intercontinental ballistic missile (ICBM) systems, as they are currently the only ones operational at this time.  Dombarovskiy, Kartaly, and Verkhnyaya Salda missile sites are quickly infiltrated and rendered inoperational.")
        print()
        print("You receive word from the forward deployed commander that 5 SEALs have been lost, while the USSR has incurred an estimated 64 casualties.  This is a high cost to pay, but preventing global nuclear war or buying more time at a minimum is well worth it at this point.")
        print()
        print("""You summon your Secretary of Defense for recommendations on next steps.  "Given that their nuclear capability has been deteriorated severely, I'd think it's safe to request an in-person meeting and put an official end to these dangerous actions.  The last thing the world wants is a global nuclear war." """)
        print()
        print(""" Your National Security Adviser disagrees, however.  "We know that the USSR still has nuclear-capable submarines out there; we also know that we don't know where they all are at the present time.  They could be sitting off our shores in Hawai'i, or even New York."  "Well what do you recommend, then, Madame Adviser?" your SecDef asks rather curtly.  "Given all we know about the current situation, I'd recommend tasking our CIA assets abroad to verify the willingness of our dear Comrade Gorbachev to meet, or consult another mediary." """)
        print()
        print(""" "These are all good recommendations; I thank you for your time and will consider these in private."  You gather your thoughts over a cup of hot chocolate, debating the pros and cons of each.  Negotiating an in-person meeting might only give them more time to task any remaining resources, like those subs your NSA adviser mentioned.  However, tasking CIA assets might only escalate the situation if their operations go sour.""")
        print()
        seals = input("Which course will you take?  Request a meeting [M], tasking CIA assets [C], or try communication through an ally [A]?  ")
        if seals.lower() == 'm':
            print("Considering that the bulk, if not all, of the USSR's land-based ICBM capabilities have been rendered useless, combined with the fact that your faith in your counter-submarine assets is apparently higher than your own SecDef's, you opt to try direct communication to arrange an in-person meeting with Gorby.  The attempt alone should be interpreted as a sign of good will.....right?")
            print()
            print(secbreak)
            War.meeting()
        elif seals.lower() == 'c':
            print("""Keenly aware that time is running out for decisive action, the CIA seems like the best option.  You open the door and shout, "Get me the CIA chief in here, NOW!" """)
            print()
            print(secbreak)
            War.cia()
        elif seals.lower() == 'a':
            c = War.random_country()
            print("Deciding that your NSA adviser may have some good points, you opt for assessing through other intermediaries before attempting communication directly with the Kremlin.  However, CIA assets are too risky; any failure on their part may be interpreted as further signs of aggression by the USSR.  Even if not, they could be easily spun that way in the public eye.  You pick up the phone to call an old friend.", '"Get me"', c, 'on the line, ASAP!"')
            print()
            print(secbreak)
            War.ally(c)
        else:
            War.errors()
            print(secbreak)
            War.seals()
        

    def cia():
        print("Heeding the counsel of your National Security Adviser, you decide to the best option is to leverage CIA assets to gain more intel on Soviet intent and, if possible, willingness to communicate.  After several tense days and deafening, maddening silence from the Kremlin, you receive word that several CIA assets have been assassinated.  It's clear there's a mole somewhere in the highest ranks of your government.  Thus, there only a few good options now available:  you may task other reconnaissance assets [R], reach out to allies [A], or try calling Gorbachev again directly [C].")
        print()
        cia = input("Which option will you choose?  Task recon assets [R], reach out to allies [A], or try calling Gorbachev again [C]?  ")
        if cia.lower() == 'r':
            print()
            print()
            print("Reconnaissance is almost always a great option.")
            print()
            print(secbreak)
            War.recon()
        if cia.lower() == 'a':
            print()
            print("I've got friends in low places....")
            print()
            c = War.random_country()
            print(secbreak)
            War.ally(c)
        if cia.lower() == 'c':
            print()
            print("Screw it.  Phone calls are cheap.  Gorby better be home this time!")
            print()
            print(secbreak)
            War.communicate()
        else:
            War.errors()
            print(secbreak)
            War.cia()

    
    def end_planeCrash():
        print("You SecDef has informed you that Moscow launched another missile, this time aimed straight at Washington, D.C.  You and your staff are evacuated form the White House.  While en route to Air Force One, you observe scores of Soviet cargo planes flying overhead with what seems like thousands of paratroopers deploying from them onto US soil.")
        print()
        print("Looking around through the bulletproof windows and from the comfy interior of the 'Beast' (the nickname given by the US Secret Service to your bulletproof limousine), you see scores of American citizens being slaughtered at the hands of Soviet troops equipped with AK-47s and RPGs.  This wasn't how you expected your presidency to go, but 'when the rich make war, it's the poor that die,' according to a Russian proverb.")
        print()
        print("You, however, arrive at Air Force One and board quickly with your spouse and closest staff.  Luckily for you, little thieves are hanged, but big ones escape (another Russian proverb).  As you climb into the air and head for Cheyenne Mountain in Colorado for an 'extended vacation,' you hear commotion coming from the front of the plane.  Inquiring about the source, the pilots inform you that the Soviets have been employing some type of heretofore unknown EMP weapon.  Watching as a Soviet bomber flies past, your pilots inform you that all electronics have just mysteriously gone completely dead, most likely due to one of these rumored EMP weapons.")
        print()
        print("As your plane slowly descends and the pilots struggle to maintain some control, you reflect on your life.  You wonder if you married the right person.  You wonder if they feel they chose wisely.  You wonder if you will all survive by some miracle that the pilots are able to glide the plane to a relatively safe landing.  You wonder why the heck you didn't approve the extra funds for the escape pod package upgrade to Air Force One.  You wonder if America will overcome as it always has, rise up against the Soviet threat, and defeat it.  You wonder if your allies will come to the aid of your citizens.  You wonder how difficult Russian might be to learn.  But most of all, you wonder how things would have turned out if you had JUST HIT THE RIGHT KEYBOARD KEY!" )
        print()
        print("Eternal peace lasts until the next war -- Russian proverb")
        print()
        War.exit_lose()

    def end_hanging():
        print()
        print("""You eventually come to, but are barely awake and don't remember much.  You see many people around you.  The heat from camera lights is almost unbearable.  The crowd is full of faces shouting and cheering.  That must have been a horrible dream.  What were you thinking?  These people LOVE you!  You're a god-damned HERO!  You then realize that your collar is tighter than you remembered.  The texture is also different; it's not the soft cotton to which you are accustomed.  It's more like wool....no, more like.....rope."  Before you can say a word, you hear a loud 'thud.'  You feel the floor disappear from beneath your feet as gravity does what gravity does.  The last thing you hear is your fans cheering and shouting.  But they're not your fans.  They never were.""")
        print()
        War.exit_lose()
        
    def end_captive():
        print("""It's dark, cold, and you have a horrific headache.  How did you get here?  Where is here?  You hear some mumbling outside of what appears to be a thick, steel door.  You approach the door and confirm it is thick and likely steel; regardless, it's nothing you're breaking through without some heavy tools.  "Hello?  Hello!!"  Someone approaches the door.  "Sto?"  Umm....that's not English.  "What you want?" the man asks in an irritated voice.  "You are honored guest of Mother Russia," the guard says as he laughs.  "This California hotel...you check in, but you not check out."  He laughs more as your fuzzy memories all coalesce into a more coherent picture.  Gorby betrayed you.  But it will be the biggest mistake that he will regret.....if you ever get out of here.""")
        print()
        War.exit_lose()
    
    #terminate the game with either a win or lose message & exit program
    def exit_win():
        print("     ***          GAME OVER - YOU WIN!!!          ***")
        print()
        input("Press any key to exit  ")
        sys.exit(secbreak)
    
    def exit_lose():
        print("     ***          GAME OVER - YOU LOSE!!!          ***")
        print()
        input("Press any key to exit  ")
        sys.exit(secbreak)
        
    #ten possible error messages if provided erroneous inputs:    
    def errors():
        x = War.random_error()
        
        if x == 'a':
            print("I can see attention to detail is not your strong suit; very unfortunate for your country. ")
            
        elif x == 'b':
            print("Time is running out here. Please pay attention.  Spasiba! (That's 'thank you' in Russian, which we will all be speaking instead of English if you aren't more careful.) ")

        elif x == 'c':
            print("The First Spouse slides you your medication and reprimands you under their breath for not taking them earlier.  You clearly aren't paying attention. ")
            
        elif x == 'd':
            print("Realizing that you just gave an order to execute an option that is neither advisable nor feasible at the time, your Vice President begins to speak in private meetings to select individuals regarding a potential coup.  Might want to be more careful with the orders you give... ")

        elif x == 'e':
            print("Word of your incompetence gets back to Gorbachev, who delights in the prospect of facing such an unworthy adversary.  He publishes the news about your inability to give reasonable, plausible orders for available options, which causes a large increase in his domestic support and approval rating.  Luckily, this news is slow to reach America and its allies and you still have time to correct your mistakes... ")

        elif x == 'f':
            print("SERIOUSLY?  Look at your available options again and choose an appropriate, VALID option.  Please and thank you.")

        elif x == 'g':
            print(" :-/   Try again. ")

        elif x == 'h':
            print("Maybe selecting an available option would make you look smarter and garner more respect from your staff and constituents.  After all, do you really want to look like Alexandra Ocasio-Cortez???  :-O ")

        elif x == 'i':
            print("Unfortunately, your inattention to details has cost the American people greatly. ")
            War.end_planeCrash()            
        
        elif x == 'j':
            print("Your National Security Adviser mumbled something under his breath about you being an idiot, followed by repeating aloud, in a rather irritated tone, the only available options....again.  Which one will we adopt at this time? ")
            
            
#start game       
War.play()