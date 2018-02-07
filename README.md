# Firmware exploration - Argon iNet2+

I created this page to document my findings from tinkering with my Argon iNet2+ DAB/FM/Internet radio. I'm not very happy with the firmware provided by Frontier Silicon (the radio is based on a FS2026-5 module), but I lack the knowledge to do anything about it. I hope to give those with the know-how some clues along the way.

CPU/processor - the system is based on the [Chorus 3 SoC](https://web.archive.org/web/20170315062559/http://www.frontier-silicon.com/sites/default/files/Chorus3_PB.pdf) with a CPU from Imagination Technologies: [META 122](https://web.archive.org/web/20180207174108/https://www.imgtec.com/news/press-release/imagination-technologies-announces-latest-member-of-the-meta-family-of-super-threaded-processors/)


I managed to capture the URL of the firmware through Wireshark and uploaded it here: 
[ Frontier-Silicon-Argon-Firmware/ir-mmi-FS2026-0500-0035.2.11.12.EX65933-4RC2.isu.bin ](ir-mmi-FS2026-0500-0035.2.11.12.EX65933-4RC2.isu.bin)

I initially tried to run it through binwalk, but I didn't get anything I could make sense of (I'm a complete novice).

A nmap scan of the radio revealed 5 open ports: 80, 514, 8080, 10003, 52253. I tried telnet on port 514 and discovered what appears to be a debugging system log: [debugger](debugger) 
