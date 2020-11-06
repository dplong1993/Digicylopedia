from dotenv import load_dotenv
load_dotenv()

from starter_app import app, db
from starter_app.models import User, Digimon

with app.app_context():
  db.drop_all()
  db.create_all()

#####################################################################################
# USERS                                                                             #
#####################################################################################

  ian = User(username = 'Ian', email = 'ian@aa.io', password = 'password')
  javier = User(username = 'Javier', email = 'javier@aa.io', password = 'password')
  dean = User(username = 'Dean', email = 'dean@aa.io', password = 'password')
  angela = User(username = 'Angela', email = 'angela@aa.io', password = 'password')
  soonmi = User(username = 'Soon-Mi', email = 'soonmi@aa.io', password = 'password')
  alissa = User(username = 'Alissa', email = 'alissa@aa.io', password = 'password')

  db.session.add(ian)
  db.session.add(javier)
  db.session.add(dean)
  db.session.add(angela)
  db.session.add(soonmi)
  db.session.add(alissa)


######################################################################
# DIGIMON                                                            #
######################################################################

  argomonB = Digimon(name="Argomon(Baby)", level="Baby", next_form=["Argomon(In-Training)"], bio="Argomon (Baby) is a Mutant Digimon. It is a Fresh Digimon born from a bug in an algorithm/computational program. It has a habit of finding and converging at places where high-capacity data leaks out. They gather one by one, growing into a horde and blanketing it.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  botamon = Digimon(name="Botamon", level="Baby", next_form=["Koromon", "Wanyamon"], bio="Botamon is a Slime Digimon. It was just born recently, and on the surface of its slime-shaped body, it has grown thick, black fuzz. It is unable to battle as it has just been born.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Botamon_b.jpg")
  chibomon = Digimon(name="Chibomon", level="Baby", next_form=["DemiVeemon"], bio="Chibomon is a Slime Digimon, and as such, it is small and young. It is a small, blue-colored, Dragon Digimon child, and although it is small and powerless, it has the potential to digivolve to every Dragon Digimon. For that reason, it is a Digimon that is considered exceedingly valuable by tamers and researchers of Dragon Digimon. It is cherished due to its personality of friendliness and overflowing curiosity, characteristic of Fresh Digimon. Just like other Fresh Digimon, it spits acidic bubbles to attack, but as usual, their power is nonexistent.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  conomon = Digimon(name="Conomon", level="Baby", next_form=["Kokomon"], bio="Conomon is a Slime Digimon. Conomon and Zerimon are extremely rare Digimon which are born in pairs from a single Digi-Egg. The reason why only Zerimon and Conomon are born as twins is unclear at the present stage. Moreover, they are not restricted to always being born as twins, and either a Zerimon or Conomon may be born from a single Digi-Egg. Compared to the extremely energetic, one-horned Zerimon, the three-horned Conomon has a relatively docile personality. Like other Fresh Digimon, it spits acid bubbles to intimidate opponents.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  dodomon = Digimon(name="Dodomon", level="Baby", next_form=["Dorimon", "Wanyamon"], bio="Dodomon is a Slime Digimon and a carrier of the X Antibody. Its whole body is covered in a tough fur named 'Mithril Hair'. It manifests an aggressive personality immediately after being born, and despite its fangs not yet being grown, it opens its mouth wide and completely intimidates the opponent with the manner in which it snaps at them. Because of this, there exist many Digimon which are completely deceived, but it is still a rare Digimon.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  jyarimon = Digimon(name="Jyarimon", level="Baby", next_form=["Gigimon"], bio="Jyarimon is a Slime Digimon. It is an extremely scarce Digimon, whose population is small. The Fresh-levels of Dragon-species Digimon are small in absolute number, and it is said that most of them are captured or die before they grow up. You wouldn't know it to look at it, but there are tiny, closely packed fangs growing within its mouth, and it is foreseen that it will grow into a powerful Dragon-species Digimon. Although it is powerless, it has the disposition to face those with bodies larger than its own, and that becomes the reason for its low survival rate.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  keemon = Digimon(name="Keemon", level="Baby", next_form=["Yaamon"], bio="Keemon is a Slime Digimon. It is an evil-eyed Digimon which is always scowling. Though it's very young, it hates being crowded by others, and lives in hiding. It likes poking its nose out of hiding and harassing with its 'Pushū'.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  ketomon = Digimon(name="Ketomon", level="Baby", next_form=["Hopmon"], bio="Ketomon is a Slime Digimon. It is a Digimon whose large eyes are its defining characteristic. These eyes have the ability to discern the nature of Digimon, allowing it to detect violent Digimon in advance and warn its allies of the danger.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  kuramon = Digimon(name="Kuramon", level="Baby", next_form=["Tsumemon", "Arcadiamon(In-Training)", "Pagumon"], bio="Kuramon is an Unidentified Digimon. It suddenly appeared on the Computer Network. Aggression, generated by the malice of people who abuse the Computer Network or the conflicts which are unfolding on the Network, manifested and a single Digi-Egg was created. Humanity's destructive instincts are condensed within that Digi-Egg, and as such, the mysterious Digimon that was born from it is an extremely dangerous being. It multiplies like a virus within the Computer Network, causing a slight degree of network failure.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  mokumon = Digimon(name="Mokumon", level="Baby", next_form=["DemiMeramon"], bio="Mokumon is a Smoke Digimon. It is a Digimon Baby which envelops its body with a smoke-like vapor. It is a unique Digimon whose DigiCore is bare, so it seems it covers its DigiCore with Smoke in order to protect it, and has an unusual way of life. Because the Smoke was generated when its DigiCore was burned, it seems it is harmful neither to Mokumon itself nor to others. Also, because it is still in the middle of digivolving, when it encounters an opponent, it immediately flees. Then, it scatters the Smoke issuing from its body all around, and seizes the opportunity to escape when the opponent loses sight of it. As stated earlier, because it isn't particularly harmful, if you happen to see one, it would be best to be quiet", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  pabumon = Digimon(name="Pabumon", level="Baby", next_form=["Tanemon", "Yokomon", "Motimon"], bio="Pabumon is a Slime Digimon. Although it looks like it is just pale green bubbles at first glance, it is a Bubble Digimon that can move freely and express a plethora of facial expressions. Because its surface has not hardened yet, its defensive power is nonexistent and it is equally unsuited for combat. From the portion that looks like a pacifier held in its mouth, it generates tiny bubbles, and proliferates them infinitely. As for that proliferation, at one point, it started being used for computer virus development, but because its life force was too weak, that was fortunately never implemented. Although its life is fleeting, it is a lovable Digimon Baby that lives earnestly.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  poyomon = Digimon(name="Poyomon", level="Baby", next_form=["Tokomon", "Bukamon"], bio="Poyomon is a Slime Digimon. With a translucent body, it is a Digimon Baby that drifts through the 'Net Ocean' like a jellyfish. As it has the most primitive structure among the Digimon discovered to date, it has been showered in attention as the 'Missing Link', the key to solving the mystery of the origin of Digimon, by the scholars and enthusiasts studying the roots of Digimon", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  punimon = Digimon(name="Punimon", level="Baby", next_form=["Tsunomon", "Nyaromon"], bio="Punimon is a Slime Digimon. It is a new kind of newborn Digimon. Its gelatinous red body is squishy, and there are three feeler-like things growing on its head. It is unable to battle, but it can produce resilient, acidic bubbles to intimidate its opponents.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")


  arcadiamonI = Digimon(name="Arcadiamon(In-Training)", level="In-Training", previous_form = ["Kuramon"], next_form=["Arcadiamon(Rookie)"], bio="Arcadiamon (In-Training) is a Digimon. It is a Digimon artificially created from the data of various Digimon. One result of an experiment to make the ultimate Digimon, it boasts amazing physical abilities despite being In-Training level. Arcadiamon demonstrates predatory behaviour. By directly absorbing the data of others, Arcadiamon achieves growth at an astounding rate.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  argomonI = Digimon(name="Argomon(In-Training)", level="In-Training", previous_form = ["Argomon(Baby)"], next_form=["Argomon(Rookie)"], bio="Argomon (In-Training) is a Mutant Digimon. It is the form that a newborn Argomon grows into. It is attached to places where large volumes of data flow and consumes that data through the mouth on its underside. It is a creepy one-eyed Digimon with a green body and tentacles that stretch out like arms. Since it's In-Training, it's still very weak, but it's up to some sort of evil and bringing a bad influence to the Real World...!", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  bukamon = Digimon(name="Bukamon", level="In-Training", previous_form = ["Poyomon"], next_form=["Otamamon", "Gomamon", "Syakomon", "Betamon"], bio="Bukamon is a Lesser Digimon. Although it has an appearance which is thought to be the infancy of an aquatic dinosaur, it is a funny Digimon with movements as clever as the seahorse. However, the friendly personality it had as Pichimon has totally vanished, and it quickly flees if others approach. Its outer skin cannot yet bear the water pressure and low temperature of the deep sea, so the length of time it can dive to the deep sea is not long.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  koromon = Digimon(name="Koromon", level="In-Training", previous_form = ["Botamon"], next_form=["Agumon", "Guilmon", "ToyAgumon", "Dracomon", "Hackmon"], bio="Koromon is a Lesser Digimon. It is a tiny Digimon that shed the fuzz covering its surface, and whose body grew even bigger. Although it has become able to move around more actively, it is still unable to battle. It can produce bubbles from its mouth to intimidate opponents.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  motimon = Digimon(name="Motimon", level="In-Training", previous_form = ["Pabumon"], next_form=["Gotsumon", "Solarmon", "Tentomon", "Hagurumon"], bio="Motimon is a Lesser Digimon. It possesses elastic skin, and is a soft-bodied Digimon that uses the protuberances on the underside of its body to toddle about. It came to be called 'Motimon' from inflating its body when it gets worked up, causing it to look like mochi. However, as a result of possessing a height of intelligence that couldn't even be imagined from its appearance, its origin is conjectured to derive from a computer's dictionary feature. It understands human languages, and it is sometimes seen freely deforming its body like it's trying to return communications.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  nyaromon = Digimon(name="Nyaromon", level="In-Training", previous_form = ["Punimon"], next_form=["Armadillomon", "Terriermon", "Salamon", "Lunamon"], bio="Nyaromon is a Lesser Digimon. It is a tiny Digimon which has cat-like characteristics. It is always capricious, and that behavior seems to have been attached to Nyaromon as a result of its being like a 'cat'. Although it is sometimes frivolous due to its overflowing curiosity, it also has a lonely side.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  pagumon = Digimon(name="Pagumon", level="In-Training", previous_form = ["Kuramon"], next_form=["Impmon", "Gazimon", "Chuumon", "Lopmon"], bio="Pagumon is a Lesser Digimon. This small Digimon can fly at low altitudes with the ear-like protrusions growing out of its head. It can move these ears like a second pair of hands, using them to mock the enemy with all kinds of gestures. It has a malicious streak, often chasing after Digimon like Koromon or Tsunomon and teasing them.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  tanemon = Digimon(name="Tanemon", level="In-Training", previous_form = ["Pabumon"], next_form=["Palmon", "FanBeemon", "Lalamon", "Renamon"], bio="Tanemon is a Bulb Digimon. It has something that looks like a plant sprout burgeoning from its head. It is a Yuramon that wandered in search of an optimal environment, then settled to the ground and digivolved. Due to its extremely timid personality, if it senses an intruder's presence, it will burrow with the four feet at the base of its body, and completely bury its body portion under the ground. Once it is completely hidden underground, the thing growing from its head assumes the camouflage of a plant, allowing it to defend its body from intruders. However, this is ineffective against herbivorous Digimon.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  tokomon = Digimon(name="Tokomon", level="In-Training", previous_form = ["Poyomon"], next_form=["Patamon", "Falcomon", "Hawkmon", "Lucemon", "Sistermon Blanc"], bio="Tokomon is a Lesser Digimon. It is a tiny Digimon which has limb-like objects growing under its body (head?). In-Training Digimon that have grown limbs are extremely rare, and their appearance is enormously cute. However, while it may be cute, you have to be careful, because if you carelessly stretch out your hand, it will suddenly open its mouth wide, and snap at you with the fangs growing closely packed within. Having said that, because its personality is very innocent, any malice is nonexistent", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  tsumemon = Digimon(name="Tsumemon", level="In-Training", previous_form = ["Kuramon"], next_form=["Agumon(Blk)", "Keramon", "Dracmon", "DemiDevimon"], bio="Tsumemon is an Unidentified Digimon. It digivolved further from Kuramon. The tips of its feelers have become claw-shaped, and it has grown even more ferocious. It corrodes data at a tremendous speed, and causes malfunctions in the Network. Also, because its speed of movement is so swift, once it digivolves to Tsumemon, it becomes even harder to capture.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  tsunomon = Digimon(name="Tsunomon", level="In-Training", previous_form = ["Punimon"], next_form=["Gabumon", "Gabumon(Blk)", "Goblimon", "Zubamon", "Veemon", "Monodramon"], bio="Tsunomon is a Lesser Digimon. It is a tiny Digimon that hardened one of the feelers on its head as Punimon. From Punimon, it has accomplished a more animal-like Digivolution, and is covered in tufty body hair. It is still at the peak of playfulness, and it has a prank-loving personality, but its combat instinct has not awakened.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  wanyamon = Digimon(name="Wanyamon", level="In-Training", previous_form = ["Botamon", "Dodomon"], next_form=["Dorumon", "Gaomon", "Kudamon", "Ryudamon"], bio="Wanyamon is a Lesser Digimon. It is a Digimon fused from the data of small, pet animals like dogs and cats. Because its unexpected movements are also quick, caution is necessary so that it doesn't get away, but it becomes very emotionally attached if shown affection like a pet.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")
  yokomon = Digimon(name="Yokomon", level="In-Training", previous_form = ["Pabumon"], next_form=["Elecmon", "Biyomon", "Mushroomon", "Wormmon"], bio="Yokomon is a Bulb Digimon. It is a Lesser Digimon with a large flower blooming from its head. It is able to move by skillfully operating its root-like tentacles, and with its lightness, it can rise into the air, but only to a small height. As it is brimming with curiosity, it is restlessly stirring and its appearance seems very cute. It has a habit of living together in flocks, and it is said that due to grouping, the flocks will grow from a few to a few hundred.", photo_url="https://digicyclopedia.s3.us-east-2.amazonaws.com/Argomon_(Fresh)_b.jpg")

  db.session.add(argomonB)
  db.session.add(botamon)
  db.session.add(chibomon)
  db.session.add(conomon)
  db.session.add(dodomon)
  db.session.add(jyarimon)
  db.session.add(keemon)
  db.session.add(ketomon)
  db.session.add(kuramon)
  db.session.add(mokumon)
  db.session.add(pabumon)
  db.session.add(poyomon)
  db.session.add(punimon)

  db.session.add(arcadiamonI)
  db.session.add(argomonI)
  db.session.add(bukamon)
  db.session.add(koromon)
  db.session.add(motimon)
  db.session.add(nyaromon)
  db.session.add(pagumon)
  db.session.add(tanemon)
  db.session.add(tokomon)
  db.session.add(tsumemon)
  db.session.add(tsunomon)
  db.session.add(wanyamon)
  db.session.add(yokomon)

  db.session.commit()
