class Pakistan():
    def Capital(self):
        print("Islamabad is the capital of Pakistan")

    def language(self):
        print("Urdu is the most widely spoken language of Pakistan")

    def type(self):
        print("Pakistan is a developing country")

class Japan():
    def Capital(self):
        print("Tokyo is the capital of Japan")

    def language(self):
        print("Japanese is the primary language of Japan")

    def type(self):
        print("Japan is a developed country")

obj_pak = Pakistan()
obj_jap = Japan()

for country in (obj_pak, obj_jap):
    country.Capital()
    country.language()
    country.type()