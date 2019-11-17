# ALevel-Networking-Board-Game
A board game that covers the AQA A-Level vocabulary required by the exam board.


Game is played on a 12 x 12 square grid. In one of the center squared make a root DNS server. On four other squares close to the root DNS add the IP addresses:
IPs = ["216.58.213.14","140.82.118.4", "151.101.60.193", "143.204.188.44"]
sites = ["YouTube.com","Github.com","Imgur.com","Soundcloud.com"]

Players choose a colour and an edge square as 127.0.01

The aim is to get a page from the correct site and return it to your terminal.

1. Start at your home square
2. Get to the DNS server to resolver the IP address
3. Get to the correct server
4. Add correct number of packets ontop of your original packet depending on which site you are on.
github = add none
imgur = add one
soundcloud = add two
youtube = add three
5. Get all packets back to your home
7. Win by doing this three times.

You can move by rolling a d10 dice and then answering a correct question. 
	• Multiple choice questions allow you to move the full dice distance. 
	• Challenge questions allow you to move double the value on the dice

You will be randomly given a site - You will have get a single packet to the root DNS unless you have it cached i.e. you have already been to that site.

When returning all dice rolls are doubled for MCQ.

When entering a site they will roll a dice
1. Encryption - take three letters and encypt them - Do this by your next turn or miss a turn
2.Database request needed - Miss next turn
3.Compression - Data is only one packet
4.Cache prize - Store all DNS entries
5.Corrupter - move the corrupter 3 spaces
6.Gigabit Ethernet - make your next roll now

The corrupter - This is a packet of interferance that if it lands on your square you have to move your request or data back to its point of origin. The piece will be controlled by the first player in the first round and move around to the next person in the next round etc. After a full cycle the piece will be moved to a random position
