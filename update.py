#!/usr/bin/env python3

import hashlib
import os
import pathlib
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree

url = "http://update.wifiradiofrontier.com/FindUpdate.aspx"
data = {"mac": "0815DEADBEEF"}

for file in pathlib.Path().glob("*.isu.bin"):
    m = re.match(r"^([^._]*)[._]V?(.*)\.isu\.bin$", str(file))
    if m:
        data["customisation"] = m.group(1)
        data["version"] = m.group(2)
        full_url = url + "?" + urllib.parse.urlencode(data)
        try:
            response = urllib.request.urlopen(full_url)
        except:
            pass
        else:
            tree = xml.etree.ElementTree.fromstring(response.read().strip())
            for software in tree.iter("software"):
                customisation = software.get("customisation")
                version = software.get("version")
                download = software.find("download").text
                md5 = software.find("md5").text
                downloadurl = urllib.parse.urlparse(download)
                outname = os.path.basename(urllib.parse.parse_qs(downloadurl.query)["f"][0])
                if not os.path.isfile(outname):
                  try:
                    content = urllib.request.urlopen(download).read()
                  except:
                    pass
                  else:
                    digest = hashlib.md5(content).hexdigest()
                    if digest == md5:
                        with open(outname, "wb") as file:
                            file.write(content)
