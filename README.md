
bloons_auto
=================

### Table of Contents

- [Summary](###Summary)
- [API](###API)
- 




### Summary
Going into this, I had no idea the scope that it would eventually cover.
The initial purpose of this repo was to gather info on what each towers hitbox is and to make a script for perfectly tessellating them. \
Needless to say, this all got a bit out of hand and now has a large variety of information covering from towers and maps all the way to documenting useful functions found with cheat engine. \
Additionally, most things are made in such a way that they can be used as an api. For example:
    
    from towers import DartMonkey, NinjaMonkey
    
    if __name__ == '__main__':
        time.sleep(5)

        # Makes a 4, 2, 0 dart monkey at (400, 600)
        DartMonkey(location=[400, 600], upgrades=[4, 2, 0])

In the future I'll probably separate things into their own repositories, but that is for another time.






