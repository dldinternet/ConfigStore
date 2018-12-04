from json import JSONDecodeError

from pyconfigstore import ConfigStore

conf = ConfigStore("vestub", {"url":"http://vestub.com"}, True)
try:
  print(conf.get("url"))
except KeyError:
  conf.set("url","http://vestub.com")
conf.set("Title", "Social Media for Idea Owners and Investors")
conf.set("Tags", "Tech, Investors, Social Media")
conf.set("Tags.Topic", "Python")
conf.set({"Subject.Topic":"English"})
print(conf.all())
print(conf.path)

conf.delete("url")
print(conf.all())
