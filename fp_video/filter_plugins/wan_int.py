class FilterModule(object):

  def get_wan_int(self,rtr_ver):
    if ("CISCO2911/K9" in rtr_ver) or ("CISCO2921/K9" in rtr_ver):
       return "GigabitEthernet0/1"
    elif ("ISR4331/K9" in rtr_ver) or ("ISR4431/K9" in rtr_ver):
       return "GigabitEthernet0/0/1"
    else:
       return "Ethernet0/1"
  def filters(self) :
    return { 'WAN_INT': self.get_wan_int }

