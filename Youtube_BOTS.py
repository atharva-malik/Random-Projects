import webbrowser  # https://www.youtube.com/watch?v=i3JGdgtIG90
import random

new = 2
Url = ["https://www.youtube.com/watch?v=bDnUIbeDQxA&lc=UgzM1ilL4f_sjCMigzl4AaABAg",
       "https://www.youtube.com/watch?v=QhaDU08HgHk",
       "https://www.youtube.com/watch?v=SozeQT-5vTQ&t=474s",
       "https://www.youtube.com/watch?v=l5Pi-k5SomM&t=737s",
       "https://www.youtube.com/watch?v=FrfmptcS0-0",
       "youtube.com/watch?v=bDnUIbeDQxA",
       "https://www.youtube.com/watch?v=sDTFYMW111M",
       "https://www.youtube.com/watch?v=2XiM2kPOBsQ"]

a = 10

while a > 0:
    tabUrl = random.choice(Url)
    webbrowser.open(tabUrl, new=new)
    a -= 1
