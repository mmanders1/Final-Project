# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Dr. Dino",color="#bb2727")

define f = Character("Dr. Nethropod",color="#bb7327")
define g = Character("Dr. Maniraptora",color="#bbb427")
define h = Character("Dr. Ornithomimidae",color="#31bb27")
define i = Character("Dr. Sauropod",color="#27bb5b")
define j = Character("Dr. Ceratopsian",color="#27bbb1")
define k = Character("Dr. Thyreophora",color="#0b9eee")
define l = Character("Dr. Pterosaur",color="#4027bb")
define m = Character("Dr. Tentanurae",color="#7d27bb")
define n = Character("Dr. Tyrannosauridae",color="#bb27b4")
define o = Character("Dr. Ornithopod",color="#bb276f")

image dr dino = "dr dino.png"
 
#images used 
image ceratosaurus =  "Ceratosaurus.jpg" 
image carnotaurus = "Carnotaurus.jpg"
image dilophosaurus = "Dilophosaurus.jpg"
image megalosaurus =  "Megalosaurus.jpg" 
image gigantosaurus = "Gigantosaurus.jpg"
image allosaurus = "Allosaurus.jpg"
image velociraptor =  "Velociraptor.jpg" 
image microrapter = "Microraptor.jpg"
image therizinosaurus = "Therizinosaurus.jpg"
image gallimimus = "Gallimimus.jpg"
image ornithomimus = "Ornithomimus.jpg"
image pachycephalosaurus =  "Pachycephalosaurus.jpg" 
image eotyrannus =  "Eotyrannus.jpg" 
image tyrannosaurus = "Tyrannosaurus.jpg"
image tarbosaurus = "Tarbosaurus.jpg"
image diplodocus =  "Diplodocus.jpg" 
image brontosaurus = "Brontosaurus.jpg"
image brachiosaurus = "Brachiosaurus.jpg"
image titanosaurus = "Titanosaurus.jpg"
image triceratops = "Triceratops.jpg"
image protoceratops = "Protoceratops.jpg"
image styracosaurus = "Styracosaurus.jpg"
image parasaurolophus = "Parasaurolophus.jpg"
image hypsolophodon = "Hypsolophodon.jpg" 
image iguanodon = "Iguanodon.jpg"
image ankylosaurus = "Iguanodon.jpg"
image stegasaurus = "Stegasaurus.jpg"
image pterodactyl = "Pterodactyl.jpg"
image pteranodon = "Pteranodon.jpg"
image quetzalcoatlus = "Quetzalcoatlus.jpg"


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene dino museum

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy at left:

    # These display lines of dialogue.

    e "Welcome to the museum!"

    e "I am Dr. Dino! I'll be happy to assist you."

    e "Do you need help identifying a dinosaur?"

    menu:

        "Yes, I do.":
            jump choice1_yes

        "No, I don't.":
            jump choice1_no

label choice1_yes:

    $ menu_flag = True

    e "Great! Let's get started."

    scene 199

    jump flight

label choice1_no:

    $ menu_flag = False

    e "okay, I'll be here if you need me!"

    jump choice1_done

label flight:
    show eileen happy at left:
 
    e "Does your dinosaur fly?"

    menu:
        "Yes! My dinosaur can fly.":
            jump pterosaur # figure out 
        "The Dinosaur I'm thinking of cannot fly.":
            jump herbivorous 

label herbivorous:
    e "Is your dinosaur an herbivore?"

    menu:
        "Yes! My dinosaur is an herbivore.":
            jump long_necked 
        "The Dinosaur I'm thinking of is not an herbivore.":
            jump three_toed #need to finish path 

label three_toed:
    e "Is your dinosaur three toed?"

    menu:
        "Yes! My dinosaur is three toed.":
            jump netheropod 
        "The Dinosaur I'm thinking of is not three toed":
            jump stiff_tailed

label stiff_tailed:
    e "Does your dinosaur have a stiff tail?"

    menu:
        "Yes! My dinosaur has a stiff tail.":
            jump tentanurae  
        "The Dinosaur I'm thinking of does not have a stiff tail":
            jump elongated_arms

label elongated_arms:
    e "Does your dinosaur have elongated arms?"

    menu:
        "Yes! My dinosaur has elongated arms.":
            jump ostrich 
        "The Dinosaur I'm thinking of does not have elongated arms.":
            jump tyrannosauridae

label ostrich:
    e "Does your dinosaur have an ostrich-like appearance?"

    menu:
        "Yes! My dinosaur has an ostrich-like appearance.":
            jump ornithomimidae
        "The Dinosaur I'm thinking of does not have an ostrich-like appearance.":
            jump maniraptora

label long_necked:
    e "Does your dinosaur have a long neck?"
    
    menu:
        "Yes! My dinosaur has a long neck.":
            jump sauropods  
        "The Dinosaur I'm thinking of does not have a long neck.":
            jump armored 

label armored:
    e "Is your dinosaur armored?"

    menu:
        "Yes! My dinosaur is armored.":
            jump horns_and_frills   
        "The Dinosaur I'm thinking of is not armored.":
            jump choice1_done # figure out  

label horns_and_frills:
    e "Does your dinosaur have horns and/or boney frills?"

    menu:
        "Yes! My dinosaur has horns and/or boney frills.":
            jump ceratopsian   
        "The Dinosaur I'm thinking of does not have horns and/or boney frills.":
            jump bipedal

label bipedal:
    e "Does your dinosaur walk on 2 legs?"

    menu:
        "Yes! My dinosaur walks on 2 legs.":
            jump ornithopods # finish this chain  
        "The Dinosaur I'm thinking of does not walk on two legs.":
            jump thyreophora


label pterosaur:
    hide eileen happy 
    show dr dino at right
    menu:
        "Pteradactyl":
            show pterodactyl at truecenter:
            l "fact"
            jump choice1_done
        "Pteranodon":
            show pteranodon at truecenter:
            l "fact"
            jump choice1_done
        "Quetzalcoatlus":
            show quetzalcoatlus at truecenter:
            l "fact"
            jump choice1_done

label netheropod:
    hide eileen happy 
    show dr dino at right
    menu:
        "Ceratosaurus":
            show ceratosaurus at truecenter:
            f "fact"
            jump choice1_done
        "Carnotaurus":
            show carnotaurus at truecenter:
            f "fact"
            jump choice1_done
        "Dilophosaurus":
            show dilophosaurus at truecenter:
            f "fact"
            jump choice1_done


label tentanurae:
    hide eileen happy 
    show dr dino at right
    menu:
        "Megalosaurus":
            show megalosaurus at truecenter:
            m "fact"
            jump choice1_done
        "Gigantosaurus":
            show gigantosaurus at truecenter:
            m "fact"
            jump choice1_done
        "Allosaurus":
            show allosaurus at truecenter:
            m "fact"
            jump choice1_done

label maniraptora:
    hide eileen happy 
    show dr dino at right
    menu:
        "Velociraptor":
            show velociraptor at truecenter:
            g "fact"
            jump choice1_done
        "Microraptor":
            show microraptor at truecenter:
            g "fact"
            jump choice1_done
        "Therizinosaurus":
            show therizinosaurus at truecenter:
            g "fact"
            jump choice1_done
            
label ornithomimidae:
    hide eileen happy 
    show dr dino at right
    menu:
        "Gallimimus":
            show gallimimus at truecenter:
            h "fact"
            jump choice1_done
        "Ornithomimus":
            show ornithomimus at truecenter:
            h "fact"
            jump choice1_done
        "Pachycephalosaurus":
            show pachycephalosaurus at truecenter:
            h "fact"
            jump choice1_done

label tyrannosauridae:
    hide eileen happy 
    show dr dino at right
    menu:
        "Eotyrannus":
            show eotyrannus at truecenter:
            n"fact"
            jump choice1_done
        "Tyrannosaurus":
            show tyrannosaurus at truecenter:
            n"fact"
            jump choice1_done
        "Tarbosaurus":
            show tarbosaurus at truecenter:
            n"fact"
            jump choice1_done

label sauropods:
    hide eileen happy 
    show dr dino at right
    menu:
        "Diplodocus":
            show diplodocus at truecenter:
            i "fact"
            jump choice1_done
        "Brontosaurus":
            show brontosaurus at truecenter:
            i "fact"
            jump choice1_done
        "Brachiosaurus":
            show brachiosaurus at truecenter:
            i "fact"
            jump choice1_done
        "Titanosaurus":
            show titanosaurus at truecenter:
            i "fact"
            jump choice1_done

label ceratopsian:
    hide eileen happy 
    show dr dino at right
    menu:
        "Triceratops":
            show triceratops at truecenter:
            j "fact"
            jump choice1_done
        "Protoceratops":
            show protoceratops at truecenter:
            j "fact"
            jump choice1_done
        "Stryacosaurus":
            show styracosaurus at truecenter:
            j "fact"
            jump choice1_done

label ornithopods:
    hide eileen happy 
    show dr dino at right
    menu:
        "Parasaurolophus":
            show parasaurolophus at truecenter:
            o "fact"
            jump choice1_done
        "Hypsolophodon":
            show hypsolophodon at truecenter:
            o "fact"
            jump choice1_done
        "Iguanodon":
            show iguanodon at truecenter:
            o "fact"
            jump choice1_done

label thyreophora:
    hide eileen happy 
    show dr dino at right
    menu:
        "Triceraankylosaurustops":
            show triceratops at truecenter:
            k "fact"
            jump choice1_done
        "Stegasaurus":
            show stegasaurus at truecenter:
            k "fact"
            jump choice1_done
    

label choice1_done:
    hide dr dino
    show eileen happy at left
    scene dino museum
    e "Do you have another dinosaur you'd like to identify?"
    menu:
        "Yes!":
            jump flight
        "No, thanks!":
            jump end 

label end:
    e "I hope that helped. See you soon!"

    # This ends the game.

    return
