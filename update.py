#!/usr/bin/env python3
# Walk through the file list and check if there is a new firmware for the radio

import hashlib
import os
import pathlib
import re
import urllib.parse
import urllib.request
import xml.etree.ElementTree

url = "http://update.wifiradiofrontier.com/FindUpdate.aspx"
data = {"mac": "0815DEADBEEF"}

lastcust = ""
for file in sorted(pathlib.Path().glob("*.isu.bin")):
    m = re.match(r"^([^._]*)[._]V?(.*)\.isu\.bin$", str(file))
    if m:
        data["customisation"] = m.group(1)
        data["version"] = m.group(2)
        if lastcust == data["customisation"]:
          continue
        lastcust = data["customisation"]

        print("Checking " + data["customisation"])
        full_url = url + "?" + urllib.parse.urlencode(data)
        try:
            response = urllib.request.urlopen(full_url)
        except urllib.error.HTTPError as err:
            print(" Server error: " + str(err.code) + " " + err.reason)
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
                print(" Current firmware: " + outname)
                if os.path.isfile(outname):
                  print(" Already downloaded")
                else:
                  print(" Downloading new firmware " + str(download))
                  try:
                    content = urllib.request.urlopen(download).read()
                  except urllib.error.HTTPError as err:
                    print(" Error downloading file: " + str(err.code) + " " + err.reason)
                    pass
                  else:
                    digest = hashlib.md5(content).hexdigest()
                    if digest == md5:
                        with open(outname, "wb") as file:
                            file.write(content)
                    else:
                        print(" Error: Digest hash does not match")
