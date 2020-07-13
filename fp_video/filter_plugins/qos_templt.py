from ttp import *
import json

class FilterModule(object):

  def get_qos(self,policy_map,qos_template):

      with open(qos_template, 'rt') as file:
          ttp_template = file.read()

      parser = ttp(data=policy_map, template=ttp_template)
      parser.parse()
      results = parser.result(format='json')[0]

      return results

  def filters(self) :
    return { 'QOS': self.get_qos }

