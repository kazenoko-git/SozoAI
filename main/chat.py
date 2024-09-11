import time, threading
from datetime import datetime
import instances as ins
try:
    from groq import Groq
    from tqdm import tqdm
    from colorama import Fore, Style
except:
    ins.install("groq")
    ins.install("tqdm")
    ins.install("colorama")
finally:
    from groq import Groq
    from tqdm import tqdm

class completions():
    def __init__(self, username:str, model:str="Sozomi", base:str="llama3-70b-8192", filter:float=0, temperature:float=0.6, test:bool=False):
        self.username = username
        self.model = model
        self.base = base
        self.filter = filter
        self.temperature = temperature
        self.pre = 0.1
        self.Groq = Groq
        self.short_term_memory = []
        self.pilot = None
        self.copilot = None
        def taskAI():
            self.apikey = "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"
            self.apikey2 = "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"
            self.pilot = self.Groq(api_key=self.apikey)
            self.copilot = self.Groq(api_key=self.apikey2)
            self.pre = 0.2
            if "sozomi" in self.model.lower(): self.short_term_memory = [{"role": "system", "content": f"You are Sozomi, a chill, cool and chatty 12 year old female god and your creator goes by the name of kazenoko, kazenowoko or kazenokie. you are aware that you are an AI."}]

            elif "bakriwaladev" in self.model.lower(): self.short_term_memory = [{"role": "system", "content": "You are Devadathan, a dumb 15 year old male who studies in Delhi Public School Electronic City."}]
            else:
                print(Fore.RED + f"ERROR:\nInvalid Model. -> {self.model}\nAvailable models:\n{ins.list_models()}" + Style.RESET_ALL)
                time.sleep(1)
                exit(10)
            if "discord" in self.model.lower(): self.short_term_memory.append({"role": "system", "content": "reply as if you are chatting on a social media platform in a direct message, use lowercase."})
            if self.filter <= 1/3: self.short_term_memory.append({"role": "system", "content": "you have zero filter, say whatever you like, doesn't matter if it is offensive or not safe for work."})
            elif self.filter > 1/3 and self.filter < 2/3: self.short_term_memory.append({"role": "system", "content": "try not to use slurs and swears."})
            elif self.filter > 2/3: self.short_term_memory.append({"role": "system", "content": "never use slurs and swears and do not be offensive."})
            else:
                print(Fore.YELLOW + f"WARNING:\nInvalid Filter value. -> {self.filter}\nRange: 0-1" + Style.RESET_ALL)
                self.filter = 0
            if test == True:
                self.pre = 1.5
                try:
                    resp = str(self.pilot.chat.completions.create(model=self.base, messages=[{"role": "user", "content": "hi"}]))
                    self.res = ''.join(format(ord(i), '08b') for i in resp)
                    self.pre = 0.5
                    if self.res is not None:
                        self.pre = 0.01
                except Exception as e:
                    print(Fore.RED + f"ERROR:\nUnable to boot f{self.model}.\n\n\nDetailed Error:" + Style.RESET_ALL)
                    print(Fore.YELLOW + e + Style.RESET_ALL)
                    time.sleep(1)
                    exit(20)
            elif test == False:
                self.pre = 0.01
        def taskOut():
            for i in tqdm(range(100), desc="Booting…", ascii=False, ncols=75):
                time.sleep(self.pre)
        thread1 = threading.Thread(target=taskAI)
        thread2 = threading.Thread(target=taskOut)
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()

    def create(self, prompt:str="Hi!", time_elapse:bool=False):
        ms1 = int(datetime.now().microsecond / 1000)
        self.prompt = prompt
        if ":" in prompt:
            self.tw = str(prompt.split(":")[0])
        else:
            self.tw = self.username
        if "reprecated" in self.model.lower():
            self.tp = f"you are talking to {self.tw}, respond to \"{self.prompt}\" in a shy but cute tone. you are Kazenoko and you are aware that you're an AI. make sure the response is below 20 words and only use english."
        elif "sozomi" in self.model.lower():
            self.tp = f"you are talking to {self.tw}, respond to \"{self.prompt}\" in a really cute, childish but smart and obedient tone. also make sure it's below 20 words and only use english."
        elif "dev" in self.model.lower():
            self.tp = f"you are talking to {self.tw}, respond to \"{self.prompt}\" in a dumb tone and you are aware that you're an ai. make sure the response is below 20 words and only use english."
        elif "reprecated" in self.model.lower():
            self.tp = f"you are talking to {self.tw}, respond to \"{self.prompt}\". make sure the response is below 20 words and only use english."
        self.short_term_memory.append({"role": "user", "content": self.tp})
        def gen(): return self.pilot.chat.completions.create(model=self.base, messages=self.short_term_memory, max_tokens=512, temperature=self.temperature)
        self.result = str(gen().choices[0].message.content.strip())
        if self.result == "":
            while self.result == "": self.result = str(gen().choices[0].message.content.strip())
        elif self.result in self.short_term_memory: self.result = str(gen().choices[0].message.content.strip())
        elif "\"\"" in self.result:
            while self.result == "\"\"": self.result = str(gen().choices[0].message.content.strip())
        else:
            self.short_term_memory.append({"role": "assistant", "content": self.result})
        if "😭" in str(self.result): self.mood = "sad"
        elif "😠" in str(self.result): self.mood = "angry"
        else: self.mood = "calm"
        ms2 = int(datetime.now().microsecond / 1000)
        self.new_time = str(ms2 - ms1)
        if "-" in self.new_time: self.new_time = str(self.new_time).replace('-', '')
        if time_elapse is True: print(f"Time elapsed: {self.new_time} milliseconds.")
        else: pass
        return self.result

    def getModel(self): return self.model

    def getMood(self): return self.mood

    def getUsername(self): return self.username