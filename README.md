# Firmware exploration - Argon iNet2+

I created this page to document my findings from tinkering with my Argon iNet2+ DAB/FM/Internet radio. I am not very happy with the firmware provided by Frontier Silicon (the radio is based on a FS2026-5 module), but I lack the knowledge to do anything about it. I hope to give those with the know-how some clues along the way.

Here is the information I have managed to gather about the module:

**CPU/processor** - the system is based on the [Chorus 3 SoC](https://web.archive.org/web/20170315062559/http://www.frontier-silicon.com/sites/default/files/Chorus3_PB.pdf) with a CPU from Imagination Technologies: [META 122](https://web.archive.org/web/20180207174108/https://www.imgtec.com/news/press-release/imagination-technologies-announces-latest-member-of-the-meta-family-of-super-threaded-processors/)

**RAM** - [Winbond W9812G6KH (128-Mbit SDRAM)](https://web.archive.org/web/20180210201930/https://www.winbond.com/resource-files/da00-w9812g6khc1.pdf)*

**Flash** - [Adesto AT45DB321E (32-Mbit SPI)](https://web.archive.org/web/20170829195416/https://www.adestotech.com/wp-content/uploads/doc8784.pdf)*

**Radio receiver** - Frontier Silicon FS1112 (Apollo 2)*

**Wi-Fi** - [Marvell 88W8782 (Avastar)](https://web.archive.org/web/20170517010222/http://www.marvell.com/wireless/assets/marvell_avastar_88W8782.pdf)*

\* I found these specs in a [post on a Czech radio forum](https://web.archive.org/web/20180210195927/https://www.kyou.cz/forum/viewtopic.php?p=49771) and have not verified them.

**OS** - it runs a proprietary RTOS called [MEOS (version 5.2)](https://web.archive.org/web/20180210193106/https://www.mips.com/develop/tools/codescape-mips-sdk/meos/), as stated in the [Wi-Fi certificate](http://certifications.prod.wi-fi.org/pdf/certificate/public/download?cid=WFA55569) of the module. According to the documentation it is almost entierly written in C.

<br>

Other info:

I managed to capture the URL of the firmware through Wireshark and uploaded it here: 
[ Frontier-Silicon-Argon-Firmware/ir-mmi-FS2026-0500-0035.2.11.12.EX65933-4RC2.isu.bin ](ir-mmi-FS2026-0500-0035.2.11.12.EX65933-4RC2.isu.bin)

I initially tried to run it through binwalk, but I didn't get anything I could make sense of (I'm a complete novice).

A nmap scan of the radio revealed 5 open ports: 80, 514, 8080, 10003, 52253. I tried telnet on port 514 and discovered what appears to be a debugging system log: [debugger](debugger) 
