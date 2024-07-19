from __future__ import annotations


class PortScanners:
    def __init__(self, target):
        self.target = target
        self.scanners = {
            "nmap": Nmap(target),
            "rustscan": Rustscan(target),
            "masscan": Masscan(target),
            "zmap": Zmap(target),
            "zgrab": Zgrab(target),
            "naabu": Naabu(target),
        }
        
    class Nmap:
        def __init__(self, target):
            self.target = target
            self.name = "nmap"
            
    class Rustscan:
        def __init__(self, target):
            self.target = target
            self.name = "rustscan"
            self.container_image = "rustscan/rustscan"